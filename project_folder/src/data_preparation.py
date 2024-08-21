import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Daten einlesen
data = pd.read_csv(r"C:\Users\Gast\Documents\Downloads\IU\Fallstudie_Modell_Engineering\sickness_table.csv")

# Erste fünf Zeilen der Daten anzeigen
print(data.head())

# Grundlegende Informationen zu den Daten anzeigen (Anzahl der Spalten und Zeilen sowie Datentyp)
print(data.info(), '\n')

# Statistische Zusammenfassung der Daten anzeigen (count, min, max, std, 25%, 50%, 75%)
print(data.describe(), '\n')

# Anzahl fehlender Werte in jeder Spalte anzeigen
print(data.isnull().sum(), '\n')

# Datum in Datumsformat konvertieren und setze sie als Index
data['date'] = pd.to_datetime(data['date'])
#data.set_index('date', inplace=True)

# Unnötige Spalte entfernen
data = data.drop(columns=['Unnamed: 0', 'n_sby'])

# Histogramme für numerische Variablen anzeigen
data.hist(bins=20, figsize=(14, 10))
plt.show()

# Korrelationen zwischen Variablen berechnen und anzeigen
correlation_matrix = data.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Korrelationsmatrix')
plt.show()

# Korrelationsmatrix als Tabelle darstellen
print(correlation_matrix.to_markdown(), '\n')

###### Saisonale Muster ######
# Durchschnittliche Anzahl der benötigten Bereitschaftseinsatzfahrenden nach Monaten berechnen
monthly_data = data.groupby(data['date'].dt.month)['sby_need'].mean()

# Visualisierung
plt.figure(figsize=(10, 6))
monthly_data.plot(kind='bar', color='skyblue')
plt.xlabel('Monat')
plt.ylabel('Durchschnittliche Anzahl der benötigten Bereitschaftseinsatzfahrenden')
plt.title('Saisonale Muster der benötigten Bereitschaftseinsatzfahrenden nach Monaten')
plt.tight_layout()
plt.show()

# Durchschnittliche Anzahl der benötigten Bereitschaftseinsatzfahrenden nach Wochentagen berechnen
weekly_data = data.groupby(data['date'].dt.dayofweek)['sby_need'].mean()

# Visualisierung
plt.figure(figsize=(10, 6))
weekly_data.plot(kind='bar', color='lightgreen')
plt.xlabel('Wochentag')
plt.ylabel('Durchschnittliche Anzahl der benötigten Bereitschaftseinsatzfahrenden')
plt.title('Saisonale Muster der benötigten Bereitschaftseinsatzfahrenden nach Wochentagen')
plt.xticks(ticks=range(7), labels=['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag'])
plt.tight_layout()
plt.show()