A full-stack airline ticket booking system built using **Flask, MySQL, HTML, CSS, and JavaScript**. This project simulates a real-world airline booking experience with a premium modern UI, real-time seat availability, and advanced backend integration.

---

## 🚀 Features

### 🔍 Flight Search & Filtering
* **Smart Search:** Find flights by flight number, source, or destination.
* **Route Filtering:** Source → Destination dropdown filtering.
* **Date Filtering:** 📅 Browse available flights by specific dates.
* **Price Sorting:** ⬆️ Sort pricing from Low → High or High → Low.
* **Smart Highlighting:** 🟢 Automatically highlights the cheapest available flight.

### 💺 Booking System
* **Real-time Seat Matrix:** Interactive, visual seat selection grid.
* **Conflict Prevention:** Logic to prevent double booking of the same seat.
* **Ticket Preview:** Review all details before final confirmation.

### 💳 Payment & UI
* **Premium Interface:** Fully responsive UI featuring a sleek deep blue and gold airline theme.
* **Payment Simulation:** Realistic checkout flow and fake payment interface.
* **Smooth Flow:** Booking is only confirmed after successful payment simulation.

### 📖 Booking Management
* **User Dashboard:** View all active and past bookings.
* **Digital Tickets:** 🎫 Beautiful ticket-style booking display.
* **Cancellations:** ❌ One-click cancel booking functionality with automatic seat release back to the available pool.

---

## 🛠️ Tech Stack

| Layer    | Technology              |
| -------- | ----------------------- |
| Backend  | Python (Flask)          |
| Database | MySQL                   |
| Frontend | HTML, CSS, JavaScript   |
| API      | RESTful APIs            |

---

## 📂 Project Structure

```text
airline-reservation-system/
│
├── backend/               # Flask backend
│   ├── app.py
│   ├── db.py
│   ├── routes/
│   └── models/
│
├── frontend/              # UI
│   ├── index.html
│   ├── dashboard.html
│   ├── bookings.html
│   ├── payment.html
│   └── style.css
│
├── screenshots/           # Images
│   └── Bgimage.png
▶️ How to Run the Project
1️⃣ Backend Setup
Navigate to the backend directory, install the required Python packages, and start the Flask server:

Bash
cd backend
pip install -r requirements.txt
python app.py
2️⃣ Database Setup
Log into your MySQL instance and create the required database (ensure your db.py file is updated with your local MySQL credentials):

SQL
CREATE DATABASE airline_system;
3️⃣ Frontend
Since the frontend uses standard web technologies, simply open the main file in your preferred web browser:

Plaintext
frontend/index.html
🔄 System Flow
Search Flights ➔ Select Flight ➔ Choose Seat ➔ Payment ➔ Booking Confirmed

📸 Screenshots
🖥️ Dashboard
(Note: Add more screenshots of your new UI here as you take them!)

🎯 Key Highlights
Full-Stack Architecture: Clean separation of Frontend, Backend, and Database.

Real-Time Logic: Robust handling of seat availability and concurrent booking attempts.

Modern Design: Responsive, accessible, and visually striking user interface.

📌 Future Improvements
Integrate a real authentication system (Login/Register).

Add a dedicated Admin dashboard to manage flights and users.

Integrate AI concepts to provide smart flight recommendations or dynamic price predictions.

Deploy the application and database to Oracle Cloud Infrastructure (OCI).

Connect a live payment gateway (e.g., Stripe or PayPal).

👨‍💻 Author
Harsh Ramrakhiani

⭐ If you like this project, consider giving it a star on GitHub!
