# Django Blog — mysite

A full-featured blog application built with Django, developed as a personal learning project covering authentication, content management, comments, SEO basics, and environment-based configuration.

🔗 **Live demo:** _coming soon_
📂 **Repository:** https://github.com/radmehrss/django-blog

---

## Features

### Blog
- Create, publish, and schedule posts (posts only appear once their `published_date` has passed)
- Image upload per post, with a default fallback image
- Multiple categories per post (many-to-many) and tag support via `django-taggit`
- Full-text search across post content
- Filter posts by category, tag, or author
- Pagination
- Previous / next post navigation on the single post page
- View counter per post
- Optional "login required" posts — visitors are redirected to log in before reading
- RSS feed for the latest posts (`django.contrib.syndication`)
- Custom template tags: latest posts widget and post-count-by-category widget

### Comments
- Comment form on each post (name, email, subject, message)
- Comments require admin approval (`approved` flag) before they appear publicly
- Live comment count per post via a custom template tag

### Accounts
- User signup, login, and logout using Django's built-in authentication forms
- Redirect-back-after-login flow for protected content

### Website / static pages
- Home, About, and Contact pages
- Contact form that stores submissions in the database
- Newsletter signup (email capture)

### SEO & admin tooling
- `django.contrib.sitemaps` for both the blog and static pages
- `django-robots` for `robots.txt` management
- Django admin with `django-summernote` rich text editor for writing posts
- CAPTCHA protection on forms
- `django-debug-toolbar` and `django-extensions` for local development

---

## Tech stack

| Layer      | Technology |
|------------|------------|
| Backend    | Python, Django |
| Database   | SQLite (development) |
| Frontend   | HTML, CSS (Bootstrap-based templates), JavaScript |
| Config     | `python-decouple` + `.env` for environment-based settings (`dev` / `prod`) |

---

## Project structure

```
mysite/
├── mysite/
│   ├── settings.py          # shared/base settings
│   └── setting/
│       ├── dev.py           # development settings
│       └── prod.py          # production settings
├── blog/                    # posts, comments, tags, categories, RSS feed
├── accounts/                 # authentication (login / signup / logout)
├── website/                  # static pages: home, about, contact, newsletter
├── templates/
├── statics/
└── manage.py
```

---

## Getting started locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/radmehrss/django-blog.git
   cd django-blog
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   Create a `.env` file in the project root:
   ```
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser** (to access the admin panel)
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000/`

---

## What I learned building this

This project was my hands-on introduction to Django after a focused workshop. Along the way I worked through:
- Structuring a multi-app Django project (`blog`, `accounts`, `website`)
- Writing custom template tags and inclusion tags
- Handling forms, validation, and messages framework
- Splitting settings for development vs. production and keeping secrets out of source control
- Debugging real, layered issues rather than following a tutorial line by line

## Roadmap

- [ ] Deploy to a live host (Railway / Liara)
- [ ] Add automated tests
- [ ] Switch to PostgreSQL for production
- [ ] Add user profile pages

---

## Author

**Radmehr Saeidi**
Materials & Metallurgical Engineering student, Iran University of Science and Technology
Learning Django with the goal of freelance web development
