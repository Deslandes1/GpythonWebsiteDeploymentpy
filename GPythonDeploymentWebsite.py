import streamlit as st
import webbrowser
from datetime import datetime
# --- A. CONFIGURATION D'IDENTITÉ (GESNER DESLANDES) ---
st.set_page_config(page_title="GESNER DESLANDES - PRO", layout="wide", page_icon="🚀")
# Style CSS pour le nom en MAJUSCULES et centré
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        color: #1E90FF;
        font-family: 'Arial Black', sans-serif;
        font-size: 60px;
        margin-bottom: 0px;
    }
    .sub-title {
        text-align: center;
        color: #555;
        font-size: 20px;
        margin-top: 0px;
    }
    </style>
    <h1 class="main-title">GESNER DESLANDES</h1>
    <p class="sub-title">Expert IT | Services Multi-Services | Production Créative</p>
    """, unsafe_allow_html=True)
# --- B. DONNÉES DE CONTACT & PAIEMENT ---
MY_EMAIL = "deslandes78@gmail.com"
MY_MONCASH = "(509) 4738-5663"
# --- C. LOGIQUE DE NOTIFICATION ---
def trigger_payment_alert(plan, price):
    # Alerte visuelle immédiate
    st.toast(f"Notification envoyée à {MY_EMAIL}", icon="📩")
    st.success(f"### Procédure de Paiement\n"
               f"1. Transférez **${price} USD** via MonCash au **{MY_MONCASH}**.\n"
               f"2. Une confirmation sera envoyée à **{MY_EMAIL}** pour activer votre plan {plan}.")
# --- D. INTERFACE UTILISATEUR & PLANS TARIFAIRES ---
st.sidebar.title("💎 ESPACE ABONNÉS")
st.sidebar.markdown(f"**Paiement MonCash :**\n{MY_MONCASH}")
st.sidebar.markdown(f"**Contact :**\n{MY_EMAIL}")
st.subheader("Choisissez votre Plan d'Accès")
plans = {
    "Essai Gratuit": {"price": 0, "feature": "Accès 24h limité"},
    "Standard": {"price": 3, "feature": "Accès Mensuel Basique"},
    "Pro": {"price": 5, "feature": "Accès Mensuel + Support IT"},
    "Premium": {"price": 10, "feature": "Accès Illimité + Snowflake Sync"},
    "Super Premium": {"price": 20, "feature": "Avantages Exclusifs GESNER DESLANDES"}
}
cols = st.columns(len(plans))
for i, (name, info) in enumerate(plans.items()):
    with cols[i]:
        st.markdown(f"### {name}")
        st.write(f"## ${info['price']}")
        st.caption(info['feature'])
        if st.button(f"S'abonner", key=f"plan_{i}"):
            trigger_payment_alert(name, info['price'])
# --- E. OPTIONS DE DÉPLOIEMENT & PLATEFORMES ---
st.divider()
st.write("### 🛠 Gestion du Déploiement Professionnel")
col1, col2, col3 = st.columns(3)
with col1:
    st.write("**Streamlit Community Cloud**")
    st.caption("Hébergement gratuit 24/7 via GitHub.")
    with col2:
     st.write("**Snowflake Integration**")
    st.caption("Déploiement sécurisé pour bases de données.")
with col3:
    st.write("**Custom Deployment**")
    st.caption("Configuration sur serveurs privés (VPS).")
# --- F. ACCÈS PROPRIÉTAIRE (ACCÈS TOTAL POUR GESNER) ---
st.sidebar.markdown("---")
admin_key = st.sidebar.text_input("Code Administrateur (Gesner)", type="password")
if admin_key == "GESNER_PRO_2026":
    st.sidebar.success("BIENVENUE GESNER. ACCÈS TOTAL 24/7 ACTIVÉ.")
    st.balloons()