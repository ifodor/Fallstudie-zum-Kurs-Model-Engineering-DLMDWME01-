import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib

# Daten einlesen
data = pd.read_csv(r"C:\Users\Gast\Documents\Downloads\IU\Fallstudie_Modell_Engineering\project_folder\data\processed_data\preprocessed_data.csv")

# Unnötige Spalte entfernen
#data = data.drop(columns=['n_sick','calls','n_duty','n_sby','sick_rate','year'])

# Feature- und Zielvariablen festlegen
features = [col for col in data.columns if col != 'sby_need']
print(data.head())
X = data[features]
y = data['sby_need']

# Aufteilen der Daten in Trainings- und Testset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Baseline-Modell
baseline_model = DummyRegressor(strategy='mean')
baseline_model.fit(X_train, y_train)
baseline_predictions = baseline_model.predict(X_test)

# Fehlermaße berechnen
mae_baseline = mean_absolute_error(y_test, baseline_predictions)
rmse_baseline = mean_squared_error(y_test, baseline_predictions, squared=False)

print(f'Baseline MAE: {mae_baseline:.2f}')
print(f'Baseline RMSE: {rmse_baseline:.2f}')

# Speichern des Baseline-Modells
joblib.dump(baseline_model, r"C:\Users\Gast\Documents\Downloads\IU\Fallstudie_Modell_Engineering\project_folder\models\baseline_model.pkl")


# Fortgeschrittenes Modell: RandomForestRegressor
precise_model = RandomForestRegressor(random_state=42)
precise_model.fit(X_train, y_train)
precise_predictions = precise_model.predict(X_test)

# Fehlermaße berechnen
mae_precise = mean_absolute_error(y_test, precise_predictions)
rmse_precise = mean_squared_error(y_test, precise_predictions, squared=False)

print(f'Precise Model MAE: {mae_precise:.2f}')
print(f'Precise Model RMSE: {rmse_precise:.2f}')

joblib.dump(precise_model, r"C:\Users\Gast\Documents\Downloads\IU\Fallstudie_Modell_Engineering\project_folder\models\precise_model.pkl")

# Feature-Importances anzeigen
importances = precise_model.feature_importances_
feature_names = X.columns

feature_importances = pd.DataFrame({
    'feature': feature_names,
    'importance': importances
}).sort_values(by='importance', ascending=False)

print("Feature Importances:")
print(feature_importances)

# Fehlerverteilung visualisieren
errors = y_test - precise_predictions
plt.figure(figsize=(10, 6))
sns.histplot(errors, kde=True)
plt.xlabel("Vorhersagefehler")
plt.title("Verteilung der Vorhersagefehler")
plt.show()

# Scatterplot der tatsächlichen vs. vorhergesagten Werte
plt.figure(figsize=(10, 6))
plt.scatter(y_test, precise_predictions, alpha=0.3)
plt.plot([0, max(y_test)], [0, max(precise_predictions)], color='red', linestyle='--')
plt.xlabel("Tatsächliche Werte")
plt.ylabel("Vorhergesagte Werte")
plt.title("Tatsächliche vs. vorhergesagte Werte")
plt.show()