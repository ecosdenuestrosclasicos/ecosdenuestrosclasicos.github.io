"""Genera el mapa de la ruta de Ecos (SVG) a partir de Natural Earth 1:10m.
Proyección equirectangular centrada en 38° N. Coordenadas reales."""
import json, math, sys
sys.setrecursionlimit(100000)

LON0, LON1, LAT0, LAT1 = -2.0, 33.0, 30.0, 45.6
COS = math.cos(math.radians(38))
W = 1400
K = W / ((LON1 - LON0) * COS)
H = round((LAT1 - LAT0) * K)

def P(lon, lat):
    return ((lon - LON0) * COS * K, (LAT1 - lat) * K)

def dp(pts, tol):
    if len(pts) < 3: return pts
    (x1, y1), (x2, y2) = pts[0], pts[-1]
    dx, dy = x2 - x1, y2 - y1; n = math.hypot(dx, dy)
    i, dmax = 0, 0
    for j in range(1, len(pts) - 1):
        if n < 1e-6:
            d = math.hypot(pts[j][0] - x1, pts[j][1] - y1)
        else:
            d = abs(dy * pts[j][0] - dx * pts[j][1] + x2 * y1 - y2 * x1) / n
        if d > dmax: i, dmax = j, d
    if dmax > tol:
        return dp(pts[:i + 1], tol)[:-1] + dp(pts[i:], tol)
    return [pts[0], pts[-1]]

land = json.load(open(sys.argv[1]))
rings = []
for f in land["features"]:
    g = f["geometry"]
    polys = g["coordinates"] if g["type"] == "MultiPolygon" else [g["coordinates"]]
    for poly in polys:
        for ring in poly:
            lons = [c[0] for c in ring]; lats = [c[1] for c in ring]
            if max(lons) < LON0 - 1 or min(lons) > LON1 + 1 or max(lats) < LAT0 - 1 or min(lats) > LAT1 + 1:
                continue
            pts = [P(*c) for c in ring]
            xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
            if (max(xs) - min(xs)) < 2.2 and (max(ys) - min(ys)) < 2.2:
                continue  # islotes de menos de 2 px
            # recorte grosero: limitar a un margen alrededor del lienzo
            pts = [(min(max(x, -40), W + 40), min(max(y, -40), H + 40)) for x, y in pts]
            pts = dp(pts, 0.45)
            if len(pts) >= 3:
                rings.append("M" + "L".join(f"{x:.1f},{y:.1f}" for x, y in pts) + "Z")
land_d = "".join(rings); print("anillos", len(rings))

# Lugares (lon, lat) — coordenadas de los yacimientos o ciudades antiguas
L = {
    "Sagunto":    (0.27, 39.68),
    "Roma":       (12.48, 41.89),
    "Pompeya":    (14.49, 40.75),
    "Siracusa":   (15.29, 37.07),
    "Ítaca":      (20.70, 38.38),
    "Delfos":     (22.50, 38.48),
    "Atenas":     (23.73, 37.97),
    "Troya":      (26.24, 39.96),
    "Éfeso":      (27.34, 37.94),
    "Alejandría": (29.92, 31.20),
}
# Puntos de paso por mar (para que la ruta no cruce tierra)
RUTA = [
    L["Sagunto"], (1.6, 39.2), (5.0, 38.6), (8.4, 38.55), (10.6, 39.6), (11.9, 41.2), L["Roma"],
    "parada",
    L["Roma"], (12.6, 41.25), (13.6, 40.75), L["Pompeya"],
    "parada",
    L["Pompeya"], (14.6, 40.1), (15.2, 39.2), (15.5, 38.45), (15.62, 38.17), (15.56, 37.55), L["Siracusa"],
    "parada",
    L["Siracusa"], (16.5, 37.2), (18.5, 37.7), (20.2, 38.25), L["Ítaca"],
    "parada",
    L["Ítaca"], (21.3, 38.32), (21.9, 38.33), (22.45, 38.30), L["Delfos"],
    "parada",
    L["Delfos"], (22.55, 38.10), (22.92, 37.93), (23.3, 37.93), L["Atenas"],
    "parada",
    L["Atenas"], (23.62, 37.9), (24.17, 37.6), (24.62, 37.93), (25.1, 38.6), (25.6, 39.4), (26.0, 39.9), L["Troya"],
    "parada",
    L["Troya"], (25.9, 39.4), (26.2, 38.7), (26.75, 38.15), L["Éfeso"],
    "parada",
    L["Éfeso"], (26.95, 37.55), (27.05, 37.0), (27.75, 36.3), (28.7, 35.0), (29.6, 32.6), L["Alejandría"],
]

def suave(pts):
    """Curva Catmull-Rom convertida en Bézier."""
    pts = [P(*p) for p in pts]
    d = f"M{pts[0][0]:.1f},{pts[0][1]:.1f}"
    for i in range(len(pts) - 1):
        p0 = pts[i - 1] if i else pts[i]; p1 = pts[i]; p2 = pts[i + 1]
        p3 = pts[i + 2] if i + 2 < len(pts) else p2
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f"C{c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}"
    return d

