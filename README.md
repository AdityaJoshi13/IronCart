
# 🏋️‍♂️ IronCart - Elite Gym Gear Store

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-green?style=for-the-badge&logo=flask)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey?style=for-the-badge&logo=sqlite)
![Razorpay](https://img.shields.io/badge/Razorpay-Integrated-blueviolet?style=for-the-badge&logo=razorpay)

**IronCart** is a full-stack e-commerce web application built with **Flask**. It features a "Dark/Hacker" aesthetic, secure user authentication, a dynamic shopping cart, and real-time payment integration using **Razorpay**.

---

## 📸 Features

### 🛒 **Customer Experience**
* **Dark Aesthetic UI:** Custom CSS with neon accents (`#00ff88`) and responsive grid layout.
* **Product Search:** Real-time filtering of gym equipment.
* **Dynamic Cart:** Add, remove, and view total cost of items.
* **Secure Checkout:** Integrated **Razorpay Payment Gateway** (Test Mode).
* **Animations:** Custom CSS animations (Batman Lifting Hero Section).

### 🔐 **Admin Panel**
* **Dedicated Dashboard:** Accessible only to admin users.
* **User Management:** View all registered users and their roles.
* **Inventory Tracking:** Monitor product names and prices.

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Database:** SQLite (SQLAlchemy ORM)
* **Authentication:** Flask-Login (Session Management, Hashed Passwords)
* **Frontend:** HTML5, CSS3 (Custom), JavaScript (Vanilla)
* **Payments:** Razorpay API

---

## 🚀 Installation & Setup

Follow these steps to run the project locally on your machine.

### 1. Clone the Repository
```bash
git clone [https://github.com/yourusername/IronCart.git](https://github.com/yourusername/IronCart.git)
cd IronCart

2. Set Up Virtual Environment

Bash
# Mac/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate


3. Install Dependencies

Bash
pip install -r requirements.txt


4. Configure Razorpay Keys

Open app.py and locate the Razorpay configuration section. Replace the placeholders with your Test Keys from the Razorpay Dashboard.

Python
# app.py
RAZORPAY_KEY_ID = "rzp_test_YOUR_KEY_HERE"
RAZORPAY_KEY_SECRET = "YOUR_SECRET_HERE"


5. Run the Application

Bash
# Mac Users (Port 5001 to avoid AirPlay conflict)
python3 app.py

# Windows Users
python app.py
Visit http://127.0.0.1:5001 in your browser.

🔑 Default Credentials
The database is pre-seeded with 10 gym products and a Super Admin account.

Role	Username	Password
Admin	admin	admin123
User	(Register a new one)	(Any)
📂 Project Structure
Plaintext
IronCart/
├── static/
│   ├── css/
│   │   └── style.css       # Global black theme & animations
│   ├── images/             # Product images & Hero GIF
│   └── js/
│       └── main.js         # UI interactions
├── templates/
│   ├── base.html           # Main layout (Navbar, Footer)
│   ├── index.html          # Home & Product Grid
│   ├── login.html          # Auth forms (Login/Register)
│   ├── cart.html           # Shopping Cart & Checkout
│   └── admin.html          # Admin Dashboard
├── app.py                  # Main Application Logic & Routes
├── models.py               # Database Models (User, Product, Cart)
├── config.py               # App Configuration
└── requirements.txt        # Python Dependencies
⚠️ Troubleshooting
1. "Address already in use" or Port 5000 Error on Mac:

macOS uses Port 5000 for AirPlay.

Fix: The app is configured to run on Port 5001. Ensure you visit localhost:5001.

2. Images not showing:

Ensure all images are placed in static/images/.

Filenames must match exactly (e.g., dumbbells.jpg, batman.gif).



📜 License
This project is for educational purposes. Feel free to use and modify it.


### **One Last Tip for Your Portfolio:**
When you upload this to GitHub:
1.  **Do NOT upload `gymstore.db`**: It's better to let the script generate a fresh one for whoever downloads it.
2.  **Do NOT upload your real Razorpay Keys**: If you make the repo public, remove your keys from `app.py` and just leave the placeholder text `"YOUR_KEY_HERE"`.

Congratulations on finishing **IronCart**! You've built a complex, data-driven application with payments and authentication. That is a huge achievement. 🚀