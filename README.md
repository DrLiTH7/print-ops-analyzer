# Print Ops Analyzer

Este projeto documenta uma solução de monitoramento de infraestrutura distribuída, desenvolvida para gerenciar o volume de impressão em múltiplas unidades geográficas do organização em foi implementada.

## 🛠️ Arquitetura da Solução

1. **Coleta nos endpoints**: Instalação em massa do PaperCut NG para geração de logs locais.
2. **Transporte automatizado**: Script em Python (distribuído via mass deployment) que identifica a máquina de origem (hostname), renomeia os arquivos e os transfere via VPN para um servidor central nos últimos 3 dias do mês.
3. **Central Intelligence**: Script centralizador que processa os múltiplos arquivos CSV usando **Pandas**, consolida os dados e gera relatórios analíticos em **HTML** para envio automático via e-mail.

## 🚀 Resultados Alcançados
- **Escalabilidade**: Solução desenhada para rodar em centenas de máquinas simultaneamente via distribuição em massa.
- **Integridade de Dados**: Tratamento de logs distribuídos e consolidação em um único Data Lake para análise.
- **Automação de Ponta a Ponta**: Eliminação de 100% da intervenção humana no processo de fechamento mensal de auditoria de impressão.
- **Visibilidade Total**: Identificação exata de quais unidades/cidades possuíam maior demanda.
- **Redução de Custos**: Dados consolidados permitiram a renegociação estratégica de contratos de locação de impressoras.
- **Zero Operação Manual**: Automação de ponta a ponta na coleta e processamento dos dados.

## 📂 Como usar
- `src/agent_collector.py`: Script que deve rodar nas estações de trabalho.
- `src/central_processor.py`: Script que roda no servidor central para gerar o relatório final.

___

# Print Ops Analyzer

This project documents a distributed infrastructure monitoring solution developed to manage print volume across multiple geographic locations within the organization where it was implemented.

## 🛠️ Solution Architecture

1. **Endpoint collection**: Mass installation of PaperCut NG for local log generation.
2. **Automated transport**: Python script (distributed via mass deployment) that identifies the source machine (hostname), renames the files, and transfers them via VPN to a central server on the last 3 days of the month.
3. **Central Intelligence**: Centralizing script that processes multiple CSV files using **Pandas**, consolidates the data, and generates analytical reports in **HTML** for automatic sending via email.

## 🚀 Results Achieved

- **Scalability**: Solution designed to run on hundreds of machines simultaneously via mass distribution.
- **Data Integrity**: Processing of distributed logs and consolidation into a single Data Lake for analysis.
- **End-to-End Automation**: Elimination of 100% of human intervention in the monthly print audit closing process.
- **Total Visibility**: Accurate identification of which units/cities had the highest demand.
- **Cost Reduction**: Consolidated data enabled strategic renegotiation of printer lease agreements.
- **Zero Manual Operation**: End-to-end automation in data collection and processing.

## 📂 How to use

- `src/agent_collector.py`: Script that should run on workstations.
- `src/central_processor.py`: Script that runs on the central server to generate the final report.
