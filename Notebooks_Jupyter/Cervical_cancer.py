#%%
import seaborn as sb
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
#%%
# Load the data
df = pd.read_csv('kag_risk_factors_cervical_cancer.csv',sep = ",",na_values = '?')

# %%
# Excluir colunas específicas
# %%
correlation_matrix = df.corr()

# Configurar a figura e o eixo
plt.figure(figsize=(12, 8))

# Criar o mapa de calor
sb.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)

# Exibir o gráfico
plt.show()


# %%
