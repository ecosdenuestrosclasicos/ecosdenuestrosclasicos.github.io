# Web de Ecos de nuestros clásicos · contexto para Claude Code

## Qué es
Web de **Ecos de nuestros clásicos**, proyecto independiente de divulgación sobre Grecia y Roma creado por **Isabel Sanz** (desde noviembre de 2026 quiere aparecer con su apellido) el 23 de noviembre de 2025. Quarto (website) + R, publicada en GitHub Pages con GitHub Actions (`.github/workflows/publicar.yml`: instala Quarto 1.6.42, R y los paquetes, ejecuta `quarto render` y publica `_site`). Isabel trabaja desde RStudio (`ecos.Rproj`) y GitHub Desktop. El README tiene las instrucciones para ella.

## Primeras tareas pendientes
1. **Nombre del repositorio.** Ahora se llama `ecosdenuestrosclasicos` y la web sale en `/ecosdenuestrosclasicos/`. Isabel va a renombrarlo a `ecosdenuestrosclasicos.github.io`. Si no lo ha hecho, recuérdaselo: `assets/miniodi.html` y `404.qmd` usan rutas absolutas (`/imagenes/...`, `/index.html`) que solo funcionan en la raíz. Actualiza el remoto de git si hace falta.
2. **Borrar `publicar.yml.txt`**: era una copia del workflow para subirlo a mano. Ya no hace falta.
3. **Probar `investigacion/confianza-gobierno.qmd` con R** (`quarto render`). Es la única página que no se pudo probar: se migró del repo antiguo `ecosdenuestrosclasicos/confianza_gov` y se corrigió la ruta a `../datos/Trust_in_gov.csv` (en Linux importan las mayúsculas). Paquetes: tidyverse, countrycode, scales, rio, janitor, knitr, rmarkdown.
4. Comprobar en la pestaña Actions de GitHub que la publicación sale en verde.

## Dominio
La web vive en **https://ecosdenuestrosclasicos.com** (comprado en DonDominio, noviembre de 2026; DNS: 4 registros A a GitHub Pages y `www` CNAME a ecosdenuestrosclasicos.github.io; dominio personalizado configurado en Settings → Pages). El repositorio sigue llamándose `ecosdenuestrosclasicos.github.io`.

## Estadísticas
GoatCounter (sin cookies), cuenta `ecosdenuestrosclasicos`: panel en https://ecosdenuestrosclasicos.goatcounter.com. El script está en `assets/cabecera.html`. Útil para dar cifras reales en la página de colaboraciones.

## Aniversario
Franja granate arriba del todo en todas las páginas, debajo del menú (`assets/aniversario.html`, incluida en `_quarto.yml`; estilos `.franja-aniversario` en `ecos.css`). Se ve del 9 al 30 de noviembre de 2026: antes del 23 cuenta los días que faltan, el 23 felicita y después enlaza al vídeo. Lleva la cita ἀρχὴ ἥμισυ παντός (Aristóteles, *Política* V, 1303b) · *Dimidium facti qui coepit habet* (Horacio, *Epístolas* I, 2, 40). Cuando esté el vídeo del domingo 22, cambiar la variable `VIDEO` del script por su enlace. Se puede cerrar con la ×; vuelve a salir en la siguiente visita.

