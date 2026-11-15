# La página impar

Archivo literario de Federico Castellano: poemas, relatos, ensayos y textos híbridos.

<https://fedec15.github.io/la-pagina-impar/>

Es un sitio estático hecho con [Jekyll](https://jekyllrb.com/) y publicado con GitHub Pages.
No usa bases de datos ni JavaScript, y solo depende de lo que ya trae GitHub Pages.
Cada texto es un archivo Markdown.

---

## Índice

1. [Publicar un texto](#publicar-un-texto)
2. [El encabezado](#el-encabezado)
3. [Cómo escribir el cuerpo](#cómo-escribir-el-cuerpo)
4. [Fechas, orden y folios](#fechas-orden-y-folios)
5. [Libros](#libros)
6. [Otras páginas y ajustes generales](#otras-páginas-y-ajustes-generales)
7. [Ver el sitio en la computadora](#ver-el-sitio-en-la-computadora)
8. [Puesta en línea](#puesta-en-línea)
9. [Control automático](#control-automático)
10. [Problemas frecuentes](#problemas-frecuentes)
11. [Estructura del repositorio](#estructura-del-repositorio)
12. [Licencia](#licencia)

---

## Publicar un texto

1. Crear un archivo `.md` en `_textos/`. El nombre del archivo define la dirección del texto:
   `_textos/cinco-segundos.md` → `/textos/cinco-segundos/`.
   Usar minúsculas y guiones, sin espacios, tildes ni ñ.
2. Escribir el encabezado y el texto (ver abajo).
3. Revisarlo en la computadora: <http://localhost:4000>.
4. Publicarlo:
   ```sh
   git add _textos/cinco-segundos.md
   git commit -m "Nuevo texto: Cinco segundos"
   git push
   ```
   GitHub Pages actualiza el sitio en uno o dos minutos.

Ejemplo completo:

```markdown
---
title: Cinco segundos
category: narrativa
forma: Relato
date: 2026-08-28
year: 2026
---

No recuerdo la fecha. Creo que fue en 2003, o quizá en 2004.

—Che, Facu, ¿estás seguro de que no cuida nadie este lugar?
```

## El encabezado

El encabezado va entre las dos líneas `---` al comienzo del archivo.

| Campo         | Obligatorio | Qué hace |
| ------------- | :---------: | -------- |
| `title`       | sí | Título del texto. |
| `category`    | sí | `poesia`, `narrativa` o `ensayos`. Define en qué sección aparece. |
| `date`        | sí | Fecha de publicación (`AAAA-MM-DD`). Ordena las listas, asigna el folio y se muestra completa debajo del título («12 de octubre de 2025»). |
| `forma`       | no | Relato, Ensayo, Híbrido, Verso libre… Se muestra junto a la fecha. Si falta, se muestra la categoría. |
| `year`        | no | Año de escritura. Si es distinto del de `date`, se agrega «· Escrito en …». En las listas se muestra este año. |
| `epigrafe`    | no | Cita que abre el texto, alineada a la derecha. Si ocupa varias líneas, ver [Problemas frecuentes](#problemas-frecuentes). |
| `dedicatoria` | no | Dedicatoria en cursiva, debajo del título. |
| `libro`       | no | Nombre del archivo de un libro de `_libros/` (sin `.md`). El texto queda vinculado a ese libro. |
| `formato`     | no | `verso` para un texto en verso que no está en la categoría poesía. |
| `published`   | no | `false` para dejarlo como borrador: no se publica. |

Epígrafe de varias líneas:

```yaml
epigrafe: |
  Once upon a midnight dreary,
  while I pondered, weak and weary,

  *The Raven*, Edgar Allan Poe
```

## Cómo escribir el cuerpo

**Párrafos y saltos de línea.** Se respetan tal cual están en el archivo, en todas las categorías.
Una línea en blanco separa párrafos (o estrofas). No hay sangría automática, salvo en diálogos y citas.
No hace falta terminar las líneas con dos espacios; si están, no molestan.

**Poesía.** En la categoría `poesia`, las estrofas tienen un poco más de aire y las palabras no se cortan con guion.

**Diálogos.** Todo párrafo que empieza con raya (—) lleva sangría en la primera línea, sin hacer nada más.

**Pseudodiálogos.** Para un pensamiento, una acción u otro párrafo que debe verse como diálogo sin empezar
con raya, se agrega `{: .dialogo}` en la línea siguiente, sin línea en blanco en medio:

```markdown
*¿Me habrá reconocido?* Martín saca el celular y finge leer algo importante.
{: .dialogo}
```

**Citas.** Para versos, letras de canciones o fragmentos de otros autores dentro de un texto en prosa,
cada línea empieza con `> `. Se muestran con sangría en todo el bloque y respetando los saltos.
Una línea con solo `>` separa estrofas dentro de la misma cita:

```markdown
> la lengua natal castra
>
> no
> las palabras
> no hacen el amor
```

**Resumen de sangrías:**

| Caso | Cómo se escribe | Cómo se ve |
| ---- | --------------- | ---------- |
| Diálogo | empieza con `—` | sangría en la primera línea |
| Pseudodiálogo | `{: .dialogo}` debajo del párrafo | sangría en la primera línea |
| Cita | cada línea empieza con `> ` | sangría en todo el bloque |

**Otros recursos:**

- `*cursiva*` y `**negrita**`.
- `***` en una línea sola: separador de sección (una línea corta centrada).
- `## I`, `## II`…: partes numeradas o subtítulos dentro del texto.
- Las comillas rectas `"…"` se convierten en comillas latinas «…». Si se escriben « » directamente, quedan como están.

## Fechas, orden y folios

- **Orden de las listas:** el índice, las páginas de cada categoría y la portada muestran primero
  lo más reciente, según `date`. En la vista «Todos» del índice, los textos se agrupan por
  categoría (Poesía, Narrativa, Ensayos e híbridos).
- **Portada:** muestra los 6 textos más recientes.
- **Folio:** cada texto recibe un número de página impar (1, 3, 5, 7…) según su orden de publicación
  en todo el sitio. Aparece en el índice y en la cornisa de cada texto, como en un libro.
  Los botones «Anterior / Siguiente» de cada texto siguen ese mismo orden.
- **Para que los folios no cambien** una vez publicado el sitio, `date` debe ser el día en que se
  sube el texto, y el año de escritura va en `year`. Un texto con fecha anterior a otros ya
  publicados se intercala y corre la numeración de los siguientes.
- **Fechas futuras:** un texto con `date` futura no aparece hasta que se vuelva a generar el sitio
  después de esa fecha (por ejemplo, con el siguiente `push`).

## Libros

Cada libro es un archivo en `_libros/`. Ejemplo: `_libros/el-nervio-y-la-rama.md`.

```markdown
---
title: El nervio y la rama
editorial: Alción Editora
estado: En preparación
compra: https://…
description: Una obra entre la poesía, el ensayo y la narrativa autobiográfica.
---

Texto de contratapa o presentación.
```

- `editorial` y `estado` se muestran debajo del título, también en la portada y en la sección Libros.
- `compra`: si tiene un enlace, aparece el botón «Comprar el libro →». Si no, no aparece nada.
- `description`: frase breve que se muestra en la sección Libros.
- `subtitulo` (opcional): subtítulo debajo del título.
- `ficha` (opcional): lista de datos editoriales (ISBN, páginas, año…):
  ```yaml
  ficha:
    ISBN: 978-…
    Páginas: 180
  ```
- Los textos del archivo que tengan `libro: el-nervio-y-la-rama` se listan en la página del libro.
- Un fragmento en verso dentro de la página del libro va en `<div class="verso" markdown="1"> … </div>`.

**Cuando salga *El nervio y la rama*:** cambiar `estado` (por ejemplo, a `Disponible`) y completar
`compra`. Actualizar también la última frase de `acerca-de.md` («Aparecerá próximamente…»).

## Otras páginas y ajustes generales

| Qué | Dónde |
| --- | ----- |
| Biografía y contacto | `acerca-de.md` |
| Nombre del sitio, autor, correo, sitio académico, URL | `_config.yml` |
| Nombres y orden de las categorías | `_data/categorias.yml` |
| Colores, tipografías y todo el diseño | `assets/css/impar.css` |

Los cambios en `_config.yml` necesitan reiniciar el servidor local (`docker restart la-pagina-impar`).

**Diseño:** fondo `#F7F5F0`, texto `#262522`, secundario `#77736B`, líneas `#DCD8CE` y acento `#A16E55`.
Literata para los textos y títulos, Inter para la navegación y los datos. Columna de lectura de unos 700 px.

## Ver el sitio en la computadora

Hace falta Docker. La primera vez se crea el servidor:

```sh
docker run -d --name la-pagina-impar -u $(id -u):$(id -g) -e JEKYLL_ROOTLESS=1 \
  -p 4000:4000 -p 35729:35729 -v "$PWD":/srv/jekyll jekyll/jekyll:pages \
  jekyll serve --host 0.0.0.0 --baseurl "" --watch --force_polling --livereload
```

Después se abre <http://localhost:4000>. Al guardar cualquier archivo, el sitio se regenera
y el navegador se actualiza solo.

| Acción | Comando |
| ------ | ------- |
| Detener | `docker stop la-pagina-impar` |
| Volver a iniciar | `docker start la-pagina-impar` |
| Reiniciar (tras cambiar `_config.yml`) | `docker restart la-pagina-impar` |
| Ver actividad y errores | `docker logs -f la-pagina-impar` |

Con Ruby instalado también se puede usar `bundle install && bundle exec jekyll serve`.

## Puesta en línea

Una sola vez, en GitHub: **Settings → Pages → Build and deployment → Source: Deploy from a branch**,
rama `master`, carpeta `/ (root)`. El sitio queda en <https://fedec15.github.io/la-pagina-impar/>.

A partir de ahí, cada `push` a `master` actualiza el sitio.

## Control automático

En cada `push` y en cada pull request, GitHub corre `.github/workflows/verificar.yml`:

1. `scripts/verificar_textos.py` revisa el encabezado de cada texto y libro: que se pueda leer,
   que tenga `title`, `category` y `date`, que la categoría exista, que el nombre del archivo
   sea válido y que `libro` apunte a un libro existente. Avisa si hay borradores o fechas futuras.
2. Se compila el sitio con la misma versión de Jekyll que GitHub Pages, en modo estricto.

Si algo falla, el commit queda marcado con una ✗ en GitHub, llega un mail y el error aparece
en la pestaña **Actions** con el nombre del archivo y la línea.

Para revisar antes de subir: `python3 scripts/verificar_textos.py`.

**Protección de `master`** (configurada en GitHub, **Settings → Rules → Rulesets**): no se puede
borrar la rama ni reescribir su historial, y el control automático tiene que pasar.

## Problemas frecuentes

**Un texto no aparece.**
- Casi siempre es un error en el encabezado. Revisar `docker logs la-pagina-impar`: si dice
  `YAML Exception reading _textos/…`, el problema está entre los `---`.
- Un valor de varias líneas (como un epígrafe) necesita `|` y dos espacios de sangría en cada línea.
- Un valor con dos puntos (`:`) o que empieza con comillas o asterisco conviene escribirlo entre comillas: `title: "Uno: dos"`.
- Revisar que `date` no sea futura y que no tenga `published: false`.

**El sitio se ve sin diseño.** Recargar sin caché (Ctrl+Shift+R). La hoja de estilos se llama
`impar.css` a propósito: si se llamara `style.css`, el tema por defecto de GitHub Pages la pisaría.

**Una sangría al principio de un párrafo desaparece.** Markdown descarta los espacios al principio
de un párrafo, y cuatro espacios o más lo convierten en código. Para diálogos, citas y
pseudodiálogos, usar las marcas de [Cómo escribir el cuerpo](#cómo-escribir-el-cuerpo).

## Estructura del repositorio

```
_config.yml             título, autor, correo, URL y configuración de Jekyll
_data/categorias.yml    nombres y orden de las categorías
_textos/                un .md por texto
_libros/                un .md por libro
_layouts/               plantillas
  default.html            esqueleto común (cabecera, pie)
  home.html               portada
  indice.html             índice completo y páginas de categoría
  texto.html              página de cada texto
  libro.html              página de cada libro
  pagina.html             páginas simples (Acerca de, 404)
_includes/              piezas reutilizables
  head.html               metadatos, tipografías, hoja de estilos
  header.html, footer.html
  lista-textos.html       lista tipo índice (título, año, folio)
  filtro.html             filtro por categoría
  folio.html              cálculo del número de página impar
  fecha.html, anio.html   fechas en castellano
  categoria-nombre.html
assets/css/impar.css    todo el diseño
scripts/                verificación de textos (no se publica)
.github/workflows/      control automático en GitHub
index.html              portada
textos/                 índice (index.html) y una página por categoría
libros/index.html       lista de libros
acerca-de.md            biografía y contacto
404.html                página no encontrada
```

## Licencia

- **Textos literarios** (`_textos/`, `_libros/`, `acerca-de.md`): © Federico Castellano.
  Todos los derechos reservados.
- **Código del sitio** (plantillas, estilos, configuración): licencia MIT.

Detalles en [LICENSE](LICENSE).
