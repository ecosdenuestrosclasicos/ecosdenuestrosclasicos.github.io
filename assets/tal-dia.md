```{=html}
<!-- «Tal día como hoy» en la portada: fecha romana calculada cada día + efeméride (datos en assets/efemerides.js) -->
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
    <p class="tal-dia-fuente"></p>
    <p class="tal-dia-correo"><a href="suscribete.html">Recibe cada lunes las efemérides de la semana en tu correo</a></p>
  </div>
</section>
<script src="assets/fecha-romana.js"></script>
<script src="assets/efemerides.js"></script>
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

  var e = EF[clave(hoy)], cuando = caja.querySelector('.tal-dia-cuando');
  if (e) {
    cuando.textContent = 'Tal día como hoy · ' + e.anno;
  } else {
    for (var i = 1; i <= 366 && !e; i++) {
      var f = new Date(hoy); f.setDate(hoy.getDate() + i);
      if (EF[clave(f)]) {
        e = EF[clave(f)];
        cuando.textContent = 'Dentro de ' + (i === 1 ? 'un día' : i + ' días') + ', el ' + f.getDate() + ' de ' + MES_ES[f.getMonth()] + ' · ' + e.anno;
      }
    }
  }
  if (!e) return;
  caja.querySelector('.tal-dia-que').textContent = e.titulo;
  caja.querySelector('.tal-dia-texto').textContent = e.texto;
  caja.querySelector('.tal-dia-fuente').textContent = 'Fuente: ' + e.fuente;
  caja.hidden = false;
})();
</script>
```
