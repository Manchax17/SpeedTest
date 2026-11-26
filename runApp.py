#!/usr/bin/env python3
"""Lanzador multiplataforma de Network Analyzer.

Busca un entorno virtual local (`.venv` o `venv`) y arranca Streamlit con él.
Funciona igual en Linux, macOS y Windows.
"""

import os
import platform
import subprocess
import sys

VENV_CANDIDATES = (".venv", "venv", "speedtest")


def find_python():
    """Devuelve la ruta al intérprete del venv o, si no hay, el actual."""
    is_windows = platform.system() == "Windows"
    for venv in VENV_CANDIDATES:
        if is_windows:
            candidate = os.path.join(venv, "Scripts", "python.exe")
        else:
            candidate = os.path.join(venv, "bin", "python")
        if os.path.exists(candidate):
            return candidate
    return sys.executable


def has_streamlit(python):
    """Comprueba si el intérprete elegido tiene Streamlit instalado."""
    try:
        result = subprocess.run(
            [python, "-c", "import streamlit"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        return result.returncode == 0
    except OSError:
        return False


def run():
    python = find_python()

    if not has_streamlit(python):
        print("Error: no se encontró un entorno con Streamlit instalado.")
        print("Crea el entorno virtual e instala las dependencias con:")
        if platform.system() == "Windows":
            print("    setup.bat")
        else:
            print("    ./setup.sh")
        print("O manualmente:")
        print("    python3 -m venv .venv")
        print("    .venv/bin/pip install -r requirements.txt   # Linux/macOS")
        print("    .venv\\Scripts\\pip install -r requirements.txt   # Windows")
        return 1

    cmd = [
        python,
        "-m",
        "streamlit",
        "run",
        "app.py",
        "--server.headless=true",
        "--browser.gatherUsageStats=false",
    ]

    try:
        print(f"Iniciando Network Analyzer en {platform.system()}...")
        print("Abre http://localhost:8501 en tu navegador.")
        return subprocess.run(cmd).returncode
    except KeyboardInterrupt:
        print("\nAplicación cerrada.")
        return 0


if __name__ == "__main__":
    sys.exit(run())
