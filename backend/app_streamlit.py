
import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(
    page_title="EstateIQ | House Price Prediction",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="expanded",
)

TRANSLATIONS = {
    "English": {
        "subtitle": "AI-powered property valuation",
        "navigation": "NAVIGATION",
        "dashboard": "Dashboard",
        "prediction": "Price Prediction",
        "about": "About",
        "language": "Language",
        "welcome": "Find the value of your next property.",
        "description": "Explore property details and estimate its market value.",
        "form_title": "Property Details",
        "location": "Location",
        "status": "Property Status",
        "transaction": "Transaction Type",
        "furnishing": "Furnishing",
        "facing": "Facing Direction",
        "overlooking": "View",
        "ownership": "Ownership",
        "bathroom": "Bathrooms",
        "balcony": "Balconies",
        "floor": "Floor Number",
        "area": "Carpet Area (sqft)",
        "parking": "Car Parking Spaces",
        "predict": "Estimate Property Price",
        "result": "Estimated Property Value",
        "area_metric": "Carpet Area",
        "bathroom_metric": "Bathrooms",
        "location_metric": "Selected Location",
        "note": "Demo estimate only. Connect your trained model for real predictions.",
        "ready": "Ready to Move",
        "construction": "Under Construction",
        "resale": "Resale",
        "new": "New Property",
        "unfurnished": "Unfurnished",
        "semi": "Semi-Furnished",
        "furnished": "Furnished",
        "garden": "Garden / Park",
        "road": "Main Road",
        "pool": "Pool",
        "club": "Club",
        "other": "Other",
        "freehold": "Freehold",
        "leasehold": "Leasehold",
        "society": "Co-operative Society",
        "attorney": "Power of Attorney",
        "result_caption": "Estimated price in Indian Rupees (INR)",
        "about_title": "About EstateIQ",
        "about_text": "A property valuation interface designed to explore housing attributes and estimate property prices.",
        "tip": "Complete the property details and select Estimate Property Price to view the result.",
    },
    "العربية": {
        "subtitle": "تقدير قيمة العقارات بالذكاء الاصطناعي",
        "navigation": "التنقل",
        "dashboard": "لوحة التحكم",
        "prediction": "توقع السعر",
        "about": "حول التطبيق",
        "language": "اللغة",
        "welcome": "اكتشف القيمة التقديرية لعقارك.",
        "description": "أدخل تفاصيل العقار للحصول على تقدير مبدئي لسعره.",
        "form_title": "تفاصيل العقار",
        "location": "الموقع",
        "status": "حالة العقار",
        "transaction": "نوع المعاملة",
        "furnishing": "التأثيث",
        "facing": "الاتجاه",
        "overlooking": "الإطلالة",
        "ownership": "الملكية",
        "bathroom": "عدد الحمامات",
        "balcony": "عدد الشرفات",
        "floor": "رقم الطابق",
        "area": "المساحة (قدم مربع)",
        "parking": "أماكن انتظار السيارات",
        "predict": "تقدير سعر العقار",
        "result": "القيمة التقديرية للعقار",
        "area_metric": "المساحة",
        "bathroom_metric": "الحمامات",
        "location_metric": "الموقع المحدد",
        "note": "هذا تقدير تجريبي فقط. اربط النموذج المدرّب للحصول على تنبؤات فعلية.",
        "ready": "جاهز للسكن",
        "construction": "تحت الإنشاء",
        "resale": "إعادة بيع",
        "new": "عقار جديد",
        "unfurnished": "غير مفروش",
        "semi": "نصف مفروش",
        "furnished": "مفروش",
        "garden": "حديقة",
        "road": "طريق رئيسي",
        "pool": "حمام سباحة",
        "club": "نادي",
        "other": "أخرى",
        "freehold": "ملكية حرة",
        "leasehold": "إيجار طويل الأجل",
        "society": "جمعية تعاونية",
        "attorney": "توكيل رسمي",
        "result_caption": "السعر التقديري بالروبية الهندية",
        "about_title": "حول EstateIQ",
        "about_text": "واجهة لتقييم العقارات واستكشاف خصائصها وتقدير أسعارها.",
        "tip": "أكمل بيانات العقار ثم اضغط على تقدير سعر العقار لعرض النتيجة.",
    },
}

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #f5f7ff 0%, #eef8ff 55%, #f7f3ff 100%);
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #111c3d 0%, #192b52 65%, #263f70 100%);
}

[data-testid="stSidebar"] * {
    color: #f5f8ff;
}

