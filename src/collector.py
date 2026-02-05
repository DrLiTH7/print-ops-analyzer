import os
import shutil
import socket
from datetime import datetime

# Locais fictícios
LOCAL_PAPERCUT_PATH = "C:/Program Files (x86)/PaperCut Print Logger/logs/csv/monthly/"
VPN_SERVER_PATH = "Z:/Central_Reports/Incoming_Logs/"

def collect_and_send():
    hostname = socket.gethostname()
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    source_file = os.path.join(LOCAL_PAPERCUT_PATH, "montlhly_report.csv")
    
    if os.path.exists(source_file):
        # Renomeia com o Hostname para identificar o relatório por localidade
        target_name = f"print_log_{hostname}_{current_date}.csv"
        destination = os.path.join(VPN_SERVER_PATH, target_name)
        
        # Envio para local mapeado por VPN
        shutil.copy(source_file, destination)
        print(f"Log enviado com sucesso: {target_name}")
    else:
        print("Arquivo de log local não encontrado.")

if __name__ == "__main__":
    collect_and_send()