## Estructura
- Páginas: `index.qmd` (portada, `page-layout: custom`, HTML en bloques `{=html}`), `proyecto`, `sobre-mi`, `biblioteca` (listado con buscador de investigacion/, lecturas/, cuadernos/ y videos/), `investigacion`, `lecturas`, `videos`, `comunidad`, `apoyame`, `colaboraciones`, `contacto`, `privacidad`, `404`.
- `assets/ecos.css`: todos los estilos. `assets/ecos.scss`: variables del tema. Las fuentes están alojadas en `assets/fuentes/`: IM Fell English para títulos, EB Garamond para el texto (incluye griego politónico) y Special Elite solo para las signaturas de las fichas y los sellos.
- `assets/mapa-ruta.md`: el mapa de la portada. Fondo `imagenes/mapa-ilustrado.jpg` (marco, adornos, monumentos y personajes recortados de la ilustración original de Isabel sobre un Mediterráneo real de Natural Earth) más una capa SVG con la ruta circular en barco, las escapadas a pie (Segovia, Guiza, Petra), los nombres y el barquito animado. Geografía rigurosa: cada monumento junto a su lugar real. Generado con `herramientas/mapa_mediterraneo.py`, `componer_mapa.py` y `capa_ruta.py`.
- `assets/miniodi.html`: Mini Odi dibujado se asoma al final de cada página; al hacer clic dice una frase.
- Plantillas: `videos/_plantilla-video.qmd` y `cuadernos/_plantilla-cuaderno.qmd`.
- Comentarios con giscus: ACTIVOS (Discussions activado, app giscus instalada solo en este repo, categoría «Comentarios» de tipo anuncio; repo-id R_kgDOVs3uXQ, category-id DIC_kwDOVs3uXc4DLIbd). Configurados en los `_metadata.yml` de cada carpeta y en la cabecera de `comunidad.qmd` y `lecturas.qmd`; tema en `assets/giscus-ecos.css`.

## Paleta
Granate `#652638`, burdeos `#421C2A`, marfil `#F6F0E5`, pergamino `#E8DCC7`, tinta `#282321`, bronce `#A78658`, oliva `#5F6152`.

## Reglas de contenido (importantes para Isabel)
- Español de España, con la voz de Isabel: cercana, curiosa, rigurosa, con humor cuando toca. Nada de frases hechas de IA («fascinante viaje», «sumérgete»…), enumeraciones simétricas, moralejas ni grandilocuencia.
- **No inventar** fuentes, traducciones, resultados, publicaciones, fechas, colaboraciones ni credenciales. Las citas clásicas, siempre con referencia precisa. Usar «a. n. e.» y «n. e.».
- **Patreon**: sin niveles ni precios. Enlace: https://www.patreon.com/cw/Ecosdenuestrosclasicos
- **El libro** (`libro.qmd` + diario en `libro/`): el título es secreto, no ponerlo. Todo el libro gira en torno a una palabra que Isabel revelará al publicarlo: **no escribirla NUNCA en ningún archivo del repositorio** (es público), ni siquiera en comentarios. En la web aparece tapada, con un formulario «¿Qué crees que es?».
- **Artículos en curso** (fichas en `investigacion.qmd`): «Ludus y bienestar emocional» y «Términos y condiciones de la paz». Solo se pueden dar los títulos: nada de contenido, universidad ni coautores. Cuando se publiquen, añadir el enlace para leerlos o comprar la edición. Poner el enlace cuando se publiquen.
- **PayPal**: activo en `apoyame.qmd`, botón a https://paypal.me/ecosclasicos (aportaciones puntuales). No usar la palabra «donativos».
- Formación: no decir que Filología Clásica quedó sin terminar; basta con «antes estudié Filología Clásica».
- No poner notas sobre ilustraciones hechas con IA.
- No publicar cifras de audiencia (en la página de colaboraciones pone «a petición»).
- La mascota se llama **Mini Odi** (no «Niodi»). Su foto real lleva logos de F1: no subirla nunca al repositorio; en la web solo se usa la versión dibujada.
- Formación de Isabel: graduada en Economía (Universitat de València, junio de 2026); antes estudió Filología Clásica (no decir que no la terminó); ahora cursa el Máster en Economía (UV) y Matemáticas en la UNED; da clase desde 2019. TFG: deterioro institucional de la República tardía en el *Bellum Catilinae* (resultados todavía no publicados).
- Correo público: ecosdenuestrosclasicos@gmail.com

## Pendiente de Isabel
Revisar las traducciones de las tres citas de la portada; fecha real de la lectura de *Los doce césares* y del TFG (hay comentarios en los archivos); resultados del TFG; ilustración definitiva de Mini Odi (`ILUSTRACION-MINI-ODI.md`); activar los comentarios.
