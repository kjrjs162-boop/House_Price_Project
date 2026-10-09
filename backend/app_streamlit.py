import os

import joblib
import numpy as np
import pandas as pd
import streamlit as st


# =========================================================
# PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# MODEL LOADING
# The model file is located beside this app file:
# House_Price_Project/backend/house_price_model.pkl
# =========================================================
@st.cache_resource
def load_model():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(current_dir, "house_price_model.pkl")

    if not os.path.isfile(model_path):
        raise FileNotFoundError(
            "Model file was not found. Expected location: " + model_path
        )

    return joblib.load(model_path)


# =========================================================
# TRANSLATIONS
# =========================================================
TRANSLATIONS = {
    "English": {
        "page_title": "House Price Prediction",
        "subtitle": "Estimate a property's price using a trained machine learning model.",
        "language": "Language",
        "sidebar_title": "Property Details",
        "sidebar_text": "Enter the property information below.",
        "location": "Location",
        "location_help": "Enter the location exactly as represented in your dataset.",
        "status": "Property Status",
        "transaction": "Transaction Type",
        "furnishing": "Furnishing",
        "facing": "Facing",
        "overlooking": "Overlooking",
        "ownership": "Ownership",
        "floor": "Floor",
        "bathroom": "Bathrooms",
        "balcony": "Balconies",
        "area": "Carpet Area (sq ft)",
        "parking": "Car Parking",
        "predict": "Predict Property Price",
        "welcome": "Welcome to House Price Prediction",
        "welcome_text": "Fill in the property details and let the trained model estimate its price.",
        "result": "Estimated Property Price",
        "success": "Prediction completed successfully.",
        "model_error": "The model could not generate a prediction.",
        "error_details": "Error details",
        "missing_model": "The model file is missing. Make sure backend/house_price_model.pkl exists in the deployed project.",
        "invalid_prediction": "The model returned an invalid price. Please check the model and input data.",
        "input_summary": "Submitted Property Details",
        "model_status": "Model Status",
        "loaded": "Model loaded",
        "not_loaded": "Model not loaded",
        "note": "This is a machine learning estimate, not a guaranteed market price.",
        "floor_help": "Enter the floor number. Use 0 for the ground floor if that matches your dataset.",
        "area_help": "Enter the property's carpet area in square feet.",
        "ready": "Ready to Move",
        "construction": "Under Construction",
        "new": "New Property",
        "resale": "Resale",
        "furnished": "Furnished",
        "semi_furnished": "Semi-Furnished",
        "unfurnished": "Unfurnished",
        "freehold": "Freehold",
        "leasehold": "Leasehold",
        "power_of_attorney": "Power of Attorney",
        "cooperative": "Co-operative Society",
        "north": "North",
        "south": "South",
        "east": "East",
        "west": "West",
        "north_east": "North-East",
        "north_west": "North-West",
        "south_east": "South-East",
        "south_west": "South-West",
        "road": "Road",
        "garden": "Garden",
        "main_road": "Main Road",
        "pool": "Pool",
        "park": "Park",
        "street": "Street",
        "other": "Other",
        "none": "None",
        "footer": "House Price Prediction | Machine Learning Project",
        "currency_note": "The currency and price scale depend on the target used to train your model.",
        "enter_location": "Please enter a location.",
    },
    "العربية": {
        "page_title": "توقع أسعار العقارات",
        "subtitle": "تقدير سعر العقار باستخدام نموذج تعلم آلي مدرّب.",
        "language": "اللغة",
        "sidebar_title": "بيانات العقار",
        "sidebar_text": "أدخل بيانات العقار في الحقول التالية.",
        "location": "الموقع",
        "location_help": "اكتب الموقع بنفس الطريقة المستخدمة في بيانات التدريب.",
        "status": "حالة العقار",
        "transaction": "نوع المعاملة",
        "furnishing": "حالة الفرش",
        "facing": "الاتجاه",
        "overlooking": "الإطلالة",
        "ownership": "نوع الملكية",
        "floor": "الطابق",
        "bathroom": "عدد الحمامات",
        "balcony": "عدد الشرفات",
        "area": "المساحة الصافية (قدم مربع)",
        "parking": "أماكن انتظار السيارات",
        "predict": "توقع سعر العقار",
        "welcome": "مرحبًا بك في تطبيق توقع أسعار العقارات",
        "welcome_text": "أدخل بيانات العقار ليقوم النموذج المدرّب بتقدير سعره.",
        "result": "السعر التقديري للعقار",
        "success": "تم تنفيذ التوقع بنجاح.",
        "model_error": "تعذر على النموذج حساب السعر.",
        "error_details": "تفاصيل الخطأ",
        "missing_model": "ملف المودل غير موجود. تأكد من وجود backend/house_price_model.pkl في المشروع المنشور.",
        "invalid_prediction": "النموذج أعاد سعرًا غير صالح. راجع المودل والبيانات المدخلة.",
        "input_summary": "بيانات العقار المدخلة",
        "model_status": "حالة المودل",
        "loaded": "تم تحميل المودل",
        "not_loaded": "لم يتم تحميل المودل",
        "note": "هذا السعر تقدير ناتج عن التعلم الآلي وليس سعرًا سوقيًا مضمونًا.",
        "floor_help": "أدخل رقم الطابق. استخدم 0 للطابق الأرضي إذا كان ذلك متوافقًا مع بيانات التدريب.",
        "area_help": "أدخل المساحة الصافية للعقار بالقدم المربع.",
        "ready": "جاهز للسكن",
        "construction": "تحت الإنشاء",
        "new": "عقار جديد",
        "resale": "إعادة بيع",
        "furnished": "مفروش",
        "semi_furnished": "نصف مفروش",
        "unfurnished": "غير مفروش",
        "freehold": "ملكية حرة",
        "leasehold": "ملكية إيجارية",
        "power_of_attorney": "توكيل رسمي",
        "cooperative": "جمعية تعاونية",
        "north": "شمال",
        "south": "جنوب",
        "east": "شرق",
        "west": "غرب",
        "north_east": "شمال شرق",
        "north_west": "شمال غرب",
        "south_east": "جنوب شرق",
        "south_west": "جنوب غرب",
        "road": "طريق",
        "garden": "حديقة",
        "main_road": "طريق رئيسي",
        "pool": "حمام سباحة",
        "park": "منتزه",
        "street": "شارع",
        "other": "أخرى",
        "none": "لا يوجد",
        "footer": "توقع أسعار العقارات | مشروع تعلم آلي",
        "currency_note": "العملة ومقياس السعر يعتمدان على المتغير المستهدف الذي دُرّب عليه المودل.",
        "enter_location": "من فضلك أدخل الموقع.",
    },
}


