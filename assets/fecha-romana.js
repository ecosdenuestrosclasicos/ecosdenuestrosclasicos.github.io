/* Fecha en el calendario romano (Kalendas, Nonas, Idus, día bisiesto).
   La usan la caja «Tal día como hoy» de la portada y el correo de la newsletter. */
(function (raiz) {
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

  var api = { fechaRomana: fechaRomana, MES_ES: MES_ES };
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  else raiz.ECOS_FECHA = api;
})(typeof window !== 'undefined' ? window : globalThis);
