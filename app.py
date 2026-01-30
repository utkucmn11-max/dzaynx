import streamlit as st

# Sayfa ayarlarını en üst seviyeye çekiyoruz
st.set_page_config(page_title="DizaynX | Advanced Drying Systems", layout="wide")

# Kurumsal ve Modern CSS (Özel Tasarım)
st.markdown("""
    <style>
    /* Arka plan ve yazı tipi */
    .stApp { background-color: #050505; color: #e0e0e0; font-family: 'Inter', sans-serif; }
    
    /* Üst Bar Tasarımı */
    .nav-bar { display: flex; justify-content: space-between; align-items: center; padding: 20px 0; border-bottom: 1px solid #222; margin-bottom: 50px; }
    .logo-text { font-size: 28px; font-weight: 900; letter-spacing: 2px; color: #fff; }
    .logo-x { color: #00e5ff; }
    
    /* Hero Section (Giriş) */
    .hero-container { text-align: center; padding: 60px 0; }
    .hero-h1 { font-size: 64px; font-weight: 800; background: linear-gradient(to right, #fff, #888); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 10px; }
    .hero-p { font-size: 20px; color: #888; letter-spacing: 1px; }

    /* Teknik Kart Tasarımı */
    .spec-card { background: #111; border: 1px solid #222; padding: 30px; border-radius: 4px; transition: 0.3s; }
    .spec-card:hover { border-color: #00e5ff; background: #151515; }
    .spec-val { font-size: 32px; font-weight: 700; color: #00e5ff; display: block; }
    .spec-label { font-size: 12px; text-transform: uppercase; color: #666; letter-spacing: 2px; }

    /* Footer */
    .footer { margin-top: 100px; padding: 40px; border-top: 1px solid #222; text-align: center; color: #444; font-size: 13px; }
    </style>
    """, unsafe_allow_html=True)

# --- NAV BAR ---
st.markdown("""
    <div class="nav-bar">
        <div class="logo-text">DIZAYN<span class="logo-x">X</span></div>
        <div style="color: #666; font-size: 14px;">PRECISION ENGINEERING</div>
    </div>
    """, unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown("""
    <div class="hero-container">
        <p class="hero-p">CDA SERIES</p>
        <h1 class="hero-h1">Ultra-High Efficiency<br>Cable Drying Systems</h1>
    </div>
    """, unsafe_allow_html=True)

# --- ANA GÖRSEL VE TE
