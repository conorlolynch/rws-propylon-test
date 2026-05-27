# Propylon Document Manager Assessment

The Propylon Document Management Technical Assessment is a simple (and incomplete) web application consisting of a basic API backend and a React based client. This API/client can be used as a bootstrap to implement the specific features requested in the assessment description.

## Getting Started

### API Development

The API project is a [Django/DRF](https://www.django-rest-framework.org/) project that utilizes a [Makefile](https://www.gnu.org/software/make/manual/make.html) for a convenient interface to access development utilities. This application uses [SQLite](https://www.sqlite.org/index.html) as the default persistence database you are more than welcome to change this. This project requires Python 3.11 in order to create the virtual environment. You will need to ensure that this version of Python is installed on your OS before building the virtual environment. Running the below commmands should get the development environment running using the Django development server.

1. `$ make build` to create the virtual environment.
2. `$ make fixtures` to create a small number of fixture file versions.
3. `$ make serve` to start the development server on port 8001.
4. `$ make test` to run the limited test suite via PyTest.

### Client Development

See the Readme [here](https://github.com/propylon/document-manager-assessment/blob/main/client/doc-manager/README.md)

##

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)

### Backend

During setup, I encountered some environment-specific issues with the `$ make serve` workflow on Windows/MSYS2, primarily related to shell activation and command compatibility assumptions in the Makefile.

To avoid spending excessive time debugging shell/runtime differences, I executed the underlying setup steps manually instead (virtual environment activation, dependency installation, migrations, and runserver execution) seen below.

Create venv manually:

```bash
py -3.11 -m venv .env_python3.11
```

Activate it

```bash
.env_python3.11\Scripts\Activate.ps1
```

Install requirements manually

```bash
pip install -r requirements/dev.txt
pip install -e .
```

Set environment variables manually

```bash
$env:PYTHONPATH="."
$env:DJANGO_SETTINGS_MODULE="propylon_document_manager.site.settings.local"
```

These exports are critical because the Makefile assumes Unix export

Run migrations manually

```bash
django-admin makemigrations
django-admin migrate
```

Start server

```bash
django-admin runserver 0.0.0.0:8001
```

Test URL - http://127.0.0.1:8001/api/file_versions/

### Frontend — React + TypeScript client

This project uses a Vite-powered React + TypeScript client. The steps below show how I created the client and how to run it in development.

Prerequisites

- Node 22.14.0
- npm 11.3.0

Create the project

```bash
cd client
npm create vite@latest doc-manager -- --template react-ts
```

When prompted select `React` and then `TypeScript`.

Start development server

```bash
cd client/doc-manager
npm install
npm run dev
```

The Vite dev server will print a local address (for example `http://localhost:5173`) where the client is available.

Build and preview (optional)

```bash
npm run build
npm run preview
```

These commands build a production bundle and run a preview server for the built app.
