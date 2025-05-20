import logging
from PIL import Image
import os

# @celery_instance.task
def resize_image(image_path: str):
    logging.debug(f"Вызывается функция image_path с {image_path=}")
    sizes = [200, 500, 1000]

    base_dir = os.path.dirname(os.path.abspath(__file__))  # Путь к текущему файлу
    output_folder = os.path.join(base_dir, "../static/images")

    # Открываем изображение
    img = Image.open(image_path)

    # Получаем имя файла и его расширение
    base_name = os.path.basename(image_path)
    name, ext = os.path.splitext(base_name)

    # Проходим по каждому размеру
    for size in sizes:
        # Сжимаем изображение
        img_resized = img.resize(
            (size, int(img.height * (size / img.width))), Image.Resampling.LANCZOS
        )
        # Формируем имя нового файла
        new_file_name = f"{name}_{size}px{ext}"
        # Полный путь для сохранения
        output_path = os.path.join(output_folder, new_file_name)
        # Сохраняем изображение
        img_resized.save(output_path)
    logging.info(f"Изображение сохранено в следующих размерах: {sizes} в папке {output_folder}")
