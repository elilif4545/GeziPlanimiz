import streamlit as st
import folium
from streamlit_folium import st_folium


# =========================================================
# SAYFA AYARLARI
# =========================================================

st.set_page_config(
    page_title="Gezi Planı",
    page_icon="💗",
    layout="wide"
)


# =========================================================
# ORTAK TASARIM
# =========================================================

st.html("""
<style>
html, body, [data-testid="stAppViewContainer"] {
    background-color: #F7D5E0 !important;
}

[data-testid="stHeader"] {
    background-color: rgba(0,0,0,0) !important;
}

.main {
    background-color: #F7D5E0 !important;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    position: relative;
    z-index: 2;
}

/* PIXEL KALPLER */
.pixel-heart {
    position: fixed;
    background: #C85C82;
    pointer-events: none;
    z-index: 0;
    clip-path: polygon(
        0% 20%, 14% 20%, 14% 0%, 43% 0%, 43% 20%,
        57% 20%, 57% 0%, 86% 0%, 86% 20%, 100% 20%,
        100% 60%, 86% 60%, 86% 80%, 71% 80%, 71% 100%,
        29% 100%, 29% 80%, 14% 80%, 14% 60%, 0% 60%
    );
}

.heart1 { top:12%; left:5%; width:70px; height:60px; opacity:.32; }
.heart2 { top:24%; right:6%; width:52px; height:45px; opacity:.27; }
.heart3 { top:43%; left:3%; width:60px; height:52px; opacity:.30; }
.heart4 { top:54%; right:5%; width:75px; height:64px; opacity:.30; }
.heart5 { top:70%; left:8%; width:45px; height:39px; opacity:.27; }
.heart6 { top:81%; right:8%; width:63px; height:54px; opacity:.30; }
.heart7 { top:91%; left:5%; width:40px; height:35px; opacity:.25; }
.heart8 { top:89%; right:17%; width:48px; height:41px; opacity:.27; }

/* ANA BAŞLIK */
.main-title {
    text-align:center;
    color:#7A2948;
    font-size:42px;
    font-weight:800;
    margin-top:10px;
    margin-bottom:45px;
}

/* ÜLKE BAŞLIĞI */
.country-title {
    text-align:center;
    color:#7A2948;
    font-size:28px;
    font-weight:800;
    margin-top:25px;
    margin-bottom:18px;
}

/* ÜLKE BUTONU */
.country-button button {
    width:100% !important;
    min-height:120px !important;
    background-color:#FCE7EF !important;
    border:3px solid #E8A9BC !important;
    border-radius:22px !important;
    color:#7A2948 !important;
    font-size:25px !important;
    font-weight:800 !important;
    box-shadow:0 6px 15px rgba(122,41,72,.12) !important;
}
