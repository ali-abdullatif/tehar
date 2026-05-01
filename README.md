# Al-Molook Jewelry E-Commerce Platform (مجوهرات الملوك)

A high-end, responsive Arabic jewelry web application featuring a modern "Golden Ratio" layout, luxury aesthetics, and a comprehensive management dashboard.

## Tech Stack

### Frontend
- **Framework**: Vue 3 (Composition API, `<script setup>`)
- **Build Tool**: Vite
- **Styling**: Custom CSS (Glassmorphism, Luxury Arabic Theme)
- **Routing**: Vue Router
- **Data Visualization**: Chart.js / Vue-Chartjs
- **HTTP Client**: Axios

### Backend
- **Framework**: FastAPI (Python)
- **Database ORM**: SQLAlchemy
- **Authentication**: JWT, bcrypt (Passlib)
- **Server**: Uvicorn & Gunicorn
- **Data Validation**: Pydantic

### Infrastructure & Services
- **Database**: MySQL 8.0
- **Database Management**: phpMyAdmin
- **Containerization**: Docker & Docker Compose
- **Web Server**: Nginx (via Frontend Dockerfile)

## Project Structure

- `/frontend` - Vue 3 Single Page Application
- `/backend` - FastAPI REST API
- `/db_data` - Local volume mount for MySQL data persistence
- `/uploads` - Local volume mount for persistent image uploads
- `docker-compose.yml` - Multi-container deployment configuration

## Getting Started

### Prerequisites
- Docker
- Docker Compose

### Running the Application

1. Clone the repository and navigate to the project directory:
   ```bash
   cd ahweb
   ```

2. Start the services using Docker Compose:
   ```bash
   docker-compose up -d --build
   ```

3. Access the application:
   - **Frontend Application**: [http://localhost:8080](http://localhost:8080)
   - **Backend API Docs (Swagger)**: [http://localhost:8000/docs](http://localhost:8000/docs)
   - **phpMyAdmin**: [http://localhost:8081](http://localhost:8081)

## Default Credentials

### Database (MySQL)
- User: `user`
- Password: `prod_db_pass_77`
- Root Password: `prod_root_pass_99`
- Database Name: `ahweb`

### Admin Dashboard
- Username: `admin`
- Password: `change_this_admin_pass`

*(Note: These are defined in `docker-compose.yml` and should be changed in a production environment via `.env` file.)*

## Deployment

The provided `docker-compose.yml` mounts local directories (`./db_data` and `./uploads`) to ensure that database records and user-uploaded media persist across container restarts. Gunicorn runs behind Uvicorn workers in the FastAPI container for robust API performance.
