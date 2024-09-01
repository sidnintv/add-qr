# add-qr

# Adding a QR code to an image or video using Python and Docker

This project allows you to automatically add a QR code to an image or video. The project is written in Python and packaged in Docker for ease of use.

## Features

- Generation of a QR code at the specified URL.
- Automatic placement of a QR code on an image or video.
- Support for resizing the QR code.
- Save the original sound when adding a QR code to a video.
- The ability to specify the name of the output file to avoid overwriting the original one.

## Installation and launch

### Requirements

- Docker

### Building a Docker image

Before using it, you need to build a Docker image:

```bash
docker build -t add-qr .
```

Launching the container
1. Adding a QR code to the image
```
docker run --rm -v $(pwd):/app add-qr python add_qr.py image /app/<image_name> <qr_url> /app/<output_image_name>
```
Example:
```
docker run --rm -v $(pwd):/app add-qr python add_qr.py image /app/image.jpeg https://example.com /app/output_image.jpeg
```
2. Adding a QR code to the video
```
docker run --rm -v $(pwd):/app add-qr python add_qr.py video /app/<video_name> <qr_url> /app/<output_video_name>
```
Example:
```
docker run --rm -v $(pwd):/app add-qr python add_qr.py video /app/video.mp4 https://example.com /app/output_video.mp4
```
How does it work?
```
The script supports two modes:

image - to add a QR code to the image.
video - to add a QR code to the video. At the same time, the audio from the original video is saved.

Parameters:
<image_name> or <video_name>: The path to the source file.
<qr_url>: URL for generating the QR code.
<output_image_name> or <output_video_name>: The path to save the output file.

Additional parameters:
When you add a QR code to a video, the original sound is saved.
The QR code is generated in black and white format for images and in RGB format for videos to ensure compatibility.
```
License:

This project is distributed under the MIT License. For details, see the LICENSE file.
