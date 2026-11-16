"""Capa interactiva del mapa de la portada: ruta circular (con salida y llegada en Valencia),
paradas que se pueden pulsar, fichas con información, el barco que navega hasta cada parada
y el «nóstos»: cuando se visitan todas, la recompensa en casa es una paella."""
import json, html
d = json.load(open("/home/claude/mapa/v3_datos.json"))
W, H = 1774, 887
FONDO = "imagenes/mapa-ilustrado.jpg"
BARCO = "imagenes/barco-ruta.webp"

# Fichas de cada parada: (texto, enlace o None, texto del enlace)
FICHAS = {
 "Valencia": ("Casa. Los romanos la fundaron en el 138 a. n. e. con el nombre de Valentia. Como Odiseo al llegar a Ítaca, aquí termina el viaje… y el regreso merece banquete: una buena paella.", "sobre-mi.html", "Conoce a Isabel"),
 "Sagunto": ("Arse para los íberos, Saguntum para los romanos. El asedio de Aníbal en el 219 a. n. e. desencadenó la segunda guerra púnica. De aquí zarpa el barco de Ecos.", None, None),
 "Segovia": ("Su acueducto romano, de finales del siglo I o comienzos del II n. e., se sostiene sin argamasa: piedra sobre piedra. Una escapada a pie desde la costa.", None, None),
 "Roma": ("La ciudad cuya República se resquebraja en la Conjuración de Catilina de Salustio, el texto que Isa estudió en su trabajo de fin de grado.", "investigacion/salustio-catilina.html", "Ver la investigación"),
 "Pompeya": ("El Vesubio la sepultó en el 79 n. e. Plinio el Joven contó la erupción en dos cartas a Tácito, y gracias a la ceniza hoy podemos pasear por sus calles.", None, None),
 "Siracusa": ("La gran ciudad griega de Sicilia. Aquí terminó la expedición ateniense de 415 a 413 a. n. e., que Tucídides narra en los libros VI y VII de su Historia.", "lecturas.html", "Tucídides en el fichero"),
 "Ítaca": ("La patria de Odiseo. Tardó diez años en volver a casa desde Troya, y la Odisea canta ese regreso: el nóstos.", "videos.html", "La serie sobre la Odisea"),
 "Atenas": ("La ciudad de la democracia, del ostracismo, de Sócrates y de Tucídides. Muchas de las palabras con las que hablamos de política nacieron aquí.", "lecturas.html", "Autores griegos en el fichero"),
 "Troya": ("Ilión, en la costa de Anatolia. Tras diez años de guerra, de aquí parte Odiseo en su largo viaje de vuelta.", None, None),
 "Éfeso": ("Una de las grandes ciudades griegas de Asia Menor. La Biblioteca de Celso, del siglo II n. e., guardaba miles de rollos.", None, None),
 "Alejandría": ("La ciudad de la gran Biblioteca y del Faro, una de las siete maravillas del mundo antiguo.", "biblioteca.html", "Entra en la biblioteca de Ecos"),
 "Giza": ("Las pirámides ya eran antiquísimas para los propios griegos: Heródoto las describe en el libro II de su Historia. Escapada a pie siguiendo el Nilo.", None, None),
 "Petra": ("La capital de los nabateos, tallada en la roca rosada. Roma la incorporó en el 106 n. e. a la nueva provincia de Arabia.", None, None),
 "Cartago": ("La gran rival de Roma en las guerras púnicas, con su famoso puerto circular. Roma la destruyó en el 146 a. n. e.", None, None),
}
ORDEN = ["Valencia", "Sagunto", "Segovia", "Roma", "Pompeya", "Siracusa", "Ítaca", "Atenas", "Troya", "Éfeso", "Alejandría", "Giza", "Petra", "Cartago"]
TIERRA = {"Segovia": "Sagunto", "Giza": "Alejandría", "Petra": "Alejandría"}   # escapadas: el barco espera en este puerto

