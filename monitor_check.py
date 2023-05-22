# -*- coding: cp1251 -*-

import smtplib
import pyscreenshot as ImageGrab
from PIL import Image
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Параметры для отправки почты
smtp_server = 'smtp.mail.ru'
smtp_port = 587
sender_email = 'your_email@example.com'
recipient_email = 'recipient_email@example.com'
password = 'your_password'

# Порог количества красного цвета на экране (0-255)
RED_THRESHOLD = 200
# Пороговое значение количества красных пикселей
THRESHOLD_VALUE = 100000

while True:
    # Захват изображения
    image = ImageGrab.grab()

    # Получение размеров экрана
    width, height = image.size

    # Получение количества пикселей красного цвета на экране
    red_pixels = 0
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            if r > RED_THRESHOLD and g < RED_THRESHOLD and b < RED_THRESHOLD:
                red_pixels += 1

    # Проверка, достигнуто ли пороговое значение
    if red_pixels > THRESHOLD_VALUE:
        # Изменение размера изображения
        resized_image = image.resize((800, 600))  # Укажите требуемые размеры изображения

        # Сохранение изображения в формате JPEG с заданным качеством сжатия (0-100)
        resized_image.save('screenshot.jpg', 'JPEG', quality=80)  # Укажите требуемое качество сжатия

        # Создание объекта MIMEMultipart и добавление текстового сообщения
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = 'Событие в программе'
        text = 'В программе обнаружено изменение поведения'
        msg.attach(MIMEText(text, 'plain'))

        # Чтение сохраненного изображения и добавление вложения
        with open('screenshot.jpg', 'rb') as f:
            image_data = f.read()
        image_mime = MIMEImage(image_data)
        image_mime.add_header('Content-Disposition', 'attachment', filename='screenshot.jpg')
        msg.attach(image_mime)

        # Отправка письма
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)

        print('Письмо успешно отправлено.')
        break
