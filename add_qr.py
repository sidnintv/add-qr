from PIL import Image, ImageDraw
import qrcode
import sys
import os
from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip

def generate_qr_code(qr_url, size=(100, 100), convert_to_rgb=False):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_url)
    qr.make(fit=True)
    
    qr_img = qr.make_image(fill='black', back_color='white')
    qr_img = qr_img.resize(size)
    
    if convert_to_rgb:
        qr_img = qr_img.convert("RGB")
    
    return qr_img

def add_qr_to_image(image_path, qr_url, output_path=None):
    image = Image.open(image_path)
    qr_img = generate_qr_code(qr_url, size=(100, 100), convert_to_rgb=False)
    position = (image.width - qr_img.width - 10, 10)
    image.paste(qr_img, position)

    if output_path is None:
        base_name, ext = os.path.splitext(image_path)
        output_path = f"{base_name}_with_qr{ext}"

    image.save(output_path)
    print(f"Изображение сохранено: {output_path}")

def add_qr_to_video(video_path, qr_url, output_path):
    qr_img = generate_qr_code(qr_url, size=(150, 150), convert_to_rgb=True)
    qr_img.save("qr_temp.png")

    video = VideoFileClip(video_path)

    qr_clip = ImageClip("qr_temp.png").set_duration(video.duration).set_position(("right", "top")).set_start(0)

    # Объединяем видео с QR-кодом и сохраняем вместе с оригинальным аудио
    result = CompositeVideoClip([video, qr_clip])
    result = result.set_audio(video.audio)  # Убедитесь, что звук сохранен

    result.write_videofile(output_path, codec="libx264", audio_codec="aac", fps=video.fps)

    os.remove("qr_temp.png")
    print(f"Видео сохранено: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python add_qr.py <mode> <file_path> <qr_url> [output_path]")
        print("mode: 'image' или 'video'")
    else:
        mode = sys.argv[1]
        file_path = sys.argv[2]
        qr_url = sys.argv[3]
        output_path = sys.argv[4] if len(sys.argv) == 5 else None

        if mode == 'image':
            add_qr_to_image(file_path, qr_url, output_path)
        elif mode == 'video':
            if output_path is None:
                base_name, ext = os.path.splitext(file_path)
                output_path = f"{base_name}_with_qr{ext}"
            add_qr_to_video(file_path, qr_url, output_path)
        else:
            print("Неверный режим. Используйте 'image' или 'video'.")
