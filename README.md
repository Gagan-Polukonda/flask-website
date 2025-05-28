# Flask Website

A simple Flask web application with user authentication and profile management.

## Project Structure

```
flask-website/
├── routes/             # Route handlers
├── static/            # Static files (CSS, JS, images)
├── templates/         # HTML templates
├── app.py            # Application factory
├── config.py         # Configuration settings
└── requirements.txt  # Project dependencies
```

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

The application will be available at `http://localhost:7000`

## Features

- User authentication
- Profile management
- JSON API endpoints
- Template rendering
- URL redirection

## Development

- Development server runs on port 7000
- Debug mode is enabled in development
- Configuration can be modified in `config.py`
