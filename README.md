# Projektname: [Automatisierung des Bereitschaftsdienstplans für Einsatzfahrende mithilfe eines Vorhersagemodells]

## 1. Einführung
Der Berliner Rotkreuz-Rettungsdienst steht vor der Herausforderung, seinen Bereitschaftsdienst optimal zu gestalten. Bisher wurde eine konstante Anzahl von 90 Bereitschaftsfahrern pro Tag eingeplant, was zu ineffizienter Ressourcennutzung führen kann. Ziel des Projekts ist die Entwicklung eines Vorhersagemodells für den Berliner Rotkreuz-Rettungsdienst, das auf Tagesbasis die Anzahl der benötigten Einsatzfahrenden im Bereitschaftsdienst effizient abschätzt. Dieses Modell soll die bisherige statische Planung mit einer fixen Anzahl von Bereitschaftsfahrern durch eine dynamische, bedarfsgerechte Planung ersetzen.

## 2. Datenbeschreibung
Eine Beschreibung der verwendeten Daten, ihrer Herkunft und wie sie für das Modell verwendet werden.

## 3. Dokumentation

### 3.1 Projektstruktur
Eine Übersicht der Verzeichnisstruktur des Projekts:

project_folder/
│
├── data/
│   ├── raw_data/
│   │   └── sickness_table.csv
│   ├── processed_data/
│   │   └── preprocessed_data.csv
│
├── notebooks/
│   ├── 01_data_analysis.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_baseline_model.ipynb
│   └── 04_fortgeschrittenes_model.ipynb
│   └── 05_model_evaluation.ipynb
│   └── GUI.ipynb
│
├── models/
│   ├── baseline_model.pkl
│   └── precise_model.pkl
│
├── documentation/
│   ├── project_plan.md
│   ├── data_quality_report.md
│   ├── model_evaluation_report.md
│   └── presentation_slides.pdf
│
├── visualization/

# Präsentationsfolien

Die **Präsentationsfolien** enthalten eine Zusammenfassung des Projekts, einschließlich:

- Projektziele und Vorgehensweise
- Überblick über die Daten und die Datenqualität
- Modellentwicklung und Evaluierungsergebnisse
- Fazit und Empfehlungen

Die Datei kann [hier öffnen](./documentation/DLMDWME01_Fodor_32112241_Vorhersagemodell_für_den_DRK-Bereitschaftsdienst.pdf).

---

