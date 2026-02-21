import streamlit as st
import speedtest
import platform
import requests
import time
import socket
from bs4 import BeautifulSoup

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Network Analyzer Master", layout="wide", page_icon="🚀")

# --- ESTILO "TECH DASHBOARD" (Inspirado en tu referencia) ---
st.markdown("""
    <style>
    header[data-testid="stHeader"] {
        background: rgba(0,0,0,0) !important;
        background-color: transparent !important;
    }

    .stApp {
        background-color: #0a0e14;
    }
    .main .block-container {
        padding-top: 2rem !important;
    }
            
    <style>
    /* Fondo General Azul Medianoche Profundo */
    .stApp {
        background-color: #0a0e14;
    }
    
    .main {
        background-color: #0a0e14;
    }

    /* Tarjetas de Velocidad (Grandes y Azules) */
    .box-speed {
        background: #3b82f6;
        border-radius: 20px;
        padding: 40px 20px;
        text-align: center;
        box-shadow: 0 10px 25px rgba(0,0,0,0.3);
        margin: 10px;
    }

    /* Textos dentro de tarjetas de velocidad */
    .speed-label {
        color: #e2e8f0;
        font-size: 16px;
        font-weight: 600;
        text-transform: uppercase;
        margin-bottom: 5px;
    }
    .speed-value {
        color: #ffffff;
        font-size: 56px;
        font-weight: 800;
    }
    .speed-unit {
        color: #bfdbfe;
        font-size: 18px;
        font-weight: 400;
    }

    /* Textos Generales */
    h1, h2, h3, p, span, label {
        color: #ffffff !important;
        font-family: 'Inter', sans-serif;
    }
    
    /* Resaltado Cian para valores de Ping */
    .ping-value {
        color: #00f2ff !important;
        font-size: 28px;
        font-weight: 700;
    }

    /* Estilo del Botón (Vibrante) */
    .stButton>button {
        background-color: #0066ff;
        color: white;
        border: none;
        border-radius: 12px;
        font-weight: bold;
        padding: 12px 24px;
        transition: 0.3s;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #3b82f6;
        box-shadow: 0 0 15px rgba(59, 130, 246, 0.5);
    }

    /* Línea Divisoria Sutil */
    hr {
        border-color: rgba(255, 255, 255, 0.1) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- FUNCIONES DE RED ---

def get_http_ping(url):
    try:
        start = time.perf_counter()
        requests.head(url, timeout=2.0)
        return int((time.perf_counter() - start) * 1000)
    except:
        return None

def get_socket_ping(host, port=80):
    try:
        start = time.perf_counter()
        s = socket.create_connection((host, port), timeout=1.5)
        latency = int((time.perf_counter() - start) * 1000)
        s.close()
        return latency
    except:
        return None

def get_google_logo(isp_name):
    try:
        clean_isp = isp_name.split('SAS')[0].strip() if 'SAS' in isp_name else isp_name
        query = f"{clean_isp} internet logo"
        url = f"https://www.google.com/search?q={query}&tbm=isch"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        images = soup.find_all("img")
        for img in images[1:]:
            src = img.get("src")
            if src and src.startswith("http"): return src
    except: pass
    return "https://cdn-icons-png.flaticon.com/512/168/168541.png"

# --- LÓGICA DE INICIO ---
try:
    net_data = requests.get("http://ip-api.com/json/", timeout=5).json()
    isp = net_data.get('isp', 'Legon Telecomunicaciones SAS')
    city = net_data.get('city', 'Arauca')
    country = net_data.get('country', 'Colombia')
    if 'isp_logo' not in st.session_state:
        st.session_state.isp_logo = get_google_logo(isp)
    isp_logo = st.session_state.isp_logo
except:
    isp, city, country, isp_logo = "Desconocido", "---", "---", None

# --- UI SUPERIOR (HEADER ESTILO REFERENCIA) ---
head_col1, head_col2 = st.columns([1, 4])
with head_col1:
    # Contenedor de Logos estilo circular/moderno
    st.markdown(f"""
        <div style="display: flex; gap: 15px; align-items: center; margin-bottom: 20px;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/a/af/Tux.png" width="60" style="border-radius: 50%; border: 2px solid #333;">
            <img src="{isp_logo}" width="65" style="border-radius: 50%; border: 2px solid #333; background: white; padding: 5px;">
        </div>
    """, unsafe_allow_html=True)
with head_col2:
    st.markdown(f"""
        <h2 style="margin-bottom: 0; color: #00f2ff !important; display: flex; align-items: center; gap: 10px;">
            📡 Network Analyzer
        </h2>
        <p style="margin-top: 0; opacity: 0.9; font-size: 1.1rem;">
            Conectado a: <b>{isp}</b><br>
            <span style="font-size: 0.9rem; color: #ff4b4b !important;">📍 Ubicación: {city}, {country}</span>
        </p>
    """, unsafe_allow_html=True)

st.divider()

# --- GAMING LATENCY SECTION ---
st.markdown("### 🎮 Gaming Latency (Ping)")
g1, g2, g3, g4 = st.columns(4)

with st.spinner("Sincronizando..."):
    # Riot mejorado
    best_ms, best_reg = 999, "N/A"
    nodes = {"LAN": "https://lan.leagueoflegends.com", "BR": "https://br.leagueoflegends.com"}
    for reg, url in nodes.items():
        ms = get_http_ping(url)
        if ms and ms < best_ms: best_ms, best_reg = ms, reg
    
    g1.markdown(f"LoL / Valorant<br><span class='ping-value'>{best_ms if best_ms < 999 else 'N/A'} ms</span>", unsafe_allow_html=True)
    
    fn_ms = get_socket_ping('dynamodb.us-east-1.amazonaws.com')
    g2.markdown(f"Fortnite<br><span class='ping-value'>{fn_ms if fn_ms else 'N/A'} ms</span>", unsafe_allow_html=True)
    
    mc_ms = get_socket_ping('mc.hypixel.net', 25565)
    g3.markdown(f"Minecraft<br><span class='ping-value'>{mc_ms if mc_ms else 'N/A'} ms</span>", unsafe_allow_html=True)
    
    dns_ms = get_socket_ping('8.8.8.8', 53)
    g4.markdown(f"Google DNS<br><span class='ping-value'>{dns_ms if dns_ms else 'N/A'} ms</span>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- SPEEDTEST SECTION ---
col_btn, col_res1, col_res2 = st.columns([1, 1.5, 1.5])

with col_btn:
    st.write("<br>"*2, unsafe_allow_html=True) # Espaciado
    do_speedtest = st.button("🚀 Iniciar Speedtest Completo")

if do_speedtest:
    with st.spinner("Midiendo ráfagas de red..."):
        try:
            s = speedtest.Speedtest(secure=True)
            s.get_best_server()
            d, u = s.download()/1e6, s.upload()/1e6
            
            col_res1.markdown(f"""
                <div class="box-speed">
                    <p class="speed-label">BAJADA Real</p>
                    <p class="speed-value">{int(d)}</p>
                    <p class="speed-unit">Mbps</p>
                </div>
            """, unsafe_allow_html=True)
            
            col_res2.markdown(f"""
                <div class="box-speed">
                    <p class="speed-label">SUBIDA Real</p>
                    <p class="speed-value">{int(u)}</p>
                    <p class="speed-unit">Mbps</p>
                </div>
            """, unsafe_allow_html=True)
        except Exception as e:
            st.error("No se pudo completar el Speedtest. Reintenta.")