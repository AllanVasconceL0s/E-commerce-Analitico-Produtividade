import pandas as pd
from sqlalchemy import create_engine
import numpy as np

# ⚠️ Configure suas credenciais do Banco de Dados
DB_USER = 'AllanVasconceL0s'
DB_PASSWORD = 'K@36kcs8p'
DB_HOST = 'localhost' # Ex: localhost
DB_NAME = 'relatorio_analitico_ecommerce'

# String de conexão (exemplo para MySQL + PyMySQL)
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

print("Conexão com o banco de dados configurada com sucesso.")