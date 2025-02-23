# Gas Service API 🚀

## 📌 Overview
Gas Service Management System
This project is a **Django-based** API that facilitates **gas service management**, allowing users to raise **service requests**, **track their status**, and **manage customers**. The system ensures seamless interaction between service **providers and customers**, addressing common challenges in traditional gas service management.

## 🔥 Features
✅ **Customer Management**  
✅ **Service Request Handling**  
✅ **Authentication & Authorization**  
✅ **RESTful API with DRF**  

## ⚙️ Tech Stack
- Backend: Django, Django REST Framework (DRF)
- Database: SQLite (pymysql)
- Authentication: Token-Based Authentication (DRF)

## 🔥How This Project Overcomes the Problem Statement
✅ **Online Service Requests: Customers can raise requests via API instead of calling or visiting.**

✅ **Authentication & Authorization: Only authenticated users can request services, ensuring security.**

✅ **Status Tracking: Users get real-time updates on service request progress.**

✅ **Admin Dashboard: Administrators can manage customer requests efficiently via the Django admin panel.**


**For More Information view -**
Link - https://docs.google.com/document/d/1BeWj02tTVy11bCirC6eBTY3bax-P8Y1_H-uWDAzfY64/edit?usp=sharing

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
