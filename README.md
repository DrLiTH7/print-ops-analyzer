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
