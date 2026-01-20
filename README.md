# Documentación de Creativa Digital 360 ITV

Esta documentación esta construida sobre MKDocs y el tema Material for MkDocs.

Para poder generar la documentación localmente, es necesario tener instalado Python y MKDocs.

## Prerrequisitos

1. Instalar Python (si no está ya instalado). Puedes descargarlo desde [python.org](https://www.python.org/downloads/).
2. Instalar pip, el gestor de paquetes de Python. Normalmente viene incluido con Python.
3. Instalar MKDocs y el tema Material for MkDocs ejecutando el siguiente comando en la terminal:

   ```bash
   pip install mkdocs-material
   ```

## Generar documentación localmente

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/CreativaDigital360/manual-creativadigital360.git
    ```

!!! note

    Ver repositorio correcto

2. Acceder a la carpeta del proyecto:

   ```bash
   cd manual-creativadigital360
   ```

3. Instalar las dependencias necesarias:

   ```bash
   pip install mkdocs-material
   ```

4. Iniciar el servidor de desarrollo:

   ```bash
   mkdocs serve
   ```

5. Abrir el navegador y acceder a `http://127.0.0.1:8000` para ver la documentación en vivo.

## Construir el sitio estático
Para generar los archivos estáticos de la documentación, ejecutar el siguiente comando:

```bash
mkdocs build
```
Los archivos generados se encontrarán en la carpeta `site/`.

## Desplegar la documentación
En un servidor web, copiar el contenido de la carpeta `site/` para que esté accesible a través de HTTP/HTTPS.

## Contribuir
Si deseas contribuir a la documentación, puedes hacerlo mediante pull requests en el repositorio de GitHub. Asegúrate de seguir las convenciones de estilo y formato establecidas en el proyecto.

## Servidor de documentación en línea
La documentación oficial está alojada en [https://docs.creativadigital360.com/](https://docs.creativadigital360.com/).

Está disponible en la maquina 404 (docs.programaitv.com-manualusuario), en el VPS PROXMOX de Creativa Digital 360 y se actualiza realizando un pull a la rama principal del repositorio de GitHub.

```bash
cd /ruta/al/repositorio/manual-creativadigital360
git pull origin main
mkdocs build --clean
```
Luego, se sirve el contenido de la carpeta `site/` a través del servidor web configurado (por ejemplo, Nginx o Apache).