lug = []
for n in ORDEN:
    x, y = d["lugares"][n]; dx, dy, a = d["et"][n]
    clases = "lugar" + (" a-pie" if n in TIERRA else "") + (" casa" if n == "Valencia" else "")
    r = 6 if n not in TIERRA else 4.5
    lug.append(
        f'<g class="{clases}" data-lugar="{n}" tabindex="0" role="button" aria-label="{n}: ver ficha">'
        f'<circle class="zona" cx="{x:.1f}" cy="{y:.1f}" r="18"/>'
        f'<circle class="punto" cx="{x:.1f}" cy="{y:.1f}" r="{r}"/>'
        f'<text x="{x+dx:.1f}" y="{y+dy:.1f}" text-anchor="{a}">{n}'
        f'<tspan class="antiguo" x="{x+dx:.1f}" dy="16">{d["ant"][n]}</tspan></text></g>')

mares = [f'<text class="mar" x="{x:.1f}" y="{y:.1f}" font-size="{fs}" letter-spacing="{ls}" text-anchor="middle" transform="rotate({rot} {x:.1f} {y:.1f})">{t}</text>'
         for t, x, y, rot, fs, ls in d["mares"]]

# paella en tierra, al oeste de Valencia, unida con una línea de puntos
vx, vy = d["lugares"]["Valencia"]
px, py = vx + 44, vy + 74
paella = f'''<g class="paella" data-lugar="Valencia" tabindex="-1" aria-hidden="true">
  <line x1="{vx:.1f}" y1="{vy:.1f}" x2="{px-10:.1f}" y2="{py-18:.1f}" class="paella-hilo"/>
  <g transform="translate({px:.1f} {py:.1f}) scale(1.5)">
    <circle r="27" class="paella-aura"/>
    <path d="M-26,-2 h-9 a3,3 0 0 0 0,6 h9z M26,-2 h9 a3,3 0 0 1 0,6 h-9z" fill="#3B3B3B" stroke="#1F1A17" stroke-width="1"/>
    <ellipse rx="25" ry="15" fill="#4A4A4A" stroke="#1F1A17" stroke-width="1.6"/>
    <ellipse rx="21.5" ry="12" fill="#E9A93A"/>
    <ellipse rx="21.5" ry="12" fill="none" stroke="#C47A1F" stroke-width="1.2" opacity=".7"/>
    <g fill="#F2C55C" opacity=".9">{''.join(f'<circle cx="{cx}" cy="{cy}" r="1.1"/>' for cx, cy in [(-14,-4),(-8,3),(-2,-6),(5,4),(12,-3),(15,5),(-15,5),(0,8),(9,-8),(-6,-9)])}</g>
    <path d="M-12,-3 q4,-3 8,0 M3,5 q4,-3 8,0 M8,-6 q4,-3 8,0" stroke="#C0392B" stroke-width="2.4" fill="none" stroke-linecap="round"/>
    <path d="M-16,4 l7,-2 M-3,-2 l7,2 M10,3 l6,-3" stroke="#5E8C31" stroke-width="2.2" stroke-linecap="round"/>
    <path d="M-4,7 a5,4 0 1 1 7,-1" fill="#F08C6A" stroke="#B35238" stroke-width="1.2"/>
    <path d="M14,-10 l7,-3 l-1,7 z" fill="#F7E36B" stroke="#B59B2A" stroke-width="1"/>
  </g>
  <text class="paella-texto" x="{px:.1f}" y="{py+40:.1f}" text-anchor="middle">la recompensa</text>
</g>'''

svg = f'''<svg class="mapa-ruta" viewBox="0 0 {W} {H}" role="img" aria-labelledby="mapa-t mapa-d" xmlns="http://www.w3.org/2000/svg">
<title id="mapa-t">La ruta de Ecos por el Mediterráneo</title>
<desc id="mapa-d">Mapa ilustrado e interactivo del Mediterráneo, con costas y lugares en su posición real. Isabel y Mini Odi, dibujados, corren por el norte de África. Una ruta circular en barco sale de Valencia y Sagunto y pasa por Roma, Pompeya, Siracusa, Ítaca, Atenas, Troya, Éfeso, Alejandría y Cartago antes de volver a casa, donde espera una paella. Tres escapadas a pie llevan a Segovia, Guiza y Petra. Cada parada se puede pulsar para ver su ficha.</desc>
<image href="{FONDO}" width="{W}" height="{H}"/>
{''.join(mares)}
<path id="ruta-lazo" class="ruta" d="{d["ruta"]}"/>
{''.join(f'<path class="escapada" d="{e}"/>' for e in d["escapadas"])}
{paella}
{''.join(lug)}
<g class="barco"><image href="{BARCO}" x="-38" y="-56" width="76" height="64"/></g>
<rect x=".5" y=".5" width="{W-1}" height="{H-1}" fill="none" stroke="#A78658"/>
</svg>'''

