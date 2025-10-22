# Unsri Bot

[![Rasa](https://img.shields.io/badge/Rasa-3.6.21-FF6B6B?style=flat-square&logo=rasa)](https://rasa.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python)](https://python.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=flat-square&logo=docker)](https://docker.com/)
[![License](https://img.shields.io/badge/License-Educational-green?style=flat-square)](#license)

A comprehensive conversational AI chatbot for **Universitas Sriwijaya (UNSRI)** built with the Rasa framework. This intelligent assistant provides detailed information about the university, including academic programs, organizational structure, admission procedures, and administrative information.

## Features

### Academic Information
- **12 Faculties** with detailed program listings
- **Comprehensive department information** across all faculties
- **Academic degree programs** (Bachelor's, Master's, Doctoral, Professional)
- **Credit system (SKS)** explanations and calculations

### University Structure
- **Leadership information** (Rector, Vice Rectors, Deans)
- **Organizational structure** and administrative units
- **Research and community service** institutions (LP2M, LP3MP)
- **Supporting units** (UPT, Centers, Bureaus)

### Admission & Student Services
- **5 admission pathways** (SNMPTN, SBMPTN, USMB, etc.)
- **Student registration procedures** and requirements
- **International student** admission process
- **Scholarship information** (KIP Kuliah)

### Technical Features
- **Natural Language Processing** in Indonesian
- **Interactive conversation flow** with context awareness
- **Custom actions** for dynamic responses
- **REST API** for integration capabilities
- **Modern Web Interface** with real-time chat experience
- **CORS-enabled API** for seamless web integration
- **Responsive design** for mobile and desktop

> **⚠️ Data Notice**: This bot contains information about Universitas Sriwijaya as of 2021. Some information may be outdated and should be verified for current accuracy.

## Quick Start

### Prerequisites

- **Docker** (version 20.10 or higher)
- **Docker Compose** (version 2.0 or higher)
- **Git** (for cloning the repository)
- **Python 3** (for web server)

### Complete Setup Guide (Step-by-Step)

Follow these steps to get your Unsri Bot running with the web interface:

```
┌─────────────────────────────────────────────────────────────┐
│                    SETUP OVERVIEW                          │
├─────────────────────────────────────────────────────────────┤
│  Terminal 1: docker-compose up --build                     │
│  ├─ Builds Docker image                                    │
│  ├─ Trains Rasa model                                      │
│  ├─ Starts Action Server (port 5055)                      │
│  └─ Starts Rasa Server with CORS (port 5005)              │
│                                                             │
│  Terminal 2: python3 -m http.server 8080 --directory .    │
│  └─ Serves chatbot_ui.html (port 8080)                    │
│                                                             │
│  Browser: http://localhost:8080/chatbot_ui.html           │
│  └─ Connects to Rasa API via CORS                         │
└─────────────────────────────────────────────────────────────┘
```

#### Step 1: Clone and Setup
```bash
# Clone the repository
git clone <repository-url>
cd unsri-chatbot
```

#### Step 2: Start the Bot Services
```bash
# Start the Rasa bot with action server
docker-compose up --build
```

**What this does:**
- Builds the Docker image with all dependencies
- Trains the Rasa model automatically
- Starts the action server on port 5055
- Starts the Rasa server with CORS enabled on port 5005

**Wait for this message:** `✅ Model training completed!` and `🚀 Starting Rasa server with CORS enabled...`

#### Step 3: Start the Web Server
Open a **new terminal** (keep the first one running) and run:
```bash
# Navigate to the project directory
cd unsri-chatbot

# Start the web server
python3 -m http.server 8080 --directory .
```

You should see: `Serving HTTP on 0.0.0.0 port 8080`

#### Step 4: Access the Chatbot UI
1. **Open your web browser**
2. **Navigate to:** [http://localhost:8080/chatbot_ui.html](http://localhost:8080/chatbot_ui.html)
3. **Start chatting!** Type messages in Indonesian

#### Step 5: Verify Everything is Working

**In the Web Interface:**
- ✅ **Green status indicator** in the top-right of the chat interface
- ✅ **Welcome message** appears when you load the page
- ✅ **Bot responds** when you type "halo" or "hello"

**Test Messages to Try:**
```
You: halo
Bot: Hallo, ada yang bisa saya bantu ?

You: berapa jumlah fakultas di unsri?
Bot: Jumlah fakultas di Universitas Sriwijaya ada 12 Fakultas. 
     Apakah jawaban ini sudah sesuai permintaan ?
     [LIHAT FAKULTAS] [IYA] [TIDAK]
```

**If something isn't working:**
1. Check that both terminals are still running
2. Look for error messages in the terminals
3. Try refreshing the browser page
4. Check the troubleshooting section below

### Quick Access Summary

Once everything is running, you can access:
- **🌐 Web Interface**: [http://localhost:8080/chatbot_ui.html](http://localhost:8080/chatbot_ui.html) (Main interface)
- **🔧 API Endpoint**: [http://localhost:5005](http://localhost:5005) (For developers)
- **⚙️ Action Server**: [http://localhost:5055](http://localhost:5055) (Custom actions)

### Common Setup Issues

#### Issue: "Cannot access chatbot UI"
**Solution:** Make sure you have **TWO terminals running**:
1. Terminal 1: `docker-compose up --build` (bot services)
2. Terminal 2: `python3 -m http.server 8080 --directory .` (web server)

#### Issue: "CORS error in browser"
**Solution:** Wait for the bot to fully start. Look for these messages in Terminal 1:
- `✅ Model training completed!`
- `🚀 Starting Rasa server with CORS enabled...`

#### Issue: "Red status indicator in UI"
**Solution:** The bot services aren't ready yet. Wait 2-3 minutes after starting Docker.

#### Issue: "Port already in use"
**Solution:** 
```bash
# Check what's using the ports
lsof -i :5005
lsof -i :5055
lsof -i :8080

# Kill the processes
kill -9 <PID>
```

### What Docker Compose Does

The `docker-compose up --build` command will:
- Build the Docker image with all dependencies
- Train the Rasa model automatically
- Start the action server (port 5055)
- Start the Rasa server with CORS enabled (port 5005)
- Ready for web interface and API access




## Manual Setup (Alternative)

If you prefer to run the bot without Docker, follow these steps:

### Prerequisites

- **Python 3.8+**
- **pip** (Python package manager)
- **Git** (for cloning the repository)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd unsri-chatbot
   ```

2. **Create and activate virtual environment**
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Train the Rasa model**
   ```bash
   rasa train
   ```

5. **Start the action server** (Terminal 1)
   ```bash
   rasa run actions
   ```

6. **Start the Rasa server** (Terminal 2)
   ```bash
   rasa run --enable-api --cors "*"
   ```

7. **Start the web server** (Terminal 3)
   ```bash
   python3 -m http.server 8080 --directory .
   ```

8. **Access the bot**
   - **🌐 Web Interface**: [http://localhost:8080/chatbot_ui.html](http://localhost:8080/chatbot_ui.html) (Recommended)
   - **🔧 Rasa API**: [http://localhost:5005](http://localhost:5005)

## Usage

### Web Interface

The easiest way to interact with Unsri Bot is through the modern web interface:

1. **Start the bot**: `docker-compose up --build`
2. **Start web server**: `python3 -m http.server 8080 --directory .`
3. **Open browser**: Navigate to [http://localhost:8080/chatbot_ui.html](http://localhost:8080/chatbot_ui.html)

**Features:**
- **Natural Language Input**: Type questions in Indonesian
- **Interactive Buttons**: Click buttons for quick actions
- **Real-time Responses**: Instant replies with typing indicators
- **Mobile-friendly**: Works on all devices
- **Visual Status**: See bot connection status

### API Integration

The bot exposes REST API endpoints for integration with other systems:

#### Available Endpoints

- **Webhook**: `POST http://localhost:5005/webhooks/rest/webhook`
- **Health Check**: `GET http://localhost:5005/health`
- **Model Info**: `GET http://localhost:5005/model`
- **CORS Enabled**: All endpoints support cross-origin requests

#### Example API Usage

```bash
# Send a message to the bot
curl -X POST http://localhost:5005/webhooks/rest/webhook \
  -H "Content-Type: application/json" \
  -d '{
    "sender": "user123", 
    "message": "Berapa jumlah fakultas di Unsri?"
  }'

# Check bot health
curl http://localhost:5005/health
```

#### Response Format

```json
{
  "recipient_id": "user123",
  "text": "Jumlah fakultas di Universitas Sriwijaya ada 12 Fakultas."
}
```

## Project Structure

```
unsri-chatbot/
├── actions/                       # Custom action implementations
│   ├── __init__.py
│   └── actions.py                 # Dynamic response actions
├── data/                          # Training data
│   ├── nlu.yml                    # Natural Language Understanding data
│   ├── stories.yml                # Conversation stories
│   └── rules.yml                  # Conversation rules
├── models/                        # Trained model files (auto-generated)
│   └── *.tar.gz                   # Rasa model archives
├── tests/                         # Test files
│   └── test_stories.yml           # Test conversation stories
├── chatbot_ui.html                # Modern web interface
├── config.yml                     # Rasa configuration
├── domain.yml                     # Domain definition (intents, entities, responses)
├── requirements.txt               # Python dependencies
├── Dockerfile                     # Docker configuration
├── docker-compose.yml             # Docker Compose configuration
├── .gitignore                     # Git ignore patterns
├── .dockerignore                  # Docker ignore patterns
└── README.md                      # This documentation
```

### Key Files Explained

- **`domain.yml`**: Defines the bot's capabilities (intents, entities, responses, actions)
- **`config.yml`**: Rasa pipeline configuration for NLU and dialogue management
- **`data/nlu.yml`**: Training examples for understanding user intents
- **`data/stories.yml`**: Conversation flow examples
- **`data/rules.yml`**: Specific conversation rules and patterns
- **`actions/actions.py`**: Custom Python actions for dynamic responses
- **`chatbot_ui.html`**: Modern web interface with real-time chat experience

## Configuration

### Environment Variables

| Variable | Description | Default Value |
|----------|-------------|---------------|
| `RASA_ENDPOINT_URL` | Rasa server endpoint | `http://localhost:5005` |
| `RASA_ACTIONS_URL` | Action server endpoint | `http://localhost:5055` |

### Port Configuration

| Port | Service | Description |
|------|---------|-------------|
| **5005** | Rasa Server | Main API endpoint with CORS enabled |
| **5055** | Action Server | Custom actions and dynamic responses |
| **8080** | Web Server | Static file server for web interface |

### Docker Configuration

The `docker-compose.yml` file configures:
- **Multi-stage build** for optimized image size
- **Volume mounting** for model persistence
- **Port mapping** for external access (5005, 5055)
- **Environment variables** for configuration
- **CORS-enabled Rasa server** for web integration

## Troubleshooting

### Common Issues

#### Port Conflicts
**Problem**: Ports 5005, 5055, or 8080 are already in use
**Solution**: 
```bash
# Check what's using the ports
lsof -i :5005
lsof -i :5055
lsof -i :8080

# Kill processes using these ports
kill -9 <PID>
```

#### Docker Build Failures
**Problem**: Docker build fails during image creation
**Solutions**:
- Ensure sufficient disk space (at least 4GB free)
- Check internet connection for package downloads
- Clear Docker cache: `docker system prune -a`
- Try building with no cache: `docker-compose up --build --no-cache`

#### Model Training Issues
**Problem**: Rasa model training fails
**Solutions**:
- Verify all training data files are present and valid
- Check YAML syntax in `data/` directory
- Ensure sufficient memory (4GB+ RAM recommended)

#### Web Interface Issues
**Problem**: Web interface shows CORS errors or cannot connect
**Solutions**:
- Verify Rasa server is running with CORS enabled: `rasa run --enable-api --cors "*"`
- Check that both Rasa server (port 5005) and action server (port 5055) are running
- Ensure web server is running on port 8080: `python3 -m http.server 8080 --directory .`
- Check browser console for specific error messages


### Logging and Debugging

#### View Application Logs

```bash
# Docker Compose logs (all services)
docker-compose logs -f

# Specific service logs
docker-compose logs -f rasa
docker-compose logs -f actions

# Docker container logs
docker logs <container_id>
```

#### Debug Mode

```bash
# Run with debug logging
docker-compose up --build --no-cache

# Manual setup with debug
rasa run --enable-api --cors "*" --debug
rasa run actions --debug
```

### Getting Help

If you encounter issues not covered here:
1. Check the [Rasa Documentation](https://rasa.com/docs/)
2. Review the application logs for specific error messages
3. Ensure all prerequisites are met
4. Try the manual setup to isolate Docker-related issues

## Development

### Adding New Responses

To add new responses to the bot:

1. **Edit `domain.yml`** to add new response templates
2. **Update training data** in `data/nlu.yml` with new examples
3. **Add conversation flows** in `data/stories.yml` or `data/rules.yml`
4. **Retrain the model**: `rasa train`
5. **Restart the servers** to apply changes

### Custom Actions

Custom actions are implemented in the `actions/` directory:

1. **Create new action classes** in `actions/actions.py`
2. **Register actions** in `domain.yml` under the `actions` section
3. **Update training data** to use the new actions
4. **Test the actions** via the web interface
5. **Retrain and restart** the servers

### Testing

```bash
# Test conversation flows
rasa test

# Test specific stories
rasa test --stories tests/test_stories.yml

# Test API endpoints
curl -X POST http://localhost:5005/webhooks/rest/webhook \
  -H "Content-Type: application/json" \
  -d '{"sender": "test", "message": "halo"}'
```

### Model Performance

```bash
# Evaluate model performance
rasa test --cross-validation

# Generate confusion matrix
rasa test --confusion-matrix
```

## Contributing

We welcome contributions to improve Unsri Bot! Here's how you can help:

### Getting Started

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes** and test thoroughly
4. **Commit your changes**: `git commit -m 'Add amazing feature'`
5. **Push to the branch**: `git push origin feature/amazing-feature`
6. **Open a Pull Request**

### Contribution Guidelines

- Follow the existing code style and structure
- Add tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting
- Use clear, descriptive commit messages

### Reporting Issues

When reporting issues, please include:
- Operating system and version
- Python/Docker versions
- Steps to reproduce the issue
- Expected vs actual behavior
- Relevant log output

## License

This project is developed for **Universitas Sriwijaya** and contains information as of 2021. 

**Educational Use**: This project is intended for educational and informational purposes related to Universitas Sriwijaya.

**Data Accuracy**: Please contact the university directly to verify current data accuracy and for official information.

**Contact**: For licensing information or official university data, please contact Universitas Sriwijaya directly.

