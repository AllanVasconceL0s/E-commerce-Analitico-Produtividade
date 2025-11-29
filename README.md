# E-commerce-Analitico-Produtividade
O objetivo central deste projeto é fornecer uma análise robusta e estatisticamente fundamentada do desempenho do e-commerce brasileiro para a Direção, transformando dados brutos em descobertas acionáveis ​​que guiem decisões de negócio.


🇧🇷 📊 Análise de Desempenho do E-commerce Brasileiro
🎯 Objetivo do Projeto
Este projeto visa fornecer respostas confiáveis ​​e estatisticamente fundamentadas sobre o desempenho de um e-commerce brasileiro. O objetivo principal é produzir um Relatório Analítico Acionável que demonstre o estado da receita, margens, logística e comportamento do cliente, auxiliando a Diretoria na tomada de decisões estratégicas.

A análise foca em garantir a qualidade dos dados e o uso de inferência estatística (Intervalos de Confiança) para validar os resultados.

🛠️ Pilha Tecnológica
Componente	Ferramenta	Uso
Banco de Dados	MySQL	Armazenamento e execução de JOINscomplexos para consolidação dos dados.
Linguagem	Python 3.x	Implementação de todo o pipeline de ETL e Análise.
Manipular/Análise	Pandas,NumPy	Limpeza, Engenharia de Recursos e cálculos estatísticos.
Estatística	SciPy	Cálculo de Intervalos de Confiança (ICs) para médias e proporções.
Visualização	Matplotlib,Seaborn	Geração de gráficos para EDA (histogramas, boxplots, heatmaps).
BD	SQLAlchemy,mysql-connector-python	Interface entre Python e MySQL.

Exportar para Planilhas

🔑 KPIs (Indicadores-chave de desempenho) analisados
Os seguintes KPIs foram calculados e analisados, incluindo a criação de variáveis ​​derivadas ( Feature Engineering ):

KPI	/ Fórmula	Status
Bilheteria	Total por pedido(após tratamento de outliers)	Calculado
Taxa de Atraso	é_tarde=1 ( Data_D>D_Previsão )	Calculado
Prazo de Entrega	prazo de entrega=( Data_D−Data_do_pedido )	Calculado
Taxa de entrega	compartilhamento de frete=P_Serviço / Total	Calculado
Conversão de Pagto.	Taxa de Confirmado vs. Cancelado por m 
e
ˊ
 pendência	Calculado
Elasticidade	Mix de Categoria/Subcategoria vs. Desconto	Analisado

Exportar para Planilhas

🚀 Pipeline de Análise (Passo a Passo)
1. Conexão e Consolidação de Dados
O script Python( notebook.ipynb) se conecta ao MySQL via SQLAlchemy.

Uma consulta SQL única e eficiente (disponível em sql/query_full_join.sql) é utilizada para realizar LEFT JOINsentre as tabelas de pedidos, clientes, produtos e pagamentos, consolidando todos os dados em um único DataFrame ( df).

2. Limpeza e pré-processamento de dados
Tipagem: Conversão de colunas de dados ( order_date,data_d,previsão_d) e valores ( total, subtotal,serviço p) para os tipos corretos.

Tratamento de NAs: Valores nulos de desconto e frete preenchidos com 0 .

Outliers: Aplicação da regra IQR (3º trimestre+1,5×IQR) nãoTotal(Receita). Outliers foram limitados ( capped ) para não distorcer oBilhete M 
e
ˊ
 dioe as análises subsequentes.


Shutterstock
3. Engenharia de Recursos
Criação das colunas-chave relacionadas acima ( ticket_medio_capped,é_tarde,compartilhamento de frete, etc.) para facilitar a análise de KPIs.

4. Análise Exploratória (EDA)
Cálculo de medidas de tendência central (média, mediana) e dispersão (desvio padrão).

Visualização de distribuições ( Ticket Médio,Tempo de espera) via Histogramas e Boxplots .

Identificação de relacionamentos via Heatmap de Correlação entre variáveis ​​financeiras e logísticas.

Análise de Sazonalidade por mês e desempenho por Região/UF .

5. Estatística de Inferência
Cálculo de Intervalos de Confiança de 95% (ICs) para:

Média doBilhete M 
e
ˊ
 dio(usando a Distribuição T).

Proporção de Atraso (é_tarde) (usando pontuação Z).

Proporção de cancelamento por método de pagamento.

