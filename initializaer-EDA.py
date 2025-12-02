import matplotlib.pyplot as plt
import seaborn as sns

# Análise Descritiva Rápida
print("\nAnálise Descritiva de Variáveis Monetárias e Logísticas:")
print(df[['Total', 'Freight_Cost', 'delivery_lead_time']].describe())

# EDA Gráfico: Distribuição do Ticket Médio
plt.figure(figsize=(10, 6))
sns.histplot(df['Total'], bins=50, kde=True)
plt.title('Distribuição do Ticket Médio (Total por Pedido)')
plt.xlabel('Total do Pedido (R$)')
plt.ylabel('Frequência')
plt.show() #