fichas_js = json.dumps({n: {"t": t, "ant": d["ant"][n], "url": u, "ut": ut} for n, (t, u, ut) in FICHAS.items()}, ensure_ascii=False)
tierra_js = json.dumps(TIERRA, ensure_ascii=False)
lugares_js = json.dumps({n: d["lugares"][n] for n in ORDEN}, ensure_ascii=False)

script = '''<script>
(function () {
  var FICHAS = ''' + fichas_js + ''';
  var TIERRA = ''' + tierra_js + ''';
  var PUNTOS = ''' + lugares_js + ''';
  var lienzo = document.querySelector('.mapa-lienzo'); if (!lienzo) return;
  var svg = lienzo.querySelector('svg'), ruta = svg.getElementById ? svg.getElementById('ruta-lazo') : document.getElementById('ruta-lazo');
  var barco = svg.querySelector('.barco'), ficha = lienzo.querySelector('.mapa-ficha');
  var progreso = document.querySelector('.mapa-progreso-cuenta'), barra = document.querySelector('.mapa-progreso-barra span');
  var reducido = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var nombres = Object.keys(FICHAS), total = nombres.length;
  var visitados = {};
  try { visitados = JSON.parse(localStorage.getItem('ecos-nostos') || '{}'); } catch (e) {}

  /* --- barco: recorre la ruta y navega hasta la parada que pulses --- */
  var largo = ruta.getTotalLength(), f = 0.03, vuelta = 90000, animando = null, ultimo = null;
  function puntoEn(fr) { return ruta.getPointAtLength(((fr % 1) + 1) % 1 * largo); }
  function colocar(fr) {
    var a = puntoEn(fr), b = puntoEn(fr + 0.002), izq = b.x < a.x;
    var ang = Math.atan2(b.y - a.y, b.x - a.x) * 180 / Math.PI + (izq ? 180 : 0);
    ang = ((ang + 540) % 360) - 180; ang = Math.max(-20, Math.min(20, ang));
    barco.setAttribute('transform', 'translate(' + a.x + ' ' + (a.y + 8) + ') rotate(' + ang + ') scale(' + (izq ? -1 : 1) + ' 1)');
  }
  var POS = {};   // fracción de la ruta más cercana a cada parada
  (function () {
    var N = 900, muestras = [];
    for (var i = 0; i < N; i++) { var p = ruta.getPointAtLength(i / N * largo); muestras.push([p.x, p.y]); }
    Object.keys(PUNTOS).forEach(function (n) {
      var q = PUNTOS[TIERRA[n] || n], mejor = 0, dm = 1e9;
      muestras.forEach(function (m, i) { var dd = (m[0] - q[0]) * (m[0] - q[0]) + (m[1] - q[1]) * (m[1] - q[1]); if (dd < dm) { dm = dd; mejor = i; } });
      POS[n] = mejor / N;
    });
  })();
  function navegarA(n) {
    var destino = POS[n]; if (destino === undefined) return;
    var dist = ((destino - f) % 1 + 1) % 1, dur = reducido ? 0 : Math.max(700, dist * 9000), inicio = null, desde = f;
    animando = function (t) {
      if (inicio === null) inicio = t;
      var k = dur ? Math.min(1, (t - inicio) / dur) : 1, e = k < .5 ? 2 * k * k : 1 - Math.pow(-2 * k + 2, 2) / 2;
      f = desde + dist * e; colocar(f);
      if (k < 1) requestAnimationFrame(animando); else { animando = null; ultimo = null; }
    };
    requestAnimationFrame(animando);
  }
  colocar(f);
  if (!reducido) {
    (function paseo(t) {
      if (!animando) { if (ultimo !== null) f += (t - ultimo) / vuelta; colocar(f); ultimo = t; } else ultimo = null;
      requestAnimationFrame(paseo);
    })(performance.now());
  }

  /* --- fichas --- */
  function pintarProgreso() {
    var n = nombres.filter(function (k) { return visitados[k]; }).length;
    if (progreso) progreso.textContent = n + ' de ' + total;
    if (barra) barra.style.width = (n / total * 100) + '%';
    svg.querySelectorAll('.lugar').forEach(function (g) { g.classList.toggle('visitado', !!visitados[g.dataset.lugar]); });
    svg.classList.toggle('nostos-completo', n === total);
    return n;
  }
  function abrir(n, g) {
    var info = FICHAS[n]; if (!info) return;
    var antes = nombres.filter(function (k) { return visitados[k]; }).length;
    visitados[n] = true; try { localStorage.setItem('ecos-nostos', JSON.stringify(visitados)); } catch (e) {}
    var ahora = pintarProgreso();
    ficha.innerHTML = '';
    var h = document.createElement('p'); h.className = 'mapa-ficha-titulo'; h.textContent = n;
    var a = document.createElement('span'); a.className = 'mapa-ficha-antiguo'; a.textContent = info.ant; h.appendChild(a);
    var p = document.createElement('p'); p.className = 'mapa-ficha-texto'; p.textContent = info.t;
    ficha.appendChild(h); ficha.appendChild(p);
    if (ahora === total && antes < total && n === 'Valencia') {
      var cv = document.createElement('p'); cv.className = 'mapa-ficha-premio';
      cv.textContent = '¡Nóstos completado! Has recorrido todo el Mediterráneo y has vuelto a casa, como Odiseo a Ítaca. La recompensa es tuya: una paella. ¡Buen provecho!';
      ficha.appendChild(cv);
    } else if (ahora === total && antes < total) {
      var c = document.createElement('p'); c.className = 'mapa-ficha-premio';
      c.textContent = '¡Has visitado todas las paradas! Como Odiseo, ya puedes volver a casa: pulsa la paella de Valencia para recoger tu recompensa.';
      ficha.appendChild(c);
    } else if (n === 'Valencia' && ahora === total) {
      var c2 = document.createElement('p'); c2.className = 'mapa-ficha-premio';
      c2.textContent = 'Has vuelto a casa después de recorrer todo el Mediterráneo. La paella es tuya. ¡Buen provecho!';
      ficha.appendChild(c2);
    }
    if (info.url) { var l = document.createElement('a'); l.href = info.url; l.className = 'mapa-ficha-enlace'; l.textContent = info.ut; ficha.appendChild(l); }
    if (TIERRA[n]) { var t = document.createElement('p'); t.className = 'mapa-ficha-nota'; t.textContent = 'El barco te espera en ' + TIERRA[n] + '.'; ficha.appendChild(t); }
    var x = document.createElement('button'); x.type = 'button'; x.className = 'mapa-ficha-cerrar'; x.setAttribute('aria-label', 'Cerrar la ficha'); x.textContent = '×';
    x.addEventListener('click', cerrar); ficha.appendChild(x);
    ficha.hidden = false;
    // colocar la ficha junto al punto
    var rl = lienzo.getBoundingClientRect(), punto = g.querySelector('.punto').getBoundingClientRect();
    var cx = punto.left + punto.width / 2 - rl.left, cy = punto.top + punto.height / 2 - rl.top;
    var fw = ficha.offsetWidth, fh = ficha.offsetHeight, x0 = cx + 18, y0 = cy - fh / 2;
    if (x0 + fw > rl.width - 8) x0 = cx - fw - 18;
    y0 = Math.max(8, Math.min(y0, rl.height - fh - 8));
    ficha.style.left = Math.max(8, x0) + 'px'; ficha.style.top = y0 + 'px';
    navegarA(n);
  }
  function cerrar() { ficha.hidden = true; }
  svg.querySelectorAll('.lugar, .paella').forEach(function (g) {
    var n = g.dataset.lugar, real = svg.querySelector('.lugar[data-lugar="' + n + '"]');
    g.addEventListener('click', function (e) { e.stopPropagation(); abrir(n, real); });
    g.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); abrir(n, real); } });
  });
  document.addEventListener('click', function (e) { if (!ficha.contains(e.target)) cerrar(); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') cerrar(); });
  var reinicio = document.querySelector('.mapa-progreso-reiniciar');
  if (reinicio) reinicio.addEventListener('click', function () { visitados = {}; try { localStorage.removeItem('ecos-nostos'); } catch (e) {} pintarProgreso(); cerrar(); });
  pintarProgreso();
})();
</script>'''

