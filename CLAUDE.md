# Web de Ecos de nuestros clásicos · contexto para Claude Code

## Qué es
Web de **Ecos de nuestros clásicos**, proyecto independiente de divulgación sobre Grecia y Roma creado por **Isabel Sanz** (desde noviembre de 2026 quiere aparecer con su apellido) el 23 de noviembre de 2025. Quarto (website) + R, publicada en GitHub Pages con GitHub Actions (`.github/workflows/publicar.yml`: instala Quarto 1.6.42, R y los paquetes, ejecuta `quarto render` y publica `_site`). Isabel trabaja desde RStudio (`ecos.Rproj`) y GitHub Desktop. El README tiene las instrucciones para ella.

## Primeras tareas pendientes
1. **Nombre del repositorio.** Ahora se llama `ecosdenuestrosclasicos` y la web sale en `/ecosdenuestrosclasicos/`. Isabel va a renombrarlo a `ecosdenuestrosclasicos.github.io`. Si no lo ha hecho, recuérdaselo: `assets/miniodi.html` y `404.qmd` usan rutas absolutas (`/imagenes/...`, `/index.html`) que solo funcionan en la raíz. Actualiza el remoto de git si hace falta.
2. **Borrar `publicar.yml.txt`**: era una copia del workflow para subirlo a mano. Ya no hace falta.
3. **Probar `investigacion/confianza-gobierno.qmd` con R** (`quarto render`). Es la única página que no se pudo probar: se migró del repo antiguo `ecosdenuestrosclasicos/confianza_gov` y se corrigió la ruta a `../datos/Trust_in_gov.csv` (en Linux importan las mayúsculas). Paquetes: tidyverse, countrycode, scales, rio, janitor, knitr, rmarkdown.
4. Comprobar en la pestaña Actions de GitHub que la publicación sale en verde.

## Estructura
- Páginas: `index.qmd` (portada, `page-layout: custom`, HTML en bloques `{=html}`), `proyecto`, `sobre-mi`, `biblioteca` (listado con buscador de investigacion/, lecturas/, cuadernos/ y videos/), `investigacion`, `lecturas`, `videos`, `comunidad`, `apoyame`, `colaboraciones`, `contacto`, `privacidad`, `404`.
- `assets/ecos.css`: todos los estilos. `assets/ecos.scss`: variables del tema. Las fuentes están alojadas en `assets/fuentes/`: IM Fell English para títulos, EB Garamond para el texto (incluye griego politónico) y Special Elite solo para las signaturas de las fichas y los sellos.
- `assets/mapa-ruta.md`: el mapa SVG de la portada, generado por `herramientas/hacer_mapa.py` con las costas de Natural Earth 1:10m y coordenadas reales. Encima van los personajes dibujados (`imagenes/personajes-ruta.webp`), recortados de la ilustración original de Isabel.
- `assets/miniodi.html`: Mini Odi dibujado se asoma al final de cada página; al hacer clic dice una frase.
- Plantillas: `videos/_plantilla-video.qmd` y `cuadernos/_plantilla-cuaderno.qmd`.
- Comentarios con giscus: preparados pero comentados en los `_metadata.yml` de cada carpeta. Hace falta activar Discussions, instalar la app de giscus y pegar `repo-id` y `category-id` (pasos en el README, apartado 4). Requiere cuenta de GitHub; las propuestas de la comunidad van por correo.

## Paleta
Granate `#652638`, burdeos `#421C2A`, marfil `#F6F0E5`, pergamino `#E8DCC7`, tinta `#282321`, bronce `#A78658`, oliva `#5F6152`.

## Reglas de contenido (importantes para Isabel)
- Español de España, con la voz de Isabel: cercana, curiosa, rigurosa, con humor cuando toca. Nada de frases hechas de IA («fascinante viaje», «sumérgete»…), enumeraciones simétricas, moralejas ni grandilocuencia.
- **No inventar** fuentes, traducciones, resultados, publicaciones, fechas, colaboraciones ni credenciales. Las citas clásicas, siempre con referencia precisa. Usar «a. n. e.» y «n. e.».
- **Patreon**: sin niveles ni precios. Enlace: https://www.patreon.com/cw/Ecosdenuestrosclasicos
- **El libro** (`libro.qmd` + diario en `libro/`): el título es secreto, no ponerlo. Todo el libro gira en torno a una palabra que Isabel revelará al publicarlo: **no escribirla NUNCA en ningún archivo del repositorio** (es público), ni siquiera en comentarios. En la web aparece tapada, con un formulario «¿Qué crees que es?».
- **Artículos en curso** (fichas en `investigacion.qmd`): «Ludus y bienestar emocional» y «Términos y condiciones de la paz». Solo se pueden dar los títulos: nada de contenido, universidad ni coautores. Cuando se publiquen, añadir el enlace para leerlos o comprar la edición. Poner el enlace cuando se publiquen.
- **PayPal**: en `apoyame.qmd` hay un hueco «En preparación»; cuando Isabel dé el enlace, cambiarlo por el botón (instrucciones en un comentario del archivo). No usar la palabra «donativos».
- Formación: no decir que Filología Clásica quedó sin terminar; basta con «antes estudié Filología Clásica».
- No poner notas sobre ilustraciones hechas con IA.
- No publicar cifras de audiencia (en la página de colaboraciones pone «a petición»).
- La mascota se llama **Mini Odi** (no «Niodi»). Su foto real (`imagenes/miniodi-referencia.jpg`) lleva logos de F1, así que en la web se usa solo la versión dibujada.
- Formación de Isabel: graduada en Economía (Universitat de València, junio de 2026); antes estudió Filología Clásica (no decir que no la terminó); ahora cursa el Máster en Economía (UV) y Matemáticas en la UNED; da clase desde 2019. TFG: deterioro institucional de la República tardía en el *Bellum Catilinae* (resultados todavía no publicados).
- Correo público: ecosdenuestrosclasicos@gmail.com

## Pendiente de Isabel
Revisar las traducciones de las tres citas de la portada; fecha real de la lectura de *Los doce césares* y del TFG (hay comentarios en los archivos); resultados del TFG; ilustración definitiva de Mini Odi (`ILUSTRACION-MINI-ODI.md`); activar los comentarios.
