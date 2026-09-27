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

.country-button button:hover {
    background-color:#E88BAA !important;
    color:white !important;
    border-color:#C85C82 !important;
}

/* GÜN BUTONU */
.day-button button {
    width:100% !important;
    min-height:105px !important;
    background-color:#FCE7EF !important;
    border:2px solid #E8A9BC !important;
    border-radius:18px !important;
    color:#7A2948 !important;
    font-size:17px !important;
    font-weight:700 !important;
    text-align:left !important;
    padding:18px 22px !important;
    white-space:pre-line !important;
    box-shadow:0 4px 12px rgba(122,41,72,.10) !important;
}

.day-button button:hover {
    background-color:#E88BAA !important;
    border-color:#C85C82 !important;
    color:white !important;
}

/* GERİ */
.back-button {
    margin-bottom:25px;
}

.back-button button {
    background-color:#FCE7EF !important;
    color:#7A2948 !important;
    border:2px solid #C85C82 !important;
    border-radius:14px !important;
    font-weight:700 !important;
}

.back-button button:hover {
    background-color:#E88BAA !important;
    color:white !important;
}

/* BİLGİ */
.info-card {
    background-color:#FCE7EF;
    border:2px solid #E8A9BC;
    border-radius:18px;
    padding:25px;
    text-align:center;
    color:#7A2948;
    margin-top:25px;
}

/* GÜN BAŞLIĞI */
.day-header {
    background:#FCE7EF;
    border:2px solid #E8A9BC;
    border-radius:22px;
    padding:22px 28px;
    margin-bottom:25px;
    box-shadow:0 6px 18px rgba(122,41,72,.10);
    text-align:center;
}

.day-header h1 {
    color:#7A2948;
    font-size:32px;
    font-weight:800;
    margin:0;
}

.day-header p {
    color:#C85C82;
    font-size:17px;
    font-weight:700;
    margin-top:7px;
    margin-bottom:0;
}

/* PROGRAM */
.program-box {
    background:#FCE7EF;
    border:2px solid #E8A9BC;
    border-radius:20px;
    padding:25px;
    margin-bottom:30px;
    box-shadow:0 5px 15px rgba(122,41,72,.08);
}

.program-heading {
    color:#7A2948;
    font-size:25px;
    font-weight:800;
    margin-bottom:20px;
}

.program-row {
    background:white;
    border-left:5px solid #E88BAA;
    border-radius:14px;
    padding:15px 18px;
    margin-bottom:12px;
}

.program-time {
    display:inline-block;
    width:105px;
    color:#C85C82;
    font-size:16px;
    font-weight:800;
    vertical-align:top;
}

.program-content {
    display:inline-block;
    color:#3D2630;
    font-size:16px;
    font-weight:600;
    line-height:1.5;
    width:calc(100% - 115px);
}

.task-title, .map-title, .section-title {
    color:#7A2948;
    font-size:26px;
    font-weight:800;
    margin-top:30px;
    margin-bottom:15px;
}

div[data-testid="stCheckbox"] {
    background:#FCE7EF !important;
    border:2px solid #E8A9BC !important;
    border-radius:13px !important;
    padding:8px 14px !important;
    margin-bottom:8px !important;
}

div[data-testid="stCheckbox"] label p {
    color:#7A2948 !important;
    font-size:17px !important;
    font-weight:700 !important;
}

@media (max-width:768px) {
    .main-title { font-size:34px; }
    .country-title { font-size:25px; }
    .country-button button { min-height:105px !important; font-size:22px !important; }
    .day-button button { min-height:95px !important; font-size:15px !important; }
    .program-time { width:75px; font-size:14px; }
    .program-content { width:calc(100% - 85px); font-size:14px; }
}
</style>

