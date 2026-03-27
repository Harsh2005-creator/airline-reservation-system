# ✈️ Airline Reservation System

A full-stack airline ticket booking system built using **Flask, MySQL, HTML, CSS, and JavaScript**.
This project simulates a real-world airline booking experience with advanced UI and backend integration.

---

## 🚀 Features

### 🔍 Flight Search & Filtering

* Search flights by flight number, source, or destination
* Source → Destination dropdown filtering
* 📅 Date-based filtering
* ⬆️ Price sorting (Low → High, High → Low)
* 🟢 Cheapest flight highlighting

### 💺 Booking System

* Real-time seat availability
* Interactive seat selection grid
* Prevents double booking
* Ticket preview before confirmation

### 💳 Payment Simulation

* Fake payment interface
* Booking confirmed only after payment
* Smooth booking flow

### 📖 Booking Management

* View all bookings
* 🎫 Ticket-style booking display
* ❌ Cancel booking functionality
* Auto seat release after cancellation

---

## 🛠️ Tech Stack

| Layer    | Technology            |
| -------- | --------------------- |
| Backend  | Python (Flask)        |
| Database | MySQL                 |
| Frontend | HTML, CSS, JavaScript |
| API      | REST APIs             |

---

## 📂 Project Structure

airline-reservation-system/
│
├── backend/           # Flask backend
│   ├── app.py
│   ├── db.py
│   ├── routes/
│   └── models/
│
├── frontend/          # UI
│   ├── index.html
│   ├── dashboard.html
│   ├── bookings.html
│   ├── payment.html
│   └── style.css
│
├── screenshots/       # Images
│   └── Bgimage.png

---

## ▶️ How to Run the Project

### 1️⃣ Backend Setup

cd backend
pip install -r requirements.txt
python app.py

---

### 2️⃣ Database Setup

CREATE DATABASE airline_system;

---

### 3️⃣ Frontend

Open in browser:
frontend/index.html

---

## 🔄 System Flow

Search Flights → Select Flight → Choose Seat → Payment → Booking Confirmed

---

## 📸 Screenshots

### 🖥️ Dashboard

![Dashboard](screenshots/Bgimage.png)

---

## 🎯 Key Highlights

* Full-stack project (Frontend + Backend + Database)
* Real-time seat handling logic
* Advanced filtering & sorting
* Clean and modern UI design
* Modular backend architecture

---

## 👨‍💻 Author

**Harsh Ramrakhiani**

---

## 📌 Future Improvements

* Real authentication system (Login/Register)
* Online payment gateway integration
* Admin dashboard
* Deployment on cloud (AWS / Render)

---

⭐ If you like this project, consider giving it a star!