# =========================================================
# CUSTOM STYLING
# =========================================================
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #f5f7fb 0%, #eaf0fa 100%);
    }
    .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .hero {
        background: linear-gradient(120deg, #123a63, #2563a6);
        color: white;
        padding: 2rem;
        border-radius: 18px;
        margin-bottom: 1.5rem;
        box-shadow: 0 8px 24px rgba(18, 58, 99, 0.16);
    }
    .hero h1 {
        color: white;
        margin-bottom: 0.5rem;
        font-size: 2.1rem;
    }
    .hero p {
        color: #e5efff;
        margin-bottom: 0;
        font-size: 1rem;
    }
    .result-card {
        background: white;
        padding: 1.6rem;
        border-radius: 16px;
        border-left: 6px solid #2563a6;
        box-shadow: 0 5px 18px rgba(18, 58, 99, 0.10);
        margin-top: 1rem;
    }
    .result-label {
        color: #52657a;
        font-size: 1rem;
        margin-bottom: 0.5rem;
    }
    .result-value {
        color: #123a63;
        font-size: 2rem;
        font-weight: 800;
        overflow-wrap: anywhere;
    }
    .section-title {
        color: #123a63;
        font-size: 1.2rem;
        font-weight: 700;
        margin-top: 0.5rem;
        margin-bottom: 0.8rem;
    }
    div[data-testid="stForm"] {
        background: rgba(255, 255, 255, 0.88);
        border: 1px solid #dce5f1;
        padding: 1.2rem;
        border-radius: 16px;
    }
    div.stButton > button,
    div[data-testid="stFormSubmitButton"] > button {
        background: linear-gradient(120deg, #123a63, #2563a6);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.65rem 1rem;
        font-weight: 700;
        min-height: 3rem;
    }
    div.stButton > button:hover,
    div[data-testid="stFormSubmitButton"] > button:hover {
        color: white;
        border: 1px solid #123a63;
        filter: brightness(1.08);
    }
    [data-testid="stSidebar"] {
        background: #edf3fb;
    }
    .footer {
        text-align: center;
        color: #64748b;
        padding-top: 2rem;
        font-size: 0.85rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# LANGUAGE SELECTION
# =========================================================
language = st.sidebar.selectbox(
    "Language / اللغة",
    ["English", "العربية"],
    index=0,
)
t = TRANSLATIONS[language]

if language == "العربية":
    st.markdown(
        """
        <style>
        .block-container {
            direction: rtl;
            text-align: right;
        }
        [data-testid="stSidebar"] {
            direction: rtl;
            text-align: right;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# HEADER
# =========================================================
st.markdown(
    f"""
    <div class="hero">
        <h1>🏠 {t['page_title']}</h1>
        <p>{t['subtitle']}</p>
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown(f"### {t['welcome']}")
st.write(t["welcome_text"])


# =========================================================
# LOAD MODEL AND SHOW STATUS
# =========================================================
st.sidebar.title(f"🏡 {t['sidebar_title']}")
st.sidebar.write(t["sidebar_text"])

model = None
model_error_message = None
try:
    model = load_model()
    model_loaded = True
except Exception as error:
    model_loaded = False
    model_error_message = str(error)

if model_loaded:
    st.sidebar.success(f"✅ {t['model_status']}: {t['loaded']}")
else:
    st.sidebar.error(f"⚠️ {t['model_status']}: {t['not_loaded']}")
    with st.sidebar.expander(t["error_details"]):
        st.code(model_error_message or "Unknown model-loading error")


# =========================================================
# INPUT FORM
# Keep feature names aligned with the model's training schema.
# =========================================================
with st.form("house_prediction_form"):
    st.markdown(
        f"<div class='section-title'>{t['sidebar_title']}</div>",
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        location = st.text_input(
            t["location"],
            value="",
            help=t["location_help"],
            placeholder="Enter location",
        )

        status = st.selectbox(
            t["status"],
            options=["Ready to Move", "Under Construction"],
            format_func=lambda value: (
                t["ready"] if value == "Ready to Move" else t["construction"]
            ),
        )

        transaction = st.selectbox(
            t["transaction"],
            options=["New Property", "Resale"],
            format_func=lambda value: (
                t["new"] if value == "New Property" else t["resale"]
            ),
        )

        furnishing = st.selectbox(
            t["furnishing"],
            options=["Furnished", "Semi-Furnished", "Unfurnished"],
            format_func=lambda value: {
                "Furnished": t["furnished"],
                "Semi-Furnished": t["semi_furnished"],
                "Unfurnished": t["unfurnished"],
            }[value],
        )

        facing = st.selectbox(
            t["facing"],
            options=[
                "North",
                "South",
                "East",
                "West",
                "North-East",
                "North-West",
                "South-East",
                "South-West",
            ],
            format_func=lambda value: {
                "North": t["north"],
                "South": t["south"],
                "East": t["east"],
                "West": t["west"],
                "North-East": t["north_east"],
                "North-West": t["north_west"],
                "South-East": t["south_east"],
                "South-West": t["south_west"],
            }[value],
        )

        overlooking = st.selectbox(
            t["overlooking"],
            options=[
                "Road",
                "Garden",
                "Main Road",
                "Pool",
                "Park",
                "Street",
                "Other",
                "None",
            ],
            format_func=lambda value: {
                "Road": t["road"],
                "Garden": t["garden"],
                "Main Road": t["main_road"],
                "Pool": t["pool"],
                "Park": t["park"],
                "Street": t["street"],
                "Other": t["other"],
                "None": t["none"],
            }[value],
        )

    with col2:
        ownership = st.selectbox(
            t["ownership"],
            options=[
                "Freehold",
                "Leasehold",
                "Power of Attorney",
                "Co-operative Society",
            ],
            format_func=lambda value: {
                "Freehold": t["freehold"],
                "Leasehold": t["leasehold"],
                "Power of Attorney": t["power_of_attorney"],
                "Co-operative Society": t["cooperative"],
            }[value],
        )

        floor = st.number_input(
            t["floor"],
            min_value=0.0,
            max_value=200.0,
            value=0.0,
            step=1.0,
            help=t["floor_help"],
        )

        bathroom = st.number_input(
            t["bathroom"],
            min_value=0.0,
            max_value=50.0,
            value=1.0,
            step=1.0,
        )

        balcony = st.number_input(
            t["balcony"],
            min_value=0.0,
            max_value=20.0,
            value=0.0,
            step=1.0,
        )

        carpet_area = st.number_input(
            t["area"],
            min_value=1.0,
            max_value=1000000.0,
            value=1000.0,
            step=50.0,
            help=t["area_help"],
        )

        car_parking = st.number_input(
            t["parking"],
            min_value=0.0,
            max_value=100.0,
            value=0.0,
            step=1.0,
        )

    submitted = st.form_submit_button(
        f"🏠 {t['predict']}",
        use_container_width=True,
    )


# =========================================================
# PREDICTION
# =========================================================
if submitted:
    if not location.strip():
        st.warning(t["enter_location"])
        st.stop()

    if not model_loaded:
        st.error(t["model_error"])
        st.info(t["missing_model"])
        if model_error_message:
            with st.expander(t["error_details"]):
                st.exception(FileNotFoundError(model_error_message))
        st.stop()

    # The feature names must match the columns used during model training.
    input_data = pd.DataFrame(
        [
            {
                "location": location.strip(),
                "Status": status,
                "Transaction": transaction,
                "Furnishing": furnishing,
                "facing": facing,
                "overlooking": overlooking,
                "Ownership": ownership,
                "Floor": float(floor),
                "Bathroom": float(bathroom),
                "Balcony": float(balcony),
                "carpet_area_sqft": float(carpet_area),
                "Car Parking": float(car_parking),
            }
        ]
    )

    try:
        prediction_array = model.predict(input_data)
        prediction = float(np.asarray(prediction_array).reshape(-1)[0])

        if not np.isfinite(prediction):
            st.error(t["invalid_prediction"])
            st.stop()

        st.success(t["success"])
        st.markdown(
            f"""
            <div class="result-card">
                <div class="result-label">{t['result']}</div>
                <div class="result-value">{prediction:,.2f}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.caption(t["currency_note"])
        st.info(t["note"])

        with st.expander(t["input_summary"]):
            st.dataframe(input_data, use_container_width=True)

    except Exception as error:
        st.error(t["model_error"])
        st.caption(t["error_details"])
        st.exception(error)


# =========================================================
# FOOTER
# =========================================================
st.markdown(
    f"""
    <div class="footer">
        {t['footer']}
    </div>
    """,
    unsafe_allow_html=True,
)