.hero {
    background: linear-gradient(120deg, #172554 0%, #3157b7 55%, #7c3aed 100%);
    padding: 35px;
    border-radius: 24px;
    color: white;
    margin-bottom: 24px;
    box-shadow: 0 14px 35px rgba(49, 87, 183, 0.20);
}

.hero h1 {
    color: white;
    font-size: 35px;
    font-weight: 800;
    margin-bottom: 10px;
}

.hero p {
    color: #e2eaff;
    font-size: 15px;
    margin-bottom: 0;
}

.eyebrow {
    color: #a5f3fc;
    text-transform: uppercase;
    letter-spacing: 2px;
    font-size: 11px;
    font-weight: 700;
}

.section-card {
    background: rgba(255,255,255,0.92);
    border: 1px solid #e3e8f5;
    padding: 22px;
    border-radius: 20px;
    box-shadow: 0 8px 25px rgba(26, 42, 80, 0.05);
    margin-bottom: 18px;
}

.section-title {
    color: #18264b;
    font-size: 20px;
    font-weight: 800;
    margin-bottom: 6px;
}

.section-caption {
    color: #74809b;
    font-size: 13px;
    margin-bottom: 18px;
}

.metric-card {
    background: white;
    border: 1px solid #e3e8f5;
    border-radius: 18px;
    padding: 20px;
    min-height: 112px;
    box-shadow: 0 8px 22px rgba(26, 42, 80, 0.05);
}

.metric-label {
    color: #78849f;
    font-size: 12px;
    font-weight: 600;
    margin-bottom: 10px;
}

.metric-value {
    color: #172554;
    font-size: 23px;
    font-weight: 800;
    overflow-wrap: anywhere;
}

.price-card {
    background: linear-gradient(115deg, #0f766e 0%, #0d9488 55%, #22c5a5 100%);
    color: white;
    border-radius: 22px;
    padding: 28px;
    margin-top: 20px;
    box-shadow: 0 12px 30px rgba(13, 148, 136, 0.22);
}

.price-card h2 {
    color: white;
    font-size: 14px;
    font-weight: 600;
}

.price-card .price {
    color: white;
    font-size: 36px;
    font-weight: 800;
    overflow-wrap: anywhere;
}

.price-card p {
    color: #d1fae5;
    font-size: 12px;
}

.stButton > button {
    background: linear-gradient(90deg, #3157b7, #7c3aed);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 12px 20px;
    font-weight: 700;
    min-height: 48px;
    transition: 0.2s ease;
}

.stButton > button:hover {
    color: white;
    border: none;
    filter: brightness(1.08);
    box-shadow: 0 8px 20px rgba(75, 85, 200, 0.25);
}

div[data-baseweb="select"] > div,
div[data-baseweb="input"] > div {
    border-radius: 10px;
    border-color: #dce3f2;
}

div[data-testid="stForm"] {
    background: white;
    border: 1px solid #e3e8f5;
    border-radius: 18px;
    padding: 22px;
}

.footer {
    text-align: center;
    color: #8490a8;
    font-size: 12px;
    padding: 24px 0 10px;
}

@media (max-width: 768px) {
    .hero { padding: 24px; }
    .hero h1 { font-size: 27px; }
    .price-card .price { font-size: 28px; }
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## 🏡 EstateIQ")
    st.caption("PROPERTY INTELLIGENCE")
    st.divider()

    language = st.selectbox(
        "Language / اللغة",
        ["English", "العربية"],
        index=0,
        key="language",
    )
    t = TRANSLATIONS[language]

    page = st.radio(
        t["navigation"],
        [t["dashboard"], t["prediction"], t["about"]],
        index=0,
    )

    st.divider()
    st.caption("HOUSE PRICE PREDICTION")
    st.caption("Version 1.0")

rtl = language == "العربية"
direction = "rtl" if rtl else "ltr"

st.markdown(
    f'<div dir="{direction}" class="hero">'
    f'<div class="eyebrow">ESTATEIQ • PROPERTY ANALYTICS</div>'
    f'<h1>🏡 {t["welcome"]}</h1>'
    f'<p>{t["description"]}</p>'
    f'</div>',
    unsafe_allow_html=True,
)

if page == t["about"]:
    st.markdown(
        f'<div dir="{direction}" class="section-card">'
        f'<div class="section-title">{t["about_title"]}</div>'
        f'<p>{t["about_text"]}</p>'
        f'</div>',
        unsafe_allow_html=True,
    )
    st.stop()

locations = [
    "thane", "mumbai", "pune", "bangalore",
    "hyderabad", "chennai", "kolkata", "delhi"
]

with st.form("property_form"):
    st.markdown(
        f'<div dir="{direction}" class="section-title">'
        f'🏠 {t["form_title"]}</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<div dir="{direction}" class="section-caption">{t["tip"]}</div>',
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        location = st.selectbox(t["location"], locations)
        status_label = st.selectbox(
            t["status"], [t["ready"], t["construction"]]
        )
        transaction_label = st.selectbox(
            t["transaction"], [t["resale"], t["new"]]
        )
        furnishing_label = st.selectbox(
            t["furnishing"], [t["unfurnished"], t["semi"], t["furnished"]]
        )

    with col2:
        facing = st.selectbox(
            t["facing"],
            ["East", "West", "North", "South",
             "North-East", "North-West", "South-East", "South-West"],
        )
        overlooking_label = st.selectbox(
            t["overlooking"],
            [t["garden"], t["road"], t["pool"], t["club"], t["other"]],
        )
        ownership_label = st.selectbox(
            t["ownership"],
            [t["freehold"], t["leasehold"], t["society"], t["attorney"]],
        )
        bathroom = st.number_input(
            t["bathroom"], min_value=1, max_value=10, value=2
        )

    with col3:
        balcony = st.number_input(
            t["balcony"], min_value=0, max_value=5, value=1
        )
        floor = st.number_input(
            t["floor"], min_value=0, max_value=100, value=2
        )
        carpet_area = st.number_input(
            t["area"], min_value=100.0, max_value=10000.0, value=600.0
        )
        parking = st.number_input(
            t["parking"], min_value=0, max_value=10, value=1
        )

    submitted = st.form_submit_button(
        f"✨ {t['predict']}", use_container_width=True
    )

if submitted:
    status_map = {
        t["ready"]: "Ready to Move",
        t["construction"]: "Under Construction",
    }
    transaction_map = {
        t["resale"]: "Resale",
        t["new"]: "New Property",
    }
    furnishing_map = {
        t["unfurnished"]: "Unfurnished",
        t["semi"]: "Semi-Furnished",
        t["furnished"]: "Furnished",
    }
    overlooking_map = {
        t["garden"]: "Garden/Park",
        t["road"]: "Main Road",
        t["pool"]: "Pool",
        t["club"]: "Club",
        t["other"]: "Other",
    }
    ownership_map = {
        t["freehold"]: "Freehold",
        t["leasehold"]: "Leasehold",
        t["society"]: "Co-operative Society",
        t["attorney"]: "Power of Attorney",
    }

    input_data = pd.DataFrame({
        "location": [location],
        "Status": [status_map[status_label]],
        "Floor": [floor],
        "Transaction": [transaction_map[transaction_label]],
        "Furnishing": [furnishing_map[furnishing_label]],
        "facing": [facing],
        "overlooking": [overlooking_map[overlooking_label]],
        "Bathroom": [bathroom],
        "Balcony": [balcony],
        "Car Parking": [parking],
        "Ownership": [ownership_map[ownership_label]],
        "carpet_area_sqft": [carpet_area],
    })

    # Demo formula only; replace with your trained model pipeline.
    prediction = carpet_area * 12000 + bathroom * 500000

    st.markdown(
        f'<div dir="{direction}" class="price-card">'
        f'<h2>💎 {t["result"]}</h2>'
        f'<div class="price">₹ {prediction:,.0f}</div>'
        f'<p>{t["result_caption"]}</p>'
        f'</div>',
        unsafe_allow_html=True,
    )

    st.write("")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            f'<div dir="{direction}" class="metric-card">'
            f'<div class="metric-label">{t["area_metric"]}</div>'
            f'<div class="metric-value">{carpet_area:,.0f} sqft</div>'
            f'</div>',
            unsafe_allow_html=True,
        )

    with c2:
        st.markdown(
            f'<div dir="{direction}" class="metric-card">'
            f'<div class="metric-label">{t["bathroom_metric"]}</div>'
            f'<div class="metric-value">{bathroom}</div>'
            f'</div>',
            unsafe_allow_html=True,
        )

    with c3:
        st.markdown(
            f'<div dir="{direction}" class="metric-card">'
            f'<div class="metric-label">{t["location_metric"]}</div>'
            f'<div class="metric-value">{location.title()}</div>'
            f'</div>',
            unsafe_allow_html=True,
        )

    st.info(f"ℹ️ {t['note']}")

st.markdown(
    '<div class="footer">ESTATEIQ • HOUSE PRICE PREDICTION</div>',
    unsafe_allow_html=True,
)