<div class="pixel-heart heart1"></div>
<div class="pixel-heart heart2"></div>
<div class="pixel-heart heart3"></div>
<div class="pixel-heart heart4"></div>
<div class="pixel-heart heart5"></div>
<div class="pixel-heart heart6"></div>
<div class="pixel-heart heart7"></div>
<div class="pixel-heart heart8"></div>
""")


# =========================================================
# YARDIMCI FONKSİYONLAR
# =========================================================

def geri_buton(hedef, yazi):
    st.markdown('<div class="back-button">', unsafe_allow_html=True)
    if st.button(yazi, key=f"geri_{hedef}", use_container_width=False):
        st.session_state.sayfa = hedef
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)


def program_goster(program):
    st.html("""
    <div class="program-box">
        <div class="program-heading">📅 Günün Programı</div>
    """)

    for saat, baslik, detay in program:
        st.html(f"""
        <div class="program-row">
            <span class="program-time">{saat}</span>
            <span class="program-content">
                {baslik}<br>{detay}
            </span>
        </div>
        """)

    st.html("</div>")


def standart_harita(route_points, key, location, zoom=12,
                    task_points=None, task_prefix="⭐"):
    coords = [(x[2], x[3]) for x in route_points]

    m = folium.Map(
        location=location,
        zoom_start=zoom,
        tiles="OpenStreetMap"
    )

    folium.PolyLine(
        coords,
        color="#C85C82",
        weight=5,
        opacity=0.85
    ).add_to(m)

    for number, name, lat, lon in route_points:
        icon = folium.DivIcon(
            html=f"""
            <div style="
                background:#7A2948;
                color:white;
                border-radius:50%;
                width:34px;
                height:34px;
                display:flex;
                align-items:center;
                justify-content:center;
                font-size:15px;
                font-weight:bold;
                border:3px solid white;
                box-shadow:0 2px 7px rgba(0,0,0,.30);
            ">{number}</div>
            """
        )

        folium.Marker(
            location=[lat, lon],
            tooltip=f"{number}) {name}",
            popup=name,
            icon=icon
        ).add_to(m)

    if task_points:
        for number, (name, coord) in enumerate(task_points, start=1):
            task_icon = folium.DivIcon(
                html=f"""
                <div style="
                    background:#E88BAA;
                    color:#7A2948;
                    border-radius:50%;
                    width:32px;
                    height:32px;
                    display:flex;
                    align-items:center;
                    justify-content:center;
                    font-size:14px;
                    border:3px solid white;
                    box-shadow:0 2px 7px rgba(0,0,0,.25);
                ">⭐</div>
                """
            )
            folium.Marker(
                location=coord,
                tooltip=f"{task_prefix} {number}) {name}",
                popup=name,
                icon=task_icon
            ).add_to(m)

        all_points = coords + [coord for _, coord in task_points]
        m.fit_bounds(all_points, padding=(30, 30))
    else:
        m.fit_bounds(coords)

    st_folium(m, width=None, height=600, key=key)


def gun_baslik(tarih, alt):
    st.html(f"""
    <div class="day-header">
        <h1>{tarih}</h1>
        <p>{alt}</p>
    </div>
    """)


# =========================================================
# HOLLANDA 1. GÜN
# =========================================================

def hollanda1():
    gun_baslik(
        "💗 28 EYLÜL — 1. GÜN",
        "🇳🇱 Amsterdam'a İlk Gün"
    )

    points = {
        "İzmir": (38.4237, 27.1428),
        "Düsseldorf Havalimanı": (51.2895, 6.7668),
        "Worringer Strasse 140 - FlixBus": (51.2217, 6.7948),
        "Amsterdam Sloterdijk": (52.3887, 4.8377),
        "Triple G Hotels": (52.3788, 4.8540),
        "Dam Meydanı": (52.3731, 4.8926),
    }

    route = [
        (1, "İzmir", *points["İzmir"]),
        (2, "Düsseldorf Havalimanı", *points["Düsseldorf Havalimanı"]),
        (3, "Worringer Strasse 140 - FlixBus", *points["Worringer Strasse 140 - FlixBus"]),
        (4, "Amsterdam Sloterdijk", *points["Amsterdam Sloterdijk"]),
        (5, "Triple G Hotels", points["Triple G Hotels"][0], points["Triple G Hotels"][1] + 0.00030),
        (6, "Dam Meydanı", *points["Dam Meydanı"]),
        (7, "Otele Dönüş - Triple G Hotels", points["Triple G Hotels"][0] + 0.00030, points["Triple G Hotels"][1]),
    ]

    program = [
        ("06:10", "✈️ KALKIŞ", "İzmir → Düsseldorf"),
        ("08:30", "🛬 İNİŞ", "Düsseldorf Havalimanı"),
        ("10:30", "🚌 FLIXBUS BİNİŞ", "Worringer Strasse 140"),
        ("14:30", "🇳🇱 AMSTERDAM'A VARIŞ", "Amsterdam Sloterdijk"),
        ("15:00", "🏠 OTELE VARIŞ", "Triple G Hotels • Willem de Zwijgerlaan 350"),
        ("15:00–17:00", "🛏️ DİNLENME", "Otele yerleşme, dinlenme ve hazırlanma"),
        ("17:00", "🌆 AKŞAM GEZİSİ", "Otelden çıkış → Dam Meydanı"),
        ("≈18:00", "🍽️ AKŞAM YEMEĞİ", "Dam çevresinde yemek"),
        ("≈22:00", "🏠 OTELE DÖNÜŞ", "Triple G Hotels"),
    ]
    program_goster(program)

    tasks = [
        ("Urban Outfitters", (52.371695, 4.892120)),
        ("SNIPES", (52.3709, 4.8918)),
        ("LEGO Winkel Amsterdam", (52.37084, 4.89187)),
        ("The Rubber Duck Store", (52.370414, 4.892262)),
        ("Stroopwafel", (52.3742333, 4.8930022)),
    ]

    st.markdown('<div class="task-title">⭐ Bugünün Yapılacakları</div>', unsafe_allow_html=True)
    for i, (name, _) in enumerate(tasks):
        st.checkbox(f"⭐ {name}", key=f"task_day1_{i}")

    st.markdown('<div class="map-title">🗺️ 28 Eylül Rotası</div>', unsafe_allow_html=True)
    standart_harita(
        route,
        "map_day1",
        (52.3731, 4.8926),
        13,
        tasks
    )


# =========================================================
# HOLLANDA 2. GÜN
# =========================================================

def hollanda2():
    gun_baslik(
        "💗 29 EYLÜL — 2. GÜN",
        "Amsterdam • Şehir Merkezi & Tekne Turu"
    )

    hotel = (52.3788, 4.8540)
    gezinme_sabah = (52.3799, 4.8883)
    manneken_pis = (52.375789, 4.896147)
    tonys = (52.37552, 4.89687)
    sexmuseum = (52.37658, 4.89728)
    basiliek = (52.37654, 4.90083)
    red_light_secrets = (52.37365, 4.89898)
    dam = (52.3731, 4.8926)
    boat_dock = (52.378360, 4.897670)
    gezinme_aksam = (52.371494, 4.895737)
    grimburgwal = (52.3693, 4.8946)

    route = [
        (1, "Triple G Hotels - Sabah Çıkış", *hotel),
        (2, "Gezinme / Oyalanma - Damrak çevresi", *gezinme_sabah),
        (3, "Manneken Pis Damrak", *manneken_pis),
        (4, "Tony's Chocolonely Super Store", *tonys),
        (5, "Sexmuseum Amsterdam", *sexmuseum),
        (6, "Basiliek van de HH Nicolaas", *basiliek),
        (7, "Red Light Secrets", *red_light_secrets),
        (8, "De Dam", *dam),
        (9, "Tekne İskelesi", *boat_dock),
        (10, "Gezinme / Oyalanma - Centrum çevresi", *gezinme_aksam),
        (11, "Grimburgwal Canal View", *grimburgwal),
        (12, "Triple G Hotels - Otele Dönüş", *hotel),
    ]

    program = [
        ("10:00", "🏠 OTELDEN ÇIKIŞ", "Triple G Hotels"),
        ("10:40–11:30", "🚶 GEZİNME / OYALANMA", "Damrak çevresi • Amsterdam merkezinde gezinme"),
        ("11:45–12:15", "🍟 MANNEKEN PIS DAMRAK", "Manneken Pis Damrak"),
        ("12:25–13:10", "🍫 TONY'S CHOCOLONELY", "Tony's Chocolonely Super Store"),
        ("13:20–14:15", "🎉 SEXMUSEUM AMSTERDAM", "Sexmuseum Amsterdam"),
        ("14:25–14:55", "⛪ BASILIEK", "Basiliek van de HH Nicolaas"),
        ("15:05–15:50", "🔴 RED LIGHT SECRETS", "Red Light Secrets"),
        ("15:50–16:40", "🏛️ DE DAM", "Dam Meydanı • çevrede vakit geçirme"),
        ("16:40–17:10", "🍽️ YEMEK MOLASI", "Dam çevresinde yemek / atıştırmalık"),
        ("17:30", "🛥️ TEKNE İSKELESİ", "İskeleye geçiş"),
        ("17:45–18:45", "🛥️ TEKNE TURU", "1 saatlik tekne turu"),
        ("19:15–20:00", "🚶 GEZİNME / OYALANMA", "Centrum çevresi"),
        ("20:00–20:30", "🍽️ YEMEK MOLASI", "Merkez çevresinde yemek"),
        ("≈20:30–20:50", "📸 GRIMBURGWAL", "Grimburgwal Canal View"),
        ("≈21:45", "🏠 OTELE DÖNÜŞ", "Triple G Hotels"),
    ]
    program_goster(program)

    st.markdown('<div class="map-title">🗺️ Günün Rotası</div>', unsafe_allow_html=True)
    standart_harita(route, "map_day2", (52.375, 4.895), 13)


# =========================================================
# HOLLANDA 3. GÜN
# =========================================================

def hollanda3():
    gun_baslik(
        "🇳🇱 30 Eylül • Çarşamba",
        "Amsterdam — Vondelpark • Museumplein • Albert Cuyp • Heineken • Dancing Houses • Centrum • De Wallen"
    )

    route = [
        (1, "Triple G Hotels", 52.3788, 4.8540),
        (2, "Vondelpark", 52.357998, 4.868444),
        (3, "Rijksmuseum / Museumplein", 52.3600, 4.8852),
        (4, "Albert Cuyp Market", 52.3560, 4.8910),
        (5, "Heineken Experience", 52.3579, 4.8915),
        (6, "Dancing Houses - Amstel 100–112", 52.36710, 4.89714),
        (7, "Staalmeestersbrug", 52.36823, 4.89767),
        (8, "Grimburgwal", 52.3693, 4.8946),
        (9, "Gezinme / Oyalanma - Centrum", 52.371494, 4.895737),
        (10, "De Wallen", 52.3732, 4.8971),
        (11, "Triple G Hotels", 52.3788, 4.8540),
    ]

    program = [
        ("09:00", "🏨 OTELDEN ÇIKIŞ", "Triple G Hotels"),
        ("09:30", "🌳 VONDELPARK", "Kahvaltı + parkta vakit geçirme"),
        ("11:00", "🏛️ MUSEUMPLEIN", "Rijksmuseum dışı • Van Gogh çevresi • Moco çevresi"),
        ("12:15", "🛍️ ALBERT CUYP MARKET", "Pazar gezisi"),
        ("13:30", "🍺 HEINEKEN EXPERIENCE", "Heineken bölgesine geçiş + öğle yemeği / hazırlık"),
        ("14:00–16:00", "🍺 HEINEKEN EXPERIENCE", "Biletli deneyim"),
        ("16:20", "📸 DANCING HOUSES", "Amstel 100–112 • Blauwbrug yanı • fotoğraf noktası"),
        ("16:40", "🌉 STAALMEESTERSBRUG", "Köprü ve kanal çevresinde kısa gezinti"),
        ("17:05", "🌊 GRIMBURGWAL", "Kanal manzarası"),
        ("17:30–18:15", "🚶 GEZİNME / OYALANMA", "Centrum çevresi"),
        ("18:15–22:00", "🌃 DE WALLEN", "Red Light District gezisi + akşam yemeği"),
        ("≈22:30", "🏠 OTELE DÖNÜŞ", "Triple G Hotels"),
    ]
    program_goster(program)

    st.markdown('<div class="map-title">🗺️ Günün Rotası</div>', unsafe_allow_html=True)
    standart_harita(route, "amsterdam_gun3_map", [52.365, 4.890], 13)


# =========================================================
# HOLLANDA 4. GÜN
# =========================================================

def hollanda4():
    gun_baslik(
        "📅 1 Ekim — 4. Gün",
        "🌾 Zaanse Schans • 🧱 Jordaan • 🧺 Laundry Boy • 🌷 Bloemenmarkt • 🌃 De Wallen"
    )

    hotel = (52.3788, 4.8540)
    centrum = (52.3731, 4.8926)
    centraal = (52.3791, 4.9003)
    zaanse = (52.4738, 4.8161)
    anne_frank = (52.3752, 4.8839)
    jordaan = (52.3764, 4.8831)
    laundry = (52.3727, 4.8812)
    vleminckx = (52.3701, 4.8897)
    bloemenmarkt = (52.3667, 4.8931)
    wallen = (52.3730, 4.8950)

    route = [
        (1, "Triple G Hotels", *hotel),
        (2, "Amsterdam Centrum", *centrum),
        (3, "Amsterdam Centraal", *centraal),
        (4, "Zaanse Schans", *zaanse),
        (5, "Anne Frank Huis", *anne_frank),
        (6, "Jordaan", *jordaan),
        (7, "Laundry Boy", *laundry),
        (8, "Vlaamsch Friteshuis Vleminckx", *vleminckx),
        (9, "Bloemenmarkt", *bloemenmarkt),
        (10, "De Wallen", *wallen),
        (11, "Triple G Hotels", *hotel),
    ]

    program = [
        ("09:00", "🏨 OTELDEN ÇIKIŞ", "Triple G Hotels"),
        ("09:30–10:30", "☕ AMSTERDAM CENTRUM", "Kahvaltı + oturma + kısa gezinti ve fotoğraf"),
        ("10:30–11:20", "🚆 ZAANSE SCHANS'A GİDİŞ", "Amsterdam Centrum → Zaanse Schans"),
        ("11:20–15:00", "🌾 ZAANSE SCHANS", "Köyü, değirmenleri ve çevreyi gezme"),
        ("15:00–15:50", "🚆 AMSTERDAM'A DÖNÜŞ", "Zaanse Schans → Amsterdam"),
        ("15:50–16:10", "🏠 ANNE FRANK HUIS", "Sadece önünden geçiş ve fotoğraf"),
        ("16:10–17:40", "🧱 JORDAAN", "Sokaklarda gezme ve takılma"),
        ("17:40–18:10", "🧺 LAUNDRY BOY", "Kısa mola"),
        ("18:10–18:25", "🚶 GEÇİŞ", "Laundry Boy → Vlaamsch Friteshuis Vleminckx"),
        ("18:25–18:55", "🍟 VLAAMSCH FRITESHUIS VLEMINCKX", "Patates molası"),
        ("18:55–19:05", "🚶 GEÇİŞ", "Vleminckx → Bloemenmarkt"),
        ("19:05–19:35", "🌷 BLOEMENMARKT", "Çiçek pazarı ve çevresini gezme"),
        ("19:35–19:50", "🚶 GEÇİŞ", "Bloemenmarkt → De Wallen"),
        ("19:50–22:00", "🌃 DE WALLEN", "Gezme + akşam yemeği"),
        ("22:00–22:45", "🏠 OTELE DÖNÜŞ", "De Wallen → Triple G Hotels"),
        ("22:45", "🛏️ OTELE VARIŞ", "Triple G Hotels"),
    ]
    program_goster(program)

    tasks = [
        ("Değirmenleri gez", zaanse),
        ("Peynir dükkanını gez", zaanse),
        ("Tahta ayakkabı atölyesini gez", zaanse),
        ("Köyü gez ve fotoğraf çek", zaanse),
    ]

    st.markdown('<div class="task-title">⭐ Zaanse Schans\'ta Yapılacaklar</div>', unsafe_allow_html=True)
    for i, (name, _) in enumerate(tasks):
        st.checkbox(f"⭐ {name}", key=f"task_day4_{i}")

    st.markdown('<div class="map-title">🗺️ 1 Ekim Rotası</div>', unsafe_allow_html=True)
    standart_harita(
        route,
        "map_day4",
        (52.4000, 4.8600),
        12,
        tasks
    )


# =========================================================
# HOLLANDA 5. GÜN — SERBEST
# =========================================================

def hollanda5():
    gun_baslik(
        "📅 2 Ekim — 5. Gün",
        "🕊️ SERBEST GÜN"
    )

    st.html("""
    <div class="info-card">
        <h2>🕊️ Amsterdam'da Serbest Gün</h2>
        <p>Bugün program serbest. İstediğiniz gibi gezebilir, alışveriş yapabilir veya dinlenebilirsiniz. 💗</p>
    </div>
    """)


# =========================================================
# ALMANYA 1. GÜN
# =========================================================

def almanya1():
    gun_baslik(
        "💗 3 EKİM — 1. GÜN",
        "🇳🇱 Amsterdam → 🇩🇪 Duisburg → Essen"
    )

    program = [
        ("08:00", "🏨 Triple G Hotel, Amsterdam — Otelden çıkış", ""),
        ("08:30", "📍 Amsterdam Sloterdijk — Otobüs durağına varış", ""),
        ("09:00", "🚌 Amsterdam Sloterdijk → Duisburg hareket", ""),
        ("11:40–12:00", "🇩🇪 Mercatorstraße 90, Duisburg — Duisburg'a varış", ""),
        ("12:15–12:25", "🏠 Wallstraße 22, 47051 Duisburg — Eve varış", ""),
        ("12:25–14:30", "🏠 Evde takılmaca / dinlenme", ""),
        ("14:30", "📍 Wallstraße 22 — Evden çıkış", ""),
        ("~15:00", "🚆 Duisburg Hbf — Essen'e hareket", ""),
        ("~15:25–15:30", "📍 Essen Hbf — Essen'e varış", ""),
        ("15:30–16:15", "🍳 Haferkater, Essen Hbf — Geç kahvaltı", ""),
        ("16:15", "🚇 Essen Hbf → Grugapark", ""),
        ("~16:40", "🌳 Grugapark — Parka giriş", ""),
        ("16:40–17:20", "🚶‍♀️ Grugapark içinden Margarethenhöhe yönüne yürüyüş", ""),
        ("~17:20", "⛲ Margarethenhöhe / Schatzgräberbrunnen — Varış", ""),
        ("17:20–18:05", "🏘️ Margarethenhöhe — Çevrede gezme + fotoğraf", ""),
        ("18:05", "🚇 Margarethenhöhe → Essen merkezine geçiş", ""),
        ("~18:25", "📍 Essen Hbf", ""),
        ("~18:35", "⛪ Essener Dom — Dış cephe + çevresi + fotoğraf", ""),
        ("18:35–19:00", "🚶‍♀️ Dom → Burgplatz → Kettwiger Straße", ""),
        ("19:00–20:00", "🛍️ Essen şehir merkezi — Çarşıda dolaşma + şehir merkezinde takılmaca", ""),
        ("20:00–21:00", "🍽️ Essen şehir merkezi — Akşam yemeği + merkezde gezinti", ""),
        ("21:00", "🚆 Essen Hbf → Duisburg dönüş", ""),
        ("~21:30", "📍 Duisburg Hbf", ""),
        ("~21:45", "🏠 Wallstraße 22 — Eve dönüş", ""),
    ]
    program_goster(program)

    points = {
        "Triple G Hotel": (52.3788, 4.8540),
        "Amsterdam Sloterdijk": (52.3887, 4.8371),
        "Mercatorstraße 90, Duisburg": (51.4344, 6.7617),
        "Wallstraße 22, Duisburg": (51.4339, 6.7652),
        "Duisburg Hbf": (51.4295, 6.7754),
        "Essen Hbf": (51.4515, 7.0132),
        "Grugapark": (51.4270, 6.9938),
        "Schatzgräberbrunnen": (51.4231, 6.9769),
        "Essener Dom": (51.4560, 7.0130),
        "Burgplatz": (51.4553, 7.0130),
        "Kettwiger Straße": (51.4536, 7.0140),
    }

    route = [
        (1, "Triple G Hotel", *points["Triple G Hotel"]),
        (2, "Amsterdam Sloterdijk", *points["Amsterdam Sloterdijk"]),
        (3, "Mercatorstraße 90, Duisburg", *points["Mercatorstraße 90, Duisburg"]),
        (4, "Wallstraße 22, Duisburg", *points["Wallstraße 22, Duisburg"]),
        (5, "Duisburg Hbf", *points["Duisburg Hbf"]),
        (6, "Essen Hbf", *points["Essen Hbf"]),
        (7, "Grugapark", *points["Grugapark"]),
        (8, "Schatzgräberbrunnen", *points["Schatzgräberbrunnen"]),
        (9, "Essener Dom", *points["Essener Dom"]),
        (10, "Burgplatz", *points["Burgplatz"]),
        (11, "Kettwiger Straße", *points["Kettwiger Straße"]),
        (12, "Duisburg Hbf", *points["Duisburg Hbf"]),
        (13, "Wallstraße 22, Duisburg", *points["Wallstraße 22, Duisburg"]),
    ]

    st.markdown('<div class="map-title">🗺️ Günün Rotası</div>', unsafe_allow_html=True)
    standart_harita(route, "map_agun1", (51.445, 6.90), 11)


# =========================================================
# ALMANYA 2. GÜN — ŞİMDİLİK HAZIRLANIYOR
# =========================================================

# 4 Ekim mevcut dosyadaki haliyle placeholder olarak bırakıldı.

# =========================================================
# ALMANYA 3. GÜN — DÜSSELDORF
# =========================================================

def almanya3():
    gun_baslik(
        "💗 5 EKİM — 3. GÜN",
        "🇩🇪 Duisburg → Düsseldorf • Hop-On Hop-Off • Altstadt • Gün Batımı • Altbier"
    )

    program = [
        ("10:30", "🏠 Wallstraße 22 — Evden çıkış", "Duisburg"),
        ("10:50", "🚆 Duisburg Hbf — İstasyona varış", ""),
        ("11:10", "🚆 Duisburg Hbf → Düsseldorf Hbf", "Tren hareketi"),
        ("~11:30", "📍 Düsseldorf Hbf — Varış", ""),
        ("11:30–12:00", "🚶 Königsallee'ye geçiş + kısa gezinti", "Königsallee"),
        ("12:00", "🚌 HOP-ON HOP-OFF — BİNİŞ", "Königsallee durağı"),
        ("12:31", "📍 RHEINTURM / MEDIENHAFEN — İNİŞ", "Hop-On Hop-Off"),
        ("12:31–13:25", "🏙️ MEDIENHAFEN", "Gehry binaları • liman çevresi • Rheinturm dışı • fotoğraf"),
        ("13:31", "🚌 HOP-ON HOP-OFF — BİNİŞ", "Medienhafen"),
        ("13:56", "🌳 NORDPARK / AQUAZOO — İNİŞ", "Aquazoo içine girilmeyecek"),
        ("13:56–14:50", "🌿 NORDPARK", "Japanese Garden • parkta yürüyüş • fotoğraf • kısa dinlenme"),
        ("14:56", "🚌 HOP-ON HOP-OFF — BİNİŞ", "Nordpark"),
        ("15:06", "📍 KUNSTAKADEMIE / ALTSTADT — İNİŞ", ""),
        ("15:10–17:30", "🏘️ DÜSSELDORF ALTSTADT", "Kunstakademie • Ratinger Straße • St. Lambertus • Marktplatz • sokaklar • kahve/tatlı • fotoğraf"),
        ("17:30–17:50", "🚶 ALTSTADT → BURGPLATZ", "Rheintreppe'ye yürüyüş"),
        ("17:50–19:00", "🌅 RHEINTREPPE — GÜN BATIMI", "Merdivenlerde oturma • Ren manzarası • gün batımı • fotoğraf • dinlenme"),
        ("19:00–21:00", "🍺 ALTBİER AKŞAMI", "Zum Schlüssel • Altbier tadımı • yemek/atıştırmalık • oturup takılmaca"),
        ("21:00–21:30", "🚶 Zum Schlüssel → Düsseldorf Hbf", ""),
        ("~21:30–22:00", "🚆 Düsseldorf Hbf → Duisburg Hbf", "Dönüş treni"),
        ("~22:00–22:15", "📍 Duisburg Hbf — Varış", ""),
        ("22:15–23:00", "🚶 Duisburg Hbf → Wallstraße 22", "Eve yürüyüş"),
        ("23:00", "🏠 Wallstraße 22 — Eve varış", "Duisburg"),
    ]
    program_goster(program)

    points = {
        "Wallstraße 22, Duisburg": (51.4339, 6.7652),
        "Duisburg Hbf": (51.4295, 6.7754),
        "Düsseldorf Hbf": (51.2206, 6.7929),
        "Königsallee": (51.2231, 6.7796),
        "Rheinturm / Medienhafen": (51.2175, 6.7620),
        "Nordpark / Aquazoo": (51.2546, 6.7680),
        "Kunstakademie": (51.2310, 6.7727),
        "St. Lambertus": (51.2271, 6.7714),
        "Marktplatz": (51.2257, 6.7719),
        "Burgplatz / Rheintreppe": (51.2267, 6.7718),
        "Zum Schlüssel": (51.2248, 6.7743),
    }

    route = [
        (1, "Wallstraße 22, Duisburg", *points["Wallstraße 22, Duisburg"]),
        (2, "Duisburg Hbf", *points["Duisburg Hbf"]),
        (3, "Düsseldorf Hbf", *points["Düsseldorf Hbf"]),
        (4, "Königsallee", *points["Königsallee"]),
        (5, "Rheinturm / Medienhafen", *points["Rheinturm / Medienhafen"]),
        (6, "Nordpark / Aquazoo", *points["Nordpark / Aquazoo"]),
        (7, "Kunstakademie", *points["Kunstakademie"]),
        (8, "St. Lambertus", *points["St. Lambertus"]),
        (9, "Marktplatz", *points["Marktplatz"]),
        (10, "Burgplatz / Rheintreppe", *points["Burgplatz / Rheintreppe"]),
        (11, "Zum Schlüssel", *points["Zum Schlüssel"]),
        (12, "Düsseldorf Hbf", *points["Düsseldorf Hbf"]),
        (13, "Duisburg Hbf", *points["Duisburg Hbf"]),
        (14, "Wallstraße 22, Duisburg", *points["Wallstraße 22, Duisburg"]),
    ]

    st.markdown('<div class="map-title">🗺️ 5 Ekim Düsseldorf Rotası</div>', unsafe_allow_html=True)
    standart_harita(route, "map_almanya3", (51.225, 6.775), 12)


# =========================================================
# ALMANYA 4. GÜN — DORTMUND
# =========================================================

def almanya4():
    gun_baslik(
        "💗 6 EKİM — 4. GÜN",
        "🇩🇪 Duisburg → Dortmund • Şehir • BVB • PHOENIX West • PHOENIX See • Bira Akşamı"
    )

    program = [
        ("10:30", "🏠 Wallstraße 22 — Evden çıkış", "Duisburg"),
        ("11:00", "🚆 Duisburg Hbf → Dortmund Hbf", "Tren hareketi"),
        ("~11:35", "📍 Dortmund Hbf — Varış", ""),
        ("11:45–12:45", "🥐 KAHVALTI", ""),
        ("", "", "Opsiyonlar: Kamps • BackWerk • Ditsch • Kamps my Deli"),
        ("12:45–13:30", "🌆 DORTMUND INNENSTADT", "Westenhellweg • Petrikirche • Reinoldikirche • Alter Markt • fotoğraf"),
        ("13:30–14:30", "🟡⚫ BVB / SIGNAL IDUNA PARK", "Stadyum çevresi • BVB atmosferi • fotoğraf"),
        ("14:30–15:00", "🚋 DORTMUND MERKEZ → PHOENIX WEST", "Toplu taşıma"),
        ("15:00–16:00", "🏭 PHOENIX WEST", "Eski sanayi bölgesi • yüksek fırınlar • fotoğraf • gezinti"),
        ("16:00–16:20", "🚶 PHOENIX WEST → PHOENIX SEE", "Göl bölgesine geçiş"),
        ("16:20–17:30", "🌊 PHOENIX SEE", "Göl çevresinde yürüyüş • fotoğraf • oturma • dinlenme"),
        ("17:30–18:00", "🚋 PHOENIX SEE → DORTMUND MERKEZ", "Toplu taşıma"),
        ("18:00–18:30", "🌆 DORTMUND MERKEZ", "Son gezinti • fotoğraf • kısa serbest zaman"),
        ("18:30–20:00", "🍺 AKŞAM YEMEĞİ + BİRA", "HÖVELS Hausbrauerei • iki kişi oturup sohbet • Hövels bira çeşitleri • Alman yemeği"),
        ("20:00–20:20", "🚶 HÖVELS → DORTMUND HBF", ""),
        ("~20:30", "🚆 Dortmund Hbf → Duisburg Hbf", "Dönüş treni"),
        ("~21:00", "🏠 Wallstraße 22 — Eve varış", "Duisburg"),
    ]
    program_goster(program)

    points = {
        "Wallstraße 22, Duisburg": (51.4339, 6.7652),
        "Duisburg Hbf": (51.4295, 6.7754),
        "Dortmund Hbf": (51.5177, 7.4588),
        "Café Bernstein": (51.5147, 7.4565),
        "Dortmunder U": (51.5134, 7.4500),
        "Reinoldikirche / Alter Markt": (51.5146, 7.4653),
        "Signal Iduna Park": (51.4926, 7.4518),
        "PHOENIX West": (51.4875, 7.4987),
        "PHOENIX See": (51.4824, 7.5029),
        "HÖVELS Hausbrauerei": (51.5108, 7.4515),
    }

    route = [
        (1, "Wallstraße 22, Duisburg", *points["Wallstraße 22, Duisburg"]),
        (2, "Duisburg Hbf", *points["Duisburg Hbf"]),
        (3, "Dortmund Hbf", *points["Dortmund Hbf"]),
        (4, "Café Bernstein", *points["Café Bernstein"]),
        (5, "Dortmunder U", *points["Dortmunder U"]),
        (6, "Reinoldikirche / Alter Markt", *points["Reinoldikirche / Alter Markt"]),
        (7, "Signal Iduna Park", *points["Signal Iduna Park"]),
        (8, "PHOENIX West", *points["PHOENIX West"]),
        (9, "PHOENIX See", *points["PHOENIX See"]),
        (10, "HÖVELS Hausbrauerei", *points["HÖVELS Hausbrauerei"]),
        (11, "Dortmund Hbf", *points["Dortmund Hbf"]),
        (12, "Duisburg Hbf", *points["Duisburg Hbf"]),
        (13, "Wallstraße 22, Duisburg", *points["Wallstraße 22, Duisburg"]),
    ]

    st.markdown('<div class="map-title">🗺️ 6 Ekim Dortmund Rotası</div>', unsafe_allow_html=True)
    standart_harita(route, "map_almanya4", (51.495, 7.48), 12)


# =========================================================
# ALMANYA 5. GÜN — DÖNÜŞ
# =========================================================

def almanya5():
    gun_baslik(
        "💗 7 EKİM — 5. GÜN",
        "✈️ Düsseldorf → İzmir • Dönüş Günü"
    )

    program = [
        ("05:30", "⏰ UYANMA", "Son hazırlıklar"),
        ("05:30–05:50", "🧳 SON HAZIRLIKLAR", "Valizleri toplama • çıkış hazırlığı"),
        ("05:50", "🏠 EVDEN ÇIKIŞ", "Wallstraße 22, Duisburg"),
        ("≈06:00", "🚶 DUISBURG HBF", "İstasyona varış"),
        ("≈06:00–06:15", "🥐 KAHVALTI", "Duisburg Hbf"),
        ("", "", "Opsiyonlar: Kamps • BackWerk • Ditsch • Kamps my Deli"),
        ("≈06:15–06:20", "🚆 RE6 — DUISBURG HBF → DÜSSELDORF FLUGHAFEN", "Direkt tren"),
        ("≈06:30–06:45", "🛫 DÜSSELDORF FLUGHAFEN", "Flughafen Fernbahnhof"),
        ("≈06:45–07:00", "🚝 SKYTRAIN → TERMİNAL", "Havalimanı terminaline geçiş"),
        ("≈07:00", "🛫 TERMİNAL", "Düsseldorf Airport"),
        ("07:00–07:45", "🧳 CHECK-IN + BAGAJ", "Uçuş işlemleri"),
        ("07:45–08:30", "🛂 GÜVENLİK / PASAPORT", "Kontroller"),
        ("08:30–09:15", "☕ BEKLEME", "Gate'e geçiş • kahve / dinlenme"),
        ("09:15", "🚶 GATE'E GEÇİŞ", "Uçağa hazırlık"),
        ("09:45", "✈️ DÜSSELDORF → İZMİR", "Uçuş"),
        ("≈13:50", "🛬 İZMİR'E VARIŞ", "Tahmini varış"),
    ]
    program_goster(program)

    points = {
        "Wallstraße 22, Duisburg": (51.4339, 6.7652),
        "Duisburg Hbf": (51.4295, 6.7754),
        "Düsseldorf Flughafen": (51.2809, 6.7897),
        "İzmir Adnan Menderes Havalimanı": (38.2924, 27.1570),
    }

    route = [
        (1, "Wallstraße 22, Duisburg", *points["Wallstraße 22, Duisburg"]),
        (2, "Duisburg Hbf", *points["Duisburg Hbf"]),
        (3, "Düsseldorf Flughafen", *points["Düsseldorf Flughafen"]),
        (4, "İzmir Adnan Menderes Havalimanı", *points["İzmir Adnan Menderes Havalimanı"]),
    ]

    st.markdown('<div class="map-title">🗺️ 7 Ekim Dönüş Rotası</div>', unsafe_allow_html=True)
    standart_harita(route, "map_almanya5", (48.0, 10.0), 5)


# =========================================================
# ALMANYA 2-5 — ŞİMDİLİK HAZIRLANIYOR
# =========================================================

def almanya_placeholder(gun, tarih, aciklama):
    gun_baslik(f"📅 {tarih} — {gun}. Gün", "🇩🇪 Almanya")

    st.html(f"""
    <div class="info-card">
        <h2>💗 {tarih} — {gun}. Gün</h2>
        <p>{aciklama}</p>
    </div>
    """)


# =========================================================
# SAYFA DURUMU
# =========================================================

if "sayfa" not in st.session_state:
    st.session_state.sayfa = "ana"


# =========================================================
# ANA SAYFA
# =========================================================

if st.session_state.sayfa == "ana":

    st.html('<div class="main-title">💗 Gezi Planı</div>')

    st.html('<div class="country-title">🇳🇱 HOLLANDA</div>')
    st.markdown('<div class="country-button">', unsafe_allow_html=True)

    if st.button(
        "🇳🇱  HOLLANDA\n\n28 Eylül — 2 Ekim • 5 Gün",
        key="ulke_hollanda",
        use_container_width=True
    ):
        st.session_state.sayfa = "hollanda"
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

    st.html('<div class="country-title">🇩🇪 ALMANYA</div>')
    st.markdown('<div class="country-button">', unsafe_allow_html=True)

    if st.button(
        "🇩🇪  ALMANYA\n\n3 Ekim — 7 Ekim • 5 Gün",
        key="ulke_almanya",
        use_container_width=True
    ):
        st.session_state.sayfa = "almanya"
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)


# =========================================================
# HOLLANDA GÜNLERİ
# =========================================================

elif st.session_state.sayfa == "hollanda":

    st.html('<div class="main-title">🇳🇱 Hollanda</div>')

    days = [
        (
            "holland_day1",
            "hollanda1",
            "📅 28 Eylül — 1. Gün\n\n✈️ İzmir → Düsseldorf → Amsterdam\n🏠 Otele yerleşme • 🌆 Dam Meydanı"
        ),
        (
            "holland_day2",
            "hollanda2",
            "📅 29 Eylül — 2. Gün\n\n🚶 Amsterdam merkez • 🛥️ Tekne turu\nDamrak • Red Light Secrets • Grimburgwal"
        ),
        (
            "holland_day3",
            "hollanda3",
            "📅 30 Eylül — 3. Gün\n\n🌳 Vondelpark • 🏛️ Rijksmuseum • 🛍️ Albert Cuyp\n🍺 Heineken • 📸 Dancing Houses • 🌉 Staalmeestersbrug"
        ),
        (
            "holland_day4",
            "hollanda4",
            "📅 1 Ekim — 4. Gün\n\n🌾 Zaanse Schans • 🧱 Jordaan • 🧺 Laundry Boy\n🌷 Bloemenmarkt • 🌃 De Wallen"
        ),
        (
            "holland_day5",
            "hollanda5",
            "📅 2 Ekim — 5. Gün\n\n🕊️ SERBEST GÜN\nAmsterdam'da serbest zaman"
        ),
    ]

    for key, target, label in days:
        st.markdown('<div class="day-button">', unsafe_allow_html=True)
        if st.button(label, key=key, use_container_width=True):
            st.session_state.sayfa = target
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    geri_buton("ana", "← Ana Sayfaya Dön")


# =========================================================
# ALMANYA GÜNLERİ
# =========================================================

elif st.session_state.sayfa == "almanya":

    st.html('<div class="main-title">🇩🇪 Almanya</div>')

    days = [
        (
            "germany_day1",
            "almanya1",
            "📅 3 Ekim — 1. Gün\n\n🇳🇱 Amsterdam → 🇩🇪 Duisburg → Essen\n🏠 Wallstraße 22 • 🍳 Haferkater • ⛪ Essener Dom"
        ),
        (
            "germany_day2",
            "almanya2",
            "📅 4 Ekim — 2. Gün\n\n🇩🇪 Almanya\nGün planı hazırlanıyor"
        ),
        (
            "germany_day3",
            "almanya3",
            "📅 5 Ekim — 3. Gün\n\n🚌 Düsseldorf Hop-On Hop-Off\n🌅 Rheintreppe gün batımı • 🍺 Altbier akşamı"
        ),
        (
            "germany_day4",
            "almanya4",
            "📅 6 Ekim — 4. Gün\n\n🏙️ Dortmund şehir turu\n🟡⚫ BVB • 🏭 PHOENIX West • 🌊 PHOENIX See • 🍺 HÖVELS"
        ),
        (
            "germany_day5",
            "almanya5",
            "📅 7 Ekim — 5. Gün\n\n✈️ Almanya → Türkiye\nDÖNÜŞ GÜNÜ"
        ),
    ]

    for key, target, label in days:
        st.markdown('<div class="day-button">', unsafe_allow_html=True)
        if st.button(label, key=key, use_container_width=True):
            st.session_state.sayfa = target
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    geri_buton("ana", "← Ana Sayfaya Dön")


# =========================================================
# DETAY SAYFALARI
# =========================================================

elif st.session_state.sayfa == "hollanda1":
    geri_buton("hollanda", "← Hollanda Günlerine Dön")
    hollanda1()

elif st.session_state.sayfa == "hollanda2":
    geri_buton("hollanda", "← Hollanda Günlerine Dön")
    hollanda2()

elif st.session_state.sayfa == "hollanda3":
    geri_buton("hollanda", "← Hollanda Günlerine Dön")
    hollanda3()

elif st.session_state.sayfa == "hollanda4":
    geri_buton("hollanda", "← Hollanda Günlerine Dön")
    hollanda4()

elif st.session_state.sayfa == "hollanda5":
    geri_buton("hollanda", "← Hollanda Günlerine Dön")
    hollanda5()

elif st.session_state.sayfa == "almanya1":
    geri_buton("almanya", "← Almanya Günlerine Dön")
    almanya1()

elif st.session_state.sayfa == "almanya2":
    geri_buton("almanya", "← Almanya Günlerine Dön")
    almanya_placeholder(2, "4 Ekim", "Bu günün detayları henüz hazırlanıyor.")

elif st.session_state.sayfa == "almanya3":
    geri_buton("almanya", "← Almanya Günlerine Dön")
    almanya3()

elif st.session_state.sayfa == "almanya4":
    geri_buton("almanya", "← Almanya Günlerine Dön")
    almanya4()

elif st.session_state.sayfa == "almanya5":
    geri_buton("almanya", "← Almanya Günlerine Dön")
    almanya5()
