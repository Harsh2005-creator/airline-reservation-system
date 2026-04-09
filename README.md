# ✈️ Airline Reservation System (Full-Stack + AI Pricing)

A **full-stack airline ticket booking system** built using **Flask, MySQL, and modern frontend technologies**, enhanced with **Machine Learning–based dynamic pricing**.

This project simulates a **real-world airline booking platform** with:

* Intelligent pricing
* Real-time seat management
* Interactive admin analytics
* Premium UI/UX

---

## 🌟 Key Features

### 🤖 AI-Powered Dynamic Pricing

* **Machine Learning Model**: Uses a *Random Forest Regressor* to predict ticket prices.
* **Demand-Based Pricing**: Prices increase as seat availability decreases.
* **Real-Time Predictions**: Integrated with backend APIs for live pricing updates.

---

### 🛠️ Admin Dashboard

* 📊 **System Overview**: Total flights, bookings, and system status
* ✈️ **Flight Management**: Add/Delete flights with automatic seat generation
* 📈 **AI Analytics**: Chart.js visualization of price vs seat availability
* ⚡ **Live Updates**: Graph refreshes on flight changes

---

### 🔍 Smart Flight Search

* Search by **flight number, source, destination**
* Filter by **route and departure date**
* Sort by **price (Low → High / High → Low)**
* 🟢 **Auto-highlight cheapest flight**

---

### 💺 Booking System

* 🎯 Interactive **seat selection grid**
* 🔒 Prevents **double booking**
* 🧾 Booking preview before confirmation

---

### 💳 Payment & UI

* 💎 Modern **airline-style UI (Blue + Gold theme)**
* 📱 Fully responsive design
* 💰 Simulated payment gateway

---

### 📖 Booking Management

* 📋 View all bookings (active + past)
* 🎫 Digital ticket UI
* ❌ One-click cancellation with seat release

---

## 🧠 Tech Stack

| Layer      | Technology                   |
| ---------- | ---------------------------- |
| Backend    | Flask, Python                |
| Database   | MySQL                        |
| Frontend   | HTML, CSS, JavaScript        |
| Charts     | Chart.js                     |
| ML Model   | Scikit-learn (Random Forest) |
| Data Tools | Pandas, NumPy                |
| Model Save | Joblib                       |

---

## 📂 Project Structure

```
airline-reservation-system/
│
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── db.py
│   ├── train_model.py
│   ├── flight_dataset.csv
│   ├── flight_price_model.pkl
│   ├── routes/
│   └── models/
│
├── frontend/
│   ├── index.html
│   ├── admin.html
│   ├── dashboard.html
│   ├── bookings.html
│   ├── payment.html
│   └── style.css
│
├── screenshots/
│   └── Bgimage.png
```

---

## ⚙️ Setup & Installation

### 1️⃣ Database Setup

```sql
CREATE DATABASE airline_system;
```

Update your credentials in:

```
backend/config.py
```

---

### 2️⃣ Backend & ML Setup

```bash
cd backend

pip install -r requirements.txt

# Train ML Model
python train_model.py

# Start Server
python app.py
```

---

### 3️⃣ Run Frontend

Simply open:

```
frontend/index.html
```

---

## 🔄 System Workflow

```
Search Flights
   ↓
View AI Pricing
   ↓
Select Flight
   ↓
Choose Seat
   ↓
Payment
   ↓
Booking Confirmation
```

---

## 🎯 Highlights

* ✅ Full-stack architecture (Flask + MySQL)
* ✅ Real-world airline pricing simulation
* ✅ ML integration using Scikit-learn
* ✅ Real-time seat tracking system
* ✅ Clean UI with responsive design

---

## 🚀 Future Improvements

* 🔐 JWT-based authentication system
* ☁️ Deployment on Oracle Cloud / AWS
* 💳 Integration with Razorpay / Stripe
* 📊 Advanced analytics dashboard

---

## 👨‍💻 Author

**Harsh Ramrakhiani**

---

## ⭐ Support

If you like this project:

👉 Give it a ⭐ on GitHub
👉 Share it with others

---
