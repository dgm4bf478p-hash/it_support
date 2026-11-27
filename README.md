# IT-қолдау өтінімдерін тіркеу жүйесі

Django-қосымша: қызметкер IT-қолдауға өтінім қалдырады (тақырып, сипаттама, басымдық),
өтінім «Жаңа» мәртебесімен тізімде көрінеді.

## Технологиялар
Python 3, Django, PostgreSQL (Render) / SQLite (жергілікті), gunicorn, WhiteNoise, python-dotenv, dj-database-url.

## Жергілікті іске қосу

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
cp .env.example .env             # Windows: copy .env.example .env
```

`.env` ішіне кілт жасап қойыңыз:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

```bash
python manage.py migrate
python manage.py runserver
```

Қосымша: http://127.0.0.1:8000/

## Конфигурация (орта айнымалылары)

| Айнымалы | Сипаттама | Жергілікті мысал |
| --- | --- | --- |
| `SECRET_KEY` | Django құпия кілті (міндетті) | кездейсоқ жол |
| `DEBUG` | `True` / `False` | `True` |
| `ALLOWED_HOSTS` | Үтірмен бөлінген хосттар | `localhost,127.0.0.1` |
| `DATABASE_URL` | PostgreSQL URL (бұлтта). Жоқ болса — SQLite | — |

`.env` репозиторийге түспейді; үлгі — `.env.example`.

## Журнал (logging)

| Оқиға | Деңгей | Хабарлама |
| --- | --- | --- |
| Өтінім сақталды | INFO | `Өтінім сақталды: id=<ID>` |
| Форма тексеруден өтпеді | WARNING | `Өтінім формасы тексеруден өтпеді` |
| Рұқсат етілмеген хост | ERROR | `DisallowedHost` (Django) |

Журналға сипаттама мәтіні мен құпия мәндер жазылмайды.

## Render-ге деплой

1. GitHub-қа репозиторий жариялаңыз (`.env` жоқ екенін тексеріңіз).
2. Render-де **PostgreSQL** құрыңыз, **Internal Database URL** көшіріңіз.
3. Сол аймақта **Web Service** құрыңыз:
   - Runtime: `Python 3`
   - Build Command: `bash build.sh`
   - Start Command: `gunicorn config.wsgi:application --bind 0.0.0.0:$PORT`
4. Environment: `SECRET_KEY` (жаңа кілт), `DEBUG=False`,
   `ALLOWED_HOSTS=<қосымша-домені>` (`https://` жоқ), `DATABASE_URL`.
5. **Deploy** → **Logs** бөлімінен INFO және WARNING жазбаларын тексеріңіз.

## Сілтемелер
- GitHub: _<сілтемені қойыңыз>_
- Render: _<сілтемені қойыңыз>_
