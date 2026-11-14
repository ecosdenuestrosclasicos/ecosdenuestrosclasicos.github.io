"""Pinta el mapa real con la textura y los colores de la ilustración original.

- Color base: manchas suaves con los colores del original (ocres, arena y verdes),
  más verdes al norte y más ocres al sur, con el relieve del mapa base.
- Detalle: las pinceladas, grietas y relieves de la tierra del original (su capa de
  alta frecuencia), repetidas sobre la tierra real. Lo mismo para el mar.
- Costas reales de Natural Earth con el contorno marrón del original.
"""
import cv2, numpy as np
rng = np.random.default_rng(23)
orig = cv2.imread("/home/claude/pers/orig.png").astype(np.float32)
H0, W0 = orig.shape[:2]
hsv = cv2.cvtColor(orig.astype(np.uint8), cv2.COLOR_BGR2HSV)
mar0 = ((orig[:, :, 0] - orig[:, :, 2]) > 4).astype(np.uint8)
mar0 = cv2.morphologyEx(mar0, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))
mar0 = cv2.morphologyEx(mar0, cv2.MORPH_OPEN, np.ones((9, 9), np.uint8))
tierra0 = 1 - mar0

prohibido = np.zeros((H0, W0), np.uint8)
for x0, y0, x1, y1 in [(0, 0, W0, 60), (0, 830, W0, H0), (0, 0, 140, H0), (W0 - 140, 0, W0, H0),
                       (0, 0, 440, 150), (W0 - 440, 0, W0, 150), (0, 520, 480, H0), (1370, 560, W0, H0),
                       (490, 500, 1010, H0), (1150, 670, 1350, 840), (560, 280, 1220, 400), (120, 390, 320, 500),
                       (470, 370, 620, 500), (970, 460, 1140, 590), (1150, 390, 1310, 510), (800, 410, 990, 480),
                       (60, 320, 250, 400), (1560, 320, 1740, 410), (1130, 600, 1300, 680), (270, 370, 700, 480)]:
    prohibido[y0:y1, x0:x1] = 1

gris = orig.mean(2)
azul = cv2.dilate(((orig[:, :, 0] - orig[:, :, 2]) > 0).astype(np.uint8), np.ones((7, 7), np.uint8))
gris_mar = cv2.medianBlur(gris.astype(np.uint8), 5).astype(np.float32)   # sin las líneas de la cuadrícula
def alta(g, s):
    b = cv2.GaussianBlur(g, (0, 0), s); return np.clip((g - b) / (b + 1), -.16, .22)
det_gris = alta(gris, 6); det_gris_mar = alta(gris_mar, 6)

MW, MH = 1738, 820

def capa_detalle(mascara, ancho, alto, P=110, detalle=None, sin_azul=False):
    m = (mascara & (1 - prohibido)).astype(np.uint8)
    if sin_azul: m = m & (1 - azul)
    m = cv2.erode(m, np.ones((15, 15), np.uint8))
    ventanas = [(x, y) for y in range(0, H0 - P, 10) for x in range(0, W0 - P, 10)
                if m[y:y + P, x:x + P].mean() > .86]
    print("ventanas", len(ventanas))
    out = np.zeros((alto, ancho, 3), np.float32); peso = np.zeros((alto, ancho), np.float32)
    paso = P - 34
    v = np.minimum(np.arange(P), np.arange(P)[::-1]).astype(np.float32)
    w2 = np.clip(np.minimum.outer(v, v) / 25, .02, 1)
    for y in range(-30, alto, paso):
        for x in range(-30, ancho, paso):
            sx, sy = ventanas[rng.integers(len(ventanas))]
            d = (detalle[sy:sy + P, sx:sx + P] * m[sy:sy + P, sx:sx + P])[..., None]
            ya, xa = max(0, y), max(0, x); yb, xb = min(alto, y + P), min(ancho, x + P)
            out[ya:yb, xa:xb] += d[ya - y:yb - y, xa - x:xb - x] * w2[ya - y:yb - y, xa - x:xb - x, None]
            peso[ya:yb, xa:xb] += w2[ya - y:yb - y, xa - x:xb - x]
    return out / np.maximum(peso, 1e-3)[..., None]

