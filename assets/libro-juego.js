/* El enigma del libro: dibuja el título, el acertijo, la ruta y la línea del tiempo
   a partir de assets/libro-datos.js. Aquí no hay ningún secreto: solo se pinta lo desvelado. */
(function () {
  var D = window.ECOS_LIBRO;
  if (!D) return;
  var NS = 'http://www.w3.org/2000/svg';
  function el(tag, attrs, padre) {
    var e = document.createElementNS(NS, tag);
    for (var k in attrs) e.setAttribute(k, attrs[k]);
    if (padre) padre.appendChild(e);
    return e;
  }
  function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }
  function revelados(lista) { return lista.filter(function (x) { return x.estado === 'revelado'; }).length; }

  /* ---------- Lacre (sello de cera) ---------- */
  function lacre(g, r) {
    var gotas = [[0, -1], [0.82, -0.57], [1, 0.12], [0.55, 0.86], [-0.42, 0.92], [-0.98, 0.25], [-0.75, -0.7]];
    gotas.forEach(function (p, i) { el('circle', { cx: p[0] * r * 0.98, cy: p[1] * r * 0.98, r: r * (i % 2 ? 0.3 : 0.24), class: 'lacre-gota' }, g); });
    el('circle', { r: r, class: 'lacre-cuerpo' }, g);
    el('circle', { r: r * 0.7, class: 'lacre-anillo' }, g);
    var t = el('text', { y: r * 0.36, class: 'lacre-signo', 'font-size': r * 1.05 }, g);
    t.textContent = '?';
  }

  /* ---------- Título ---------- */
  var cajaTitulo = document.getElementById('libro-titulo');
  if (cajaTitulo) {
    var T = D.titulo || { estado: 'sellado' };
    if (T.estado === 'revelado') {
      cajaTitulo.innerHTML = '<p class="titulo-revelado">' + esc(T.titulo) + '</p>' + (T.subtitulo ? '<p class="titulo-subtitulo">' + esc(T.subtitulo) + '</p>' : '');
    } else if (T.estado === 'parcial' && T.palabras) {
      cajaTitulo.innerHTML = '<div class="titulo-fichas" role="img" aria-label="Título parcialmente desvelado">' +
        T.palabras.map(function (p) {
          return '<span class="titulo-palabra">' + p.split('').map(function (c) {
            return '<span class="titulo-letra' + (c === '_' ? ' oculta' : '') + '">' + (c === '_' ? '' : esc(c)) + '</span>';
          }).join('') + '</span>';
        }).join('') + '</div><p class="titulo-pie">Algunas casillas ya se han abierto. El resto, con los próximos acertijos.</p>';
    } else {
      cajaTitulo.innerHTML = '<div class="titulo-sellado"><svg viewBox="-40 -40 80 80" class="titulo-lacre" aria-hidden="true"></svg>' +
        '<p><strong>El título está sellado.</strong><br>Se irá abriendo poco a poco: una pista, una letra, una palabra.</p></div>';
      lacre(cajaTitulo.querySelector('svg'), 26);
    }
  }

  /* ---------- Acertijo ---------- */
  var cajaAcertijo = document.getElementById('libro-acertijo');
  var formAcertijo = document.getElementById('libro-acertijo-form');
  if (cajaAcertijo) {
    var A = D.acertijo;
    if (A && A.texto) {
      cajaAcertijo.innerHTML = '<p class="acertijo-numero">Acertijo ' + esc(A.numero || '') + (A.fecha ? ' · ' + esc(A.fecha) : '') + '</p>' +
        '<blockquote class="acertijo-texto">' + esc(A.texto) + '</blockquote>' +
        (A.pista ? '<p class="acertijo-pista">Pista: ' + esc(A.pista) + '</p>' : '');
      if (formAcertijo) { formAcertijo.hidden = false; formAcertijo.dataset.etiqueta = 'Acertijo ' + (A.numero || ''); }
    } else {
      cajaAcertijo.innerHTML = '<p class="acertijo-espera">El primer acertijo está al caer. Lo recibirá antes que nadie quien esté suscrito a <a href="suscribete.html">la newsletter de los lunes</a>.</p>';
    }
  }

  /* ---------- Contadores ---------- */
  var cuenta = document.getElementById('libro-progreso');
  if (cuenta) {
    cuenta.innerHTML = '<span><strong>' + revelados(D.lugares) + '</strong> de ' + D.lugares.length + ' lugares desvelados</span>' +
      '<span><strong>' + revelados(D.fechas) + '</strong> de ' + D.fechas.length + ' fechas desveladas</span>';
  }

  /* ---------- Mapa ---------- */
  var lienzo = document.getElementById('libro-mapa');
  var ficha = document.getElementById('libro-mapa-ficha');
  if (lienzo) {
    var svg = el('svg', { viewBox: '0 0 1774 887', class: 'mapa-ruta libro-mapa', role: 'img', 'aria-label': 'Mapa de la ruta del libro, con los lugares todavía sellados' }, lienzo);
    el('image', { href: 'imagenes/mapa-ilustrado.jpg', width: 1774, height: 887 }, svg);
    var porId = {}; D.lugares.forEach(function (l) { porId[l.id] = l; });
    var pts = (D.ruta || []).map(function (id) { return porId[id]; }).filter(Boolean);
    if (pts.length > 1) {
      // curva suave que pasa por todos los puntos (Catmull-Rom convertida a Bézier)
      var d = 'M' + pts[0].x + ',' + pts[0].y;
      for (var i = 0; i < pts.length - 1; i++) {
        var p0 = pts[i - 1] || pts[i], p1 = pts[i], p2 = pts[i + 1], p3 = pts[i + 2] || p2;
        var c1x = p1.x + (p2.x - p0.x) / 6, c1y = p1.y + (p2.y - p0.y) / 6;
        var c2x = p2.x - (p3.x - p1.x) / 6, c2y = p2.y - (p3.y - p1.y) / 6;
        d += ' C' + c1x.toFixed(1) + ',' + c1y.toFixed(1) + ' ' + c2x.toFixed(1) + ',' + c2y.toFixed(1) + ' ' + p2.x + ',' + p2.y;
      }
      el('path', { d: d, class: 'libro-ruta-sombra' }, svg);
      el('path', { d: d, class: 'libro-ruta' }, svg);
    }
    D.lugares.forEach(function (l) {
      var g = el('g', { class: 'libro-lugar ' + l.estado, transform: 'translate(' + l.x + ' ' + l.y + ')', tabindex: '0', role: 'button' }, svg);
      if (l.estado === 'revelado') {
        g.setAttribute('aria-label', l.nombre + ': ver qué ocurre aquí');
        el('circle', { r: 20, class: 'zona' }, g);
        el('circle', { r: 8, class: 'punto' }, g);
        var t = el('text', { x: l.dx || 0, y: l.dy || -16, 'text-anchor': l.ancla || 'middle' }, g);
        t.textContent = l.nombre;
      } else {
        g.setAttribute('aria-label', 'Lugar sellado');
        el('circle', { r: 28, class: 'zona' }, g);
        lacre(el('g', { class: 'lacre' }, g), 17);
      }
      function abrir() {
        if (!ficha) return;
        if (l.estado === 'revelado') {
          ficha.innerHTML = '<p class="libro-ficha-cap">' + esc(l.capitulo || '') + '</p><p class="libro-ficha-nombre">' + esc(l.nombre) + '</p><p>' + esc(l.texto || '') + '</p>';
        } else {
          ficha.innerHTML = '<p class="libro-ficha-nombre">Lugar sellado</p><p>Aquí ocurre algo que cuento en el libro. Se desvelará más adelante… o antes, si alguien resuelve el acertijo.</p>';
        }
        ficha.hidden = false;
      }
      g.addEventListener('click', abrir);
      g.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); abrir(); } });
    });
  }

  /* ---------- Línea del tiempo ---------- */
  var linea = document.getElementById('libro-linea');
  var fichaT = document.getElementById('libro-linea-ficha');
  if (linea) {
    var W = 1000, EJE = 178, X0 = 40, X1 = 850, HOY = 950, A0 = -800, A1 = 150;
    function xDe(a) { return a === 'hoy' ? HOY : X0 + (a - A0) / (A1 - A0) * (X1 - X0); }
    var s = el('svg', { viewBox: '0 0 ' + W + ' 240', class: 'libro-linea-svg', role: 'img', 'aria-label': 'Línea del tiempo del libro, con las fechas todavía selladas' }, linea);
    el('line', { x1: X0 - 20, y1: EJE, x2: X1 + 15, y2: EJE, class: 'eje' }, s);
    el('line', { x1: X1 + 40, y1: EJE, x2: HOY + 30, y2: EJE, class: 'eje' }, s);
    // corte entre la Antigüedad y hoy
    el('path', { d: 'M' + (X1 + 20) + ',' + (EJE + 9) + ' l8,-18 M' + (X1 + 30) + ',' + (EJE + 9) + ' l8,-18', class: 'corte' }, s);
    [[-800, '800 a. n. e.'], [-600, '600'], [-400, '400'], [-200, '200'], [1, '1 n. e.'], [100, '100']].forEach(function (m) {
      var x = xDe(m[0]);
      el('line', { x1: x, y1: EJE - 5, x2: x, y2: EJE + 5, class: 'marca' }, s);
      el('text', { x: x, y: EJE + 24, class: 'etiqueta' }, s).textContent = m[1];
    });
    el('text', { x: HOY, y: EJE + 24, class: 'etiqueta hoy' }, s).textContent = 'Hoy';
    el('text', { x: (xDe(-800) + xDe(-500)) / 2, y: 225, class: 'era' }, s).textContent = 'Grecia arcaica';
    el('text', { x: (xDe(-480) + xDe(-323)) / 2, y: 225, class: 'era' }, s).textContent = 'Atenas clásica';
    el('text', { x: (xDe(-200) + xDe(120)) / 2, y: 225, class: 'era' }, s).textContent = 'Roma, de la República al Imperio';

    var carriles = [];
    D.fechas.slice().sort(function (a, b) { return xDe(a.anno) - xDe(b.anno); }).forEach(function (f) {
      var x = xDe(f.anno), c = 0;
      while (carriles[c] !== undefined && x - carriles[c] < 26) c++;
      carriles[c] = x;
      var y = EJE - 32 - c * 30;
      el('line', { x1: x, y1: y + 9, x2: x, y2: EJE, class: 'tallo' }, s);
      var g = el('g', { class: 'libro-fecha ' + f.estado, transform: 'translate(' + x.toFixed(1) + ' ' + y + ')', tabindex: '0', role: 'button' }, s);
      el('circle', { r: 15, class: 'zona' }, g);
      if (f.estado === 'revelado') {
        g.setAttribute('aria-label', (f.etiqueta || '') + ': ' + (f.titulo || ''));
        el('circle', { r: 7, class: 'punto' }, g);
      } else {
        g.setAttribute('aria-label', 'Fecha sellada');
        lacre(el('g', { class: 'lacre' }, g), 11);
      }
      function abrir() {
        if (!fichaT) return;
        fichaT.innerHTML = f.estado === 'revelado'
          ? '<p class="libro-ficha-cap">' + esc(f.etiqueta || '') + '</p><p class="libro-ficha-nombre">' + esc(f.titulo || '') + '</p><p>' + esc(f.texto || '') + '</p>'
          : '<p class="libro-ficha-nombre">Fecha sellada</p><p>Un momento de la historia que aparece en el libro. Pronto sabrás cuál.</p>';
        fichaT.hidden = false;
      }
      g.addEventListener('click', abrir);
      g.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); abrir(); } });
    });
  }
})();
