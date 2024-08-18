from PIL import Image, ImageDraw
import qrcode
import sys
import os

def add_qr_to_image(image_path, qr_url, output_path=None):
    # Открываем изображение
    image = Image.open(image_path)
    
    # Генерируем QR-код для указанного URL
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_url)
    qr.make(fit=True)
    
    # Создаем изображение из QR-кода
    qr_img = qr.make_image(fill='black', back_color='white')
    
    # Изменяем размер QR-кода пропорционально
    qr_size = (110, 110)  # Размер QR-кода
    qr_img = qr_img.resize(qr_size)

    # Указываем позицию QR-кода
    position = (image.width - qr_img.width - 10, 10)  # Верхний правый угол
    
    # Вставляем QR-код на изображение
    image.paste(qr_img, position)

    # Генерируем имя выходного файла, если оно не указано
    if output_path is None:
        base_name, ext = os.path.splitext(image_path)
        output_path = f"{base_name}_with_qr{ext}"

    # Сохраняем отредактированное изображение
    image.save(output_path)
    print(f"Изображение сохранено: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("Usage: python add_qr.py <image_path> <qr_url> [output_path]")
    else:
        image_path = sys.argv[1]
        qr_url = sys.argv[2]
        output_path = sys.argv[3] if len(sys.argv) == 4 else None
        add_qr_to_image(image_path, qr_url, output_path)