tramos, cur = [], []
for p in RUTA:
    if p == "parada":
        tramos.append(cur); cur = []
    else:
        cur.append(p)
tramos.append(cur)
ruta_d = " ".join(suave(t) for t in tramos)

# Etiquetas: (dx, dy, anclaje)
ET = {
    "Sagunto": (-12, -14, "end"), "Roma": (10, -10, "start"), "Pompeya": (12, 16, "start"),
    "Siracusa": (-12, 20, "end"), "Ítaca": (-12, -12, "end"), "Delfos": (0, -20, "middle"),
    "Atenas": (12, 20, "start"), "Troya": (12, -8, "start"), "Éfeso": (12, 6, "start"),
    "Alejandría": (12, 18, "start"),
}
GR = {"Atenas": "Ἀθῆναι", "Delfos": "Δελφοί", "Troya": "Ἴλιον", "Éfeso": "Ἔφεσος", "Ítaca": "Ἰθάκη",
      "Roma": "Roma", "Pompeya": "Pompeii", "Siracusa": "Συράκουσαι", "Sagunto": "Saguntum",
      "Alejandría": "Ἀλεξάνδρεια"}

lugares = []
for n, (lon, lat) in L.items():
    x, y = P(lon, lat); dx, dy, a = ET[n]
    lugares.append(
        f'<g class="lugar"><circle cx="{x:.1f}" cy="{y:.1f}" r="5.2"/>'
        f'<text x="{x+dx:.1f}" y="{y+dy:.1f}" text-anchor="{a}">{n}'
        f'<tspan class="antiguo" x="{x+dx:.1f}" dy="15">{GR[n]}</tspan></text></g>')

mares = [("Mar Mediterráneo", 20.5, 33.9, 0, "grande"), ("Mar Tirreno", 12.0, 39.3, 0, ""),
         ("Mar Jónico", 18.4, 36.4, 0, ""), ("Mar Egeo", 25.2, 36.45, 0, ""),
         ("Mar Adriático", 16.0, 42.75, -37, ""), ("Mar Negro", 31.3, 43.6, 0, "")]
mtxt = []
for t, lon, lat, rot, c in mares:
    x, y = P(lon, lat)
    sp = ' letter-spacing="7"' if c else ' letter-spacing="3"'
    mtxt.append(f'<text class="mar {c}" x="{x:.1f}" y="{y:.1f}" text-anchor="middle"{sp} transform="rotate({rot} {x:.1f} {y:.1f})">{t}</text>')

# Retícula cada 5°
ret = []
for lon in range(0, 34, 5):
    x, _ = P(lon, 0); ret.append(f"M{x:.1f},0V{H}")
for lat in range(30, 46, 5):
    _, y = P(0, lat); ret.append(f"M0,{y:.1f}H{W}")
ret_d = "".join(ret)

sx, sy = P(*L["Sagunto"])
svg = f'''<svg class="mapa-ruta" viewBox="0 0 {W} {H}" role="img" aria-labelledby="mapa-t mapa-d" xmlns="http://www.w3.org/2000/svg">
<title id="mapa-t">La ruta de Ecos por el Mediterráneo</title>
<desc id="mapa-d">Mapa del Mediterráneo. Isabel y Mini Odi, dibujados, corren por el norte de África. Una ruta discontinua sale de Sagunto y pasa por Roma, Pompeya, Siracusa, Ítaca, Delfos, Atenas, Troya y Éfeso hasta Alejandría.</desc>
<defs>
  <path id="tierra-forma" d="{land_d}"/>
  <clipPath id="mapa-marco"><rect width="{W}" height="{H}"/></clipPath>
</defs>
<g clip-path="url(#mapa-marco)">
  <rect class="mar-fondo" width="{W}" height="{H}"/>
  <path class="reticula" d="{ret_d}"/>
  <use class="costa-3" href="#tierra-forma"/>
  <use class="costa-2" href="#tierra-forma"/>
  <use class="costa-1" href="#tierra-forma"/>
  <use class="tierra" href="#tierra-forma"/>
  {''.join(mtxt)}
  <path class="ruta" d="{ruta_d}"/>
  {''.join(lugares)}
  <ellipse cx="330" cy="758" rx="215" ry="11" fill="#421C2A" opacity=".13"/>
  <image class="personajes" href="imagenes/personajes-ruta.webp" x="105" y="440" width="472" height="329">
    <title>Isabel y Mini Odi, dibujados, corren por la ruta</title>
  </image>
</g>
<rect class="marco" x="0.5" y="0.5" width="{W-1}" height="{H-1}"/>
</svg>'''
open(sys.argv[2], "w").write(svg)
print(W, H, len(svg) // 1024, "KB")
