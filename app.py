import streamlit as st

# Sayfa Genişliği ve Tarayıcı Başlığı
st.set_page_config(page_title="DizaynX Industrial | Precision Cooling", layout="wide", initial_sidebar_state="collapsed")

# --- KURUMSAL STİL (CSS) ---
st.markdown("""
    <style>
    /* Karanlık ve Premium Arka Plan */
    .stApp { background-color: #080808; color: #ffffff; font-family: 'Inter', sans-serif; }
    
    /* Navigasyon Barı */
    .nav-bar { display: flex; justify-content: space-between; align-items: center; padding: 25px 0; border-bottom: 1px solid #1a1a1a; margin-bottom: 40px; }
    .logo-text { font-size: 30px; font-weight: 900; letter-spacing: 3px; color: #fff; }
    .logo-x { color: #00d4ff; text-shadow: 0 0 15px rgba(0,212,255,0.4); }
    
    /* Hero Başlıkları */
    .hero-label { font-size: 14px; letter-spacing: 5px; color: #666; text-transform: uppercase; margin-bottom: 10px; }
    .hero-title { font-size: 72px; font-weight: 800; background: linear-gradient(180deg, #fff 0%, #444 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; line-height: 1.1; }

    /* Teknik Bilgi Kartları */
    .card-container { background: #111111; border: 1px solid #1a1a1a; padding: 40px; border-radius: 2px; }
    .spec-value { font-size: 42px; font-weight: 700; color: #00d4ff; line-height: 1; }
    .spec-unit { font-size: 12px; color: #444; text-transform: uppercase; letter-spacing: 2px; margin-top: 5px; display: block; }
    
    /* Footer */
    .footer { margin-top: 80px; padding: 40px 0; border-top: 1px solid #111; color: #333; font-size: 12px; letter-spacing: 1px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- NAV BAR ---
st.markdown("""
    <div class="nav-bar">
        <div class="logo-text">DIZAYN<span class="logo-x">X</span></div>
        <div style="font-size: 12px; color: #555; letter-spacing: 2px;">ENGINEERED FOR EXCELLENCE</div>
    </div>
    """, unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown('<p class="hero-label">Technical Precision</p>', unsafe_allow_html=True)
st.markdown('<h1 class="hero-title">CDA-0110-06C<br>Air Drying Solutions</h1>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# --- PRODUCT DISPLAY ---
col_left, col_right = st.columns([1.4, 1])

with col_left:
    # Makine Görseli (Placeholder ama karanlık temaya uygun)
    st.image("https://images.unsplash.com/photo-1537462715879-360eeb61a0ad?auto=format&fit=crop&q=80&w=1200", 
             caption="DizaynX Series | Industrial Grade Build")

with col_right:
    st.markdown('<div class="card-container">', unsafe_allow_html=True)
    st.write("### Üretim Hattı Performansı")
    st.write("Kablo ve boru hatlarında su kalıntısını %99.9 oranında temizleyen yüksek hızlı hava türbülansı teknolojisi.")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Teknik Veri Grid
    v1, v2 = st.columns(2)
    with v1:
        st.markdown('<span class="spec-value">300</span><span class="spec-unit">L/MIN AIR FLOW</span>', unsafe_allow_html=True)
    with v2:
        st.markdown('<span class="spec-value">6.0</span><span class="spec-unit">OPERATING BAR</span>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    v3, v4 = st.columns(2)
    with v3:
        st.markdown('<span class="spec-value">10</span><span class="spec-unit">MAX DIAMETER (MM)</span>', unsafe_allow_html=True)
    with v4:
        st.markdown('<span class="spec-value">AISI</span><span class="spec-unit">STAINLESS STEEL</span>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.button("İletişime Geç & Teklif Al", use_container_width=True)

# --- GLOBAL CONTACT ---
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.write("---")
c1, c2, c3 = st.columns(3)

with c1:
    st.caption("GLOBAL SALES MANAGER")
    st.write("**Mr. Göksel YILMAZ**")

with c2:
    st.caption("OFFICE & PRODUCTION")
    st.write("Ergene Vadisi, Çorlu / Tekirdağ")

with c3:
    st.caption("EMAIL ENQUIRIES")
    st.write("goksel@dizaynx.com.tr")

st.markdown('<div class="footer">DIZAYNX © 2026 | ALL RIGHTS RESERVED.</div>', unsafe_allow_html=True)