Verificação de Suposições: Confirmação da validade do Teorema do Limite Central (TLC) devido ao tamanho da amostra (n > 30), mesmo com distribuição não-normal doBilhete M 
e
ˊ
 dio.

📁 Estrutura do Repositório
.
├── code/
│   ├── notebook.ipynb         # Código Python completo com ETL, EDA e Inferência
│   └── pipeline_script.py     # Script Python executável (opcional)
├── reports/
│   ├── Relatorio_Analitico.pdf  # Versão final do relatório em PDF
│   └── Relatorio_Analitico.md   # Conteúdo do relatório em Markdown
└── sql/
    └── query_full_join.sql    # Consulta SQL utilizada para carregar os dados
└── README.md                  # Este arquivo
🔎 Principais Insights
Risco Logístico: A taxa de atraso médio é de 19,0% (IC 95%∈[ 18,5% ;19,5% ]). A diferença de desempenho entre o serviço Standard e Same-Day exige uma reavaliação da precificação/subsídio logístico.

Ineficiência do Desconto: A aparência quase nula entre desconto eBilhete M 
e
ˊ
 diosugere que os descontos são aplicados de forma ampla, sem resultados positivos da compra, corroendo a margem de lucro.

Conversão de Pagamento: O PIX demonstra a melhor conversão ( 98,5% ), enquanto o Boleto é o principal ponto de perda de conversão ( 75,2% ).

📧 Contato
Para dúvidas ou sugestões, por favor, abra uma Issue neste repositório ou contate [AllanVasconceL0s].

🎯Principais Objetivos do Trabalho

1. 1. Qualidade e Preparação de Dados (Integridade de Dados) 🛡️Garantir que os dados utilizados para a análise sejam seguros, limpos e estruturados.
2. Validação da Fonte: Carregar, juntar e consolidar dados de múltiplas tabelas (pedidos, clientes, pagamentos, produtos) via SQL.
3. Tratamento de Missing Values ​​(NA): Preencher ou remover dados faltantes de forma justificada (ex: preenchimento Discounte FreightNAs com zero).Outliers e Tipagem: identificar e mitigar o impacto de outliers (ex: utilizar a regra IQR no$\text{Ticket Médio}$) e garantir a digitação correta de dados e valores numéricos.
4.
5. 2. Criação de KPIs e Análise Descritiva (EDA) 📈Transformar dados transacionais em análises de negócios relevantes e explorar suas distribuições e relações.Engenharia de Recursos: Calcular KPIs chave como$\text{Ticket Médio}$,$\text{Take-rate de frete}$($\text{freight\_share}$), Prazo de Entrega ($\text{delivery\_lead\_time}$) e Atraso ($\text{is\_late}$).
   3. Distribuição e Dispersão: Analisar medidas de tendência central (média, mediana) e dispersão (desvio padrão) das métricas financeiras e logísticas.Relacionamentos: identificar correlações entre variáveis ​​(ex: desconto vs. ticket, frete vs. atraso) para entender dinâmicas de preço e logística.Sazonalidade e Mix: Mapear tendências de receita e demanda por mês e analisar o mix de produtos por$\text{Category/Subcategory}$.
   4.
   5. 3. Inferência Estatística e Confiabilidade 🔬Utilizar ferramentas estatísticas para validar os achados descritivos e quantificar a incerteza.
      4. Intervalos de Confiança (ICs 95%): Calcular ICs para análises críticas (Ticket Médio, Proporção de Atraso e Proporção de Cancelamento) para fornecer um intervalo de valores prováveis ​​da população, em vez de apenas uma estimativa pontual.
      5. Verificação de Suposições: Assegurar que os testes e cálculos são estatisticamente válidos (ex: validando o uso do Teorema do Limite Central devido ao tamanho da amostra).
      6.
      7. 4. Geração de Insights Acionáveis ​​(Business Value) 💡Concluir o trabalho com recomendações práticas e diretas para a Direção.Diagnóstico: Apresentar os sinais de alerta (ex: alta taxa de cancelamento em um método de pagamento, baixa oferta de desconto) e as oportunidades (ex: otimização logística em regiões específicas).
         5. Relatório e Reprodutibilidade: Entregar um Relatório Analítico conciso e bem estruturado (PDF/MD), acompanhado do código ( notebooke SQL), garantindo transparência e reprodutibilidade da análise.
