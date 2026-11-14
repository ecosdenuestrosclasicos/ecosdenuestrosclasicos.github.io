"""Mapa ilustrado de la ruta de Ecos (versión 3, con la estética de la ilustración original).

1. Dibuja el Mediterráneo real (Natural Earth 1:10m: costas, ríos y lagos) como SVG.
2. Lo pega dentro del marco de la ilustración original de Isabel.
3. Encima coloca, recortados de esa misma ilustración, las columnas, los laureles,
   el globo, los libros, el casco, la rosa de los vientos, los monumentos (cada uno
   en su lugar real) y los personajes.
4. Genera la capa con la ruta circular, los nombres y el barco (SVG).

Coordenadas en píxeles del lienzo original: 1774 × 887.
"""
import json, math, sys
sys.setrecursionlimit(100000)

NE = "/tmp/ne/geojson/"
CW, CH = 1774, 887                     # lienzo
MX0, MY0, MW, MH = 18, 38, 1738, 820   # hueco del mapa dentro del marco
L0, L1 = -10.0, 44.0
COS = math.cos(math.radians(38))
K = MW / ((L1 - L0) * COS)
B1 = 46.6
B0 = B1 - MH / K

def P(lon, lat):          # coordenadas del lienzo
    return (MX0 + (lon - L0) * COS * K, MY0 + (B1 - lat) * K)
def Pm(lon, lat):         # coordenadas dentro del mapa
    x, y = P(lon, lat); return (x - MX0, y - MY0)

def dp(pts, tol):
    if len(pts) < 3: return pts
    (x1, y1), (x2, y2) = pts[0], pts[-1]
    dx, dy = x2 - x1, y2 - y1; n = math.hypot(dx, dy)
    i, dmax = 0, 0
    for j in range(1, len(pts) - 1):
        d = math.hypot(pts[j][0] - x1, pts[j][1] - y1) if n < 1e-6 else abs(dy * pts[j][0] - dx * pts[j][1] + x2 * y1 - y2 * x1) / n
        if d > dmax: i, dmax = j, d
    if dmax > tol: return dp(pts[:i + 1], tol)[:-1] + dp(pts[i:], tol)
    return [pts[0], pts[-1]]

def dentro(coords, m=2):
    lons = [c[0] for c in coords]; lats = [c[1] for c in coords]
    return not (max(lons) < L0 - m or min(lons) > L1 + m or max(lats) < B0 - m or min(lats) > B1 + m)

def anillos(path, minpx=2.0):
    out = []
    for f in json.load(open(path))["features"]:
        g = f["geometry"]
        if g is None: continue
        polys = g["coordinates"] if g["type"] == "MultiPolygon" else [g["coordinates"]]
        for poly in polys:
            for ring in poly:
                if not dentro(ring): continue
                pts = [Pm(*c[:2]) for c in ring]
                xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
                if max(xs) - min(xs) < minpx and max(ys) - min(ys) < minpx: continue
                pts = [(min(max(x, -40), MW + 40), min(max(y, -40), MH + 40)) for x, y in pts]
                pts = dp(pts, 0.45)
                if len(pts) >= 3: out.append("M" + "L".join(f"{x:.1f},{y:.1f}" for x, y in pts) + "Z")
    return "".join(out)

def rios(path):
    out = []
    for f in json.load(open(path))["features"]:
        g = f["geometry"]; pr = f["properties"]
        if g is None or (pr.get("scalerank") or 99) > 6: continue
        lines = g["coordinates"] if g["type"] == "MultiLineString" else [g["coordinates"]]
        for ln in lines:
            if not dentro(ln, 0): continue
            pts = dp([Pm(*c[:2]) for c in ln], 0.6)
            if len(pts) >= 2: out.append("M" + "L".join(f"{x:.1f},{y:.1f}" for x, y in pts))
    return "".join(out)

