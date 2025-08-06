# MailEase - Flask Email Sender App

MailEase is a simple Flask-based web app that allows users to send emails through a clean and responsive web interface.

## 💡 Features

- 📬 Send emails using Gmail SMTP
- 🔐 Uses environment variables to store email credentials securely
- 🎨 User-friendly interface with Bootstrap 5

## 🚀 How to Run

1. **Clone the repo**
```
git clone https://github.com/your-username/mailease-flask-app.git
cd mailease-flask-app
```

2.**Create and Activate Virtual Environment**
```
python -m venv venv
venv\Scripts\activate  # Windows
```

3. **Create a `.env` file** and add:

    ```
    EMAIL=your_email@gmail.com
    APP_PASSWORD=your_app_password
    ```
    ⚠️ Make sure you have enabled 2-Step Verification on your Gmail and generated an App Password.

4. **Install required packages**:

    ```
    pip install -r requirements.txt
    ```

5. **Run the app**:

    ```
    python app.py
    ```

6. **Open in browser**:  
   Navigate to `http://127.0.0.1:5000`

## Project Structure
```
mailease-flask-app/
│
├── templates/
│   └── form.html
├── static/
│   └── (optional custom styles or images)
├── .env
├── .gitignore
├── app.py
├── requirements.txt
└── README.md
```

## 🛠 Tech Stack

- Python
- Flask
- HTML & Bootstrap 5
- Gmail SMTP

## 👩‍💻 Author
```
Akshitha C H
Final year Computer Science Engineering Student
📍 St. Joseph Engineering College, Mangalore
```

## 📜 License

This project is open source and available under the MIT License.
