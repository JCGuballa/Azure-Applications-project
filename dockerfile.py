
# =========================
# Stage 1: Build layer
# =========================
FROM python:3.10-slim-bullseye AS builder

# Avoid interactive tzdata prompts, and speed up pip
ENV DEBIAN_FRONTEND=noninteractive \
    PIP_NO_CACHE_DIR=1

# System build deps + unixODBC headers (needed to build or use pyodbc wheels)
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        gnupg2 \
        apt-transport-https \
        ca-certificates \
        unixodbc-dev \
    && rm -rf /var/lib/apt/lists/*

# Add Microsoft’s repo (Debian 11 "bullseye") for ODBC Driver 18
RUN curl -sSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > /usr/share/keyrings/ms.gpg \
 && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/ms.gpg] https://packages.microsoft.com/debian/11/prod bullseye main" \
    > /etc/apt/sources.list.d/microsoft.list \
 && apt-get update \
 && ACCEPT_EULA=Y apt-get install -y --no-install-recommends msodbcsql18 \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy only requirements first to leverage Docker layer caching
COPY requirements.txt /app/requirements.txt

# Create a clean install layer under /install (no venv needed)
RUN pip install --upgrade pip \
 && pip install --prefix=/install -r requirements.txt

# Copy the rest of the app
COPY . /app


# =========================
# Stage 2: Runtime layer
# =========================
FROM python:3.10-slim-bullseye AS runtime

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    # App Service will route traffic to this port (set WEBSITES_PORT=8000 in App Settings)
    PORT=8000

# Install only runtime libs: unixODBC (runtime), Microsoft ODBC Driver 18
RUN apt-get update && apt-get install -y --no-install-recommends \
        curl \
        gnupg2 \
        apt-transport-https \
        ca-certificates \
        unixodbc \
    && curl -sSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > /usr/share/keyrings/ms.gpg \
    && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/ms.gpg] https://packages.microsoft.com/debian/11/prod bullseye main" \
       > /etc/apt/sources.list.d/microsoft.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y --no-install-recommends msodbcsql18 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Bring site-packages from builder layer
COPY --from=builder /install /usr/local
# Bring your source code
COPY --from=builder /app /app

# If you use a private package index (e.g., enterprise Artifactory),
# COPY a pip.conf here and set PIP_CONFIG_FILE=/app/pip.conf

# Expose the internal port
EXPOSE 8000

# Start with Gunicorn. Your repo has "application.py" at root and a Flask "app" object.
# If your entry changes, update "application:app".
CMD ["gunicorn", "--bind=0.0.0.0:8000", "--timeout=600", "application:app"]
