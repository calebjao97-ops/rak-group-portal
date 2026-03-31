import streamlit as st

# 1. PAGE CONFIG
st.set_page_config(page_title="RAK Group of Companies", page_icon="🏢", layout="wide")

# 2. INJECT CUSTOM CSS FOR ELEGANCE
st.markdown("""
    <style>
    /* Change Background and Font */
    .stApp {
        background-color: #f8f9fa;
    }
    
    /* Luxury Header */
    .main-header {
        font-family: 'Inter', sans-serif;
        color: #1B263B;
        font-weight: 800;
        font-size: 3rem;
        margin-bottom: 0px;
    }
    
    .sub-header {
        color: #778DA9;
        font-size: 1.2rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 30px;
    }

    /* Professional Cards */
    .card {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        border-left: 5px solid #1B263B;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        height: 200px;
        transition: 0.3s;
    }
    .card:hover {
        box-shadow: 0 8px 15px rgba(0,0,0,0.2);
        transform: translateY(-5px);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. SIDEBAR NAVIGATION
st.sidebar.markdown("<h2 style='color: #1B263B;'>RAK GROUP</h2>", unsafe_allow_html=True)
st.sidebar.markdown("---")
page = st.sidebar.radio("Executive Menu", [
    "Corporate Overview", 
    "MC Petrofuel Global", 
    "Zionlife Real Estate", 
    "Industrial Procurement",
    "PhilHealth YAKAP",
    "Logistics & Trading",
    "Partner Portal"
])

# 4. PAGE CONTENT: CORPORATE OVERVIEW
if page == "Corporate Overview":
    st.markdown('<p class="main-header">RAK Group of Companies</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Real Quality Matters</p>', unsafe_allow_html=True)
    
    st.write("---")
    
    # 6-Subsidiary Grid
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""<div class="card">
            <h3>⛽ Energy</h3>
            <p>MC Petrofuel Global: Leading maritime fuel logistics and global energy trading operations.</p>
        </div>""", unsafe_allow_html=True)
        st.write("") # Spacer
        st.markdown("""<div class="card">
            <h3>🏥 Health</h3>
            <p>PhilHealth YAKAP: Empowering communities through corporate health card distribution.</p>
        </div>""", unsafe_allow_html=True)

    with col2:
        st.markdown("""<div class="card">
            <h3>🏠 Real Estate</h3>
            <p>Zionlife: Premium property investment strategies and luxury Airbnb management.</p>
        </div>""", unsafe_allow_html=True)
        st.write("") # Spacer
        st.markdown("""<div class="card">
            <h3>🚢 Logistics</h3>
            <p>Seamless supply chain management for global industrial commodities.</p>
        </div>""", unsafe_allow_html=True)

    with col3:
        st.markdown("""<div class="card">
            <h3>🏗️ Procurement</h3>
            <p>High-volume industrial steel and diesel supply chain facilitation.</p>
        </div>""", unsafe_allow_html=True)
        st.write("") # Spacer
        st.markdown("""<div class="card">
            <h3>🤝 Consultancy</h3>
            <p>Strategic facilitation for international trade and corporate partnerships.</p>
        </div>""", unsafe_allow_html=True)

# 5. OTHER PAGES (MC Petrofuel Example)
elif page == "MC Petrofuel Global":
    st.title("⛽ MC Petrofuel Global")
    st.info("Authorized Maritime Fuel Procurement & Logistics")
    # You can add more details here...

# FOOTER
st.sidebar.markdown("---")
st.sidebar.caption("© 2026 RAK Group | Makati City, Philippines")
