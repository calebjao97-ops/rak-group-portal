import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="RAK Group of Companies", layout="wide")

# 2. Sidebar Navigation for 6 Subsidiaries
st.sidebar.title("RAK Group")
st.sidebar.subheader("Our Subsidiaries")
selection = st.sidebar.radio("Go to:", [
    "RAK Group Home", 
    "Energy & Fuel (MC Petrofuel)", 
    "Real Estate (Zionlife)", 
    "Industrial Procurement",
    "Health Services (Yakap)",
    "Logistics & Trading",
    "Consultancy & Facilitation"
])

# 3. Main Content Logic
if selection == "RAK Group Home":
    st.title("RAK Group of Companies")
    st.header("Real Quality Matters")
    st.write("Welcome to the official portal of RAK Group. We are a diversified conglomerate committed to excellence across energy, real estate, and industrial sectors.")
    
    # Showcase Grid
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("### Energy")
        st.write("Global fuel logistics.")
    with col2:
        st.info("### Real Estate")
        st.write("Luxury & Investment properties.")
    with col3:
        st.info("### Procurement")
        st.write("Industrial steel & commodities.")

elif selection == "Energy & Fuel (MC Petrofuel)":
    st.title("MC Petrofuel Global")
    st.subheader("Maritime Fuel & Energy Trading")
    st.write("Managing high-volume diesel procurement (1M Liters/Month).")
    st.button("Request Quote")

elif selection == "Real Estate (Zionlife)":
    st.title("Zionlife")
    st.subheader("Premier Real Estate & Airbnb Strategies")
    st.write("Specializing in high-end developments and investment growth.")

# Add similar 'elif' blocks for the other 4 companies...

# 4. Shared Footer
st.markdown("---")
st.caption("© 2026 RAK Group of Companies | Professional Facilitation & Marketing")