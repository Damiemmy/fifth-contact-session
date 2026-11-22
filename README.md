# MediaHub — Fifth Contact Session Django Project

MediaHub is a responsive multimedia website built with Django. It lets visitors explore and search a library of videos, audio recordings and images, open media detail pages, and upload new content.

## Features
- Homepage with featured/latest media and format shortcuts
- Media library with keyword search, format filter and category filter
- Upload form for video, audio and image files
- HTML5 video and audio playback; image viewing
- Category and media management through Django admin
- SQLite database and local media-file storage
- Responsive layout for desktop and mobile
- Basic automated tests

## Requirements
- Python 3.10+
- pip

## Run locally

Open a terminal in the extracted `mediahub` project folder.

### Windows PowerShell
```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py makemigrations
python manage.py migrate
python manage.py seed_categories
python manage.py runserver
```

### Linux / macOS / WSL
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_categories
python manage.py runserver
```

Open http://127.0.0.1:8000/

## Admin dashboard
Create an administrator account:
```bash
python manage.py createsuperuser
```
Then visit http://127.0.0.1:8000/admin/ to manage categories and media items.

## Run tests
```bash
python manage.py test
```

## Uploading media
Choose **Upload media** from the navigation. Select a media format that matches the uploaded file. Supported extensions: MP4, WebM, MOV, MP3, WAV, OGG, M4A, JPG, JPEG, PNG, GIF and WebP. Upload limit: 100 MB. Actual playback depends on browser codec support.

## Project structure
```text
mediahub/
├── config/                 # Django project settings and URL configuration
├── media_library/          # Models, views, forms, admin, tests and templates
├── static/media_library/   # Responsive CSS
├── media/                  # Uploaded files (created automatically)
├── manage.py
└── requirements.txt
```

## Notes
- The project uses SQLite for a simple classroom setup.
- `DEBUG=True` and the development secret key are intended only for local coursework, not production deployment.
- The database and uploaded files are created locally when you run migrations and upload media.
- Seed categories are added by `python manage.py seed_categories`.
