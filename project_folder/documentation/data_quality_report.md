# Datenqualitätsbericht

## 1. Übersicht der Daten
- Die Rohdaten umfassen 1152 Datensätze und 7 Features, die sowohl numerische als auch kategorische Daten darstellen. Die relevanten Features sind:

date: Datum (kategorisch)
n_sick: Anzahl der kranken Personen (numerisch)
calls: Anzahl der Anrufe (numerisch)
n_duty: Anzahl der im Dienst befindlichen Personen (numerisch)
n_sby: Anzahl der Bereitschaftspersonen (numerisch)
sby_need: Anzahl der benötigten Bereitschaftspersonen (numerisch)
dafted: Anzahl der Entwürfe (numerisch)

- Zusätzlich wurden folgende Variablen zur Analyse erstellt:

year: Jahr (numerisch)
month: Monat (numerisch)
adjusted_need: Angepasster Bedarf (numerisch), berechnet durch die Funktion calculate_adjusted_need(sby_need)
day_of_week: Wochentag (numerisch)
day_of_week_sin: Sinus-Koordinate des Wochentags (numerisch)
day_of_week_cos: Kosinus-Koordinate des Wochentags (numerisch)
avg_calls_last_30_days: Durchschnittliche Anrufe der letzten 30 Tage (numerisch)
avg_sick_last_30_days: Durchschnittliche Anzahl kranker Personen der letzten 30 Tage (numerisch)
season_Spring, season_Summer, season_Autumn, season_Winter: Saison-Kategorisierungen (kategorisch)
calls_per_duty: Anrufe pro im Dienst befindlicher Person (numerisch)

- Die ausgewählten Features für die Modellierung sind:

Features: ['calls_per_duty', 'month_sin', 'month_cos', 'year', 'day_of_week']
Zielvariable: adjusted_need

## 2. Fehlende Daten
### Analyse der fehlenden Werte:
- Keine fehlenden Daten in de Features

## 3. Ausreißer
- calls und n_sick haben einige Ausreißer, sie scheinen aber nicht extrem zu sein
- adjusted_need hat hohe Ausreißer, diese werden mittels Z-Scores behandelt und durch den Median ersetzt

## 4. Datenverteilung
- Die Datenverteilung wurde für numerische Features überprüft. Hierbei zeigte sich:

Numerische Daten:
n_sick: Mittelwert: 68.81 und Standardabweichung: 14.29.
calls: Positiv schief, nahezu normalverteilt mit einem Mittelwert von 7919.53 und einer Standardabweichung von 1290.06.
n_duty: Mittelwert 1820.57 und Standardabweichung 80.09.
n_sby: Konstante Werte, immer 90.
sby_need: Mittelwert: 34.72 und Standardabweichung: 79.69.
dafted: Positiv schief, mit einem Mittelwert von 16.34 und einer Standardabweichung von 53.39.
adjusted_need: Mittelwert: 101.05, Standardabweichung: 57.56, Minimum: 2, Maximum: 555