def base_svg():
    tierra = anillos(NE + "ne_10m_land.geojson")
    lagos = anillos(NE + "ne_10m_lakes.geojson", 3)
    r = rios(NE + "ne_10m_rivers_lake_centerlines.geojson")
    ret = []
    for lon in range(-10, 45, 5):
        x, _ = Pm(lon, 0); ret.append(f"M{x:.1f},0V{MH}")
    for lat in range(25, 50, 5):
        _, y = Pm(0, lat); ret.append(f"M0,{y:.1f}H{MW}")
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{MW}" height="{MH}" viewBox="0 0 {MW} {MH}">
<defs>
  <path id="t" d="{tierra}"/>
  <clipPath id="ct"><use href="#t"/></clipPath>
  <linearGradient id="gt" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#CEC593"/><stop offset=".4" stop-color="#DECDA0"/>
    <stop offset=".65" stop-color="#E7D2A2"/><stop offset="1" stop-color="#EBD4A2"/>
  </linearGradient>
  <radialGradient id="gm" cx=".5" cy=".5" r=".8">
    <stop offset="0" stop-color="#B2D0E3"/><stop offset="1" stop-color="#8AB3D3"/>
  </radialGradient>
  <filter id="relieve" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency=".02 .026" numOctaves="6" seed="11" result="r"/>
    <feDiffuseLighting in="r" surfaceScale="7" lighting-color="#FFF6E2" result="l"><feDistantLight azimuth="225" elevation="48"/></feDiffuseLighting>
    <feComposite in="l" in2="SourceGraphic" operator="arithmetic" k1="1.08" k2="0" k3="0" k4="0"/>
  </filter>
  <filter id="manchas" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency=".035" numOctaves="3" seed="5"/>
    <feColorMatrix values="0 0 0 0 .45  0 0 0 0 .52  0 0 0 0 .26  0 0 0 -2.8 1.5"/>
  </filter>
  <filter id="grano" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency=".75" numOctaves="2" seed="9"/>
    <feColorMatrix values="0 0 0 0 .36  0 0 0 0 .25  0 0 0 0 .14  0 0 0 .9 -.32"/>
  </filter>
  <filter id="agua" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency=".9 .06" numOctaves="2" seed="2"/>
    <feColorMatrix values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .3 0"/>
  </filter>
