# Django REST Framework Company API

This project is a beginner-friendly Django REST Framework API for managing companies and their employees. It provides CRUD operations for both resources, exposes them under `/api/`, and also includes Django admin support for creating and managing records from the browser.

## Project Structure

```text
DRF/
├── api/
│   ├── admin.py          # Admin configuration for Company and Employee
│   ├── models.py         # Company and Employee models
│   ├── serializer.py     # DRF serializers
│   ├── tests.py          # Test module
│   ├── urls.py           # API routes
│   └── views.py          # ViewSets and custom company employees endpoint
├── company_apis/
│   ├── settings.py       # Django settings
│   └── urls.py           # Project-level URL configuration
├── manage.py             # Django management entry point
├── requirements.txt      # Project dependencies
└── README.md
```

## Main Endpoints

- `/api/companies/` - CRUD for companies
- `/api/employees/` - CRUD for employees
- `/api/companies/<id>/employees/` - list employees for a single company
- `/admin/` - Django admin panel

## How To Use

1. Fork this repository, then clone your fork:

```bash
git clone <your-fork-url>
cd DRF
```

2. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py migrate
```

5. Optional but useful: create an admin user:

```bash
python manage.py createsuperuser
```

6. Run the development server:

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/api/`.

## Testing

Run the test suite with:

```bash
python manage.py test
```

Note: the project includes a test module, but it is currently minimal.

## Important Note About Data

After a fresh setup, the database will be empty by default. You will need to create your own `Company` and `Employee` records, either from the Django admin panel or through the API endpoints.
