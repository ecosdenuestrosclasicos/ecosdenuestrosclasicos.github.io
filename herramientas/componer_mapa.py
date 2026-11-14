"""Compone el mapa ilustrado: marco y adornos de la ilustración original + mapa real + monumentos."""
import json, numpy as np, cv2
from PIL import Image, ImageFilter, ImageDraw

ORIG = "/home/claude/pers/orig.png"
CUT = "/home/claude/pers/cut/"
d = json.load(open("/home/claude/mapa/v3_datos.json"))
orig = Image.open(ORIG).convert("RGBA")
W, H = orig.size
lienzo = orig.copy()

# 1. mapa real dentro del marco, con bordes difuminados
from PIL import ImageEnhance
mapa = Image.open("/home/claude/mapa/tex_full.png").convert("RGB")
mapa = ImageEnhance.Color(mapa).enhance(1.0)
mapa = ImageEnhance.Contrast(mapa).enhance(1.06).convert("RGBA")
MX0, MY0 = 18, 38
m = Image.new("L", mapa.size, 0)
ImageDraw.Draw(m).rectangle([6, 4, mapa.size[0] - 7, mapa.size[1] - 6], fill=255)
m = m.filter(ImageFilter.GaussianBlur(5))
lienzo.paste(mapa, (MX0, MY0), m)

# 2. esquinas superiores: columna entera + hojas de laurel (sin el mapa antiguo que asoma entre ellas)
o = cv2.cvtColor(np.array(orig.convert("RGB")), cv2.COLOR_RGB2HSV)
azul = (o[:, :, 0] >= 85) & (o[:, :, 0] <= 130) & (o[:, :, 1] > 30)
mask = np.zeros((H, W), np.uint8)
# columnas
for x0, x1, cx0, cx1 in [(0, 98, 0, 130), (W - 99, W, W - 131, W)]:
    cv2.rectangle(mask, (cx0, 0), (cx1, 70), 255, -1)                 # capitel
    for y in range(70, 250):                                          # fuste, que se desvanece abajo
        mask[y, x0:x1] = 255 if y < 205 else int(255 * (250 - y) / 45)
cv2.rectangle(mask, (0, 0), (23, 310), 255, -1); cv2.rectangle(mask, (W - 24, 0), (W, 310), 255, -1)  # greca lateral
# franja superior del marco
cv2.rectangle(mask, (0, 0), (W, 36), 255, -1)
hojas = np.zeros((H, W), np.uint8)
izq = np.array([(85, 132), (98, 70), (150, 22), (250, 5), (420, 10), (438, 30), (438, 62), (380, 60),
                (300, 62), (220, 76), (160, 98), (122, 134)], np.int32)
cv2.fillPoly(hojas, [izq], 255)
der = izq.copy(); der[:, 0] = W - 1 - der[:, 0]
cv2.fillPoly(hojas, [der], 255)
hojas[azul] = 0
# las hojas: quitar también el mapa claro (amarillo pálido) dentro del polígono, quedarse con verde oscuro/tallo
v = o[:, :, 2]; s = o[:, :, 1]
hoja_color = (s > 60) & (v < 200)
hojas[~hoja_color & (np.arange(H)[:, None] > 36)] = 0
hojas = cv2.morphologyEx(hojas, cv2.MORPH_CLOSE, np.ones((3, 3), np.uint8))
mask = np.maximum(mask, hojas)
mask = cv2.GaussianBlur(mask, (3, 3), 0)
capa = orig.copy(); capa.putalpha(Image.fromarray(mask))
lienzo.alpha_composite(capa)

def pegar(nombre, x, y, escala=1.0, recorte_x=None):
    im = Image.open(CUT + nombre + ".png").convert("RGBA")
    if recorte_x is not None:
        a = np.array(im); a[:, :recorte_x, 3] = 0; im = Image.fromarray(a)
    if escala != 1.0:
        im = im.resize((round(im.width * escala), round(im.height * escala)), Image.LANCZOS)
    lienzo.alpha_composite(im, (round(x), round(y)))
    return im

def pos(nombre):
    x, y = open(CUT + nombre + ".pos").read().split(); return int(x), int(y)

# 3. esquinas inferiores (globo, libros, pergamino / casco) en su sitio original
x, y = pos("esq_ii"); pegar("esq_ii", x, y)
x, y = pos("esq_id"); pegar("esq_id", x, y, recorte_x=1585 - x)   # sin el laurel, que tapaba Petra

# 4. rosa de los vientos, en el mar Negro
rx, ry = d["lugares"]["Troya"]; cx, cy = 1372, 196
im = Image.open(CUT + "rosa.png"); esc = .72
pegar("rosa", cx - im.width * esc / 2, cy - im.height * esc / 2, esc)

# 5. monumentos en su lugar real, con su sombra para que se asienten en el terreno
for nombre, (lugar, alto, dx, dy, _) in d["monumentos"].items():
    archivo = CUT + (nombre + "_p.png" if nombre.startswith("d_") else nombre + ".png")
    im = Image.open(archivo).convert("RGBA")
    bb = im.getchannel("A").point(lambda v: 255 if v > 40 else 0).getbbox(); im = im.crop(bb)
    esc = alto / im.height
    im = im.resize((max(1, round(im.width * esc)), round(alto)), Image.LANCZOS)
    px, py = d["lugares"][lugar]
    x = px + dx - im.width / 2; y = py + dy - im.height
    sombra = Image.new("RGBA", lienzo.size, (0, 0, 0, 0))
    ImageDraw.Draw(sombra).ellipse([x + im.width * .08, y + im.height - 7, x + im.width * .92, y + im.height + 7], fill=(70, 45, 25, 95))
    lienzo.alpha_composite(sombra.filter(ImageFilter.GaussianBlur(5)))
    lienzo.alpha_composite(im, (round(x), round(y)))

# 6. personajes, exactamente donde estaban
per = Image.open("/home/claude/pers/personajes-ruta.png").convert("RGBA")
lienzo.alpha_composite(per, (501, 521))

lienzo.convert("RGB").save("/home/claude/mapa/v3_fondo.jpg", quality=90)
print("ok", lienzo.size)
