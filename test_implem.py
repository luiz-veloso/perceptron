import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)

df['target'] = iris.target

# Isso remove automaticamente todas as instâncias da classe 2 (Virginica)

df_final = df[df['target'] != 2].copy()

# Visualizando o resultado no console

print(f"Instâncias antes do filtro: {len(df)}")
print(f"Instâncias depois do filtro: {len(df_final)}\n")
print("Amostra dos dados processados:")
print(df_final.head())