import base64

def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

img = get_base64("cover.jpg")  # <-- export your first slide as image

st.markdown(f"""
<style>
.hero {{
    background-image: url("data:image/jpg;base64,{img}");
    background-size: cover;
    background-position: center;
    height: 90vh;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
}}

.hero-text {{
    background: rgba(0,0,0,0.6);
    padding: 40px;
    border-radius: 15px;
}}

.hero h1 {{
    font-size: 60px;
    color: white;
}}

.hero p {{
    font-size: 20px;
    color: #e2e8f0;
}}
</style>

<div class="hero">
    <div class="hero-text">
        <h1>RAK Group</h1>
        <p>Empowering Progress and Innovation</p>
    </div>
</div>
""", unsafe_allow_html=True)

# CUSTOM CSS (Professional Corporate Style)
st.markdown("""
<style>
body {
    background-color: #0f172a;
    color: white;
}
h1, h2, h3 {
    color: #38bdf8;
}
.section {
    padding: 40px 0;
}
.card {
    background-color: #1e293b;
    padding: 25px;
    border-radius: 15px;
    margin-bottom: 20px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
}
.highlight {
    color: #22c55e;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# HERO SECTION
st.title("RAK Group")
st.subheader("Empowering Progress and Innovation")

st.markdown("""
A diversified conglomerate driving **sustainable development, innovation, and operational excellence** across critical industries in the Philippines and ASEAN.

""")

st.divider()

# ABOUT SECTION
st.header("About Us")

st.markdown("""
RAK Group is a **multi-sector holding company** focused on building an integrated ecosystem that enhances quality of life.

### Core Strengths:
- Financial Strength & Stability  
- Corporate Governance & Transparency  
- Technology-Driven Operations (ERP, CRM, IoT)  
- Sustainability through *Green RAK Initiative*  
""")

# OPERATIONS SECTION
st.divider()
st.header("Our Business Units")

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Infrastructure")
    st.write("EMET Port Builders Inc.")
    st.write("• Ports, bridges, pipelines, and construction")
    st.write("• Industrial and maritime infrastructure")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Waste Management")
    st.write("RAK Waste Management Services Inc.")
    st.write("• Recycling & landfill diversion")
    st.write("• DENR-compliant sustainable solutions")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Healthcare")
    st.write("RAK Health Solutions Inc.")
    st.write("• Medical distribution & clinics")
    st.write("• Pharmacy and telemedicine services")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Logistics")
    st.write("RAK Value Distribution Network Inc.")
    st.write("• Nationwide supply chain & last-mile delivery")
    st.write("• Route optimization & real-time tracking")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Trading")
    st.write("RAK Gen Merch Trading Inc.")
    st.write("Zion Enterprises Inc.")
    st.write("• Import/export, wholesale & retail")
    st.write("• Consignment-based distribution model")
    st.markdown('</div>', unsafe_allow_html=True)

# STRATEGY SECTION
st.divider()
st.header("Strategic Vision")

st.markdown("""
### 2027–2030 Growth Strategy
- ASEAN Expansion  
- Renewable Energy & Water Treatment  
- Digital B2B Platforms  
- Strategic Mergers & Acquisitions  

### Key Focus:
- <span class="highlight">Sustainability</span>  
- <span class="highlight">Digital Transformation</span>  
- <span class="highlight">Operational Synergy</span>  
""", unsafe_allow_html=True)

# TECHNOLOGY SECTION
st.divider()
st.header("Technology & Innovation")

st.markdown("""
We leverage advanced technologies to ensure operational excellence:

- ERP Systems for integrated operations  
- CRM for client management  
- IoT for real-time monitoring  
- Cloud-based financial systems  
- Cybersecurity and data protection  
""")

# SUSTAINABILITY SECTION
st.divider()
st.header("Sustainability: Green RAK")

st.markdown("""
Our sustainability framework focuses on:

- Carbon footprint reduction  
- Renewable energy adoption  
- Circular economy practices  
- Water conservation  
- ISO-aligned environmental compliance  
""")

# MARKET POSITION
st.divider()
st.header("Market Position")

st.markdown("""
RAK Group is positioned as a **national leader** by:

- Serving essential sectors  
- Building integrated ecosystems  
- Driving economic growth and employment  
- Expanding into underserved regions  
""")

# CALL TO ACTION
st.divider()
st.header("Partner With Us")

st.markdown("""
Join us in building a **future-ready Philippines** through innovation, sustainability, and strategic collaboration.

📩 Contact us today for partnerships and business opportunities.
""")

# FOOTER
st.divider()
st.caption("© 2026 RAK Group | All Rights Reserved")
