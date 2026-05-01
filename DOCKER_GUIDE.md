# 🐳 Dockerizing the Frontend

I have updated your Docker configuration to ensure a professional, production-ready setup. This includes optimized build caching and support for SPA routing.

## 🛠 Files Created/Updated

1.  **`Dockerfile`**: Multi-stage build (builds with Node 20, serves with Nginx).
2.  **`docker-compose.yml`**: Simplified configuration to run the container on port `8080`.
3.  **`nginx.conf`**: Custom configuration to handle SPA routing (redirects all requests to `index.html`).
4.  **`.dockerignore`**: Prevents unnecessary files (like `node_modules`) from being sent to the Docker daemon.

## 🚀 How to Run

To build and start your application, run:

```bash
docker-compose up --build -d
```

### 📍 Access points
- **URL**: [http://localhost:8080](http://localhost:8080)
- **Container Name**: `ahweb-frontend`

### 🔧 Useful Commands

- **Stop the container**:
  ```bash
  docker-compose down
  ```

- **View Logs**:
  ```bash
  docker-compose logs -f
  ```

- **Rebuild after changes**:
  ```bash
  docker-compose up --build -d
  ```

---
> [!TIP]
> This setup is optimized for production. If you want a development environment where changes update instantly (HMR), let me know and I can create a `docker-compose.dev.yml` for you!
