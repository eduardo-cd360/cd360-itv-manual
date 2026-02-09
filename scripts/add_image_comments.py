#!/usr/bin/env python3
"""
Script para agregar comentarios con rutas absolutas de GitHub a las imágenes
en archivos Markdown del repositorio.

Ejemplo de resultado:
<!-- https://github.com/eduardo-cd360/cd360-itv-manual/tree/main/docs/path/to/images/image.png -->
![alt text](images/image.png)
"""

import os
import re
from pathlib import Path

# Ruta base del repositorio en GitHub
GITHUB_BASE_URL = "https://github.com/eduardo-cd360/cd360-itv-manual/tree/main"

# Ruta raíz del repositorio local
REPO_ROOT = Path(__file__).parent.parent

# Directorio docs
DOCS_DIR = REPO_ROOT / "docs"

# Patrón para encontrar imágenes en Markdown
# Captura: ![alt text](path/to/image.png) o ![alt text](path/to/image.png "title") o ![alt text](<path with spaces.png>)
IMAGE_PATTERN = re.compile(r'(!\[.*?\]\(<?[^)>]+\.(png|jpg|jpeg|gif|webp|svg)>?(?:\s+"[^"]*")?\)(?:\{[^}]*\})?)', re.IGNORECASE)

# Patrón para extraer la ruta de la imagen (incluye soporte para rutas con <>)
IMAGE_PATH_PATTERN = re.compile(r'!\[.*?\]\(<?([^)>"]+\.(png|jpg|jpeg|gif|webp|svg))>?(?:\s+"[^"]*")?\)', re.IGNORECASE)

# Patrón para detectar si ya hay un comentario con la URL de GitHub antes de la imagen
COMMENT_PATTERN = re.compile(r'<!--\s*https://github\.com/eduardo-cd360/cd360-itv-manual.*?-->\s*\n')


def get_absolute_image_path(md_file_path: Path, relative_image_path: str) -> str:
    """
    Convierte una ruta relativa de imagen a una ruta absoluta de GitHub.
    
    Args:
        md_file_path: Ruta absoluta al archivo Markdown
        relative_image_path: Ruta relativa de la imagen desde el archivo MD
    
    Returns:
        URL absoluta de la imagen en GitHub
    """
    # Directorio del archivo Markdown
    md_dir = md_file_path.parent
    
    # Resolver la ruta de la imagen
    if relative_image_path.startswith('./'):
        relative_image_path = relative_image_path[2:]
    
    # Ruta absoluta local de la imagen
    image_path = (md_dir / relative_image_path).resolve()
    
    # Convertir a ruta relativa desde la raíz del repositorio
    try:
        relative_from_root = image_path.relative_to(REPO_ROOT)
        return f"{GITHUB_BASE_URL}/{relative_from_root}"
    except ValueError:
        # Si la imagen está fuera del repositorio, devolver la ruta original
        return relative_image_path


def process_markdown_file(md_file_path: Path) -> tuple[bool, int]:
    """
    Procesa un archivo Markdown y agrega comentarios con rutas absolutas de GitHub
    antes de cada imagen que no los tenga.
    
    Args:
        md_file_path: Ruta al archivo Markdown
    
    Returns:
        Tupla (modificado, num_imagenes_procesadas)
    """
    with open(md_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    lines = content.split('\n')
    new_lines = []
    images_processed = 0
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Buscar imágenes en la línea actual
        match = IMAGE_PATTERN.search(line)
        
        if match:
            # Extraer la ruta de la imagen
            path_match = IMAGE_PATH_PATTERN.search(line)
            
            if path_match:
                image_path = path_match.group(1)
                
                # Verificar si la línea anterior ya es un comentario con la URL de GitHub
                has_comment = False
                if i > 0 and new_lines:
                    prev_line = new_lines[-1]
                    if COMMENT_PATTERN.match(prev_line + '\n') or '<!-- https://github.com/eduardo-cd360/cd360-itv-manual' in prev_line:
                        has_comment = True
                
                if not has_comment:
                    # Generar la URL absoluta
                    absolute_url = get_absolute_image_path(md_file_path, image_path)
                    
                    # Agregar el comentario antes de la imagen
                    comment = f"<!-- {absolute_url} -->"
                    new_lines.append(comment)
                    images_processed += 1
        
        new_lines.append(line)
        i += 1
    
    new_content = '\n'.join(new_lines)
    
    if new_content != original_content:
        with open(md_file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True, images_processed
    
    return False, 0


def main():
    """Procesa todos los archivos Markdown en el directorio docs."""
    print(f"Procesando archivos Markdown en: {DOCS_DIR}")
    print(f"URL base de GitHub: {GITHUB_BASE_URL}")
    print("-" * 60)
    
    total_files_modified = 0
    total_images_processed = 0
    
    # Buscar todos los archivos .md en docs/
    for md_file in DOCS_DIR.rglob("*.md"):
        modified, num_images = process_markdown_file(md_file)
        
        if modified:
            relative_path = md_file.relative_to(REPO_ROOT)
            print(f"✓ {relative_path} - {num_images} imagen(es) procesada(s)")
            total_files_modified += 1
            total_images_processed += num_images
    
    print("-" * 60)
    print(f"Total: {total_files_modified} archivo(s) modificado(s), {total_images_processed} imagen(es) procesada(s)")


if __name__ == "__main__":
    main()
