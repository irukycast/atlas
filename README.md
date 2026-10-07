# Atlas

Landing page estática para **Atlas**, nombre comercial utilizado por **Juan Manuel Castro** para la prestación de servicios de consultoría en tecnología de la información en Argentina.

## Estructura

```text
atlas/
├── index.html
├── styles.css
├── script.js
├── privacy.html
├── terms.html
├── data-deletion.html
└── README.md
```

No requiere backend, base de datos, framework ni dependencias externas.

## Email configurado

El email comercial configurado es juanlucky518@gmail.com. Si necesitás cambiarlo en el futuro, actualizá script.js, privacy.html y 	erms.html.

El formulario abre el cliente de correo del visitante mediante `mailto:`. No finge enviar ni guardar información.

## Probar localmente

Desde la carpeta que contiene `atlas` podés usar cualquier servidor estático. Con Node.js:

```powershell
cd atlas
npx --yes serve .
```

Abrí la URL que muestre el comando. También podés abrir `index.html` directamente, aunque un servidor local refleja mejor el comportamiento de un hosting.

## GitHub Pages

### Crear el repositorio y subir los archivos

Reemplazá `TU_USUARIO` y `atlas` por los valores que uses en GitHub:

```powershell
cd ruta\a\atlas
git init
git add .
git commit -m "Crear landing de Atlas"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/atlas.git
git push -u origin main
```

### Activar Pages

1. Abrí el repositorio en GitHub.
2. Entrá en **Settings**.
3. En la barra lateral, abrí **Pages**.
4. En **Build and deployment**, elegí **Deploy from a branch**.
5. Elegí la rama `main` y la carpeta `/(root)`.
6. Presioná **Save**.
7. GitHub mostrará la URL pública, normalmente `https://TU_USUARIO.github.io/atlas/`.

Al ser una carpeta estática con rutas relativas, funciona tanto en la raíz de un dominio como dentro de la ruta de un repositorio.

## Vercel

### Opción 1: importar desde GitHub

1. Iniciá sesión en Vercel.
2. Elegí **Add New… → Project**.
3. Importá el repositorio `atlas`.
4. Dejá el framework como **Other** o sin framework.
5. Dejá vacíos el comando de build y el directorio de salida.
6. Presioná **Deploy**.

### Opción 2: deploy manual

```powershell
npm i -g vercel
cd ruta\a\atlas
vercel login
vercel
```

Cuando pregunte por el directorio del proyecto, usá la carpeta actual. No hace falta configuración especial para este sitio estático.

Revisá las condiciones vigentes del plan de Vercel que vayas a usar: el plan Hobby está limitado a uso personal o no comercial. Para un sitio oficial de un emprendimiento, elegí un plan y proveedor cuyo uso permitido sea compatible con tu actividad.

## Validación rápida

- `index.html` contiene título, descripción y metadatos Open Graph.
- La navegación usa anclas relativas y las páginas legales son `privacy.html` y `terms.html`.
- El diseño funciona en desktop, tablet y mobile.
- No hay imágenes externas, trackers ni dependencias pesadas.
- No hay datos ficticios de contacto, clientes, certificaciones o estadísticas.

GitHub Pages también publica sitios en internet, pero sus términos indican que no debe usarse como hosting gratuito para operar un negocio online o un SaaS comercial. Verificá la política vigente antes de elegirlo para el sitio oficial.


## Eliminación de datos (octubre de 2026)

La página `data-deletion.html` usa el email público existente y los mismos estilos
que las páginas legales. Hay enlaces visibles desde los tres footers.

URL final: https://irukycast.github.io/atlas/data-deletion.html

Publicación: GitHub Pages desde la rama `main`. Tras cada push, comprobar que
la URL pública devuelve 200 y contiene el email y las instrucciones vigentes.

Validar sin dependencias externas:

```powershell
python -m unittest discover -s tests -v
```

Los tests comprueban titular legal, correo consistente, enlaces y fragmentos bajo
`/atlas/`, ausencia de placeholders y uso del CSS compartido. Para servir la ruta
exacta localmente, desde la carpeta padre de `atlas`:

```powershell
python -m http.server 8766 --bind 127.0.0.1
```

Abrir `http://127.0.0.1:8766/atlas/data-deletion.html`. Esta URL local es solo una
vista previa; no debe usarse en la configuración de Meta.
