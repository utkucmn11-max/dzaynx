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

# --- ANA GÖRSEL VE TEKNİK VERİLER ---
col1, col2 = st.columns([1.5, 1])

with col1:
    # Profesyonel bir ürün görseli yer tutucusu (Kendi makine resmini buraya koyacağız)
    st.image("https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?auto=format&fit=crop&q=80&w=1000", 
             caption="CDA-0110-06C Next-Gen Dryer")

with col2:
    st.write("### Technical Mastery")
    st.write("Hava tüketimini optimize eden, patentli türbülans teknolojisi ile kablo yüzeyindeki nemi mikron seviyesinde temizler.")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Teknik Veri Kartları
    c_a, c_b = st.columns(2)
    with c_a:
        st.markdown('<div class="spec-card"><span class="spec-val">0-10</span><span class="spec-label">MM ÇAP</span></div>', unsafe_allow_html=True)
    with c_b:
        st.markdown('<div class="spec-card"><span class="spec-val">300</span><span class="spec-label">L/MIN HAVA</span></div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    c_c, c_d = st.columns(2)
    with c_c:
        st.markdown('<div class="spec-card"><span class="spec-val">6.0</span><span class="spec-label">BAR BASINÇ</span></div>', unsafe_allow_html=True)
    with c_d:
        st.markdown('<div class="spec-card"><span class="spec-val">IP67</span><span class="spec-label">KORUMA</span></div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# --- İLETİŞİM PANELİ ---
st.write("---")
st.write("### Global Inquiry")
ic1, ic2, ic3 = st.columns(3)

with ic1:
    st.caption("SALES DIRECTOR")
    st.write("**Mr. Göksel YILMAZ**")

with ic2:
    st.caption("HEADQUARTERS")
    st.write("Ergene Vadisi, Tekirdağ, TR")

with ic3:
    st.caption("DIRECT CONTACT")
    st.write("goksel@dizaynx.com.tr")

st.markdown('<div class="footer">© 2026 DIZAYNX INDUSTRIAL SOLUTIONS. BUİLT FOR PERFORMANCE.</div>', unsafe_allow_html=True)
