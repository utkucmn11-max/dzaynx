import streamlit as st
import streamlit.components.v1 as components

# Sayfa Genişlik Ayarları
st.set_page_config(page_title="DizaynX | Kurumsal", layout="wide", initial_sidebar_state="collapsed")

# Gönderdiğin HTML Kodunu Python Değişkenine Alıyoruz
html_template = """
<!DOCTYPE html>
<html lang="tr" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@700&family=Lato:wght@300;400&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Lato', sans-serif; background-color: #1a1a1a; color: #e0e0e0; overflow-x: hidden; }
        .text-neon-blue { color: #00e5ff; }
        .bg-neon-blue { background-color: #00e5ff; }
        .border-neon-blue { border-color: #00e5ff; }
        .hero-section {
            background: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.8)), 
            url('https://images.unsplash.com/photo-1537462715879-360eeb61a0ad?q=80&w=2000');
            background-size: cover; background-position: center;
        }
    </style>
</head>
<body>
    <header class="bg-[#1a1a1a] shadow-lg sticky top-0 z-50 border-b border-[#333]">
        <nav class="container mx-auto px-6 py-4 flex justify-between items-center">
            <div class="flex items-center space-x-2">
                <span class="text-2xl font-bold text-white uppercase tracking-tighter">Dizayn<span class="text-neon-blue">X</span></span>
            </div>
            <div class="hidden md:flex space-x-8 items-center text-xs font-bold tracking-widest">
                <a href="#" class="hover:text-neon-blue transition">ANA SAYFA</a>
                <a href="#products" class="hover:text-neon-blue transition">ÜRÜNLER</a>
                <a href="#contact" class="hover:text-neon-blue transition">İLETİŞİM</a>
            </div>
        </nav>
    </header>

    <section class="hero-section h-screen flex items-center justify-center text-center px-6">
        <div class="max-w-4xl">
            <h1 class="text-6xl md:text-8xl font-bold text-white mb-6 uppercase italic tracking-tighter">
                Kusursuz <span class="text-neon-blue">Kuruluk.</span>
            </h1>
            <p class="text-xl text-gray-400 mb-10 tracking-widest uppercase">Endüstriyel Kablo Kurutma Teknolojileri</p>
            <div class="flex flex-col sm:flex-row justify-center space-y-4 sm:space-y-0 sm:space-x-6">
                <a href="#products" class="px-10 py-4 bg-neon-blue text-black font-black uppercase transition hover:scale-105">Ürünleri İncele</a>
            </div>
        </div>
    </section>

    <section id="products" class="py-20 bg-[#121212] px-6">
        <div class="container mx-auto text-center mb-16">
            <h2 class="text-4xl font-bold text-white uppercase">Mühendislik <span class="text-neon-blue">Harikası</span></h2>
        </div>
        <div class="grid md:grid-cols-3 gap-10">
            <div class="bg-[#1a1a1a] border border-[#333] hover:border-neon-blue transition p-2">
                <img src="https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?q=80&w=800" class="w-full grayscale hover:grayscale-0 transition">
                <div class="p-6">
                    <h3 class="text-xl font-bold text-white">CDA-0110-06C</h3>
                    <p class="text-gray-500 text-sm mt-2">0-10mm çaplı hatlar için ultra verimli kurutma.</p>
                </div>
            </div>
            <div class="bg-[#1a1a1a] border border-[#333] hover:border-neon-blue transition p-2">
                <img src="https://images.unsplash.com/photo-1504917595217-d4dc5ebe6122?q=80&w=800" class="w-full grayscale hover:grayscale-0 transition">
                <div class="p-6">
                    <h3 class="text-xl font-bold text-white">CDA-0500-08B</h3>
                    <p class="text-gray-500 text-sm mt-2">30-80mm kılıf hatları için yüksek performans.</p>
                </div>
            </div>
            <div class="bg-[#1a1a1a] border border-[#333] hover:border-neon-blue transition p-2">
                <img src="https://images.unsplash.com/photo-1565608087341-404b254586ce?q=80&w=800" class="w-full grayscale hover:grayscale-0 transition">
                <div class="p-6">
                    <h3 class="text-xl font-bold text-white">Özel Çözümler</h3>
                    <p class="text-gray-500 text-sm mt-2">İhtiyaca özel endüstriyel tasarımlar.</p>
                </div>
            </div>
        </div>
    </section>

    <section id="contact" class="py-20 bg-[#1a1a1a] border-t border-[#333] px-6 text-center">
        <h2 class="text-3xl font-bold mb-10 uppercase tracking-widest">Global İletişim</h2>
        <div class="grid md:grid-cols-3 gap-8 text-sm">
            <div>
                <p class="text-gray-500 uppercase">Yetkili</p>
                <p class="font-bold">Göksel YILMAZ</p>
            </div>
            <div>
                <p class="text-gray-500 uppercase">E-Posta</p>
                <p class="font-bold text-neon-blue">goksel@dizaynx.com.tr</p>
            </div>
            <div>
                <p class="text-gray-500 uppercase">Lokasyon</p>
                <p class="font-bold text-white">Çorlu / Tekirdağ</p>
            </div>
        </div>
    </section>
</body>
</html>
"""

# HTML'i Streamlit Ekranına Basıyoruz
components.html(html_template, height=2500, scrolling=False)
