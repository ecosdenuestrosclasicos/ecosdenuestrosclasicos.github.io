"""Da a los monumentos dibujados el acabado pintado de la ilustración: pinceladas
del original, luz desde la izquierda y sombras propias."""
import cv2, numpy as np, glob
rng = np.random.default_rng(3)
orig = cv2.imread('/home/claude/pers/orig.png').astype(np.float32)
g = orig.mean(2); b = cv2.GaussianBlur(g, (0, 0), 4); det = np.clip((g - b) / (b + 1), -.2, .2)
src = det[100:330, 1150:1600]          # pinceladas de la tierra de Asia en el original
for f in glob.glob('/home/claude/pers/cut/d_*.png'):
    if f.endswith('_p.png'): continue
    im = cv2.imread(f, cv2.IMREAD_UNCHANGED); a = im[:, :, 3].copy(); rgb = im[:, :, :3].astype(np.float32)
    h, w = a.shape
    bg = im[:, :, :3].copy(); bg[a < 10] = (170, 200, 225)
    st = cv2.stylization(bg, sigma_s=8, sigma_r=0.18).astype(np.float32)
    st = st * .45 + rgb * .55
    tex = cv2.resize(src, (w, h))
    tex = cv2.GaussianBlur(tex, (0, 0), .8)
    luz = (1.12 - .24 * np.linspace(0, 1, w))[None, :] * (1.06 - .12 * np.linspace(0, 1, h))[:, None]
    # sombra propia: oscurecer cerca del borde inferior y derecho de la silueta
    m = (a > 40).astype(np.uint8)
    d = cv2.distanceTransform(m, cv2.DIST_L2, 5)
    desplaz = np.roll(np.roll(m, -6, 0), -6, 1)
    sombra = ((m == 1) & (desplaz == 0)).astype(np.float32)
    sombra = cv2.GaussianBlur(sombra, (0, 0), 4) * .35
    out = st * (1 + .45 * tex)[..., None] * luz[..., None] * (1 - sombra)[..., None]
    out = out * np.array([0.93, 0.99, 1.05])        # BGR: más cálido
    cv2.imwrite(f.replace('.png', '_p.png'), np.dstack([np.clip(out, 0, 255).astype(np.uint8), a]))
print('ok')
