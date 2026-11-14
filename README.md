# Ecos de nuestros clásicos · web

Web de **Ecos de nuestros clásicos**, hecha con [Quarto](https://quarto.org) desde RStudio y publicada en GitHub Pages.

Dirección prevista: <https://ecosdenuestrosclasicos.github.io>

---

## 1. Cómo subirla a GitHub (la primera vez)

1. En GitHub, dentro de la organización **ecosdenuestrosclasicos**, crea un repositorio nuevo **público** que se llame exactamente
   `ecosdenuestrosclasicos.github.io`
   (con ese nombre la web queda en la dirección principal, sin `/confianza_gov/` detrás). No marques «Add a README».
2. En el repositorio vacío, pulsa **uploading an existing file**.
3. En el Finder, abre esta carpeta y pulsa **Cmd + Mayús + .** (punto) para ver los archivos ocultos. Tienen que aparecer `.github` y `.gitignore`. Sin `.github` la web no se publica.
4. Selecciona **todo el contenido** de la carpeta (no la carpeta en sí) y arrástralo a GitHub. Pulsa **Commit changes**.
5. Ve a **Settings → Pages** y, en **Source**, elige **GitHub Actions**.
6. Abre la pestaña **Actions**. Verás «Publicar la web» trabajando. La primera vez tarda unos 5–8 minutos (instala R y los paquetes). Cuando salga el check verde, la web está en <https://ecosdenuestrosclasicos.github.io>.

El repositorio antiguo, `confianza_gov`, no se toca y sigue funcionando. Su análisis ya está copiado aquí, en `investigacion/confianza-gobierno.qmd`, con los datos en `datos/`.

## 2. Cómo actualizarla después

Cada vez que subas un cambio a la rama `main` (desde la web de GitHub, con GitHub Desktop o desde RStudio), la web se vuelve a generar y publicar sola. No hace falta renderizar en local ni subir ninguna carpeta `docs/`.

Si quieres verla antes en tu ordenador: abre `ecos.Rproj` en RStudio y en la pestaña **Build** pulsa **Render Website** (o escribe `quarto preview` en el Terminal).

## 3. Cómo añadir contenido

| Quiero añadir… | Qué hago |
|:---|:---|
| Un vídeo con sus fuentes | Copia `videos/_plantilla-video.qmd` dentro de `videos/` con un nombre nuevo (sin tildes ni espacios) y rellénalo. |
| Un texto de Cuadernos | Copia `cuadernos/_plantilla-cuaderno.qmd` dentro de `cuadernos/`. |
| Una investigación | Crea un `.qmd` en `investigacion/` y añade su ficha en `investigacion.qmd`. |
| Una lectura | Crea un `.qmd` en `lecturas/` y añade su ficha en `lecturas.qmd`. |

Todo lo que pongas en esas carpetas aparece solo en **La biblioteca**, con buscador y temas (los `categories` del principio de cada archivo). Los archivos que empiezan por `_` no se publican.

Bloques especiales que puedes usar dentro de un texto:

```markdown
::: {.cita}
[Iam pridem equidem nos vera vocabula rerum amisimus.]{.original lang="la"}

[Hace ya tiempo que perdimos los verdaderos nombres de las cosas.]{.traduccion}

[Catón, en Salustio, *Bellum Catilinae* 52.11]{.referencia}
:::

::: {.capitular}
Párrafo con letra capitular.
:::
```

Para griego, usa `lang="grc"`. Para las fichas de biblioteca y los sellos (Terminado, En curso, Propuesta), copia el HTML de `investigacion.qmd`.

## 4. Comentarios (giscus)

Los comentarios están preparados pero **desactivados**, porque necesitan que hagas tres cosas en GitHub:

1. En el repositorio: **Settings → General → Features**, marca **Discussions**.
2. En **Discussions**, crea una categoría llamada `Comentarios` de tipo *Announcement* (así solo giscus puede abrir hilos nuevos y no se llena de spam).
3. Instala la app de giscus en el repositorio: <https://github.com/apps/giscus>.
4. Entra en <https://giscus.app/es>, escribe `ecosdenuestrosclasicos/ecosdenuestrosclasicos.github.io` y elige la categoría `Comentarios`. Abajo te dará dos códigos: `data-repo-id` y `data-category-id`.
5. Abre `investigacion/_metadata.yml`, `lecturas/_metadata.yml`, `cuadernos/_metadata.yml` y `videos/_metadata.yml`, quita los `#` del bloque `comments` y pega los dos códigos.
6. En `comunidad.qmd`, cambia el último apartado («Comentarios en los artículos») para decir que ya están abiertos.

**Lo que hay que saber:** para comentar con giscus hace falta una cuenta de GitHub. Para tu público eso es una barrera; por eso la página de Comunidad recoge propuestas y preguntas por correo, que no exige nada. Moderas desde la pestaña **Discussions** del repositorio (puedes borrar, ocultar o bloquear usuarios). Si más adelante quieres comentarios sin registro, las alternativas realistas son de pago (Hyvor Talk, Commento) o requieren mantener un servidor (Remark42); en ese caso habría que actualizar también la página de privacidad.

## 5. Identidad visual

**Colores**

| Nombre | Hex | Uso |
|:---|:---|:---|
| Granate | `#652638` | Títulos de portada, enlaces, la ruta, botones |
| Burdeos | `#421C2A` | Títulos, pie de página |
| Marfil | `#F6F0E5` | Fondo |
| Pergamino | `#E8DCC7` | Bloques destacados (Patreon, contacto) |
| Tinta | `#282321` | Texto |
| Bronce | `#A78658` | Filetes, marcos, la greca del pie |
| Oliva | `#5F6152` | Textos secundarios (algo más oscuro que `#747665` para que se lea bien en pequeño) |

**Tipografías** (alojadas en `assets/fuentes/`, con sus licencias libres):

- **IM Fell English** para títulos: es la digitalización de los tipos que donó John Fell a la imprenta de Oxford en el siglo XVII. Tiene la irregularidad de la tinta sobre papel y una cursiva con mucho carácter, que es lo más cercano a «lettering» sin caer en una letra de fantasía.
- **EB Garamond** para el texto: una Garamond muy legible, con griego politónico completo, así que el griego y el latín se ven bien sin cambiar de fuente.
- **Special Elite**, de máquina de escribir, solo en las signaturas de las fichas y en los sellos. Es el contrapunto de «edición antigua» y por eso se usa poquísimo.

**El elemento propio**: la ruta discontinua granate del mapa de la portada se convierte en el índice de la web («Qué vas a encontrar aquí»). La greca solo aparece una vez, en el borde del pie de página.

## 6. El mapa de la portada

Es la ilustración original de Isabel con el mapa corregido. El marco, las columnas, los laureles, el globo, los libros, el casco, la rosa de los vientos, los monumentos, el barco y los personajes están recortados de esa ilustración. Debajo hay un mapa real del Mediterráneo (costas, ríos y lagos de [Natural Earth](https://www.naturalearthdata.com), dominio público, escala 1:10m), y cada monumento está junto a su lugar real: el acueducto en Segovia, el Coliseo en Roma, el Partenón en Atenas, la Biblioteca de Celso en Éfeso, las pirámides en Guiza y el Tesoro en Petra.

La ruta es circular y va en barco: Sagunto, Roma, Pompeya, Siracusa, Ítaca, Atenas (cruzando el istmo de Corinto), Troya, Éfeso, Alejandría, Cartago y de vuelta a Sagunto. Segovia, Guiza y Petra son escapadas a pie, con línea de puntos. El barquito recorre la ruta en la web (se queda quieto si el sistema pide menos movimiento).

- `imagenes/mapa-ilustrado.jpg`: el fondo (marco, mapa, monumentos y personajes).
- `assets/mapa-ruta.md`: la capa con la ruta, los nombres y el barco.
- `imagenes/mapa-ruta.jpg`: el mapa completo en una sola imagen, para redes.
- `herramientas/`: los programas que lo generan.

## 7. Pendiente

- [ ] Ilustración definitiva de Mini Odi: ver la dirección artística en `ILUSTRACION-MINI-ODI.md`.
- [ ] Fecha real de la lectura conjunta de *Los doce césares* y del TFG (dentro de cada archivo hay un comentario).
- [ ] Resultados del TFG, cuando quieras publicarlos.
- [ ] Revisar las traducciones de las citas de la portada (son traducciones de trabajo).
- [ ] Activar los comentarios (apartado 4).
- [ ] Dominio propio, si algún día lo quieres: se añade en **Settings → Pages → Custom domain**.
