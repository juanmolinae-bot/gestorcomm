# GestorComm

Sistema de gestión de incidencias para proyectos de construcción y comisionamiento eléctrico.

Desarrollado con Django como parte del curso APTC106 de la universidad Universidad Andrés Bello.

## Funcionalidades

- Login / Logout con autenticación nativa de Django.
- Pantalla de perfil de usuario.
- CRUD completo de incidencias (crear, listar, ver detalle, editar, eliminar y modificar).
- Filtros por estado y prioridad de las incidencias.
- Panel de administración en /admin/
- Interfaz responsive con Bootstrap 5

## Stack

- Python 3.10+
- Django 4.2
- Bootstrap 5
- PostgreSQL (producción) / SQLite (local)
- Whitenoise para archivos estáticos
- Gunicorn como WSGI server
- Capacitor para empaquetar como APK Android

## Instalación local (Linux Mint)

```bash
git clone https://github.com/juanmolinae-bot/gestorcomm.git
cd gestorcomm

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Abrir en http://127.0.0.1:8000/

## Despliegue en Render.com

1. Crear un Web Service en Render conectado a este repositorio.
2. Configurar:
   - **Build command**: `./build.sh`
   - **Start command**: `gunicorn gestorcomm.wsgi:application`
3. Crear una base PostgreSQL en Render y vincularla.
4. Variables de entorno:
   - `SECRET_KEY` (generar una nueva, no usar la de dev)
   - `DEBUG` = `False`
   - `DATABASE_URL` (la entrega Render automáticamente al vincular la BD)

## Empaquetado APK con Capacitor

Ver el archivo `capacitor.config.json`. Para generar el APK:

```bash
npm init -y
npm install @capacitor/core @capacitor/cli @capacitor/android
mkdir www && echo "<meta http-equiv='refresh' content='0;url=https://gestorcomm.onrender.com'>" > www/index.html
npx cap add android
npx cap sync
cd android && ./gradlew assembleDebug
```

El APK queda en `android/app/build/outputs/apk/debug/app-debug.apk`.

## Estructura del proyecto

```
gestorcomm/
├── gestorcomm/          # configuración principal Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   └── incidencias/     # app principal
│       ├── models.py
│       ├── views.py
│       ├── forms.py
│       ├── urls.py
│       ├── admin.py
│       └── templates/
├── templates/
│   └── base.html
├── static/
├── build.sh             # build script para Render
├── capacitor.config.json
├── requirements.txt
└── manage.py
```

## Autor

Juan Molina Escalante 22-05-2026
