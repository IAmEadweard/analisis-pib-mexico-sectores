import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar los datos
df = pd.read_csv('economia.csv')

# 2. Exploración rápida (siempre haz esto primero)
print(df.head())
print(df.shape)          # filas y columnas
print(df['Year'].min(), df['Year'].max())
print(df['Sector'].nunique())

# 3. Convertir a formato ancho: filas=año, columnas=sector
pivot = df.pivot(index='Year', columns='Sector', values='GDP')

# 4. Encontrar los 5 sectores con mayor PIB promedio
top5 = pivot.mean().sort_values(ascending=False).head(5).index.tolist()
print("Top 5 sectores:", top5)

# 5. Gráfico de líneas
pivot[top5].plot(figsize=(12, 6), title='PIB por sector (1994-2026)')
plt.ylabel('PIB')
plt.tight_layout()
plt.show()