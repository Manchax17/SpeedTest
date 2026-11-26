# 🚀 Network Analyzer

Dashboard de diagnóstico de red hecho con Streamlit: latencia para juegos, ping a DNS y speedtest completo de bajada/subida.

Funciona en **Linux**, **macOS**, **Windows** y **Docker**.

## Requisitos

- Python 3.9 o superior (probado con 3.12 y 3.14)
- Conexión a Internet (el test de velocidad y la geolocalización lo necesitan)

## Instalación y ejecución en Linux / macOS

```bash
git clone https://github.com/Manchax17/SpeedTest.git
cd SpeedTest

# Crea .venv e instala dependencias
./setup.sh

# Arranca la app
python3 runApp.py
```

Si prefieres hacerlo a mano:

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python -m streamlit run app.py
```

Abre <http://localhost:8501> en el navegador.

> En algunos sistemas `python3 -m venv` requiere el paquete `python3-venv`.
> En Debian/Ubuntu: `sudo apt install python3-venv`.

## Instalación y ejecución en Windows

```bat
git clone https://github.com/Manchax17/SpeedTest.git
cd SpeedTest
setup.bat
python runApp.py
```

## Docker

```bash
docker build -t speedtest .
docker run --rm -p 8501:8501 speedtest
```

Luego abre <http://localhost:8501>.

## Estructura del proyecto

```
app.py             # Aplicación Streamlit
runApp.py          # Lanzador multiplataforma
setup.sh           # Instalación automática (Linux/macOS)
setup.bat          # Instalación automática (Windows)
requirements.txt   # Dependencias
Dockerfile         # Imagen de contenedor
```

## Notas

- El proyecto usa `speedtest-cli`, que mide contra servidores de Ookla.
- La latencia de juegos se estima con peticiones HTTP/TCP, no con los servidores oficiales de cada juego.
- `ip-api.com` se usa para mostrar ISP y ubicación aproximada.
