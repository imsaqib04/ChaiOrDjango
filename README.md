## ☕ChaiOrDjango
A simple Django project named chaiOrCode with a custom application called chai. This project demonstrates basic Django setup, URL routing, templates, and static file usage.


## 📁 Project Structure

```
.
├── chai
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── templates
│   │   └── chai
│   │       └── all_chai.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── chaiOrCode
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
├── static
│   └── style.css
└── templates
    └── index.html
```

## 👥 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Clone** your fork: `git clone https://github.com/imsaqib04/ChaiOrDjango.git`
3. **Create** a new branch: `git checkout -b feature/your-feature`
4. **Commit** your changes: `git commit -am 'Add some feature'`
5. **Push** to your branch: `git push origin feature/your-feature`
6. **Open** a pull request

```
Home, About, and Contact pages in the main project

Custom chai app with a dedicated all_chai page

Template rendering for both project and app views

Static file handling for CSS styling

SQLite3 database (default Django configuration)
```

### 🚀 Setup & Installation

***1️⃣ Prerequisites***

Python 3.x installed

Django installed (pip install django)

***2️⃣ Clone the Repository***

git clone <repository-url>

cd chaiOrDjango

***3️⃣ Apply Migrations***

python manage.py migrate

***4️⃣ Run the Development Server***


python manage.py runserver

***5️⃣ Open in Browser***

Visit: http://127.0.0.1:8000/

### 📜 License
This project is open-source and available under the MIT License.
