import pandas as pd
import random
from sklearn.linear_model import LinearRegression
import joblib

# 1. Create fake historical data (Supply & Demand)
# Features: total_seats, available_seats
# Target: price
data = []
for _ in range(500):
    total = random.randint(50, 200)
    available = random.randint(0, total)
    
    # Base price is 2000. Price goes up as available seats go down (scarcity)
    scarcity_multiplier = 1 + ((total - available) / total) 
    price = int(2000 * scarcity_multiplier + random.randint(-200, 200))
    
    data.append([total, available, price])

df = pd.DataFrame(data, columns=['total_seats', 'available_seats', 'price'])

# 2. Train the Model
X = df[['total_seats', 'available_seats']]
y = df['price']

model = LinearRegression()
model.fit(X, y)

# 3. Save the model to a file
joblib.dump(model, 'flight_price_model.pkl')
print("Model trained and saved as 'flight_price_model.pkl'")