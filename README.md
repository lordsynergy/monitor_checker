# Monitor Red Color Tracker

This is a simple Python program that tracks the presence of red color on the computer screen. It takes screenshots at regular
intervals and checks for the amount of red pixels present in the captured image. If the threshold value is exceeded, 
indicating a significant amount of red color, it saves the screenshot and sends it via email. This is necessary for remote 
automatic error detection in a number of programs in which a red window appears when errors occur.

## Prerequisites

Make sure you have the following dependencies installed:

- Python (version 3.6 or above)
- Pillow
- pyscreenshot

## Installation / Установка

1. Clone this repository to your local machine or download the source code as a ZIP file.

2. Open a terminal or command prompt and navigate to the project directory.

3. Install the required dependencies by running the following commands:

   ```shell
   pip install Pillow
   pip install pyscreenshot

## Usage

1. Open the `monitor_check.py` file in a text editor.

2. Modify the email settings in the code:

    - Update the `smtp_server`, `smtp_port`, `sender_email`, `recipient_email`, and `password` variables with your own email credentials.

3. Adjust the threshold values (`RED_THRESHOLD` and `THRESHOLD_VALUE`) as per your requirements.

4. Save the changes to the file.

5. Run the program by executing the following command in the terminal or command prompt:

   ```shell
   python monitor_check.py

***

# Мониторинг красного цвета

Программа на языке Python для отслеживания наличия красного цвета на экране компьютера. Она делает скриншоты с определенным 
интервалом времени и проверяет количество красных пикселей на захваченном изображении. Если значение превышает пороговое 
значение, указывающее на значительное количество красного цвета, программа сохраняет скриншот и отправляет его по электронной 
почте. Это необходимо для дистанционного автоматического выявления ошибок в ряде программ, в которых при возникновении ошибок
появляется окно красного цвета.

## Подготовка

Перед использованием программы убедитесь, что у вас установлены следующие зависимости:

- Python (версия 3.6 и выше)
- Pillow
- pyscreenshot

## Установка

1. Склонируйте репозиторий на свой компьютер или загрузите исходный код как ZIP-архив.

2. Откройте терминал или командную строку и перейдите в каталог проекта.

3. Установите необходимые зависимости, выполнив следующие команды:

   ```shell
   pip install Pillow
   pip install pyscreenshot

## Использование

1. Откройте файл `monitor_check.py` в текстовом редакторе.

2. Измените настройки электронной почты в коде:

   - Обновите переменные `smtp_server`, `smtp_port`, `sender_email`, `recipient_email`, и `password` вашими учетными данными электронной почты.

3. Подстройте пороговые значения (`RED_THRESHOLD` и `THRESHOLD_VALUE`) в соответствии с вашими требованиями.

4. Сохраните внесенные изменения.

5. Запустите программу, выполните следующую команду в терминале или командной строке:

   ```shell
   python monitor_check.py