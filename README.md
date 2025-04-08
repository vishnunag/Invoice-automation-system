# 🧾 Invoice Sender Web App

A Django-based web application that automates invoice creation and email delivery to clients. The goal of this project is to simplify the process of generating and sending invoices with minimal manual effort.

---

## 🚀 Features

- 📝 Create professional invoices with client details
- 📧 Send invoices to client emails with one click
- 📂 Store and view past invoices
- 🖨️ Download invoices as PDFs
- 🔒 Secured with authentication (optional)

---

## 🛠️ Tech Stack

- **Backend**: Django, Python
- **Frontend**: HTML, CSS, JavaScript
- **PDF Generation**: WeasyPrint / ReportLab / xhtml2pdf (depending on what you used)
- **Email**: Django Email Backend (SMTP)

---

## 📂 Folder Structure

```plaintext
invoice-sender/
│
├── invoices/              # Main Django app
├── templates/             # HTML invoice templates
├── static/                # CSS/JS assets
├── db.sqlite3             # Database
├── manage.py              # Django runner
└── README.md              # Project overview
