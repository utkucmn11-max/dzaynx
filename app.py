import streamlit as st

# Sayfa Yapılandırması
st.set_page_config(page_title="DIZAYNX | Industrial Excellence", layout="wide")

# --- CUSTOM CSS (Sitenin Ruhunu Değiştiriyoruz) ---
st.markdown("""
    <style>
    /* Global Karartma ve Fontlar */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700;900&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #050505 !important;
        font-family: 'Inter', sans-serif;
    }

    /* Streamlit'in standart menülerini gizle */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Modern Başlık Stili */
    .main-title {
        font-size: 80px;
        font-weight: 900;
        letter-spacing: -3px;
        line-height: 0.9;
        background: linear-gradient(180deg, #fff 0%, #333 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 20px;
    }

    /* Teknik Kartlar */
    .metric-card {
        background: #0f0f0f;
        border: 1px solid #1a1a1a;
        padding: 30px;
        border-radius: 0px;
        border-left: 2px solid #00fbff;
        transition: 0.4s all;
    }
    .metric-card:hover {
        background: #151515;
        border-color: #00fbff;
    }

    .metric-value {
        font-size: 38px;
        font-weight: 700;
        color: #fff;
        display: block;
    }
    .metric-label {
        font-size: 11px;
        text-transform: uppercase;
        color: #555;
        letter-spacing: 2px;
    }

    /* Kurumsal X Vurgusu */
    .logo-container {
        font-size: 24px;
        font-weight: 900;
        color: #fff;
        letter-spacing: 2px;
        margin-bottom: 50px;
    }
    .x-mark { color: #00fbff; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<div class="logo-container">DIZAYN<span class="x-mark">X</span></div>', unsafe_allow_html=True)

# --- HERO SECTION ---
col_hero, _ = st.columns([2, 1])
with col_hero:
    st.markdown('<h1 class="main-title">ADVANCED<br>DRYING<br>SYSTEMS.</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color:#666; font-size:20px; max-width:500px;">Kablo üretim hatları için tasarlanmış, dünyanın en verimli hava kurutma teknolojileri.</p>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# --- PRODUCT SHOWCASE ---
col_img, col_specs = st.columns([1.5, 1])

with col_img:
    # Profesyonel endüstriyel render görseli
    st.image("https://images.unsplash.com/photo-1537462715879-360eeb61a0ad?q=80&w=2000", use_container_width=True)
    st.caption("MODEL: CDA-0110-06C // HIGH-SPEED CABLE DRYER")

with col_specs:
    st.markdown("<br><br>", unsafe_allow_html=True)
    # Teknik Veri Gridleri
    m1, m2 = st.columns(2)
    with m1:
        st.markdown('<div class="metric-card"><span class="metric-value">300</span><span class="metric-label">L/MIN AIR</span></div>', unsafe_allow_html=True)
    with m2:
        st.markdown('<div class="metric-card"><span class="metric-value">0-10</span><span class="metric-label">MM RANGE</span></div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    m3, m4 = st.columns(2)
    with m3:
        st.markdown('<div class="metric-card"><span class="metric-value">6.0</span><span class="metric-label">OP. BAR</span></div>', unsafe_allow_html=True)
    with m4:
        st.markdown('<div class="metric-card"><span class="metric-value">AISI</span><span class="metric-label">304 STEEL</span></div>', unsafe_allow_html=True)

# --- CONTACT FOOTER ---
st.markdown("<br><br><br><br>", unsafe_allow_html=True)
st.divider()

f1, f2, f3 = st.columns(3)
with f1:
    st.markdown('<p class="metric-label">Global Sales</p>', unsafe_allow_html=True)
    st.write("**Mr. Göksel YILMAZ**")
with f2:
    st.markdown('<p class="metric-label">Headquarters</p>', unsafe_allow_html=True)
    st.write("Tekirdağ, Türkiye")
with f3:
    st.markdown('<p class="metric-label">Direct Mail</p>', unsafe_allow_html=True)
    st.write("goksel@dizaynx.com.tr")
