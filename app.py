import streamlit as st

# 1. INITIALIZE & PREVENT ERRORS
st.set_page_config(page_title="RAK Group of Companies", page_icon="🏢", layout="wide")

# 2. CUSTOM CSS (Backgrounds & Luxury Styling)
st.markdown("""
    <style>
    /* Full Page Background Gradient */
    .stApp {
        background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
    }

    /* Professional Sidebar Background */
    [data-testid="stSidebar"] {
        background-color: #1B263B !important;
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Hero Section with Background Image */
    .hero-section {
        background-image: linear-gradient(rgba(27, 38, 59, 0.8), rgba(27, 38, 59, 0.8)), 
                          url('https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=2070');
        background-size: cover;
        background-position: center;
        padding: 100px 20px;
        text-align: center;
        border-radius: 20px;
        color: white;
        margin-bottom: 40px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    }

    /* Glassmorphism Card for Description */
    .glass-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 40px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.05);
        margin: -60px 40px 40px 40px; /* Pulls it up into the Hero image */
        position: relative;
        z-index: 10;
    }

    /* Animated Metrics */
    div[data-testid="stMetricValue"] {
        color: #C5A059 !important; /* Gold Numbers */
        font-weight: 800;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. SIDEBAR NAVIGATION
st.sidebar.markdown("<h2 style='text-align: center;'>RAK GROUP</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align: center; font-size: 0.8rem; letter-spacing: 2px;'>REAL QUALITY MATTERS</p>", unsafe_allow_html=True)
st.sidebar.markdown("---")
page = st.sidebar.radio("Go to:", [
    "Corporate Home", 
    "MC Petrofuel Global", 
    "Zionlife Real Estate", 
    "Industrial Procurement",
    "Logistics & Trading"
])

# 4. PAGE LOGIC
if page == "Corporate Home":
    # HERO SECTION
    st.markdown("""
        <div class="hero-section">
            <h1 style="font-size: 4rem; margin-bottom: 0;">RAK GROUP</h1>
            <p style="font-size: 1.5rem; letter-spacing: 5px; color: #C5A059;">OFFICIAL PORTAL</p>
        </div>
    """, unsafe_allow_html=True)

    # DESCRIPTION BOX (Pushed up into Hero)
    st.markdown("""
        <div class="glass-card">
            <h2 style="color: #1B263B; margin-top: 0;">Executive Summary</h2>
            <p style="font-size: 1.2rem; color: #4A5568; line-height: 1.8;">
                RAK Group of Companies is a diversified industrial conglomerate based in the Philippines. 
                We specialize in <b>High-Volume Energy Logistics</b>, <b>Commodity Procurement</b>, 
                and <b>Luxury Real Estate</b>. By bridging global supply chains with localized growth, 
                we manage multi-billion peso contracts with institutional precision and unyielding quality.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # TRUST METRICS
    st.markdown("<br>", unsafe_allow_html=True)
    m1, m2, m3 = st.columns(3)
    m1.metric("Fuel Facilitation", "1M Liters/Mo", "Verified")
    m2.metric("Industrial Steel", "11,000 MT", "Active")
    m3.metric("Project Value", "₱1.0B+", "Institutional")

elif page == "MC Petrofuel Global":
    st.title("⛽ MC Petrofuel Global")
    st.image("https://images.unsplash.com/photo-1518640165980-d3e0e2ba6c1e?q=80&w=1600", caption="Maritime Logistics")
    st.write("Professional facilitation for large-scale energy trading and diesel supply.")

# FOOTER
st.markdown("---")
st.caption("© 2026 RAK Group of Companies | Makati City, Philippines")