estilo = '''<style>
.mapa-ruta .ruta { fill: none; stroke: #7A1F2E; stroke-width: 3; stroke-dasharray: 11 7; stroke-linecap: round; }
.mapa-ruta .escapada { fill: none; stroke: #7A1F2E; stroke-width: 2.2; stroke-dasharray: 1.5 6; stroke-linecap: round; }
.mapa-ruta .lugar { cursor: pointer; outline: none; }
.mapa-ruta .lugar .zona { fill: transparent; }
.mapa-ruta .lugar .punto { fill: #FBF3E2; stroke: #7A1F2E; stroke-width: 3; transition: r .2s ease, fill .2s ease; }
.mapa-ruta .lugar.a-pie .punto { stroke-width: 2.4; }
.mapa-ruta .lugar.visitado .punto { fill: #7A1F2E; }
.mapa-ruta .lugar.casa .punto { fill: #E9C46A; stroke: #7A1F2E; }
.mapa-ruta .lugar:hover .punto, .mapa-ruta .lugar:focus-visible .punto { r: 9; }
.mapa-ruta .lugar:focus-visible text { text-decoration: underline; }
.mapa-ruta .lugar text { font-family: "IM Fell English", Georgia, serif; font-size: 22px; fill: #3B1A22; paint-order: stroke; stroke: #F5E7C6; stroke-width: 5px; stroke-linejoin: round; }
.mapa-ruta .lugar .antiguo { font-family: "EB Garamond", Georgia, serif; font-style: italic; font-size: 14.5px; fill: #5A4A32; stroke-width: 4px; }
.mapa-ruta .mar { font-family: "IM Fell English", Georgia, serif; font-style: italic; fill: #2F5578; opacity: .85; pointer-events: none; }
.mapa-ruta .paella { cursor: pointer; }
.mapa-ruta .paella-hilo { stroke: #7A1F2E; stroke-width: 1.6; stroke-dasharray: 2 4; }
.mapa-ruta .paella-aura { fill: #FFF3C9; opacity: 0; }
.mapa-ruta .paella-texto { font-family: "EB Garamond", Georgia, serif; font-style: italic; font-size: 15px; fill: #3B1A22; paint-order: stroke; stroke: #EAF2F7; stroke-width: 4px; }
.mapa-ruta .paella:hover > g { filter: drop-shadow(0 0 6px #FFE08A); }
.mapa-ruta.nostos-completo .paella-aura { opacity: .85; animation: paella-brilla 1.8s ease-in-out infinite; }
@keyframes paella-brilla { 50% { opacity: .35; } }
@media (prefers-reduced-motion: reduce) { .mapa-ruta.nostos-completo .paella-aura { animation: none; } }
</style>'''

