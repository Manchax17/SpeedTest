import os
import subprocess
import sys
import platform

def run():
    # Detectar la ruta del ejecutable de python dentro del venv
    if platform.system() == "Windows":
        python_venv = os.path.join(".venv", "Scripts", "python.exe")
    else:
        python_venv = os.path.join(".venv", "bin", "python")

    # Verificar si el venv existe
    if not os.path.exists(python_venv):
        print("Error: No se encontró la carpeta '.venv'.")
        print("Asegúrate de que el entorno virtual esté en la raíz del proyecto.")
        return

    # Comando para ejecutar streamlit usando el python del entorno virtual
    cmd = [python_venv, "-m", "streamlit", "run", "app.py"]
    
    try:
        print(f"Iniciando Network Analyzer Master en {platform.system()}...")
        subprocess.run(cmd)
    except KeyboardInterrupt:
        print("\nAplicación cerrada.")

if __name__ == "__main__":
    run()