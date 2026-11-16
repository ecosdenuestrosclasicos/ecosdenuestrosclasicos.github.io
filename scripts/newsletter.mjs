// Newsletter de Ecos de nuestros clásicos.
// Prepara el correo semanal (sale los lunes) y, con --enviar, lo manda a la lista de Brevo.
//
//   node scripts/newsletter.mjs semanal --vista   → escribe newsletter/vista-semanal.html
//   node scripts/newsletter.mjs semanal --enviar  → lo envía (necesita las variables de Brevo)
//   --fecha 2026-11-23                             → simula otro día
//
// Contenido: lo que Isa cuenta esa semana (newsletter/notas.md), la fecha romana de cada día
// con sus efemérides (assets/efemerides.js) y la cuenta atrás para el aniversario de Ecos.
// (El modo «diario» existe por si algún día se quiere, pero el envío automático solo usa el semanal.)
// Para pausar todos los envíos basta con crear el archivo newsletter/PAUSA.

import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);
const RAIZ = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..');
const WEB = 'https://ecosdenuestrosclasicos.com';
const { fechaRomana, MES_ES } = require(path.join(RAIZ, 'assets/fecha-romana.js'));
const DIAS_ES = ['domingo', 'lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado'];

// ---------- argumentos ----------
const args = process.argv.slice(2);
const modo = args.find(a => a === 'diario' || a === 'semanal') || 'semanal';
const enviar = args.includes('--enviar');
const iFecha = args.indexOf('--fecha');

// «Hoy» en Madrid, a mediodía para evitar líos de horario
function hoyEnMadrid() {
  const p = new Intl.DateTimeFormat('en-CA', { timeZone: 'Europe/Madrid', year: 'numeric', month: '2-digit', day: '2-digit' }).format(new Date());
  return deCadena(p);
}
function deCadena(s) { const [a, m, d] = s.split('-').map(Number); return new Date(a, m - 1, d, 12); }
function iso(f) { return f.getFullYear() + '-' + String(f.getMonth() + 1).padStart(2, '0') + '-' + String(f.getDate()).padStart(2, '0'); }
function clave(f) { return iso(f).slice(5); }
function masDias(f, n) { const g = new Date(f); g.setDate(g.getDate() + n); return g; }
function fechaEs(f) { return f.getDate() + ' de ' + MES_ES[f.getMonth()]; }

const HOY = iFecha >= 0 ? deCadena(args[iFecha + 1]) : hoyEnMadrid();

// ---------- datos ----------
const ctx = { window: {} };
vm.runInNewContext(fs.readFileSync(path.join(RAIZ, 'assets/efemerides.js'), 'utf8'), ctx);
const EF = ctx.window.ECOS_EFEMERIDES;

// Notas de Isa: secciones «## AAAA-MM-DD» en newsletter/notas.md
function leerNotas() {
  const f = path.join(RAIZ, 'newsletter/notas.md');
  if (!fs.existsSync(f)) return {};
  const notas = {};
  let actual = null;
  const texto = fs.readFileSync(f, 'utf8').replace(/<!--[\s\S]*?-->/g, '');
  for (const linea of texto.split('\n')) {
    const m = linea.match(/^##\s+(\d{4}-\d{2}-\d{2})\s*$/);
    if (m) { actual = m[1]; notas[actual] = []; continue; }
    if (/^#\s/.test(linea)) { actual = null; continue; }
    if (actual) notas[actual].push(linea);
  }
  for (const k of Object.keys(notas)) notas[k] = notas[k].join('\n').trim();
  return notas;
}
const NOTAS = leerNotas();

// Markdown mínimo para las notas: párrafos, **negrita**, *cursiva* y [enlaces](url)
function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;'); }
function md(texto) {
  return texto.split(/\n\s*\n/).map(p => {
    let h = esc(p.trim()).replace(/\n/g, '<br>');
    h = h.replace(/\[([^\]]+)\]\((https?:[^)\s]+)\)/g, '<a href="$2" style="color:#652638;">$1</a>');
    h = h.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>').replace(/\*([^*]+)\*/g, '<em>$1</em>');
    return '<p style="margin:0 0 12px;">' + h + '</p>';
  }).join('');
}

