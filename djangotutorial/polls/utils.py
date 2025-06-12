import uuid

from PIL import Image
import io
from django.core.files.base import ContentFile


def optimize_image(image_field, max_size=(800, 800), quality=85):
    if not image_field:
        return None

    # Відкриваємо зображення і конвертуємо в RGB
    img = Image.open(image_field).convert('RGB')

    # Обрізаємо до квадрату по центру
    width, height = img.size
    min_dim = min(width, height)
    left = (width - min_dim) // 2
    top = (height - min_dim) // 2
    right = left + min_dim
    bottom = top + min_dim
    img = img.crop((left, top, right, bottom))

    # Зменшуємо розмір до max_size (thumbnail зберігає пропорції)
    img.thumbnail(max_size, Image.Resampling.LANCZOS)

    # Оптимізоване зображення зберігаємо в памʼять
    output = io.BytesIO()
    img.save(output, format='WEBP', quality=quality, optimize=True)
    output.seek(0)

    # Повертаємо вміст як ContentFile
    optimized_image = ContentFile(output.getvalue())

    # Генеруємо унікальне імʼя файлу
    uid = str(uuid.uuid4())[:8]
    new_name = f"{uid}.webp"

    return optimized_image, new_name