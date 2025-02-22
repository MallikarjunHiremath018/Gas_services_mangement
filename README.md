# Gas Service API 🚀

## 📌 Overview
Gas Service API is a **Django Rest Framework (DRF)** project that manages customer requests for gas services efficiently.

## 🔥 Features
✅ **Customer Management**  
✅ **Service Request Handling**  
✅ **Authentication & Authorization**  
✅ **RESTful API with DRF**  

## ⚙️ Tech Stack
- Django & Django REST Framework (DRF)
- SQLite (pymysql)
- Token-based Authentication (DRF)

## 🔥How This Project Overcomes the Problem Statement
✅ **Online Service Requests: Customers can raise requests via API instead of calling or visiting. **
✅ **Authentication & Authorization: Only authenticated users can request services, ensuring security.**
✅ **Status Tracking: Users get real-time updates on service request progress.**
✅ **Admin Dashboard: Administrators can manage customer requests efficiently via the Django admin panel.**

## 🛠️ Installation

```bash
# Clone the repo
git clone https://github.com/your-username/gas-service-api.git

# Navigate to the project folder
cd gas-service-api

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Start the server
python manage.py runserver
'''
