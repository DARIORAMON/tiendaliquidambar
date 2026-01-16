🍃 Tienda Liquidambar - Almacén Natural
Tienda Liquidambar es una plataforma de e-commerce robusta desarrollada con Django, diseñada específicamente para la venta de productos naturales y sustentables. El sistema permite una gestión integral desde la administración de stock hasta la experiencia de compra del usuario final.

🚀 Características Principales
Gestión de Catálogo Dinámica: Los productos se organizan por categorías y tipologías, con soporte para múltiples imágenes por artículo.

Lógica de Negocio en Tiempo Real: Filtros inteligentes en la tienda que validan automáticamente el estado de publicación, stock disponible, precio y peso antes de mostrar un producto.

Experiencia de Usuario Interactiva:

Vista Rápida: Modales con zoom de imagen y selección de variantes.

Carrito de Compras: Sistema persistente basado en sesiones de Django para gestionar pedidos.

Panel Administrativo: Interfaz completa para la carga de productos, cuidados especiales y gestión de imágenes.

🛠️ Stack Tecnológico
Lenguaje: Python 3.x

Framework: Django

Frontend: HTML5, CSS3, Bootstrap 5, JavaScript (jQuery, GSAP para animaciones).

Base de Datos: PostgreSQL (Producción) / SQLite (Desarrollo).

Despliegue: Railway.

📦 Análisis del requirements.txt

django>=4.0
psycopg2-binary  # Necesario para PostgreSQL en Railway o plataformas similares
pillow           # Vital para el procesamiento de imágenes (ImagenProducto)
gunicorn         # Recomendado para servir la app en producción (Linux)
whitenoise       # Para la gestión eficiente de archivos estáticos en la nube

⚙️ Recomendaciones para Reutilización (Otras Plataformas)
Si descargas este proyecto para adaptarlo a otra tienda o desplegarlo en una plataforma distinta a Railway, ten en cuenta los siguientes puntos técnicos:

1. Variables de Entorno (Seguridad)
SECRET_KEY: No uses la que viene en el código; genera una nueva para producción.

DEBUG: Asegúrate de cambiar DEBUG = True a False en el archivo settings.py de producción.

2. Gestión de Archivos Media (Imágenes)
En este proyecto, las imágenes se sirven localmente. Si escalas a plataformas como Heroku, deberás configurar un servicio externo como AWS S3 o Cloudinary, ya que los sistemas de archivos en la nube suelen ser efímeros.

3. Base de Datos
El proyecto utiliza django-environ o variables de entorno para conectarse a PostgreSQL. Si usas otro motor (como MySQL), recuerda instalar el driver correspondiente y actualizar el diccionario DATABASES en settings.py.

4. Lógica de Visibilidad de Productos
Importante: Por diseño actual, si un producto tiene Stock=0, Peso=0.00 o Precio=0.00, no aparecerá en la tienda aunque esté "Publicado". Puedes modificar estos filtros en views_tienda.py si tu modelo de negocio permite preventas o productos digitales sin peso.

💻 Instalación Local
Clonar: git clone https://github.com/DARIORAMON/tiendaliquidambar.git

Entorno Virtual: python -m venv venv

Activar:

Windows: venv\Scripts\activate

Linux/Mac: source venv/bin/activate

Dependencias: pip install -r requirements.txt

Migraciones: python manage.py migrate

Admin: python manage.py createsuperuser

Run: python manage.py runserver

Desarrollado por: https://github.com/DARIORAMON
