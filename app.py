import streamlit as st

# 1. INITIALIZE (This prevents the NameError)
st.set_page_config(page_title="RAK Group of Companies", page_icon="🏢", layout="wide")

# 2. SIDEBAR SELECTION (Defining 'page' here)
st.sidebar.title("RAK GROUP")
page = st.sidebar.radio("Executive Menu", [
    "Corporate Overview", 
    "MC Petrofuel Global", 
    "Zionlife Real Estate", 
    "Industrial Procurement",
    "PhilHealth YAKAP",
    "Logistics & Trading"
])

# 3. CSS STYLING
st.markdown("""
    <style>
    .main-header { font-size: 3rem; font-weight: 800; color: #1B263B; text-align: center; }
    .sub-header { font-size: 1.2rem; color: #C5A059; text-align: center; letter-spacing: 2px; }
    .glass-box { background: white; padding: 30px; border-radius: 15px; border: 1px solid #e0e0e0; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

# 4. PAGE LOGIC
if page == "Corporate Overview":
    st.markdown('<p class="main-header">RAK Group of Companies</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">REAL QUALITY MATTERS</p>', unsafe_allow_html=True)
    
    st.markdown("""
        <div class="glass-box">
            <h3>Executive Summary</h3>
            <p>RAK Group is a diversified conglomerate specializing in high-volume energy logistics, 
            industrial procurement, and luxury real estate. We bridge global supply chains with 
            local market excellence.</p>
        </div>
    """, unsafe_allow_html=True)

    # Trust Metrics
    m1, m2, m3 = st.columns(3)
    m1.metric("Fuel Capacity", "1M Liters/Mo")
    m2.metric("Steel Volume", "11,000 MT")
    m3.metric("Project Value", "₱1.0B+")

elif page == "MC Petrofuel Global":
    st.title("⛽ MC Petrofuel Global")
    st.image("https://images.unsplash.com/photo-1518640165980-d3e0e2ba6c1e?q=80&w=1600")
    st.write("Specializing in maritime fuel logistics and energy trading.")

elif page == "Zionlife Real Estate":
    st.title("🏠 Zionlife Real Estate")
    st.image("https://images.unsplash.com/photo-1522204523234-8729aa6e3d5f?q=80&w=1600")
    st.write("Luxury property investment and Airbnb management strategies.")

# (Add other elif blocks as needed)
