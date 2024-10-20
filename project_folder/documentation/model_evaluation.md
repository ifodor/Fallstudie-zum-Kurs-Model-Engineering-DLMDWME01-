# Modellbewertungsbericht

## 1. Eingesetzte Modelle
- **Baseline-Modell**: DummyRegressor, der den Median der Zielvariable für alle Datenpunkte vorhersagt. Dieses Modell dient als Vergleichspunkt für die Leistungsbewertung fortgeschrittener Modelle.
- **Fortgeschrittenes Modell**: RandomForestRegressor mit optimierten Hyperparametern mittels RandomizedSearchCV.
- Weitere Modelle, darunter ARIMA, SARIMA, GradientBoosting und GridSearch, wurden getestet, jedoch aufgrund ihrer schlechteren Leistung verworfen. Aus Gründen des vorgegebenen Umfangs der Arbeit wird hier nicht näher darauf eingegangen.

## 2. Bewertungsmethoden
Folgende Metriken wurden herangezogen:
- **Root Mean Squared Error (RMSE)**: 
Baseline MAE: 11.28 (Durchschnittliche absolute Abweichung von etwa 11 Einheiten).
Baseline RMSE: 31.06 (Höhere Sensitivität gegenüber großen Fehlern).
R²: -0.01 (Keine erklärbare Varianz).
- **Mean Absolute Error (MAE)**: 
MAE: 4.47 (Durchschnittliche Abweichung von etwa 4 Einsatzfahrenden).
RMSE: 14.19 (Hinweis auf einige größere Abweichungen).
R²: 0.90 (Sehr gute Anpassung an die Daten).
Benutzerdefinierte Verlustfunktion: 1862.52 (bestraft Untervorhersagen dreimal stärker als Übervorhersagen).

Zusätzlich dazu wurde das fortgeschrittene Modell mittels 5-facher Cross-Validation bewertet. 

Die Ergebnisse zeigen eine signifikante Verbesserung des fortgeschrittenen Modells gegenüber der Baseline. 

## 3. Visualisierung der Ergebnisse
Die Visualisierung konzentriert sich ausschließlich auf das fortgeschrittene Modell, da das Baseline-Modell lediglich den Median vorhersagt und daher keine aufschlussreiche Visualisierung bietet.

Für das fortgeschrittene Modell wurden die Vorhersagefehler und die tatsächlichen gegen die vorhergesagten Werte visualisiert:

Fehlerverteilung: Die Verteilung der Vorhersagefehler wurde mit einem Histogramm und einer Dichtekurve dargestellt, um die Fehlerverteilung des Modells zu analysieren.

![Verteilung der Vorhersagefehler des fortgeschrittenen Modells](..\visualizations\Verteilung der Vorhersagefehler des des fortgeschrittenen Modells.png)

Scatterplot der Vorhersagen: Ein Scatterplot zeigt die tatsächlichen Werte im Vergleich zu den vorhergesagten Werten. Die rote gestrichelte Linie repräsentiert die ideale Vorhersage, in der die Vorhersagen den tatsächlichen Werten entsprechen.

![Tatsächliche vs. vorhergesagte Werte des fortgeschrittenen Modells](..\visualizations\Tatsächliche vs. vorhergesagte Werte des fortgeschrittenen Modells.png)