// Cuenta atrás para el próximo 23 de noviembre (Ecos nació el 23-11-2025)
function cuentaAtras(f) {
  let ani = new Date(f.getFullYear(), 10, 23, 12);
  if (ani < f) ani = new Date(f.getFullYear() + 1, 10, 23, 12);
  const dias = Math.round((ani - f) / 86400000);
  const annos = ani.getFullYear() - 2025;
  const cuantos = annos === 1 ? 'su primer año' : annos + ' años';
  if (dias === 0) return { dias, texto: '¡Hoy Ecos cumple ' + cuantos + '! Gracias por estar aquí.' };
  if (dias === 1) return { dias, texto: 'Mañana, 23 de noviembre, Ecos cumple ' + cuantos + '.' };
  return { dias, texto: 'Faltan <strong>' + dias + ' días</strong> para que Ecos cumpla ' + cuantos + ', el 23 de noviembre.' };
}

// ---------- piezas del correo (estilos en línea para que se vean bien en cualquier gestor) ----------
const C = { granate: '#652638', burdeos: '#421C2A', marfil: '#F6F0E5', pergamino: '#E8DCC7', tinta: '#282321', bronce: '#A78658', oliva: '#5F6152' };
const SERIF = "Georgia, 'Times New Roman', serif";

function bloqueEfemeride(e, etiqueta) {
  return `
  <p style="margin:0 0 4px;font-family:'Courier New',monospace;font-size:12px;color:${C.oliva};letter-spacing:.02em;">${esc(etiqueta)}</p>
  <h2 style="margin:0 0 8px;font-family:${SERIF};font-weight:normal;font-size:24px;line-height:1.25;color:${C.burdeos};">${esc(e.titulo)}</h2>
  <p style="margin:0 0 8px;">${esc(e.texto)}</p>
  <p style="margin:0;font-size:13px;font-style:italic;color:${C.oliva};">Fuente: ${esc(e.fuente)}</p>`;
}

function proxima(f) {
  for (let i = 1; i <= 366; i++) { const g = masDias(f, i); if (EF[clave(g)]) return { f: g, e: EF[clave(g)], i }; }
  return null;
}

function correoDiario(f) {
  const r = fechaRomana(f);
  const e = EF[clave(f)];
  let cuerpo;
  if (e) cuerpo = bloqueEfemeride(e, 'Tal día como hoy · ' + e.anno);
  else {
    const p = proxima(f);
    cuerpo = `<p style="margin:0 0 14px;">Hoy no hay efeméride en nuestro calendario. Te adelanto la próxima:</p>` +
      bloqueEfemeride(p.e, 'Dentro de ' + (p.i === 1 ? 'un día' : p.i + ' días') + ', el ' + fechaEs(p.f) + ' · ' + p.e.anno);
  }
  const nota = NOTAS[iso(f)];
  const asunto = e ? `${r.corta} · ${e.titulo}` : `${r.corta} · Hoy en el calendario romano`;
  return {
    asunto,
    previa: e ? e.texto : 'La fecha de hoy en el calendario romano y lo que viene.',
    html: plantilla({
      cabeza: cabeceraFecha(f, r),
      secciones: [cuerpo, nota ? seccionNota(nota) : '', seccionAniversario(f)],
      frecuencia: 'diaria'
    })
  };
}

function correoSemanal(f) {
  // La semana va de este lunes al domingo
  const lunes = masDias(f, -((f.getDay() + 6) % 7));
  const dias = [...Array(7)].map((_, i) => masDias(lunes, i));
  const filas = dias.map(d => {
    const r = fechaRomana(d), e = EF[clave(d)];
    return `
    <tr>
      <td style="padding:10px 12px 10px 0;border-top:1px solid ${C.pergamino};vertical-align:top;width:150px;">
        <div style="font-family:${SERIF};font-size:15px;color:${C.granate};">${esc(r.corta)}</div>
        <div style="font-size:13px;color:${C.oliva};">${DIAS_ES[d.getDay()]} ${d.getDate()}</div>
      </td>
      <td style="padding:10px 0;border-top:1px solid ${C.pergamino};vertical-align:top;">
        ${e ? `<div style="font-family:${SERIF};font-size:17px;color:${C.burdeos};">${esc(e.titulo)} <span style="font-size:13px;color:${C.oliva};">· ${esc(e.anno)}</span></div>
        <div style="font-size:15px;margin-top:3px;">${esc(e.texto)}</div>
        <div style="font-size:12px;font-style:italic;color:${C.oliva};margin-top:3px;">Fuente: ${esc(e.fuente)}</div>`
        : ''}
      </td>
    </tr>`;
  }).join('');
  const notas = dias.map(d => NOTAS[iso(d)]).filter(Boolean);
  const titulo = dias[0].getMonth() === dias[6].getMonth()
    ? `Del ${dias[0].getDate()} al ${fechaEs(dias[6])}`
    : `Del ${fechaEs(dias[0])} al ${fechaEs(dias[6])}`;
  return {
    asunto: `La semana en Ecos · ${titulo.toLowerCase()}`,
    previa: notas.length ? md(notas[0]).replace(/<[^>]+>/g, '').slice(0, 140) : 'Lo que trae la semana en Ecos y lo que pasó tal día como estos en Grecia y Roma.',
    html: plantilla({
      cabeza: `<p style="margin:0 0 4px;font-size:14px;font-style:italic;color:${C.oliva};">La semana en el calendario romano</p>
        <p style="margin:0;font-family:${SERIF};font-size:26px;color:${C.granate};">${esc(titulo)}</p>`,
      secciones: [notas.length ? seccionNota(notas.join('\n\n'), 'Esta semana en Ecos') : '',
        `<p style="margin:0 0 6px;font-family:${SERIF};font-style:italic;font-size:18px;color:${C.granate};">Tal día como esta semana</p><table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse;">${filas}</table>`,
        seccionAniversario(dias[0])],
      frecuencia: 'semanal'
    })
  };
}