figura = f'''```{{=html}}
<figure class="lamina lamina-ilustrada">
<div class="mapa-lienzo">
{estilo}
{svg}
<div class="mapa-ficha" role="dialog" aria-live="polite" hidden></div>
</div>
<figcaption>Isabel y Mini Odi, de ruta por el Mediterráneo. Las costas y cada monumento están en su lugar real. <strong>Pulsa cada parada</strong> para ver su ficha y mandar allí el barco.<span class="lamina-pista">Desliza para recorrer el mapa.</span></figcaption>
</figure>
<div class="mapa-progreso">
  <p class="mapa-progreso-texto"><strong>Tu nóstos, el viaje de vuelta a casa.</strong> Los héroes griegos, como Odiseo, tenían que regresar a casa después de la aventura. Visita todas las paradas del mapa y, al final, en Valencia te espera la recompensa.</p>
  <p class="mapa-progreso-estado">Paradas visitadas: <span class="mapa-progreso-cuenta">0 de 14</span> <button type="button" class="mapa-progreso-reiniciar">Empezar de nuevo</button></p>
  <div class="mapa-progreso-barra" aria-hidden="true"><span></span></div>
</div>
{script}
```
'''
open("/home/claude/mapa/mapa-ruta-interactivo.md", "w").write(figura)
print(len(figura) // 1024, "KB")
