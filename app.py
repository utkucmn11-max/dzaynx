import streamlit as st

# Sayfa Konfigürasyonu
st.set_page_config(page_title="DizaynX | Endüstriyel Çözümler", page_icon="⚡", layout="wide")

# Modern Stil Ayarları
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stApp { color: #ffffff; }
    .hero-text { font-size: 45px; font-weight: 800; color: #00fbff; margin-bottom: 0px; }
    .info-card { background-color: #1a1c24; padding: 20px; border-radius: 10px; border-left: 4px solid #00fbff; }
    </style>
    """, unsafe_allow_html=True)

# --- ÜST BİLGİ (HEADER) ---
col1, col2 = st.columns([1, 3])
with col1:
    # Profesyonel SVG Logo (Sırtmayan Tasarım)
    st.markdown("""
        <svg width="80" height="80" viewBox="0 0 100 100">
            <rect width="100" height="100" rx="20" fill="#00fbff" fill-opacity="0.1"/>
            <path d="M30 30L70 70M70 30L30 70" stroke="#00fbff" stroke-width="8" stroke-linecap="round"/>
        </svg>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("<h1 class='hero-text'>DIZAYNX</h1>", unsafe_allow_html=True)
    st.write("### Endüstriyel Kablo Kurutma Teknolojileri")

st.divider()

# --- ÜRÜN BÖLÜMÜ ---
st.header("🔍 Ürün İnceleme: CDA-0110-06C")
col_img, col_info = st.columns([1.5, 1])

with col_img:
    # Geçici resim (Buraya kendi makine fotoğrafını yükleyebilirsin)
    st.image("https://via.placeholder.com/600x400/1a1c24/00fbff?text=CDA-0110-06C+Kablo+Kurutucu", 
             caption="CDA-0110-06C Modeli")

with col_info:
    st.markdown("""
    <div class="info-card">
        <h4>Teknik Özellikler</h4>
        <ul>
            <li><b>Kapasite:</b> 0 - 10 mm Çap</li>
            <li><b>Hava Tüketimi:</b> 300 L/dak (@6 Bar)</li>
            <li><b>Malzeme:</b> Yüksek Dayanımlı Gövde</li>
            <li><b>Kullanım:</b> Hat Tipi Kurutma</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.button("Teknik Çizim İndir (PDF)")

st.divider()

# --- İLETİŞİM (FOTOĞRAFTAKİ GERÇEK BİLGİLER) ---
st.header("📞 İletişim & Destek")
c1, c2, c3 = st.columns(3)

with c1:
    st.info("**Yetkili Kişi**")
    st.write("Mr. Göksel YILMAZ")
    st.write("Global Satış Müdürü")

with c2:
    st.info("**E-Posta**")
    st.write("goksel@dizaynx.com.tr")
    st.write("info@dizaynx.com.tr")

with c3:
    st.info("**Adres**")
    st.write("Esentepe Mah. Adnan Doğu Cad. No:18")
    st.write("Ergene Vadisi, Çorlu / Tekirdağ")

# Alt Bilgi
st.markdown("<br><p style='text-align: center; color: #444;'>© 2026 DizaynX Endüstriyel. Tüm hakları saklıdır.</p>", unsafe_allow_html=True)