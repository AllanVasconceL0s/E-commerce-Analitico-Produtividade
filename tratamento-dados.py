# Carregue a query SQL acima em um DataFrame pandas
sql_query = """
SELECT
    o.Order_ID, o.Order_Date, o.Subtotal, o.Discount AS Discount_Rate, o.Total,
    d.Service, d.P_Service AS Freight_Cost, d.D_Forecast, d.D_Date,
    p.Payment_Type, p.Purchase_Status,
    DATEDIFF(d.D_Date, d.D_Forecast) AS delivery_delay_days,
    DATEDIFF(d.D_Date, o.Order_Date) AS delivery_lead_time,
    CASE WHEN DATEDIFF(d.D_Date, d.D_Forecast) > 0 THEN 1 ELSE 0 END AS is_late,
    CASE WHEN p.Purchase_Status = 'Confirmado' THEN 1 ELSE 0 END AS is_confirmed,
    CASE WHEN o.Total > 0 THEN d.P_Service / o.Total ELSE 0 END AS freight_share,
    o.Discount * o.Subtotal AS discount_abs
FROM 
    orders o
JOIN deliveries d ON o.Order_ID = d.Order_ID
JOIN payments p ON o.Order_ID = p.Order_ID
WHERE 
    d.D_Date IS NOT NULL AND d.D_Forecast IS NOT NULL 
    AND o.Total > 0;
"""

df = pd.read_sql(sql_query, engine)

## Data Cleaning Avançado no Python
# 1. Converter colunas de data (já é feito em SQL, mas é boa prática checar)
date_cols = ['Order_Date', 'D_Forecast', 'D_Date']
for col in date_cols:
    df[col] = pd.to_datetime(df[col], errors='coerce')

# 2. Verificação de Chave Única (Deduplicação)
# Garanta que Order_ID seja único (se houver mais de uma linha por pedido, investigue/agregue)
if not df['Order_ID'].is_unique:
    print(f"⚠️ Alerta: {df.duplicated(subset='Order_ID', keep=False).sum()} linhas duplicadas por Order_ID.")
    # Exemplo: Agregação simples para manter a primeira ocorrência
    df = df.drop_duplicates(subset='Order_ID', keep='first') 

# 3. Trimming em Strings (Limpar espaços em Service ou Payment_Type)
string_cols = ['Service', 'Payment_Type', 'Purchase_Status']
for col in string_cols:
    if col in df.columns:
        df[col] = df[col].astype(str).str.strip()

print(f"Dados carregados e limpos. Total de pedidos para análise: {len(df)}")