/* Rellena las cajas .palabra-dia (portada y página de efemérides) con la palabra griega
   y la latina de hoy. Las listas están en assets/palabras-dia.js. */
(function () {
  var P = window.ECOS_PALABRAS_DIA;
  var zona = document.querySelector('.palabra-dia');
  if (!P || !zona) return;
  var hoy = new Date(); hoy.setHours(12, 0, 0, 0);
  var inicio = new Date(hoy.getFullYear(), 0, 1, 12);
  var n = Math.round((hoy - inicio) / 864e5) + 366 * (hoy.getFullYear() % 7);
  function poner(lengua, p) {
    var c = zona.querySelector('[data-lengua="' + lengua + '"]');
    if (!c || !p) return;
    if (lengua === 'griego') {
      c.querySelector('.palabra-dia-forma').textContent = p[0];
      c.querySelector('.palabra-dia-lema').innerHTML = '<span lang="grc">' + p[1] + '</span> · <i>' + p[2] + '</i> · ' + p[3];
      c.querySelector('.palabra-dia-nota').textContent = p[4];
    } else {
      c.querySelector('.palabra-dia-forma').textContent = p[0];
      c.querySelector('.palabra-dia-lema').innerHTML = '<i lang="la">' + p[1] + '</i> · ' + p[2];
      c.querySelector('.palabra-dia-nota').textContent = p[3];
    }
  }
  poner('griego', P.griego[n % P.griego.length]);
  poner('latin', P.latin[n % P.latin.length]);
  zona.hidden = false;
})();
