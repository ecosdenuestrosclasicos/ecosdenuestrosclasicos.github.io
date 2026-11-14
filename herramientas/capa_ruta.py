"""Capa vectorial del mapa ilustrado: ruta circular, escapadas, nombres y barco."""
import json, sys
d = json.load(open("/home/claude/mapa/v3_datos.json"))
FONDO = sys.argv[1] if len(sys.argv) > 1 else "imagenes/mapa-ilustrado.jpg"
BARCO = sys.argv[2] if len(sys.argv) > 2 else "imagenes/barco-ruta.webp"
W, H = 1774, 887

PARADAS = ["Sagunto", "Roma", "Pompeya", "Siracusa", "Ítaca", "Atenas", "Troya", "Éfeso", "Alejandría", "Cartago"]
TIERRA = ["Segovia", "Giza", "Petra"]

lug = []
for n in PARADAS + TIERRA:
    x, y = d["lugares"][n]; dx, dy, a = d["et"][n]
    cls = "lugar" + (" a-pie" if n in TIERRA else "")
    lug.append(f'<g class="{cls}"><circle cx="{x:.1f}" cy="{y:.1f}" r="{6 if n in PARADAS else 4.5}"/>'
               f'<text x="{x+dx:.1f}" y="{y+dy:.1f}" text-anchor="{a}">{n}'
               f'<tspan class="antiguo" x="{x+dx:.1f}" dy="16">{d["ant"][n]}</tspan></text></g>')

mares = []
for t, x, y, rot, fs, ls in d["mares"]:
    mares.append(f'<text class="mar" x="{x:.1f}" y="{y:.1f}" font-size="{fs}" letter-spacing="{ls}" text-anchor="middle" transform="rotate({rot} {x:.1f} {y:.1f})">{t}</text>')

mon = []
for k, (lugar, esc, dx, dy, nombre) in d["monumentos"].items():
    x, y = d["lugares"][lugar]
    mon.append(f'<title>{nombre}</title>')

svg = f'''<svg class="mapa-ruta" viewBox="0 0 {W} {H}" role="img" aria-labelledby="mapa-t mapa-d" xmlns="http://www.w3.org/2000/svg">
<title id="mapa-t">La ruta de Ecos por el Mediterráneo</title>
<desc id="mapa-d">Mapa ilustrado del Mediterráneo, con costas y lugares en su posición real, dentro de un marco con columnas jónicas, laureles, un globo terráqueo, libros y un casco romano. Isabel y Mini Odi, dibujados, corren por el norte de África. Una ruta circular en barco sale de Sagunto y pasa por Roma, Pompeya, Siracusa, Ítaca, Atenas, Troya, Éfeso, Alejandría y Cartago antes de volver a Sagunto. Tres escapadas a pie llevan a Segovia, a Guiza y a Petra. Hay dibujos del acueducto de Segovia, el Coliseo, el Partenón, la Biblioteca de Celso en Éfeso, las pirámides y la Esfinge de Guiza y el Tesoro de Petra.</desc>
<style>
.mapa-ruta .ruta {{ fill: none; stroke: #7A1F2E; stroke-width: 3; stroke-dasharray: 11 7; stroke-linecap: round; }}
.mapa-ruta .escapada {{ fill: none; stroke: #7A1F2E; stroke-width: 2.2; stroke-dasharray: 1.5 6; stroke-linecap: round; }}
.mapa-ruta .lugar circle {{ fill: #FBF3E2; stroke: #7A1F2E; stroke-width: 3; }}
.mapa-ruta .lugar.a-pie circle {{ stroke-width: 2.4; }}
.mapa-ruta .lugar text {{ font-family: "IM Fell English", Georgia, serif; font-size: 22px; fill: #3B1A22; paint-order: stroke; stroke: #F5E7C6; stroke-width: 5px; stroke-linejoin: round; }}
.mapa-ruta .lugar .antiguo {{ font-family: "EB Garamond", Georgia, serif; font-style: italic; font-size: 14.5px; fill: #5A4A32; stroke-width: 4px; }}
.mapa-ruta .mar {{ font-family: "IM Fell English", Georgia, serif; font-style: italic; fill: #2F5578; opacity: .85; }}
</style>
<image href="{FONDO}" width="{W}" height="{H}"/>
{''.join(mares)}
<path id="ruta-lazo" class="ruta" d="{d["ruta"]}"/>
{''.join(f'<path class="escapada" d="{e}"/>' for e in d["escapadas"])}
{''.join(lug)}
<g class="barco"><image href="{BARCO}" x="-38" y="-56" width="76" height="64"/></g>
<script>
(function () {{
  var ruta = document.getElementById('ruta-lazo');
  var barco = document.querySelector('.mapa-ruta .barco');
  if (!ruta || !barco || !ruta.getTotalLength) return;
  var largo = ruta.getTotalLength(), vuelta = 90000, inicio = null, salida = 0.045;
  function colocar(f) {{
    var a = ruta.getPointAtLength(f * largo), b = ruta.getPointAtLength(Math.min(largo, f * largo + 2));
    var izquierda = b.x < a.x;
    var ang = Math.atan2(b.y - a.y, b.x - a.x) * 180 / Math.PI + (izquierda ? 180 : 0);
    ang = ((ang + 540) % 360) - 180; ang = Math.max(-20, Math.min(20, ang));
    barco.setAttribute('transform', 'translate(' + a.x + ' ' + (a.y + 8) + ') rotate(' + ang + ') scale(' + (izquierda ? -1 : 1) + ' 1)');
  }}
  colocar(salida);
  if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  function paso(t) {{
    if (inicio === null) inicio = t;
    colocar(((t - inicio) / vuelta + salida) % 1);
    requestAnimationFrame(paso);
  }}
  requestAnimationFrame(paso);
}})();
</script>
<rect x=".5" y=".5" width="{W-1}" height="{H-1}" fill="none" stroke="#A78658"/>
</svg>'''
open("/home/claude/mapa/v3_capa.svg", "w").write(svg)
print(len(svg) // 1024, "KB")
