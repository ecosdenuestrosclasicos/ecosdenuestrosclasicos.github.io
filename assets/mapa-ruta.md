```{=html}
<figure class="lamina lamina-ilustrada" id="mapa">
<div class="mapa-lienzo">
<style>
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
</style>
<svg class="mapa-ruta" viewBox="0 0 1774 887" role="img" aria-labelledby="mapa-t mapa-d" xmlns="http://www.w3.org/2000/svg">
<title id="mapa-t">La ruta de Ecos por el Mediterráneo</title>
<desc id="mapa-d">Mapa ilustrado e interactivo del Mediterráneo, con costas y lugares en su posición real. Isabel y Mini Odi, dibujados, corren por el norte de África. Una ruta circular en barco sale de Valencia y Sagunto y pasa por Roma, Pompeya, Siracusa, Ítaca, Atenas, Troya, Éfeso, Alejandría y Cartago antes de volver a casa, donde espera una paella. Tres escapadas a pie llevan a Segovia, Guiza y Petra. Cada parada se puede pulsar para ver su ficha.</desc>
<image href="imagenes/mapa-ilustrado.jpg" width="1774" height="887"/>
<text class="mar" x="1080.1" y="540.4" font-size="26" letter-spacing="9" text-anchor="middle" transform="rotate(0 1080.1 540.4)">MAR MEDITERRÁNEO</text><text class="mar" x="719.6" y="332.1" font-size="17" letter-spacing="3" text-anchor="middle" transform="rotate(0 719.6 332.1)">Mar Tirreno</text><text class="mar" x="925.6" y="458.7" font-size="17" letter-spacing="3" text-anchor="middle" transform="rotate(0 925.6 458.7)">Mar Jónico</text><text class="mar" x="1163.8" y="468.9" font-size="17" letter-spacing="3" text-anchor="middle" transform="rotate(0 1163.8 468.9)">Mar Egeo</text><text class="mar" x="825.8" y="168.7" font-size="17" letter-spacing="3" text-anchor="middle" transform="rotate(-37 825.8 168.7)">Mar Adriático</text><text class="mar" x="1418.1" y="148.3" font-size="20" letter-spacing="6" text-anchor="middle" transform="rotate(0 1418.1 148.3)">MAR NEGRO</text><text class="mar" x="1466.3" y="826.3" font-size="16" letter-spacing="3" text-anchor="middle" transform="rotate(-58 1466.3 826.3)">Mar Rojo</text>
<path id="ruta-lazo" class="ruta" d="M327.6,329.2C327.4,327.4 334.8,326.2 338.2,324.7C341.7,323.3 339.7,318.1 348.5,320.6C357.4,323.2 366.0,332.9 391.3,340.2C416.7,347.6 464.3,360.3 500.8,364.7C537.3,369.2 580.2,373.6 610.2,366.8C640.2,360.0 662.2,341.9 681.0,323.9C699.8,305.9 712.8,274.1 722.9,258.6C732.9,243.0 737.8,230.7 741.5,230.4C745.3,230.0 739.4,248.8 745.4,256.5C751.4,264.3 767.4,273.5 777.6,276.9C787.7,280.3 800.9,272.5 806.2,276.9C811.6,281.4 805.9,292.9 809.8,303.5C813.6,314.0 824.2,329.0 829.1,340.2C833.9,351.5 836.5,363.9 838.7,370.9C841.0,377.9 842.3,376.2 842.6,382.3C842.9,388.4 842.4,400.1 840.7,407.6C838.9,415.1 826.9,424.9 832.0,427.2C837.0,429.6 853.7,426.2 870.9,421.9C888.1,417.6 915.4,408.7 935.3,401.5C955.1,394.4 978.2,383.7 990.0,379.0C1001.8,374.4 1000.2,374.2 1006.1,373.7C1012.0,373.3 1019.0,375.8 1025.4,376.2C1031.8,376.5 1038.5,375.3 1044.7,375.8C1050.9,376.3 1058.4,377.3 1062.4,379.0C1066.4,380.7 1066.3,383.8 1068.8,386.0C1071.4,388.2 1074.0,391.1 1077.5,392.1C1081.0,393.1 1085.4,392.4 1089.8,392.1C1094.1,391.8 1101.9,390.3 1103.6,390.5C1105.3,390.7 1097.7,390.8 1100.1,393.3C1102.4,395.9 1112.4,405.8 1117.8,405.6C1123.1,405.4 1127.3,398.9 1132.3,392.1C1137.2,385.3 1142.4,374.8 1147.7,364.7C1153.0,354.7 1159.0,340.9 1163.8,332.1C1168.6,323.2 1173.2,315.5 1176.7,311.7C1180.1,307.8 1184.9,305.8 1184.4,309.2C1183.9,312.6 1173.7,323.5 1173.4,332.1C1173.2,340.7 1178.5,352.2 1183.1,360.7C1187.7,369.2 1194.7,378.0 1200.8,383.1C1206.9,388.3 1218.7,387.6 1219.8,391.7C1220.9,395.8 1208.8,401.2 1207.2,407.6C1205.7,414.0 1206.2,421.6 1210.5,430.1C1214.8,438.6 1224.1,445.1 1233.0,458.7C1241.8,472.3 1253.6,486.6 1263.6,511.8C1273.5,537.0 1286.0,583.9 1292.5,609.8C1299.1,635.7 1311.4,662.9 1302.8,667.0C1294.2,671.1 1267.4,647.3 1241.0,634.3C1214.6,621.4 1182.0,601.0 1144.5,589.4C1106.9,577.8 1058.7,574.4 1015.7,564.9C972.8,555.4 926.7,548.5 887.0,532.2C847.3,515.9 807.6,485.2 777.6,466.9C747.5,448.5 724.4,427.0 706.8,421.9C689.2,416.8 687.6,438.9 672.0,436.2C656.4,433.5 642.0,412.7 613.4,405.6C584.9,398.4 535.6,400.1 500.8,393.3C465.9,386.5 427.8,372.6 404.2,364.7C380.6,356.9 369.9,351.3 359.2,346.4C348.4,341.5 345.1,338.2 339.9,335.3C334.6,332.5 327.9,331.0 327.6,329.2Z"/>
<path class="escapada" d="M348.5,320.6C342.3,318.8 323.6,313.8 310.9,309.6C298.2,305.4 285.1,299.7 272.3,295.3C259.4,290.9 244.5,287.5 233.6,283.1C222.8,278.6 211.6,271.1 207.2,268.8"/><path class="escapada" d="M1302.8,667.0C1305.4,669.0 1313.0,673.8 1318.3,679.2C1323.5,684.7 1330.5,693.4 1334.4,699.7C1338.3,705.9 1340.5,714.0 1341.8,716.8"/><path class="escapada" d="M1341.8,716.8C1348.1,715.3 1366.2,708.0 1379.4,707.8C1392.7,707.7 1408.9,715.3 1421.3,716.0C1433.6,716.7 1443.6,714.2 1453.5,711.9C1463.3,709.7 1476.0,704.1 1480.5,702.5"/>
<g class="paella" data-lugar="Valencia" tabindex="-1" aria-hidden="true">
  <line x1="327.6" y1="329.2" x2="361.6" y2="385.2" class="paella-hilo"/>
  <g transform="translate(371.6 403.2) scale(1.5)">
    <circle r="27" class="paella-aura"/>
    <path d="M-26,-2 h-9 a3,3 0 0 0 0,6 h9z M26,-2 h9 a3,3 0 0 1 0,6 h-9z" fill="#3B3B3B" stroke="#1F1A17" stroke-width="1"/>
    <ellipse rx="25" ry="15" fill="#4A4A4A" stroke="#1F1A17" stroke-width="1.6"/>
    <ellipse rx="21.5" ry="12" fill="#E9A93A"/>
    <ellipse rx="21.5" ry="12" fill="none" stroke="#C47A1F" stroke-width="1.2" opacity=".7"/>
    <g fill="#F2C55C" opacity=".9"><circle cx="-14" cy="-4" r="1.1"/><circle cx="-8" cy="3" r="1.1"/><circle cx="-2" cy="-6" r="1.1"/><circle cx="5" cy="4" r="1.1"/><circle cx="12" cy="-3" r="1.1"/><circle cx="15" cy="5" r="1.1"/><circle cx="-15" cy="5" r="1.1"/><circle cx="0" cy="8" r="1.1"/><circle cx="9" cy="-8" r="1.1"/><circle cx="-6" cy="-9" r="1.1"/></g>
    <path d="M-12,-3 q4,-3 8,0 M3,5 q4,-3 8,0 M8,-6 q4,-3 8,0" stroke="#C0392B" stroke-width="2.4" fill="none" stroke-linecap="round"/>
    <path d="M-16,4 l7,-2 M-3,-2 l7,2 M10,3 l6,-3" stroke="#5E8C31" stroke-width="2.2" stroke-linecap="round"/>
    <path d="M-4,7 a5,4 0 1 1 7,-1" fill="#F08C6A" stroke="#B35238" stroke-width="1.2"/>
    <path d="M14,-10 l7,-3 l-1,7 z" fill="#F7E36B" stroke="#B59B2A" stroke-width="1"/>
  </g>
  <text class="paella-texto" x="371.6" y="443.2" text-anchor="middle">la recompensa</text>
</g>
<g class="lugar casa" data-lugar="Valencia" tabindex="0" role="button" aria-label="Valentia (Valencia): ver ficha"><circle class="zona" cx="327.6" cy="329.2" r="18"/><circle class="punto" cx="327.6" cy="329.2" r="6"/><text x="315.6" y="353.2" text-anchor="end">Valentia<tspan class="antiguo" x="315.6" dy="16">Valencia, casa</tspan></text></g><g class="lugar" data-lugar="Sagunto" tabindex="0" role="button" aria-label="Sagunto: ver ficha"><circle class="zona" cx="348.5" cy="320.6" r="18"/><circle class="punto" cx="348.5" cy="320.6" r="6"/><text x="358.5" y="308.6" text-anchor="start">Sagunto<tspan class="antiguo" x="358.5" dy="16">Saguntum</tspan></text></g><g class="lugar a-pie" data-lugar="Segovia" tabindex="0" role="button" aria-label="Segovia: ver ficha"><circle class="zona" cx="207.2" cy="268.8" r="18"/><circle class="punto" cx="207.2" cy="268.8" r="4.5"/><text x="197.2" y="286.8" text-anchor="end">Segovia<tspan class="antiguo" x="197.2" dy="16">Segovia</tspan></text></g><g class="lugar" data-lugar="Roma" tabindex="0" role="button" aria-label="Roma: ver ficha"><circle class="zona" cx="741.5" cy="230.4" r="18"/><circle class="punto" cx="741.5" cy="230.4" r="6"/><text x="751.5" y="244.4" text-anchor="start">Roma<tspan class="antiguo" x="751.5" dy="16">Roma</tspan></text></g><g class="lugar" data-lugar="Pompeya" tabindex="0" role="button" aria-label="Pompeya: ver ficha"><circle class="zona" cx="806.2" cy="276.9" r="18"/><circle class="punto" cx="806.2" cy="276.9" r="6"/><text x="817.2" y="289.9" text-anchor="start">Pompeya<tspan class="antiguo" x="817.2" dy="16">Pompeii</tspan></text></g><g class="lugar" data-lugar="Siracusa" tabindex="0" role="button" aria-label="Siracusa: ver ficha"><circle class="zona" cx="832.0" cy="427.2" r="18"/><circle class="punto" cx="832.0" cy="427.2" r="6"/><text x="822.0" y="446.2" text-anchor="end">Siracusa<tspan class="antiguo" x="822.0" dy="16">Συράκουσαι</tspan></text></g><g class="lugar" data-lugar="Ítaca" tabindex="0" role="button" aria-label="Ítaca: ver ficha"><circle class="zona" cx="1006.1" cy="373.7" r="18"/><circle class="punto" cx="1006.1" cy="373.7" r="6"/><text x="996.1" y="377.7" text-anchor="end">Ítaca<tspan class="antiguo" x="996.1" dy="16">Ἰθάκη</tspan></text></g><g class="lugar" data-lugar="Atenas" tabindex="0" role="button" aria-label="Atenas: ver ficha"><circle class="zona" cx="1103.6" cy="390.5" r="18"/><circle class="punto" cx="1103.6" cy="390.5" r="6"/><text x="1093.6" y="378.5" text-anchor="end">Atenas<tspan class="antiguo" x="1093.6" dy="16">Ἀθῆναι</tspan></text></g><g class="lugar" data-lugar="Troya" tabindex="0" role="button" aria-label="Troya: ver ficha"><circle class="zona" cx="1184.4" cy="309.2" r="18"/><circle class="punto" cx="1184.4" cy="309.2" r="6"/><text x="1194.4" y="307.2" text-anchor="start">Troya<tspan class="antiguo" x="1194.4" dy="16">Ἴλιον</tspan></text></g><g class="lugar" data-lugar="Éfeso" tabindex="0" role="button" aria-label="Éfeso: ver ficha"><circle class="zona" cx="1219.8" cy="391.7" r="18"/><circle class="punto" cx="1219.8" cy="391.7" r="6"/><text x="1229.8" y="409.7" text-anchor="start">Éfeso<tspan class="antiguo" x="1229.8" dy="16">Ἔφεσος</tspan></text></g><g class="lugar" data-lugar="Alejandría" tabindex="0" role="button" aria-label="Alejandría: ver ficha"><circle class="zona" cx="1302.8" cy="667.0" r="18"/><circle class="punto" cx="1302.8" cy="667.0" r="6"/><text x="1292.8" y="685.0" text-anchor="end">Alejandría<tspan class="antiguo" x="1292.8" dy="16">Ἀλεξάνδρεια</tspan></text></g><g class="lugar a-pie" data-lugar="Giza" tabindex="0" role="button" aria-label="Giza: ver ficha"><circle class="zona" cx="1341.8" cy="716.8" r="18"/><circle class="punto" cx="1341.8" cy="716.8" r="4.5"/><text x="1353.8" y="746.8" text-anchor="start">Giza<tspan class="antiguo" x="1353.8" dy="16">Πυραμίδες</tspan></text></g><g class="lugar a-pie" data-lugar="Petra" tabindex="0" role="button" aria-label="Petra: ver ficha"><circle class="zona" cx="1480.5" cy="702.5" r="18"/><circle class="punto" cx="1480.5" cy="702.5" r="4.5"/><text x="1490.5" y="720.5" text-anchor="start">Petra<tspan class="antiguo" x="1490.5" dy="16">Πέτρα</tspan></text></g><g class="lugar" data-lugar="Cartago" tabindex="0" role="button" aria-label="Cartago: ver ficha"><circle class="zona" cx="672.0" cy="436.2" r="18"/><circle class="punto" cx="672.0" cy="436.2" r="6"/><text x="662.0" y="428.2" text-anchor="end">Cartago<tspan class="antiguo" x="662.0" dy="16">Carthago</tspan></text></g>
<g class="barco"><image href="imagenes/barco-ruta.webp" x="-38" y="-56" width="76" height="64"/></g>
<rect x=".5" y=".5" width="1773" height="886" fill="none" stroke="#A78658"/>
</svg>
<div class="mapa-ficha" role="dialog" aria-live="polite" hidden></div>
</div>
<figcaption>Isabel y Mini Odi, de ruta por el Mediterráneo. Las costas y cada monumento están en su lugar real. <strong>Empieza en Valentia</strong> y pulsa cada parada para ver su ficha, recoger su palabra y mandar allí el barco.<span class="lamina-pista">Desliza para recorrer el mapa.</span></figcaption>
</figure>
<div class="mapa-progreso">
  <p class="mapa-progreso-texto"><strong>La odisea de Ecos.</strong> Sales de casa, de Valentia, para recoger las palabras que nos dejaron los clásicos: una en cada parada. Cuando las tengas todas, haz como Odiseo y vuelve a casa. El regreso, el <i>nóstos</i>, merece banquete: te espera una paella.</p>
  <p class="mapa-progreso-estado">Paradas visitadas: <span class="mapa-progreso-cuenta">0 de 14</span> <button type="button" class="mapa-progreso-reiniciar">Empezar de nuevo</button></p>
  <div class="mapa-progreso-barra" aria-hidden="true"><span></span></div>
  <p class="mapa-zurron-titulo">Tu zurrón</p>
  <ul class="mapa-zurron" aria-label="Palabras recogidas"></ul>
  <p class="mapa-zurron-enlace"><a href="palabras.html">Las catorce palabras, explicadas con su diccionario</a></p>
</div>
<script>
(function () {
  var ANCLA = {"Valencia": "valentia", "Sagunto": "fides", "Segovia": "aquaeductus", "Roma": "res-publica", "Pompeya": "domus", "Siracusa": "hybris", "Ítaca": "nostos", "Atenas": "demokratia", "Troya": "kleos", "Éfeso": "biblion", "Alejandría": "pharos", "Giza": "pyramis", "Petra": "petra", "Cartago": "qart-hadasht"};
  var FICHAS = {"Valencia": {"p": "valentia", "sig": "vigor, fuerza", "t": "Casa. Los romanos fundaron Valentia en el 138 a. n. e., y su nombre en latín significa «vigor». De aquí zarpas para recoger las palabras que nos dejaron los clásicos. Cuando las tengas todas, vuelve: el regreso merece banquete.", "ant": "Valentia", "url": "sobre-mi.html", "ut": "Conoce a Isabel"}, "Sagunto": {"p": "fides", "sig": "lealtad", "t": "Saguntum resistió el asedio de Aníbal en el 219 a. n. e. sin abandonar su alianza con Roma, y su lealtad se hizo proverbial. Ese asedio desencadenó la segunda guerra púnica.", "ant": "Saguntum", "url": null, "ut": null}, "Segovia": {"p": "aquaeductus", "sig": "conducción del agua", "t": "Una escapada a pie para ver cómo llevaban el agua los romanos: el acueducto, de finales del siglo I o comienzos del II n. e., se sostiene sin argamasa, piedra sobre piedra.", "ant": "Segovia", "url": null, "ut": null}, "Roma": {"p": "res publica", "sig": "la cosa de todos", "t": "La República romana y su larga crisis, que Salustio cuenta en la Conjuración de Catilina. Es el texto que Isa estudió en su trabajo de fin de grado.", "ant": "Roma", "url": "investigacion/salustio-catilina.html", "ut": "Ver la investigación"}, "Pompeya": {"p": "domus", "sig": "casa", "t": "El Vesubio la sepultó en el 79 n. e. y la ceniza conservó sus casas, sus calles y su vida diaria. Plinio el Joven contó la erupción en dos cartas a Tácito.", "ant": "Pompeii", "url": null, "ut": null}, "Siracusa": {"p": "hybris", "sig": "desmesura", "t": "Aquí terminó la expedición ateniense a Sicilia de 415 a 413 a. n. e., que Tucídides narra en los libros VI y VII. Una lección sobre la ambición que se pasa de la raya.", "ant": "Συράκουσαι", "url": "lecturas.html", "ut": "Tucídides en el fichero"}, "Ítaca": {"p": "nóstos", "sig": "el regreso a casa", "t": "La patria de Odiseo, que tardó diez años en volver desde Troya. Aquí entiendes el sentido del viaje: toda aventura termina en el regreso.", "ant": "Ἰθάκη", "url": "videos.html", "ut": "La serie sobre la Odisea"}, "Atenas": {"p": "demokratía", "sig": "el poder del pueblo", "t": "La ciudad de la democracia, del ostracismo, de Sócrates y de Tucídides. Muchas palabras con las que hablamos de política nacieron aquí.", "ant": "Ἀθῆναι", "url": "lecturas.html", "ut": "Autores griegos en el fichero"}, "Troya": {"p": "kléos", "sig": "la gloria que se recuerda", "t": "Ilión, en la costa de Anatolia. Los héroes de la Ilíada luchan por un kléos que dure para siempre. Tras diez años de guerra, de aquí parte Odiseo hacia casa.", "ant": "Ἴλιον", "url": null, "ut": null}, "Éfeso": {"p": "biblíon", "sig": "libro", "t": "Una de las grandes ciudades griegas de Asia Menor. La Biblioteca de Celso, del siglo II n. e., guardaba miles de rollos.", "ant": "Ἔφεσος", "url": "biblioteca.html", "ut": "Entra en la biblioteca de Ecos"}, "Alejandría": {"p": "pháros", "sig": "faro", "t": "La ciudad de la gran Biblioteca y del Faro, una de las siete maravillas. La palabra «faro» viene de Pháros, la isla donde se levantaba.", "ant": "Ἀλεξάνδρεια", "url": null, "ut": null}, "Giza": {"p": "pyramís", "sig": "pirámide", "t": "Una escapada siguiendo el Nilo. Las pirámides ya eran antiquísimas para los griegos: Heródoto las describe en el libro II de su Historia, y la palabra «pirámide» nos llega del griego.", "ant": "Πυραμίδες", "url": null, "ut": null}, "Petra": {"p": "pétra", "sig": "roca", "t": "La capital de los nabateos, tallada en la roca rosada, y por eso su nombre griego significa «roca». Roma la incorporó en el 106 n. e. a la provincia de Arabia.", "ant": "Πέτρα", "url": null, "ut": null}, "Cartago": {"p": "Qart-hadasht", "sig": "ciudad nueva", "t": "Así se llamaba en fenicio. Fue la gran rival de Roma hasta su destrucción en el 146 a. n. e., y casi todo lo que sabemos de ella lo contaron sus enemigos. Una buena razón para leer las fuentes con cuidado.", "ant": "Carthago", "url": null, "ut": null}};
  var TIERRA = {"Segovia": "Sagunto", "Giza": "Alejandría", "Petra": "Alejandría"};
  var PUNTOS = {"Valencia": [327.6214814814815, 329.2147700016019], "Sagunto": [348.5418518518519, 320.6376168879502], "Segovia": [207.2488888888889, 268.7662623434852], "Roma": [741.5229629629631, 230.37329126333023], "Pompeya": [806.2151851851853, 276.93497959458216], "Siracusa": [831.9633333333335, 427.2393770147637], "Ítaca": [1006.0851851851853, 373.73427902007944], "Atenas": [1103.6062962962965, 390.48014938482805], "Troya": [1184.391111111111, 309.20141273641457], "Éfeso": [1219.794814814815, 391.70545697249264], "Alejandría": [1302.8325925925928, 666.9912283344555], "Giza": [1341.7766666666666, 716.8204035661461], "Petra": [1480.4948148148148, 702.5251483767267], "Cartago": [672.002962962963, 436.2249659909702]};
  var ORDEN = ["Valencia", "Sagunto", "Segovia", "Roma", "Pompeya", "Siracusa", "Ítaca", "Atenas", "Troya", "Éfeso", "Alejandría", "Giza", "Petra", "Cartago"];
  var NOMBRE = { 'Valencia': 'Valentia' };
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
    var zurron = document.querySelector('.mapa-zurron');
    if (zurron) {
      zurron.innerHTML = '';
      ORDEN.forEach(function (k) {
        var li = document.createElement('li');
        if (visitados[k]) { li.textContent = FICHAS[k].p; li.title = (NOMBRE[k] || k) + ': ' + FICHAS[k].sig; }
        else { li.textContent = '?'; li.className = 'vacia'; li.title = 'Por descubrir'; }
        zurron.appendChild(li);
      });
    }
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
    var h = document.createElement('p'); h.className = 'mapa-ficha-titulo'; h.textContent = NOMBRE[n] || n;
    var a = document.createElement('span'); a.className = 'mapa-ficha-antiguo'; a.textContent = n === 'Valencia' ? 'Valencia, tu casa' : info.ant; h.appendChild(a);
    var w = document.createElement('p'); w.className = 'mapa-ficha-palabra';
    w.innerHTML = 'Palabra para el zurrón: <a class="mapa-ficha-palabra-enlace"><i></i></a> <span></span>';
    w.querySelector('i').textContent = info.p; w.querySelector('span').textContent = '(' + info.sig + ')';
    w.querySelector('a').href = 'palabras.html#' + (ANCLA[n] || '');
    w.querySelector('a').title = 'Qué significa y de dónde viene';
    var p = document.createElement('p'); p.className = 'mapa-ficha-texto'; p.textContent = info.t;
    ficha.appendChild(h); ficha.appendChild(w); ficha.appendChild(p);
    if (ahora === total && antes < total && n === 'Valencia') {
      var cv = document.createElement('p'); cv.className = 'mapa-ficha-premio';
      cv.textContent = '¡Nóstos completado! Vuelves a Valentia con las catorce palabras en el zurrón, como Odiseo al llegar a Ítaca. El viaje merece banquete: la paella es tuya. ¡Buen provecho!';
      ficha.appendChild(cv);
    } else if (ahora === total && antes < total) {
      var c = document.createElement('p'); c.className = 'mapa-ficha-premio';
      c.textContent = '¡Ya tienes todas las palabras! Como Odiseo, es hora de volver a casa: pulsa la paella de Valentia para celebrarlo.';
      ficha.appendChild(c);
    } else if (n === 'Valencia' && ahora === total) {
      var c2 = document.createElement('p'); c2.className = 'mapa-ficha-premio';
      c2.textContent = 'Ya has vuelto a casa con todas las palabras. La paella es tuya. ¡Buen provecho!';
      ficha.appendChild(c2);
    }
    if (info.url) { var l = document.createElement('a'); l.href = info.url; l.className = 'mapa-ficha-enlace'; l.textContent = info.ut; ficha.appendChild(l); }
    if (TIERRA[n]) { var t = document.createElement('p'); t.className = 'mapa-ficha-nota'; t.textContent = 'El barco te espera en ' + TIERRA[n] + '.'; ficha.appendChild(t); }
    var pendientes = ORDEN.filter(function (k) { return !visitados[k]; });
    var sig = null, idx = ORDEN.indexOf(n);
    for (var s2 = 1; s2 <= ORDEN.length; s2++) { var cand = ORDEN[(idx + s2) % ORDEN.length]; if (!visitados[cand]) { sig = cand; break; } }
    if (!sig && n !== 'Valencia') sig = 'Valencia';
    if (sig) {
      var bt = document.createElement('button'); bt.type = 'button'; bt.className = 'mapa-ficha-siguiente';
      bt.textContent = sig === 'Valencia' && !pendientes.length ? 'Volver a casa, a Valentia' : 'Siguiente parada: ' + (NOMBRE[sig] || sig);
      bt.addEventListener('click', function (e) { e.stopPropagation(); abrir(sig, svg.querySelector('.lugar[data-lugar="' + sig + '"]')); });
      ficha.appendChild(bt);
    }
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
</script>
```
