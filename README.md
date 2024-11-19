# Freelance Management System

A web-based platform for managing freelance projects, clients, and invoices. The system is built using `FastAPI` for the backend and `PostgreSQL` as the database.

### Features

-  User Management: User authentication and management for freelancers and clients.
-  Projects: Track and manage freelance projects.
-  Clients: Maintain client information and associated project details.
-  Invoices: Create, update, and manage invoices.
-  Authentication: Secure user login and signup system.
-  CRUD Operations: Easy to manage data for users, clients, and projects.

#### Tech Stack

-  Backend: FastAPI
-  Database: PostgreSQL
-  Authentication: JWT (JSON Web Token)
-  ORM: SQLAlchemy
-  Password Hashing: Passlib
-  Environment Variables: python-dotenv

### Installation

Follow these steps to set up the project locally:

#### Prerequisites

1. Python 3.7 or above
2. PostgreSQL Database (Instructions for setting up a PostgreSQL database can be found here: [link to PostgreSQL documentation])

#### Setup

Clone the repository:

```shell
https://github.com/BertinKimberly/fms_fastapi.git

cd fms_fastapi

```

install dependencies

```shell
pip install -r requirements.txt
```

#### Set up the PostgreSQL database:

-  Create a new database in PostgreSQL.

-  Add the database URL to your `.env` file:

```js
DATABASE_URL=postgresql://user:password@localhost/dbname
```

#### run migrations

```shell
 alembic init migrations
```

#### Run the application

Use uvicorn

```shell
 uvicorn app.main:app --reload
```

for tseting, navigate to `/docs` or `/redoc`
