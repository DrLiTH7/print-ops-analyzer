import pandas as pd
import glob
import os

def generate_monthly_report():
    input_folder = "Z:/Central_Reports/Incoming_Logs/"
    all_files = glob.glob(os.path.join(input_folder, "*.csv"))
    
    li = []
    # Lê todos os relatórios de todas as máquinas/cidades
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        # Extrai o nome da máquina do nome do arquivo
        df['Machine_ID'] = os.path.basename(filename).split('_')[2]
        li.append(df)

    # Consolida tudo em um único DataFrame
    frame = pd.concat(li, axis=0, ignore_index=True)
    
    # Gera análise por máquina ou cidade
    summary = frame.groupby('Machine_ID')['Pages'].sum().reset_index()
    
    # Exporta para HTML (o relatório que ia por e-mail)
    html_content = summary.to_html(classes='table table-striped')
    with open("relatorio_mensal.html", "w") as f:
        f.write(f"<html><body><h1>Relatório Consolidado de Impressão</h1>{html_content}</body></html>")
    
    print("Relatório HTML gerado com sucesso.")

if __name__ == "__main__":
    generate_monthly_report()