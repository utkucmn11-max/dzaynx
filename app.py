import streamlit as st

# 1. Sayfa Temelleri
st.set_page_config(page_title="DizaynX | Endüstriyel Çözümler", page_icon="⚡", layout="wide")

# 2. Kurumsal Stil (CSS) - Logonu ve Tasarımı Buradan Düzenliyoruz
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .title-text { font-size: 48px; font-weight: 800; color: #00fbff; letter-spacing: -1px; }
    .section-card { background-color: #1a1c24; padding: 25px; border-radius: 12px; border-left: 5px solid #00fbff; }
    </style>
    """, unsafe_allow_html=True)

# 3. Logo ve Başlık (Artık Sırıtmıyor!)
col1, col2 = st.columns([1, 5])
with col1:
    st.markdown("""
        <svg width="70" height="70" viewBox="0 0 100 100">
            <rect width="100" height="100" rx="20" fill="#00fbff" fill-opacity="0.1"/>
            <path d="M30 30L70 70M70 30L30 70" stroke="#00fbff" stroke-width="10" stroke-linecap="round"/>
        </svg>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("<h1 class='title-text'>DIZAYNX</h1>", unsafe_allow_html=True)
    st.write("### Endüstriyel Kablo Kurutma Sistemleri")

st.divider()

# 4. Ürün Tanıtımı (CDA-0110-06C)
st.header("📦 Öne Çıkan Ürün")
c_img, c_info = st.columns([1.5, 1])

with c_img:
    # Yer tutucu görsel (Gerçek makine resmini daha sonra buraya ekleyebiliriz)
    st.image("https://via.placeholder.com/800x450/1a1c24/00fbff?text=CDA-0110-06C+Dryer", 
             caption="CDA-0110-06C Endüstriyel Ünite")

with c_info:
    st.markdown("""
    <div class="section-card">
        <h4>Teknik Özellikler</h4>
        <ul>
            <li><b>Uygulama:</b> 0 - 10 mm Kablo Çapı</li>
            <li><b>Hava Tüketimi:</b> 300 L/dak (@6 Bar)</li>
            <li><b>Malzeme:</b> Paslanmaz Çelik & Alüminyum</li>
            <li><b>Verimlilik:</b> %99 Nem Arındırma</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    st.button("📄 Teknik Veri Sayfasını İndir")

st.divider()

# 5. İletişim Bilgileri (Göksel Bey'in Bilgileri)
st.header("📞 İletişim & Destek")
k1, k2, k3 = st.columns(3)

with k1:
    st.info("**Yetkili:** Mr. Göksel YILMAZ")
    st.write("Global Satış Müdürü")

with k2:
    st.success("**E-Posta:**")
    st.write("goksel@dizaynx.com.tr")

with k3:
    st.warning("**Adres:**")
    st.write("Ergene Vadisi, Çorlu / Tekirdağ")

st.markdown("<br><p style='text-align: center; color: #555;'>© 2026 DizaynX | Çorlu, Türkiye</p>", unsafe_allow_html=True)