det_t = capa_detalle(tierra0, MW, MH, 110, det_gris, True)
det_m = capa_detalle(mar0, MW, MH, 90, det_gris_mar)

def colores(mascara):
    return orig[(mascara & (1 - prohibido)).astype(bool)]
ct = colores(tierra0); cm = colores(mar0)
g, r_ = ct[:, 1], ct[:, 2]
c_verde = np.median(ct[g > r_ * .92], 0)
c_ocre = np.median(ct[g < r_ * .8], 0)
c_arena = np.median(ct[(g >= r_ * .8) & (g <= r_ * .92)], 0)
c_mar = np.median(cm, 0); c_mar_claro = np.percentile(cm, 85, 0)
# paleta fijada a ojo sobre la ilustración (BGR)
c_verde = np.array([78, 160, 146.]); c_arena = np.array([140, 205, 236.]); c_ocre = np.array([92, 176, 226.])
c_mar = np.array([214, 184, 140.]); c_mar_claro = np.array([228, 210, 180.])
print("BGR verde", c_verde, "ocre", c_ocre, "arena", c_arena, "mar", c_mar, c_mar_claro)

def ruido(esc, sem):
    r = np.random.default_rng(sem).normal(0, 1, (MH // esc + 2, MW // esc + 2)).astype(np.float32)
    return cv2.resize(r, (MW, MH), interpolation=cv2.INTER_CUBIC)
n1 = ruido(60, 1) * .6 + ruido(18, 2) * .3 + ruido(6, 3) * .1
n2 = ruido(45, 4) * .7 + ruido(12, 5) * .3
lat = np.linspace(0, 1, MH)[:, None] * np.ones((1, MW))
p_verde = np.clip(.62 - lat * .95 + n1 * .4, 0, .85)
p_ocre = np.clip(lat * .9 - .3 + n2 * .3, 0, 1) * (1 - p_verde)
p_arena = 1 - p_verde - p_ocre
base_t = c_arena * p_arena[..., None] + c_verde * p_verde[..., None] + c_ocre * p_ocre[..., None]

rel = cv2.imread("/home/claude/mapa/v3_base.png").astype(np.float32).mean(2)
rel = cv2.GaussianBlur(rel, (0, 0), 1.5); rel = (rel - rel.mean()) / (rel.std() + 1)
tierra = base_t * (1 + .07 * rel[..., None]) * (1 + 1.25 * det_t)

cx = np.linspace(-1, 1, MW)[None, :]; cy = np.linspace(-1, 1, MH)[:, None]
rr = np.clip(np.sqrt(cx ** 2 + cy ** 2) / 1.4, 0, 1)
mar = (c_mar_claro * (1 - rr[..., None]) + c_mar * rr[..., None]) * (1 + .7 * det_m)

m_t = cv2.imread("/home/claude/mapa/m_tierra.png", 0).astype(np.float32) / 255
dist = cv2.distanceTransform((m_t < .5).astype(np.uint8), cv2.DIST_L2, 5)
somero = np.exp(-dist / 14)[..., None]
mar = mar * (1 - .12 * somero) + c_mar_claro * .12 * somero
dist_t = cv2.distanceTransform((m_t >= .5).astype(np.uint8), cv2.DIST_L2, 5)
tierra = tierra * (1 - .16 * np.exp(-dist_t / 5)[..., None])
out = tierra * m_t[..., None] + mar * (1 - m_t[..., None])
cv2.imwrite("/home/claude/mapa/tex_mapa.png", np.clip(out, 0, 255).astype(np.uint8))
print("ok")
