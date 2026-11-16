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
  </div>
</section>
<script src="assets/efemerides.js"></script>
<script>
(function () {
  var caja = document.querySelector('.tal-dia');
  if (!caja || !window.ECOS_EFEMERIDES) return;
  var EF = window.ECOS_EFEMERIDES;

  /* Meses: acusativo (tras ante diem / pridie), ablativo (el mismo día) y abreviatura */
  var AC = ['Ianuarias','Februarias','Martias','Apriles','Maias','Iunias','Iulias','Augustas','Septembres','Octobres','Novembres','Decembres'];
  var AB = ['Ianuariis','Februariis','Martiis','Aprilibus','Maiis','Iuniis','Iuliis','Augustis','Septembribus','Octobribus','Novembribus','Decembribus'];
  var CORTO = ['Ian.','Feb.','Mart.','Apr.','Mai.','Iun.','Iul.','Aug.','Sept.','Oct.','Nov.','Dec.'];
  var MES_ES = ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre'];

  function romano(n) {
    var v = [[10,'X'],[9,'IX'],[5,'V'],[4,'IV'],[1,'I']], r = '';
    v.forEach(function (p) { while (n >= p[0]) { r += p[1]; n -= p[0]; } });
    return r;
  }
  function bisiesto(a) { return (a % 4 === 0 && a % 100 !== 0) || a % 400 === 0; }

  /* Fecha romana: Kalendas (día 1), Nonas (5, o 7 en marzo, mayo, julio y octubre),
     Idus (13, o 15 en esos meses). Se cuenta hacia atrás contando ambos extremos.
     En año bisiesto se repite el sexto día antes de las Kalendas de marzo (24 de febrero). */
  function fechaRomana(f) {
    var a = f.getFullYear(), m = f.getMonth(), d = f.getDate();
    var largo = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    var tardio = (m === 2 || m === 4 || m === 6 || m === 9);
    var non = tardio ? 7 : 5, idus = tardio ? 15 : 13;
    var bis = false;
    if (m === 1 && bisiesto(a)) {
      if (d === 24) bis = true;
      else if (d > 24) d = d - 1;
    }
    var hito, mesH, n;
    if (d === 1) return { corta: 'Kal. ' + CORTO[m], larga: 'Kalendis ' + AB[m] };
    if (d === non) return { corta: 'Non. ' + CORTO[m], larga: 'Nonis ' + AB[m] };
    if (d === idus) return { corta: 'Id. ' + CORTO[m], larga: 'Idibus ' + AB[m] };
    if (bis) { n = 6; hito = 'Kal'; mesH = 2; }
    else if (d < non) { n = non - d + 1; hito = 'Non'; mesH = m; }
    else if (d < idus) { n = idus - d + 1; hito = 'Id'; mesH = m; }
    else { n = largo[m] - d + 2; hito = 'Kal'; mesH = (m + 1) % 12; }
    var nombre = { Kal: ['Kal.', 'Kalendas'], Non: ['Non.', 'Nonas'], Id: ['Id.', 'Idus'] }[hito];
    if (n === 2) return { corta: 'prid. ' + nombre[0] + ' ' + CORTO[mesH], larga: 'pridie ' + nombre[1] + ' ' + AC[mesH] };
    var num = (bis ? 'bis ' : '') + romano(n);
    return { corta: 'a. d. ' + num + ' ' + nombre[0] + ' ' + CORTO[mesH], larga: 'ante diem ' + (bis ? 'bis ' : '') + romano(n) + ' ' + nombre[1] + ' ' + AC[mesH] };
  }

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
