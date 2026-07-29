from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pandas as pd
from pydantic import BaseModel
# إنشاء التطبيق
app = FastAPI(title="House Price Prediction API")

# السماح للـ Frontend بالاتصال
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# تحميل الموديل
import os

model_path = os.path.join(os.path.dirname(__file__), "house_price_model.pkl")

model = joblib.load(model_path)

class HouseData(BaseModel):
    location: str
    Status: str
    Transaction: str
    Furnishing: str
    facing: str
    overlooking: str
    Ownership: str

    Floor: float
    Bathroom: float
    Balcony: float
    carpet_area_sqft: float
    Car_Parking: float
@app.get("/")
def home():
    return {"message": "House Price Prediction API is Running"}

@app.post("/predict")
def predict(data: HouseData):

    df = pd.DataFrame([{
        "location": data.location,
        "Status": data.Status,
        "Transaction": data.Transaction,
        "Furnishing": data.Furnishing,
        "facing": data.facing,
        "overlooking": data.overlooking,
        "Ownership": data.Ownership,
        "Floor": data.Floor,
        "Bathroom": data.Bathroom,
        "Balcony": data.Balcony,
        "carpet_area_sqft": data.carpet_area_sqft,
        "Car Parking": data.Car_Parking
    }])

    prediction = model.predict(df)[0]

    return {
        "Predicted Price": float(prediction)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)