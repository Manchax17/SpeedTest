#!/usr/bin/env bash
# Prepara el entorno virtual e instala las dependencias en Linux/macOS.
set -euo pipefail

cd "$(dirname "$0")"

PYTHON="${PYTHON:-python3}"

if ! command -v "$PYTHON" >/dev/null 2>&1; then
    echo "Error: no se encontró '$PYTHON'. Instala Python 3.9 o superior." >&2
    exit 1
fi

if [ ! -d ".venv" ]; then
    echo "Creando entorno virtual en .venv..."
    "$PYTHON" -m venv .venv
fi

echo "Actualizando pip e instalando dependencias..."
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.txt

echo
echo "Listo. Inicia la aplicación con:"
echo "    python3 runApp.py"
echo "o:"
echo "    .venv/bin/python -m streamlit run app.py"
