# add-qr

# Добавление QR-кода на изображение или видео с использованием Python и Docker

Этот проект позволяет автоматически добавлять QR-код на изображение или видео. Проект написан на Python и упакован в Docker для удобства использования.

## Возможности

- Генерация QR-кода по указанному URL.
- Автоматическое размещение QR-кода на изображении или видео.
- Поддержка изменения размера QR-кода.
- Сохранение оригинального звука при добавлении QR-кода в видео.
- Возможность указания имени выходного файла, чтобы избежать перезаписи исходного.

## Установка и запуск

### Требования

- Docker

### Сборка Docker-образа

Перед началом использования необходимо собрать Docker-образ:

```bash
docker build -t add-qr .
```

Запуск контейнера
1. Добавление QR-кода на изображение
```
docker run --rm -v $(pwd):/app add-qr python add_qr.py image /app/<image_name> <qr_url> /app/<output_image_name>
```
Пример:
```
docker run --rm -v $(pwd):/app add-qr python add_qr.py image /app/image.jpeg https://example.com /app/output_image.jpeg
```
2. Добавление QR-кода на видео
```
docker run --rm -v $(pwd):/app add-qr python add_qr.py video /app/<video_name> <qr_url> /app/<output_video_name>
```
Пример:
```
docker run --rm -v $(pwd):/app add-qr python add_qr.py video /app/video.mp4 https://example.com /app/output_video.mp4
```
Как работает
Скрипт поддерживает два режима:

image - для добавления QR-кода на изображение.

video - для добавления QR-кода на видео. При этом звук из оригинального видео сохраняется.

Параметры:
<image_name> или <video_name>: Путь к исходному файлу.
<qr_url>: URL для генерации QR-кода.
<output_image_name> или <output_video_name>: Путь для сохранения выходного файла.

Дополнительные параметры:
При добавлении QR-кода на видео сохраняется оригинальный звук.
QR-код генерируется в черно-белом формате для изображений и в формате RGB для видео, чтобы обеспечить совместимость.

Лицензия:
Этот проект распространяется под MIT License. Подробности см. в файле LICENSE.
