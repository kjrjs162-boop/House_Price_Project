import streamlit as st
import pandas as pd
import numpy as np
import joblib

# إعدادات الصفحة
st.set_page_config(page_title="House Price Prediction", page_icon="🏠", layout="wide")

@st.cache_resource
def load_model():
    # تأكد من مسار حفظ المودل الخاص بك (أو قم بتحميل Pipeline التدريب)
    # model = joblib.load("model.pkl")
    return None

def main():
    st.title("🏠 House Price Prediction App")
    st.write("أدخل تفاصيل العقار التابعة للمشروع للتنبؤ بالسعر المتوقع بالروبية الهندية.")

    # مدخلات المستخدم بناءً على الأعمدة المستخدمة في التنظيف
    col1, col2, col3 = st.columns(3)

    with col1:
        location = st.selectbox("Location", [
            "thane", "mumbai", "pune", "bangalore", "hyderabad", "chennai", "kolkata", "delhi"
        ]) # يمكنك تعديلها أو جعلها قائمة Locations الخاصة بك
        status = st.selectbox("Status", ["Ready to Move", "Under Construction"])
        transaction = st.selectbox("Transaction", ["Resale", "New Property"])
        furnishing = st.selectbox("Furnishing", ["Unfurnished", "Semi-Furnished", "Furnished"])

    with col2:
        facing = st.selectbox("Facing", ["East", "West", "North", "South", "North-East", "North-West", "South-East", "South-West"])
        overlooking = st.selectbox("Overlooking", ["Garden/Park", "Main Road", "Pool", "Club", "Other"])
        ownership = st.selectbox("Ownership", ["Freehold", "Leasehold", "Co-operative Society", "Power of Attorney"])
        bathroom = st.number_input("Bathrooms", min_value=1, max_value=10, value=2)

    with col3:
        balcony = st.number_input("Balconies", min_value=0, max_value=5, value=1)
        floor = st.number_input("Floor", min_value=0, max_value=100, value=2)
        carpet_area = st.number_input("Carpet Area (sqft)", min_value=100.0, max_value=10000.0, value=600.0)

    if st.button("توقع السعر (Predict Price)", type="primary"):
        # هنا يتم تجهيز البيانات بنفس شكل الداتا فريم المدربة
        input_data = pd.DataFrame({
            'location': [location],
            'Status': [status],
            'Floor': [floor],
            'Transaction': [transaction],
            'Furnishing': [furnishing],
            'facing': [facing],
            'overlooking': [overlooking],
            'Bathroom': [bathroom],
            'Balcony': [balcony],
            'Car Parking': [np.nan], # إذا كان عمود Car Parking موجوداً في التدريب
            'Ownership': [ownership],
            'carpet_area_sqft': [carpet_area]
        })

        # محاكاة التنبؤ (استبدل السطر التالي بكود المودل الفعلي الخاص بك)
        # prediction = model.predict(input_data)[0]
        
        # مثال تجريبي:
        prediction = carpet_area * 12000 + (bathroom * 500000)
        
        st.success(f"💰 السعر المتوقع للعقار هو تقريباً: {prediction:,.2f} روبية")

if __name__ == '__main__':
    main()