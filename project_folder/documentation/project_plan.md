# Projektplan

## 1. Projektziele
Das Hauptziel dieses Projekts ist die Erstellung eines Vorhersagemodells, um Bereitschaftsdienst des Berliner Rotkreuz-Rettungsdienstes dynamisch vorherzusagen. Dabei wird der gesamte Machine-Learning-Prozess, von der Datenaufbereitung über die Modellentwicklung bis hin zur Evaluation, berücksichtigt.

## 2. Grundidee und Realisierung
### Phase 1: Datenanalyse und Feature Engineering
- **Schritte**: Im ersten Schritt (01_data_analysis) werden die gegebenen Daten gründlich analysiert. Hierbei betrachten wir die Verteilung und Korrelation der Variablen, um relevante Informationen zu gewinnen. Basierend auf dieser Analyse identifizieren wir potenziell wichtige Features und treffen erste Entscheidungen über geeignete Modelle.
Im zweiten Schritt (02_feature_engineering) erweitern wir die Datensätze um neue, zeitbasierte Features und definieren eine neue Zielvariable. Die Verteilung dieser neuen Features wird ebenfalls untersucht, um sicherzustellen, dass sie zur Modellierung beitragen. Die aufbereiteten Features werden in einer Datei gespeichert, um sie für die nachfolgenden Schritte nutzbar zu machen.

### Phase 2: Modellentwicklung 
- **Schritte**: In der nächsten Phase (03_baseline_model) teilen wir die gespeicherten Features in Trainings- und Testdaten auf und verwenden diese Aufteilung sowohl für das Baseline- als auch für das fortgeschrittene Modell. Das Baseline-Modell dient als Vergleichspunkt, indem es die Vorhersagen auf Basis des Medians der Zielvariable trifft.
Im darauffolgenden Schritt (04_fortgeschrittenes_modell) setzen wir einen Random Forest Regressor auf denselben Trainings- und Testdaten ein. Hierbei testen wir auch alternative Modelle wie ARIMA und SARIMA, die jedoch nicht die gewünschte Leistung erbringen. In dieser Phase wird auch die Korrelation zwischen den Features berücksichtigt, um sicherzustellen, dass wir nur informative Variablen verwenden.

### Phase 3: Modellvalidierung und Evaluation
- **Schritte**: Im letzten Schritt (05_model_evaluation) vergleichen wir die Leistung der beiden Modelle anhand von Metriken wie MAE, RMSE und R². Die Ergebnisse des fortgeschrittenen Modells werden visuell aufbereitet, um die Stärken und Schwächen der Vorhersagen zu verdeutlichen.

### Phase 4: Graphische Oberfläche (GUI)
- **Schritte**: Das fortgeschrittene Modell wird beispielhaft in einer graphischen Oberfläche eingebunden.

### Phase 5: Ergebnispräsentation 
- **Schritte**: Endergebnisse dokumentieren und Präsentationsfolien erstellen

---