</defs>
<rect width="{MW}" height="{MH}" fill="url(#gm)"/>
<rect width="{MW}" height="{MH}" filter="url(#agua)"/>
<path d="{"".join(ret)}" fill="none" stroke="#5C6F86" stroke-width=".7" opacity=".35"/>
<use href="#t" fill="none" stroke="#6C93B3" stroke-width="16" opacity=".18" stroke-linejoin="round"/>
<use href="#t" fill="none" stroke="#557EA2" stroke-width="7" opacity=".22" stroke-linejoin="round"/>
<use href="#t" fill="url(#gt)"/>
<rect width="{MW}" height="{MH}" fill="url(#gt)" filter="url(#relieve)" clip-path="url(#ct)"/>
<rect width="{MW}" height="{MH}" filter="url(#manchas)" clip-path="url(#ct)" opacity=".38"/>
<rect width="{MW}" height="{MH}" filter="url(#grano)" clip-path="url(#ct)"/>
<path d="{r}" fill="none" stroke="#4C7FAA" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" opacity=".9"/>
<path d="{lagos}" fill="#9EC3DA" stroke="#5E8FB5" stroke-width=".8"/>
<use href="#t" fill="none" stroke="#4A3324" stroke-width="1.1" stroke-linejoin="round"/>
</svg>'''

# ------------------------------------------------------------------ lugares
L = {
    "Sagunto": (0.27, 39.68), "Roma": (12.48, 41.89), "Pompeya": (14.49, 40.75),
    "Siracusa": (15.29, 37.07), "Ítaca": (20.70, 38.38),
    "Atenas": (23.73, 37.97), "Troya": (26.24, 39.96), "Éfeso": (27.34, 37.94),
    "Alejandría": (29.92, 31.20), "Cartago": (10.32, 36.85),
    # escapadas por tierra
    "Segovia": (-4.12, 40.95), "Giza": (31.13, 29.98), "Petra": (35.44, 30.33),
}
ANT = {"Atenas": "Ἀθῆναι", "Delfos": "Δελφοί", "Troya": "Ἴλιον", "Éfeso": "Ἔφεσος", "Ítaca": "Ἰθάκη",
       "Roma": "Roma", "Pompeya": "Pompeii", "Siracusa": "Συράκουσαι", "Sagunto": "Saguntum",
       "Alejandría": "Ἀλεξάνδρεια", "Cartago": "Carthago", "Segovia": "Segovia", "Giza": "Γίζα", "Petra": "Πέτρα"}
# etiqueta: dx, dy, anclaje
ET = {"Sagunto": (-11, 4, "end"), "Roma": (10, 14, "start"), "Pompeya": (11, 13, "start"),
      "Siracusa": (-10, 19, "end"), "Ítaca": (-10, 4, "end"), "Delfos": (-2, -12, "middle"),
      "Atenas": (-10, -12, "end"), "Troya": (10, -2, "start"), "Éfeso": (10, 18, "start"),
      "Alejandría": (-10, 18, "end"), "Cartago": (-10, -8, "end"),
      "Segovia": (-10, 18, "end"), "Giza": (12, 30, "start"), "Petra": (10, 18, "start")}

RUTA = [
    L["Sagunto"], (1.6, 39.2), (5.0, 38.6), (8.4, 38.55), (10.6, 39.6), (11.9, 41.2), L["Roma"],
    (12.6, 41.25), (13.6, 40.75), L["Pompeya"],
    (14.6, 40.1), (15.2, 39.2), (15.5, 38.45), (15.62, 38.17), (15.56, 37.55), L["Siracusa"],
    (16.5, 37.2), (18.5, 37.7), (20.2, 38.25), L["Ítaca"],
    (21.3, 38.32), (21.9, 38.33), (22.45, 38.25),
    (22.65, 38.08), (22.92, 37.93), (23.3, 37.93), L["Atenas"],
    (23.62, 37.9), (24.17, 37.6), (24.62, 37.93), (25.1, 38.6), (25.6, 39.4), (26.0, 39.9), L["Troya"],
    (25.9, 39.4), (26.2, 38.7), (26.75, 38.15), L["Éfeso"],
    (26.95, 37.55), (27.05, 37.0), (27.75, 36.3), (28.7, 35.0), (29.6, 32.6), L["Alejandría"],
    (28.0, 32.0), (25.0, 33.1), (21.0, 33.7), (17.0, 34.5), (13.6, 36.1), (11.4, 37.2), L["Cartago"],
    (8.5, 37.6), (5.0, 37.9), (2.0, 38.6), (0.9, 39.25),
]
# escapadas a pie (por tierra), con puntos de paso reales
ESCAPADAS = [
    [L["Sagunto"], (-0.9, 39.95), (-2.1, 40.3), (-3.3, 40.6), L["Segovia"]],                 # por la Meseta
    [L["Alejandría"], (30.4, 30.9), (30.9, 30.4), L["Giza"]],                                # siguiendo el Nilo
    [L["Giza"], (32.3, 30.2), (33.6, 30.0), (34.6, 30.1), L["Petra"]],                       # cruzando el Sinaí
]

def curva(pts, cerrada=False):
    pts = [P(*p) for p in pts]; n = len(pts)
    d = f"M{pts[0][0]:.1f},{pts[0][1]:.1f}"
    rng = range(n) if cerrada else range(n - 1)
    for i in rng:
        p0 = pts[i - 1] if (cerrada or i) else pts[i]
        p1 = pts[i]; p2 = pts[(i + 1) % n]
        p3 = pts[(i + 2) % n] if (cerrada or i + 2 < n) else p2
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f"C{c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}"
    return d + ("Z" if cerrada else "")

# monumentos recortados: archivo -> (lugar, escala, dx, dy) ; la base del dibujo queda junto al punto
MONUMENTOS = {   # archivo: (lugar, alto en px, dx, dy de la base respecto al punto)
    "acueducto":   ("Segovia", 92, 0, -12),
    "d_castillo":  ("Sagunto", 62, -66, 72),
    "coliseo":     ("Roma", 92, -92, -10),
    "d_vesubio":   ("Pompeya", 96, 52, -4),
    "d_teatro":    ("Siracusa", 62, -78, -6),
    "d_olivo":     ("Ítaca", 64, -10, -16),
    "partenon":    ("Atenas", 80, -40, 80),
    "d_caballo":   ("Troya", 82, 56, -10),
    "celso":       ("Éfeso", 86, 62, -4),
    "d_faro":      ("Alejandría", 104, 62, -2),
    "piramides":   ("Giza", 96, -74, 104),
    "petra":       ("Petra", 98, 36, -10),
    "d_puerto":    ("Cartago", 54, -104, 40),
}
NOMBRE_MON = {"d_castillo": "Castillo de Sagunto", "d_vesubio": "El Vesubio", "d_teatro": "Teatro griego de Siracusa", "d_olivo": "Un olivo de Ítaca", "d_caballo": "El caballo de Troya", "d_faro": "Faro de Alejandría", "d_puerto": "Puerto circular de Cartago", "acueducto": "Acueducto de Segovia", "coliseo": "Anfiteatro Flavio (Coliseo)", "partenon": "Partenón",
              "celso": "Biblioteca de Celso", "piramides": "Pirámides de Guiza y la Esfinge", "petra": "El Tesoro de Petra"}

MARES = [("MAR MEDITERRÁNEO", 23.0, 34.3, 0, 26, 9), ("Mar Tirreno", 11.8, 39.4, 0, 17, 3), ("Mar Jónico", 18.2, 36.3, 0, 17, 3),
         ("Mar Egeo", 25.6, 36.05, 0, 17, 3), ("Mar Adriático", 15.1, 43.4, -37, 17, 3), ("MAR NEGRO", 33.5, 43.9, 0, 20, 6),
         ("Mar Rojo", 35.0, 27.3, -58, 16, 3)]

if __name__ == "__main__":
    open("/home/claude/mapa/v3_base.svg", "w").write(base_svg())
    datos = {
        "lugares": {n: P(*c) for n, c in L.items()}, "ant": ANT, "et": ET,
        "ruta": curva(RUTA, True), "escapadas": [curva(e) for e in ESCAPADAS],
        "monumentos": {k: (v[0], v[1], v[2], v[3], NOMBRE_MON[k]) for k, v in MONUMENTOS.items()},
        "mares": [(t, *P(lon, lat), rot, fs, ls) for t, lon, lat, rot, fs, ls in MARES],
    }
    json.dump(datos, open("/home/claude/mapa/v3_datos.json", "w"), ensure_ascii=False)
    print("B0", round(B0, 2), "K", round(K, 2))
