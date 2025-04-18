# import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import LabelEncoder, StandardScaler
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import classification_report, accuracy_score
# from db import engine
# from fastapi import APIRouter

# ml = APIRouter()

# df = pd.read_sql("SELECT * FROM energy_usage", con=engine) 

# label_encoder = LabelEncoder()
# df['appliance_encoded'] = label_encoder.fit_transform(df['appliance'])
# df['room_encoded'] = label_encoder.fit_transform(df['room'])
# df['day_encoded'] = label_encoder.fit_transform(df['day'])

# X = df[['appliance_encoded', 'room_encoded', 'day_encoded', 'duration_hrs', 'power_usage_kWh', 'outside_temperature']]
# y = df['label']

# y = label_encoder.fit_transform(y)

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# scaler = StandardScaler()
# X_train = scaler.fit_transform(X_train)
# X_test = scaler.transform(X_test)

# model = RandomForestClassifier(n_estimators=100, random_state=42)
# model.fit(X_train, y_train)

# # Predict on the test data
# y_pred = model.predict(X_test)

# print("Accuracy:", accuracy_score(y_test, y_pred))
# print(classification_report(y_test, y_pred))




# @router.post("/predict-wastage")
# def predict_wastage(data: EnergyUsageInput):
#     # Convert input data into a format for the model
#     appliance_encoded = label_encoder.transform([data.appliance])[0]
#     room_encoded = label_encoder.transform([data.room])[0]
#     day_encoded = label_encoder.transform([data.day])[0]
    
#     # Prepare features for prediction
#     features = np.array([[appliance_encoded, room_encoded, day_encoded, 
#                           data.duration_hrs, data.power_usage_kWh, data.outside_temperature]])
    
#     # Scale the input features
#     features_scaled = scaler.transform(features)
    
#     # Predict the label using the trained model
#     prediction = model.predict(features_scaled)
    
#     # Decode the predicted label
#     label = label_encoder.inverse_transform(prediction)[0]
    
#     return {"predicted_label": label}