# Proxy6 Proxy Parser

Этот проект предназначен для автоматического входа на сайт Proxy6 и извлечения информации о прокси-серверах, используя Selenium WebDriver. Он получает данные с главной страницы и страницы пользователя, включая IP-адреса и даты окончания срока действия.

## Установка

Для начала работы с проектом вам нужно установить все зависимости, а также настроить файл `.env` с вашими учетными данными.

### 1. Клонируйте репозиторий

Склонируйте репозиторий с помощью Git:

```bash
git clone https://github.com/avfomin15/proxy_life_parser.git
```

### 2. Установите зависимости
Для установки необходимых библиотек используйте pip:

```bash

pip install -r requirements.txt
```

### 3. Настройка .env файла
Создайте файл .env в корне проекта и добавьте в него ваши данные для входа:


```env

LOGIN=your_login
PASSWORD=your_password
```

### 4. Убедитесь, что у вас установлен chromedriver
Для работы с Selenium необходимо скачать соответствующую версию ChromeDriver для вашего браузера. Поместите файл chromedriver.exe в папку chromedriver/ или укажите путь к нему в коде.