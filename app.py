import streamlit as st

# 1. ENHANCED CSS (The "Luxury" Layer)
st.markdown("""
    <style>
    /* Professional Font Import */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Glassmorphism Effect for the Description Box */
    .glass-box {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 40px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.07);
        margin-bottom: 40px;
    }

    /* Animated Hover Cards */
    .sub-card {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 15px;
        border-bottom: 4px solid #1B263B; /* Navy Base */
        transition: all 0.3s ease-in-out;
        height: 250px;
    }
    .sub-card:hover {
        transform: translateY(-10px);
        border-bottom: 4px solid #C5A059; /* Gold Accent on Hover */
        box-shadow: 0 12px 20px rgba(0,0,0,0.1);
    }
    
    /* Elegant Button Styling */
    .stButton>button {
        border-radius: 50px;
        padding: 10px 25px;
        background-color: #1B263B;
        color: white;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #C5A059;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. THE PAGE CONTENT
if page == "Corporate Overview":
    st.markdown('<p style="text-align:center; font-size: 3.5rem; font-weight:800; color:#1B263B; margin-bottom:0;">RAK GROUP</p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#C5A059; font-weight:700; letter-spacing:3px;">REAL QUALITY MATTERS</p>', unsafe_allow_html=True)
    
    # Hero Image - A high-end office/cityscape
    st.image("https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=2070", use_container_width=True)

    # THE DESCRIPTION BOX (Glassmorphism)
    st.markdown("""
        <div class="glass-box">
            <h2 style="color: #1B263B;">Executive Summary</h2>
            <p style="font-size: 1.15rem; color: #4A5568; line-height: 1.8;">
                RAK Group is a diversified industrial conglomerate and strategic facilitation partner based in the Philippines. 
                We specialize in <b>High-Volume Energy Logistics</b>, <b>Industrial Commodity Procurement</b>, and <b>Luxury Real Estate Investment</b>. 
                Our expertise bridges the gap between international suppliers and localized market growth, managing multi-billion peso 
                contracts with institutional precision.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # TRUST METRICS BAR
    m1, m2, m3 = st.columns(3)
    m1.metric("Diesel Supply", "1M Liters/Mo", "Verified")
    m2.metric("Steel Volume", "11,000 MT", "Active")
    m3.metric("Project Value", "₱1.0B+", "Institutional")

    st.markdown("<br><h3 style='text-align:center;'>Our Subsidiaries</h3>", unsafe_allow_html=True)

    # THE 6 SUBSIDIARY GRID (Animated Cards)
    row1_col1, row1_col2, row1_col3 = st.columns(3)
    
    with row1_col1:
        st.markdown("""<div class="sub-card">
            <h4 style="color:#1B263B;">⛽ MC Petrofuel</h4>
            <p style="font-size:0.9rem; color:#666;">Global maritime fuel trading and large-scale diesel logistics.</p>
        </div>""", unsafe_allow_html=True)

    with row1_col2:
        st.markdown("""<div class="sub-card">
            <h4 style="color:#1B263B;">🏠 Zionlife</h4>
            <p style="font-size:0.9rem; color:#666;">High-end property investment, SMDC specialist, and Airbnb ROI management.</p>
        </div>""", unsafe_allow_html=True)

    with row1_col3:
        st.markdown("""<div class="sub-card">
            <h4 style="color:#1B263B;">🏗️ Industrial</h4>
            <p style="font-size:0.9rem; color:#666;">Bulk procurement of steel, fuel, and raw industrial materials.</p>
        </div>""", unsafe_allow_html=True)
    
    # (Add a second row of 3 here for your total of 6)
