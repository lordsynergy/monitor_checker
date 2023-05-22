
# -*- coding: cp1251 -*-

import subprocess

# Список зависимостей, которые требуется установить
dependencies = ['pyscreenshot', 'Pillow']

# Проверка наличия зависимостей и их установка при необходимости
for dependency in dependencies:
    try:
        subprocess.check_output(['pip', 'show', dependency])
    except subprocess.CalledProcessError:
        print(f'Зависимость {dependency} отсутствует. Установка...')
        try:
            subprocess.check_call(['pip', 'install', dependency])
            print(f'Зависимость {dependency} успешно установлена.')
        except Exception as e:
            print(f'Ошибка при установке зависимости {dependency}: {str(e)}')

import time
import smtplib
import pyscreenshot as ImageGrab
from PIL import Image
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

## Параметры для отправки почты
 smtp_server = 'smtp.mail.ru'
 smtp_port = 587
 sender_email = 'your_email@example.com'
 recipient_email = 'recipient_email@example.com'
 password = 'your_password'

# Порог количества красного цвета на экране (0-255)
RED_THRESHOLD = 200
# Пороговое значение количества красных пикселей
THRESHOLD_VALUE = 100000

print('Программа для отслеживания красного цвета на экране компьютера. Ожидание начала работы...')
print('Программа успешно запущена. Отслеживание красного цвета на экране.')

try:
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

            print('Найдено изменение поведения. Снимок экрана сохранен и отправлен по электронной почте.')

        time.sleep(1)  # Задержка в 1 секунду перед повторной проверкой

except KeyboardInterrupt:
    print('Программа остановлена по запросу пользователя.')