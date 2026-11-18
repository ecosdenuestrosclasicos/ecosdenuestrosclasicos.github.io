```{=html}
<!-- «Tal día como hoy» en la portada: fecha romana calculada cada día + curiosidad del día
     (datos en assets/efemerides.js) + palabra del día griega y latina (assets/palabras-dia.js) -->
<section class="tal-dia" aria-labelledby="tal-dia-titulo" hidden>
  <div class="tal-dia-fecha">
    <p class="tal-dia-etiqueta" id="tal-dia-titulo">Hoy en el calendario romano</p>
    <p class="tal-dia-romana" lang="la"></p>
    <p class="tal-dia-larga" lang="la"></p>
    <p class="tal-dia-hoy"></p>
  </div>
  <div class="tal-dia-suceso">
    <p class="tal-dia-cuando"></p>
    <h2 class="tal-dia-que"></h2>
    <p class="tal-dia-texto"></p>
    <p class="tal-dia-mas"><a class="tal-dia-enlace" href="efemerides.html">Leer la historia completa</a> · <a href="efemerides.html">las 366 curiosidades del año</a></p>
    <p class="tal-dia-correo"><a href="suscribete.html">Recibe cada lunes las curiosidades de la semana en tu correo</a></p>
  </div>
</section>
<section class="palabra-dia" aria-label="Palabras del día" hidden>
  <div class="palabra-dia-caja" data-lengua="griego">
    <p class="palabra-dia-etiqueta">Palabra griega del día</p>
    <p class="palabra-dia-forma" lang="grc"></p>
    <p class="palabra-dia-lema"></p>
    <p class="palabra-dia-nota"></p>
  </div>
  <div class="palabra-dia-caja" data-lengua="latin">
    <p class="palabra-dia-etiqueta">Palabra latina del día</p>
    <p class="palabra-dia-forma" lang="la"></p>
    <p class="palabra-dia-lema"></p>
    <p class="palabra-dia-nota"></p>
  </div>
</section>
<script src="assets/fecha-romana.js"></script>
<script src="assets/efemerides.js"></script>
<script src="assets/palabras-dia.js"></script>
<script src="assets/palabra-dia.js"></script>
<script>
(function () {
  var caja = document.querySelector('.tal-dia');
  if (!caja || !window.ECOS_EFEMERIDES || !window.ECOS_FECHA) return;
  var EF = window.ECOS_EFEMERIDES;
  var fechaRomana = window.ECOS_FECHA.fechaRomana, MES_ES = window.ECOS_FECHA.MES_ES;
  function clave(f) { return ('0' + (f.getMonth() + 1)).slice(-2) + '-' + ('0' + f.getDate()).slice(-2); }

  var hoy = new Date(); hoy.setHours(12, 0, 0, 0);
  var r = fechaRomana(hoy);
  caja.querySelector('.tal-dia-romana').textContent = r.corta;
  caja.querySelector('.tal-dia-larga').textContent = r.larga;
  caja.querySelector('.tal-dia-hoy').textContent = hoy.getDate() + ' de ' + MES_ES[hoy.getMonth()];

  var k = clave(hoy), e = EF[k];
  if (!e) return;
  caja.querySelector('.tal-dia-cuando').textContent = (/^(calendario|por estas|mito)/.test(e.anno) ? 'Hoy · ' : 'Tal día como hoy · ') + e.anno;
  caja.querySelector('.tal-dia-que').textContent = e.titulo;
  caja.querySelector('.tal-dia-texto').textContent = e.texto;
  caja.querySelector('.tal-dia-enlace').href = 'efemerides.html#d-' + k;
  caja.hidden = false;
})();
</script>
```
