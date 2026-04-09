import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# 1. Load the REAL dataset from your CSV
print("1. Loading dataset...")
df = pd.read_csv('flight_dataset.csv')

# 2. Separate Features (X) and Target (y)
X = df[['total_seats', 'available_seats']]
y = df['price']

# 3. Train the Model
print("2. Training the Advanced Machine Learning model...")
# RandomForest is perfect for your data because it understands sudden price jumps!
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# 4. Save the smart model
joblib.dump(model, 'flight_price_model.pkl')
print("3. ✅ Model trained successfully and saved as 'flight_price_model.pkl'")