import uuid

from PIL import Image
import io
from django.core.files.base import ContentFile


def optimize_image(image_field, max_size=(800, 800), quality=85):
    if not image_field:
        return None

    img = Image.open(image_field).convert('RGB')

    img.thumbnail(max_size, Image.Resampling.LANCZOS)

    # Save the optimized image
    output = io.BytesIO()
    img.save(output, format='WEBP', quality=quality, optimize=True)
    output.seek(0)

    # Create a new ContentFile with the optimized image
    optimized_image = ContentFile(output.getvalue())

    # Generate new filename with .webp extension
    uid = str(uuid.uuid4())[:8]
    new_name = f"{uid}.webp"

    # повертає фото і його назву
    return optimized_image, new_name