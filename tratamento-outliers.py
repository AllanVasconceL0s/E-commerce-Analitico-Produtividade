# 1. Calcular Q1 e Q3
Q1 = df['Total'].quantile(0.25)
Q3 = df['Total'].quantile(0.75)
IQR = Q3 - Q1

# 2. Definir Limite Superior e Inferior
limite_superior = Q3 + 1.5 * IQR
limite_inferior = Q1 - 1.5 * IQR

print(f"IQR para o Ticket Médio: R$ {IQR:.2f}")
print(f"Limite Superior (Outliers acima): R$ {limite_superior:.2f}")

# 3. Remover Outliers (Exemplo de Remoção para Análise de Média)
df_clean_outliers = df[(df['Total'] <= limite_superior) & (df['Total'] >= limite_inferior)].copy()

print(f"\nPedidos removidos: {len(df) - len(df_clean_outliers)}")
print(f"Ticket Médio ANTES do tratamento: R$ {df['Total'].mean():.2f}")
print(f"Ticket Médio DEPOIS do tratamento: R$ {df_clean_outliers['Total'].mean():.2f}")