# Платформа экопросвещения

Этот Django-проект служит основой для платформы экопросвещения: челленджи, сортировка отходов и карта пунктов приёма.

## Getting started

1. Activate the virtual environment:
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

2. Install dependencies (if any new):
   ```powershell
   pip install -r requirements.txt
   ```

3. Run migrations:
   ```powershell
   python manage.py migrate
   ```

4. (Optional) create a superuser to access the admin interface:
   ```powershell
   python manage.py createsuperuser
   ```

5. Launch the development server:
   ```powershell
   python manage.py runserver
   ```

Откройте http://127.0.0.1:8000/ чтобы увидеть главную страницу. Вы можете перейти по `/accounts/`, `/challenges/` и `/locations/` для соответствующих разделов. Чтобы загрузить тестовые данные:

```
python manage.py loaddata fixtures/initial_data.json
```


## Структура проекта

- `accounts`, `challenges`, `locations` — Django-приложения для основных функций.
- `config` содержит настройки и маршруты проекта.

Не стесняйтесь расширять приложения моделями, шаблонами и API по мере необходимости.