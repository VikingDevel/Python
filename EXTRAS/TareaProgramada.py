import time
from datetime import datetime

def tarea():
    print(f"Tarea ejecutada a las: {datetime.now().strftime('%H:%M:%S')}")

# Configuración de la hora de ejecución.
hora_programada = "14:30"

print(f"Esperando hasta las {hora_programada}...")

while True:
    now = datetime.now().strftime("%H:%M")
    if now == hora_programada:
        tarea()
        # Se pone una pausa de 60 segundos para evitar que la tarea se ejecute múltiples veces en el mismo minuto
        time.sleep(60)
    time.sleep(10) # comprueba cada 10 segundos si es la hora programada.
