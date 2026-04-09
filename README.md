✈️ Full-Stack Airline Reservation SystemA full-stack airline ticket booking system built using Flask, MySQL, HTML, CSS, and JavaScript. This project simulates a real-world airline booking experience with a premium modern UI, real-time seat availability, AI-powered dynamic pricing, and an administrative dashboard.🚀 Features🤖 AI-Powered Dynamic PricingMachine Learning Integration: Utilizes a Random Forest regression model to adjust flight prices dynamically.Supply & Demand Logic: Ticket prices automatically scale based on the total capacity and real-time available seats.🛠️ Admin DashboardSystem Overview: View total flights, active bookings, and system status at a glance.Manage Inventory: Add new flights (which auto-generates seat maps) and delete existing flights.Data Visualization: Interactive Chart.js graphs mapping out the AI's predicted price curve as seats fill up.🔍 Flight Search & FilteringSmart Search: Find flights by flight number, source, or destination.Route & Date Filtering: Dropdown filtering for Source → Destination and specific departure dates.Price Sorting: Sort pricing from Low → High or High → Low.Smart Highlighting: Automatically highlights the cheapest available flight.💺 Booking SystemReal-time Seat Matrix: Interactive, visual seat selection grid.Conflict Prevention: Backend logic to prevent double booking of the same seat.Ticket Preview: Review all details before final confirmation.💳 Payment & UIPremium Interface: Fully responsive UI featuring a sleek deep blue and gold airline theme.Payment Simulation: Realistic checkout flow and simulated payment interface.📖 Booking ManagementUser Dashboard: View all active and past bookings.Digital Tickets: Beautiful ticket-style booking display.Cancellations: One-click cancel booking functionality with automatic seat release back to the available pool.🛠️ Tech StackLayerTechnologyBackendPython (Flask, Pandas, Scikit-Learn)DatabaseMySQLFrontendHTML, CSS, JavaScript, Chart.jsMachine LearningRandom Forest Regressor (joblib for model saving)APIRESTful APIs📂 Project StructurePlaintextairline-reservation-system/
│
├── backend/               # Flask backend & ML logic
│   ├── app.py
│   ├── config.py
│   ├── db.py
│   ├── train_model.py     # ML training script
│   ├── flight_dataset.csv # Training data
│   ├── flight_price_model.pkl # Compiled ML model
│   ├── routes/            # API Endpoints (admin, auth, booking)
│   └── models/            # Data models (user, flight, booking)
│
├── frontend/              # UI
│   ├── index.html
│   ├── admin.html         # Admin dashboard & Analytics
│   ├── dashboard.html
│   ├── bookings.html
│   ├── payment.html
│   └── style.css
│
├── screenshots/           # Images
│   └── Bgimage.png
▶️ How to Run the Project1️⃣ Database SetupLog into your MySQL instance and create the required database. (Ensure your backend/config.py file is updated with your local MySQL credentials):SQLCREATE DATABASE airline_system;
2️⃣ Backend & Machine Learning SetupNavigate to the backend directory, install the required Python packages, train the ML model, and start the Flask server:Bashcd backend
pip install -r requirements.txt

# Train the dynamic pricing model first
python train_model.py

# Start the Flask server
python app.py
3️⃣ FrontendSince the frontend uses standard web technologies, simply open the main file in your preferred web browser:Plaintextfrontend/index.html
(To access the Admin panel, click 'Admin' and use the admin credentials defined in the codebase).🔄 System FlowSearch Flights ➔ Check AI Pricing ➔ Select Flight ➔ Choose Seat ➔ Payment ➔ Booking Confirmed🎯 Key HighlightsFull-Stack Architecture: Clean separation of Frontend, Backend, and Database using Flask Blueprints.Intelligent Pricing: Real-world simulation of airline pricing models using Scikit-Learn.Real-Time Logic: Robust handling of seat availability and concurrent booking attempts.Modern Design: Responsive, accessible, and visually striking user interface.📌 Future ImprovementsIntegrate a complete authentication system with JWTs for seamless Login/Register.Deploy the application and database to Oracle Cloud Infrastructure (OCI).Connect a live payment gateway (e.g., Stripe or Razorpay).👨‍💻 AuthorHarsh Ramrakhiani⭐ If you like this project, consider giving it a star on GitHub!
