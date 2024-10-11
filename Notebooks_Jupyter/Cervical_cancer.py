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
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('kag_risk_factors_cervical_cancer.csv',sep  = ",",na_values = '?')
colunas_para_remover = ['STDs: Time since first diagnosis', 'STDs: Time since last diagnosis']  # Substitua pelos nomes das colunas que deseja remover
df = df.drop(columns=colunas_para_remover)

# %%
df['Dx:Cancer'].value_counts(normalize=True)
df['Dx:Cancer'].value_counts().plot(kind="bar", color=["salmon", "lightblue"]);

# %%
pd.crosstab(df["Dx:Cancer"], df["Smokes"])
# %%
pd.crosstab(df["Dx:Cancer"], df["Smokes"]).plot(kind="bar",
                                            figsize=(10,6),
                                            color=["green", "blue"]);
# %%
