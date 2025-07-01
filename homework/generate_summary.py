import pandas as pd
import os
import matplotlib.pyplot as plt

# asegurar directorios
os.makedirs("files/output", exist_ok=True)
os.makedirs("files/plots", exist_ok=True)

# leer los archivos
drivers = pd.read_csv("files/input/drivers.csv")
timesheet = pd.read_csv("files/input/timesheet.csv")

# contar registros de actividad por driverId
summary = timesheet['driverId'].value_counts().reset_index()
summary.columns = ['driverId', 'record_count']

# asociar con el nombre
summary = summary.merge(drivers[['driverId', 'name']], on='driverId')

# ordenamos descendente
summary = summary.sort_values(by='record_count', ascending=False)

# guardar CSV
summary.to_csv("files/output/summary.csv", index=False)

# top 10 gráfico
top10 = summary.head(10)

plt.figure(figsize=(10,6))
plt.bar(top10['name'], top10['record_count'], color='skyblue')
plt.xticks(rotation=45, ha='right')
plt.title('Top 10 Drivers by Timesheet Records')
plt.ylabel('Number of Records')
plt.tight_layout()
plt.savefig("files/plots/top10_drivers.png")

print("✅ summary.csv y top10_drivers.png generados con éxito")
