import streamlit as st

# 1. PAGE CONFIG
st.set_page_config(page_title="RAK Group of Companies", page_icon="🏢", layout="wide")

# 2. INJECT CUSTOM CSS FOR ELEGANCE
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    
    /* Professional Banners */
    .hero-banner {
        width: 100%;
        height: 350px;
        object-fit: cover;
        border-radius: 20px;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    /* Executive Headers */
    .main-header { font-family: 'Inter', sans-serif; color: #1B263B; font-weight: 800; font-size: 3rem; margin-bottom: 0px; text-align: center; }
    .sub-header { color: #778DA9; font-size: 1.2rem; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 30px; text-align: center; }

    /* Interactive Cards */
    .card { background-color: white; padding: 25px; border-radius: 15px; border-left: 5px solid #1B263B; box-shadow: 0 4px 6px rgba(0,0,0,0.1); height: 210px; transition: 0.3s; margin-bottom: 20px;}
    .card:hover { box-shadow: 0 8px 15px rgba(0,0,0,0.2); transform: translateY(-5px); }
    .card-title { color: #1B263B; font-size: 1.4rem; font-weight: 700; margin-bottom: 10px;}
    </style>
    """, unsafe_allow_html=True)

# 3. SIDEBAR NAVIGATION
# Link to your logo later
# st.sidebar.image("https://path-to-your-logo.png", width=150)
st.sidebar.markdown("<h2 style='color: #1B263B; text-align: center;'>RAK GROUP</h2>", unsafe_allow_html=True)
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
            <p class="card-title">⛽ Energy & Fuel</p>
            <p>MC Petrofuel Global: Driving maritime logistics and strategic energy trading on a global scale.</p>
        </div>""", unsafe_allow_html=True)
        st.markdown("""<div class="card">
            <p class="card-title">🏥 Health Services</p>
            <p>PhilHealth YAKAP: Strengthening public health access through corporate health card distribution.</p>
        </div>""", unsafe_allow_html=True)

    with col2:
        st.markdown("""<div class="card">
            <p class="card-title">🏠 Real Estate</p>
            <p>Zionlife: High-growth property investment strategies and premier Airbnb management in Makati.</p>
        </div>""", unsafe_allow_html=True)
        st.markdown("""<div class="card">
            <p class="card-title">🚢 Global Logistics</p>
            <p>Seamless supply chain management for diversified industrial commodities and international trade.</p>
        </div>""", unsafe_allow_html=True)

    with col3:
        st.markdown("""<div class="card">
            <p class="card-title">🏗️ Procurement</p>
            <p>Industrial Steel & Wholesale Fuel supply chain facilitation for major infrastructure projects.</p>
        </div>""", unsafe_allow_html=True)
        st.markdown("""<div class="card">
            <p class="card-title">🤝 Consultancy</p>
            <p>Strategic facilitation for international partnerships, investments, and corporate trade.</p>
        </div>""", unsafe_allow_html=True)

# 5. SUBSIDIARY PAGES WITH HIGH-QUALITY BANNERS

elif page == "MC Petrofuel Global":
    st.markdown('<p class="main-header">MC Petrofuel Global</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Authorized Maritime Fuel Logistics</p>', unsafe_allow_html=True)
    
    # Energy Hero Image (Source: Unsplash - Fuel Tanker/Energy Infrastructure)
    st.markdown('<img src="https://images.unsplash.com/photo-1518640165980-d3e0e2ba6c1e?q=80&w=1600" class="hero-banner">', unsafe_allow_html=True)
    
    st.info("Direct facilitation for high-volume diesel procurement (1,000,000 Liters/Month).")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Our Scope")
        st.write("- Maritime Fuel Supply\n- Global Energy Trading\n- Storage & Distribution")
    with col2:
        st.subheader("Verified Capacity")
        st.metric(label="Monthly Volume Facilitated", value="1.0M Liters")

elif page == "Zionlife Real Estate":
    st.markdown('<p class="main-header">Zionlife Real Estate</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Luxury Investment Agency & Management</p>', unsafe_allow_html=True)
    
    # Real Estate Hero Image (Source: Unsplash - Modern High-Rise Apartment)
    st.markdown('<img src="https://images.unsplash.com/photo-1522204523234-8729aa6e3d5f?q=80&w=1600" class="hero-banner">', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Makati Investment Portfolio")
        st.write("- Glam Residences (SMDC Specialist)\n- Premier High-End Developments\n- Passive Income Strategies")
    with col2:
        st.subheader("Airbnb Management")
        st.write("- Full-service property management for maximum ROI\n- Client portfolio optimization")

elif page == "Industrial Procurement":
    st.markdown('<p class="main-header">Industrial Procurement</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Commodity Supply Chain Facilitation</p>', unsafe_allow_html=True)
    
    # Procurement Hero Image (Source: Unsplash - Construction Site/Steel Structure)
    st.markdown('<img src="https://images.unsplash.com/photo-1541888946425-d81bb19240f5?q=80&w=1600" class="hero-banner">', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Core Commodities")
        st.write("- Industrial Steel (11,000 MT capacity)\n- Bulk Diesel Supply (1M Liters)")
    with col2:
        st.subheader("Facilitation Scope")
        st.write("- ICPO & FCO Management\n- Contract Negotiation\n- International Supply Chains")

elif page == "Logistics & Trading":
    st.markdown('<p class="main-header">Logistics & Trading</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Global Supply Chain Management</p>', unsafe_allow_html=True)
    
    # Logistics Hero Image (Source: Unsplash - Container Ship/Port)
    st.markdown('<img src="https://images.unsplash.com/photo-1578575437130-527eed3abbec?q=80&w=1600" class="hero-banner">', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Our Services")
        st.write("- Multi-modal Transport (Sea, Land)\n- Customs Brokerage Facilitation\n- Warehousing")
    with col2:
        st.subheader("Market Reach")
        st.write("- Trans-Pacific Logistics\n- Southeast Asia Trade Routes")

# Footer (appears on every page)
st.sidebar.markdown("---")
st.sidebar.caption("© 2026 **RAK Group** | Principal Facilitator & Marketing")
st.sidebar.caption("Makati City, Philippines")