function cabeceraFecha(f, r) {
  return `<p style="margin:0 0 2px;font-size:14px;font-style:italic;color:${C.oliva};">Hoy en el calendario romano</p>
    <p style="margin:0;font-family:${SERIF};font-size:30px;line-height:1.15;color:${C.granate};">${esc(r.corta)}</p>
    <p style="margin:4px 0 0;font-size:14px;font-style:italic;color:${C.burdeos};">${esc(r.larga)} · ${DIAS_ES[f.getDay()]} ${fechaEs(f)}</p>`;
}
function seccionNota(texto, titulo = 'Isa te cuenta') {
  return `<p style="margin:0 0 8px;font-family:${SERIF};font-style:italic;font-size:18px;color:${C.granate};">${titulo}</p>${md(texto)}`;
}
function seccionAniversario(f) {
  const c = cuentaAtras(f);
  return `<p style="margin:0;font-size:15px;color:${C.burdeos};">${c.texto}</p>`;
}

function plantilla({ cabeza, secciones, frecuencia }) {
  const bloques = secciones.filter(Boolean).map(s => `
      <tr><td style="padding:22px 28px;border-top:1px solid ${C.pergamino};">${s}</td></tr>`).join('');
  return `<!DOCTYPE html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Ecos de nuestros clásicos</title></head>
<body style="margin:0;padding:0;background:${C.marfil};">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:${C.marfil};">
<tr><td align="center" style="padding:24px 12px;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="max-width:600px;background:#FBF7EF;border:1px solid ${C.bronce};font-family:${SERIF};font-size:16px;line-height:1.55;color:${C.tinta};">
    <tr><td style="background:${C.granate};padding:18px 28px;border-bottom:3px double ${C.bronce};">
      <a href="${WEB}" style="font-family:${SERIF};font-style:italic;font-size:22px;color:${C.marfil};text-decoration:none;">Ecos de nuestros clásicos</a>
    </td></tr>
    <tr><td style="padding:24px 28px 20px;background:${C.pergamino};">${cabeza}</td></tr>
    ${bloques}
    <tr><td style="padding:20px 28px;border-top:3px double ${C.bronce};font-size:15px;">
      <a href="${WEB}" style="color:${C.granate};">La web</a> &nbsp;·&nbsp;
      <a href="${WEB}/palabras.html" style="color:${C.granate};">Las palabras del zurrón</a> &nbsp;·&nbsp;
      <a href="https://www.youtube.com/@Ecosdenuestrosclásicos" style="color:${C.granate};">YouTube</a> &nbsp;·&nbsp;
      <a href="https://www.patreon.com/cw/Ecosdenuestrosclasicos" style="color:${C.granate};">Patreon</a>
    </td></tr>
    <tr><td style="padding:16px 28px 22px;font-size:12px;line-height:1.5;color:${C.oliva};">
      Recibes este correo porque te suscribiste a la newsletter ${frecuencia} en ecosdenuestrosclasicos.com.
      Si ya no quieres recibirlo: <a href="{{ unsubscribe }}" style="color:${C.oliva};">darme de baja</a>.<br>
      Para contestar, responde a este correo: me llega a mí, a Isa.
    </td></tr>
  </table>
</td></tr></table>
</body></html>`;
}

