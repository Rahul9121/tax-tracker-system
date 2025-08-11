# Tax Tracker System

A web-based tax tracking application built with Flask and SQLite for managing company tax records and payments.

## Features

- **Employee Dashboard**: Secure login with password authentication
- **Customer Portal**: Access company-specific tax information
- **Record Management**: Add, edit, and delete tax records
- **Payment Processing**: Mark invoices as paid
- **User Registration**: New company signup functionality

## Demo Credentials

- **Employee Login Password**: `123`
- **Sample Companies**: `derm`, `tek`

## Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python app.py
   ```

3. Open your browser and visit: `http://localhost:5000`

## Database

The application uses SQLite with sample data automatically populated on first run.

## Deployment

This application is configured for deployment on Heroku and other cloud platforms, currently Deployed on Render(link attached).

## Project Structure

```
├── app.py              # Main Flask application
├── db.py               # Database initialization script
├── requirements.txt    # Python dependencies
├── Procfile           # Heroku deployment configuration
├── runtime.txt        # Python version specification
└── templates/         # HTML templates
    ├── index.html
    ├── employee_login.html
    ├── employee_dashboard.html
    ├── customer_login.html
    ├── customer_dashboard.html
    ├── company_info.html
    ├── new_user_signup.html
    └── edit_record.html
```

## Technologies Used

- Flask (Python web framework)
- SQLite (Database)
- HTML/CSS (Frontend)
- Gunicorn (WSGI server for deployment)
