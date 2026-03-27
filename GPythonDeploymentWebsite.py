import streamlit as st

st.set_page_config(
    page_title="GlobalInternet.py – Advanced Surveillance & Discovery Tools",
    page_icon="🔴",
    layout="wide"
)

# -------------------------------------------------------------------
# Branding & Style
# -------------------------------------------------------------------
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #00209F 0%, #D21034 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 2rem;
    }
    .product-card {
        border: 1px solid #ddd;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        background-color: #f9f9f9;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
    }
    .product-title {
        color: #D21034;
        font-size: 1.8rem;
        font-weight: bold;
    }
    .price {
        font-size: 1.6rem;
        font-weight: bold;
        color: #00209F;
    }
    .contact {
        background-color: #eef2f6;
        padding: 1rem;
        border-radius: 10px;
        margin-top: 2rem;
    }
    .footer {
        text-align: center;
        font-size: 0.8rem;
        color: #666;
        margin-top: 2rem;
        padding: 1rem;
        border-top: 1px solid #ddd;
    }
</style>
""", unsafe_allow_html=True)

# Haitian flag (simple)
st.markdown("""
<div style="display: flex; justify-content: center; margin-bottom: 20px;">
    <svg width="320" height="192" viewBox="0 0 960 576" xmlns="http://www.w3.org/2000/svg">
        <rect width="960" height="288" fill="#00209F" />
        <rect y="288" width="960" height="288" fill="#D21034" />
    </svg>
</div>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header"><h1>GlobalInternet.py</h1><p>Advanced Surveillance & Discovery Tools</p></div>', unsafe_allow_html=True)

# Introduction
st.markdown("""
Welcome to **GlobalInternet.py** – your source for cutting‑edge software that puts real‑time intelligence in your hands.

We develop professional‑grade surveillance, geological discovery, and data analysis tools. All our products are delivered as ready‑to‑deploy Python code, compatible with Streamlit Cloud or your own server.
""")

# -------------------------------------------------------------------
# Product 1: Global Surveillance Radar
# -------------------------------------------------------------------
st.markdown('<div class="product-card">', unsafe_allow_html=True)
st.markdown('<span class="product-title">🔴 Global Surveillance Radar</span>', unsafe_allow_html=True)
st.markdown("""
- **Real‑time tracking** of all ADS‑B equipped aircraft (airliners, military jets, drones) anywhere on Earth.
- **Military & drone detection** – automatic classification via ICAO hex, callsigns, and flight behaviour.
- **Rotating polar radar** + interactive map with range rings.
- **Detailed reports** – click any aircraft for full info and download as text.
- **Works with your own Flightradar24 API key** for true global coverage (optional).
- **Price:** $500 USD (one‑time license)
""")
st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------------------------
# Product 2: Infinity Engine – Geological Research Platform
# -------------------------------------------------------------------
st.markdown('<div class="product-card">', unsafe_allow_html=True)
st.markdown('<span class="product-title">🚀 Infinity Engine</span>', unsafe_allow_html=True)
st.markdown("""
- **AI‑powered resource identification** from photos (camera or upload).
- **Geolocation capture** – manual coordinates or automatic GPS.
- **Interactive map** – visualise all discoveries with colour‑coded markers.
- **Multi‑language** – English, French, Spanish, Haitian Creole.
- **Export full research history** as CSV.
- **Price:** $299 USD (one‑time license)
""")
st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------------------------
# Bundle Offer
# -------------------------------------------------------------------
st.markdown('<div class="product-card">', unsafe_allow_html=True)
st.markdown('<span class="product-title">🎁 Bundle Deal</span>', unsafe_allow_html=True)
st.markdown("""
Get **both the Global Surveillance Radar and the Infinity Engine** for a single payment of **$649 USD** – save $150.
""")
st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------------------------
# Purchase & Contact
# -------------------------------------------------------------------
st.markdown('<div class="contact">', unsafe_allow_html=True)
st.markdown("### 💸 How to Purchase")
st.markdown("""
1. **Send payment** via **Prisme Transfer** (Digicel Moncash) to:  
   📞 **(509) 4738-5663**  
   *Reference: “Radar Purchase” or “Infinity Engine” or “Bundle”*

2. **Email confirmation** to **deslandes78@gmail.com** with:
   - Your name
   - Which product(s) you are buying
   - The payment reference

3. You will receive the software package and setup instructions within 24 hours.
""")

st.markdown("### 📧 Need Help?")
st.markdown("""
- **Email**: deslandes78@gmail.com  
- **Phone**: (509) 4738-5663 (Prisme Transfer / Moncash only for payments)
""")
st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------------------------
# Footer
# -------------------------------------------------------------------
st.markdown('<div class="footer">© 2025 Gesner Deslandes – GlobalInternet.py | All rights reserved</div>', unsafe_allow_html=True)