// ---------- Brevo ----------
async function brevo(ruta, cuerpo, metodo = 'POST') {
  const r = await fetch('https://api.brevo.com/v3' + ruta, {
    method: metodo,
    headers: { 'api-key': process.env.BREVO_API_KEY, 'content-type': 'application/json', accept: 'application/json' },
    body: cuerpo ? JSON.stringify(cuerpo) : undefined
  });
  const t = await r.text();
  if (!r.ok) throw new Error(`Brevo ${ruta}: ${r.status} ${t}`);
  return t ? JSON.parse(t) : {};
}

// Aviso a Isa si los envíos del día se acercan al límite gratuito de Brevo (300 al día)
const LIMITE_DIARIO = Number(process.env.BREVO_LIMITE_DIARIO || 300);
async function suscritos(id) {
  if (!id) return 0;
  const l = await brevo('/contacts/lists/' + id, null, 'GET');
  return Number(l.uniqueSubscribers ?? l.totalSubscribers ?? 0);
}
async function avisoLimite() {
  try {
    const total = await suscritos(process.env.BREVO_LISTA_SEMANAL);
    console.log(`Envíos previstos hoy: ${total} de ${LIMITE_DIARIO}.`);
    if (total < LIMITE_DIARIO * 0.8) return total;
    await brevo('/smtp/email', {
      sender: { name: 'Newsletter de Ecos', email: process.env.BREVO_REMITENTE },
      to: [{ email: process.env.BREVO_RESPONDER || 'ecosdenuestrosclasicos@gmail.com' }],
      subject: `Aviso: la newsletter se acerca al límite gratuito (${total} de ${LIMITE_DIARIO})`,
      htmlContent: `<p>Hola, Isa:</p><p>Hoy la newsletter sale a <strong>${total}</strong> personas. El plan gratuito de Brevo permite ${LIMITE_DIARIO} correos al día, contando las confirmaciones de alta, así que estás cerca del límite.</p><p>La opción más sencilla es pasar al plan Starter de Brevo, que quita el límite diario.</p>`
    });
    return total;
  } catch (e) { console.log('No se pudo comprobar el límite: ' + e.message); return null; }
}

async function principal() {
  const correo = modo === 'semanal' ? correoSemanal(HOY) : correoDiario(HOY);
  if (!enviar) {
    const destino = path.join(RAIZ, `newsletter/vista-${modo}.html`);
    fs.mkdirSync(path.dirname(destino), { recursive: true });
    fs.writeFileSync(destino, correo.html);
    console.log(`Asunto: ${correo.asunto}\nVista previa: ${destino}`);
    return;
  }
  if (fs.existsSync(path.join(RAIZ, 'newsletter/PAUSA'))) { console.log('Newsletter en pausa (existe newsletter/PAUSA). No se envía nada.'); return; }
  const faltan = ['BREVO_API_KEY', 'BREVO_REMITENTE', modo === 'semanal' ? 'BREVO_LISTA_SEMANAL' : 'BREVO_LISTA_DIARIA'].filter(v => !process.env[v]);
  if (faltan.length) { console.log('Falta configurar: ' + faltan.join(', ') + '. No se envía nada.'); return; }
  const lista = Number(modo === 'semanal' ? process.env.BREVO_LISTA_SEMANAL : process.env.BREVO_LISTA_DIARIA);
  if (modo === 'semanal') {
    const total = await avisoLimite();
    if (total === 0) { console.log('La lista todavía está vacía: esta semana no se envía nada. Conexión con Brevo correcta.'); return; }
  }
  const camp = await brevo('/emailCampaigns', {
    name: `Ecos ${modo} ${iso(HOY)}`,
    subject: correo.asunto,
    previewText: correo.previa,
    sender: { name: 'Isa · Ecos de nuestros clásicos', email: process.env.BREVO_REMITENTE },
    replyTo: process.env.BREVO_RESPONDER || 'ecosdenuestrosclasicos@gmail.com',
    htmlContent: correo.html,
    recipients: { listIds: [lista] }
  });
  await brevo(`/emailCampaigns/${camp.id}/sendNow`);
  console.log(`Enviado: «${correo.asunto}» a la lista ${lista} (campaña ${camp.id}).`);
}

principal().catch(e => { console.error(e.message); process.exit(1); });
