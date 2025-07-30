# INDITEL — Mobile Recharge & Payments Platform

INDITEL is a Django‑based platform for secure mobile, DTH, prepaid, postpaid, and Wi‑Fi recharges with Cashfree Payment Gateway integration, user authentication via email or social logins like Google, webhook‑based payment updates, and an admin dashboard to manage users, orders, and transactions.
---

## 🚀 Overview

**INDITEL** enables users to:
- Sign up / log in (email/password, optional **Google login**)
- Manage profiles and saved numbers
- Initiate mobile recharges
- Pay securely via **Cashfree Payment Gateway (PG)** (sandbox and production)
- Admin staff can review transactions, users, and logs

---

## ✨ Key Features

- **Authentication**: Email/password via **django-allauth**, optional Google login
- **Recharge Workflow**: Create order → Redirect to Cashfree → Webhook callback → Status update
- **Payment Gateway**: Cashfree PG (sandbox/production environments)
- **Admin Dashboard**: Django admin for users, orders, payment logs, and failures
- **Config via `.env`**: No secrets in code; easy per-environment config
---


## 🔧 Tech Stack

- **Python** 3.12/3.13
- **Django** 5.x
- **django-allauth** (auth), **django-environ** (env vars)
- **Cashfree PG** (`cashfree-pg` package; import as `cashfree_pg`)
- **DB**: SQLite (local) 


> If you’re on Windows and Python 3.13, prefer **Django 5.1+** for compatibility.

---

## 🔧 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/YogeshSharma185/INDITEL.git
   cd INDITEL
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Database and Env**
   Place the database and env inside my_site folder , in parallel to manage.py
   **The database is not included in the repo. Please email me if you need it.**

5. **Run the app**
   ```bash
   cd my_site
   python manage.py runserver
   ```

---
**The database is not included in the repo. Please email me if you need it.**

> Built with ❤️ by Yogesh