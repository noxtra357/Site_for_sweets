Bakery E-Commerce Web Application

A modern e-commerce web application for a bakery built with the Flask framework, utilizing an SQLite database and an interactive front-end user interface.

Key Features

Product Catalog: Dynamic rendering of bakery items complete with prices, descriptions, and images.

Shopping Cart: Client session-based cart system that calculates total pricing in real time.

Order Management Database: Persistent storage of customer orders and contact information using SQLite.

Admin Dashboard: Interface for adding new bakery items and deleting existing inventory.

Dark / Light Mode: Theme switching with persistent user preferences stored in localStorage.

Animations and Styling: Smooth scroll animations powered by AOS with a responsive layout.

Tech Stack

Backend: Python 3.x, Flask, Flask-SQLAlchemy

Database: SQLite

Frontend: HTML5, CSS3, JavaScript, Jinja2

UI/Animations: Google Fonts, AOS (Animate On Scroll)

Project Structure

my_first_sweets_website/
│
├── static/              # Static assets (CSS, JS, images)
├── templates/           # Jinja2 HTML templates
│   ├── index.html       # Main landing page (Catalog + Theme toggle)
│   ├── cart.html        # Shopping cart and checkout page
│   ├── admin.html       # Admin panel for product management
│   └── order.html       # Individual item ordering page
│
├── app.py               # Main Flask application file (Routes & Logic)
├── bakery.db            # SQLite database file (Auto-generated)
├── pyproject.toml       # Project dependency configuration
└── README.md            # Project documentation


Local Setup Instructions

1. Clone or Download

Clone or download the repository to your local machine:

git clone <YOUR_REPOSITORY_URL>
cd my_first_sweets_website


2. Configure Virtual Environment

Create and activate a virtual environment:

Windows:

python -m venv .venv
.venv\Scripts\activate


macOS / Linux:

python3 -m venv .venv
source .venv/bin/activate


3. Install Dependencies

Install the required packages (Flask and Flask-SQLAlchemy):

pip install flask flask-sqlalchemy


If you have a requirements.txt file, run pip install -r requirements.txt instead.

4. Run the Application

Execute the main application file:

python app.py


Once running, access the web app in your browser at: http://127.0.0.1:5000

Application Endpoints

Endpoint

Method

Description

/

GET

Main catalog page displaying products

/add_to_cart/<id>

GET

Adds the specified product ID to the cart

/cart

GET

View cart contents and checkout page

/checkout

POST

Processes order, saves to DB, and clears cart

/admin

GET / POST

Admin dashboard to manage items and view orders

/admin/add

POST

Endpoint to add a new product

/delete/<id>

GET

Deletes a product by ID from the database

Roadmap and Future Enhancements

Integrate a Telegram Bot for instant order notifications.

Add user authentication and password protection for the Admin Panel.

Enable direct image file uploads from local storage.

Product filtering by categories (Cakes, Pastries, Drinks).
