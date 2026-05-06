# Tihar Jewelry E-Commerce Platform

A premium, full-stack Arabic e-commerce platform built for luxury jewelry. The platform features a responsive, dynamic frontend for customers, a secure backend API, and a fully functional admin dashboard for managing products, categories, analytics, and site configuration.

## 🚀 Tech Stack
- **Frontend:** Vue.js 3, Vanilla CSS (Glassmorphism & Gold Theme)
- **Backend:** Python (FastAPI), SQLAlchemy, MySQL
- **Infrastructure:** Docker, Docker Compose, Nginx (Reverse Proxy)
- **Security:** Let's Encrypt (Certbot SSL), JWT Authentication

## 📂 Project Structure
- `/frontend`: Vue.js storefront and Admin Panel.
- `/backend`: FastAPI application, endpoints, and database models.
- `/nginx`: Nginx reverse proxy configurations (HTTP & HTTPS).
- `docker-compose.yml`: Main container orchestration file.

---

## 💻 Local Development (Testing)

For local development, the platform is configured to run entirely over HTTP on port 80.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ali-abdullatif/tehar.git
   cd tehar
   ```

2. **Start the containers:**
   ```bash
   docker compose up --build -d
   ```

3. **Access the platform:**
   - Storefront: `http://localhost`
   - Admin Panel: `http://localhost/admin`
   - PhpMyAdmin: `http://localhost/phpmyadmin`

---

## 🌍 Production Deployment (VPS)

When deploying to a public server (VPS), you must secure the platform with HTTPS.

1. **Point your Domain:**
   Ensure your domain (e.g., `tihar.site`) has an `A Record` pointing to your VPS IP address.

2. **Run the Initial Setup:**
   On your VPS, clone the code and run the setup script to install Docker and build the project:
   ```bash
   chmod +x setup_vps.sh
   sudo ./setup_vps.sh
   ```

3. **Enable SSL (HTTPS):**
   Run the automated Certbot script. This will automatically generate Let's Encrypt certificates and configure Nginx to use them securely.
   ```bash
   chmod +x init-letsencrypt.sh
   sudo ./init-letsencrypt.sh
   ```
   *(Note: This script automatically creates a `.env` file containing `NGINX_CONF=nginx-ssl.conf`. This tells Docker to use the secure HTTPS configuration instead of the default local HTTP configuration. If your site ever drops back to HTTP on the VPS, simply recreate this file and restart Nginx).*

4. **Updating the Code in the Future:**
   When you push new changes to GitHub, log into your VPS and run:
   ```bash
   git pull
   sudo docker compose up --build -d && sudo docker compose restart nginx
   ```
   *(Your SSL certificates are safely stored and will not be broken by git pulls or container rebuilds).*

---

## 🔒 Default Admin Credentials
For security, change these inside `docker-compose.yml` or your `.env` file before going to production:
- **Username:** `admin`
- **Password:** `change_this_admin_pass`

## 💾 Backups
You can download a full backup (Database + Uploaded Images + SSL Certificates) directly from the **Admin Dashboard -> Site Settings**. 
Alternatively, the raw files are persistently mapped to the `./db_data`, `./uploads`, and `./data/certbot` directories on your host machine.
