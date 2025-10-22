# Use Python 3.8 slim image
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    curl \
    pkg-config \
    libhdf5-dev \
    libhdf5-serial-dev \
    hdf5-tools \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install build tools
RUN pip install --upgrade pip setuptools wheel

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies with retry mechanism
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir h5py || \
    (pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir h5py) && \
    pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Create necessary directories
RUN mkdir -p models

# Expose ports
EXPOSE 5005 5055

# Create startup script for action server and Rasa server with CORS
RUN echo '#!/bin/bash\n\
echo "🤖 Starting Unsri Bot..."\n\
echo "📚 Training model..."\n\
rasa train --quiet\n\
echo "✅ Model training completed!"\n\
echo "🚀 Starting action server in background..."\n\
rasa run actions --port 5055 &\n\
ACTION_PID=$!\n\
echo "⏳ Waiting for action server to start..."\n\
sleep 10\n\
echo "🚀 Starting Rasa server with CORS enabled..."\n\
rasa run --enable-api --cors "*" --port 5005\n\
' > start.sh && chmod +x start.sh

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
    CMD curl -f http://localhost:5005/health || exit 1

# Start the application
CMD ["./start.sh"]
