import os
import pandas as pd
from sklearn.model_selection import train_test_split
from data_preparation import load_data, preprocess_data, save_processed_data
from model_training import train_baseline_model, train_precise_model, save_model
from evaluation import evaluate_model
from visualization import plot_correlation_matrix, plot_feature_importances, plot_prediction_errors, plot_actual_vs_predicted

# Dateipfade festlegen
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, '../data')
raw_data_path = os.path.join(data_dir, 'raw_data/sickness_table.csv')
processed_data_dir = os.path.join(data_dir, 'processed_data')
processed_data_path = os.path.join(processed_data_dir, 'preprocessed_data.csv')
baseline_model_path = os.path.join(current_dir, '../models/baseline_model.pkl')
precise_model_path = os.path.join(current_dir, '../models/precise_model.pkl')

# Sicherstellen, dass die Verzeichnisse existieren
os.makedirs(processed_data_dir, exist_ok=True)
os.makedirs(os.path.join(data_dir, 'final'), exist_ok=True)
os.makedirs(os.path.join(current_dir, '../models'), exist_ok=True)

# Schritt 1: Datenvorbereitung
data = load_data(raw_data_path)
processed_data = preprocess_data(data)
save_processed_data(processed_data, processed_data_path)

# Schritt 2: Modelltraining
features = [col for col in processed_data.columns if col != 'sby_need']
X = processed_data[features]
y = processed_data['sby_need']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

baseline_model = train_baseline_model(X_train, y_train)
save_model(baseline_model, baseline_model_path)

precise_model = train_precise_model(X_train, y_train)
save_model(precise_model, precise_model_path)

# Schritt 3: Modellebewertung
mae_baseline, rmse_baseline = evaluate_model(baseline_model, X_test, y_test)
mae_precise, rmse_precise = evaluate_model(precise_model, X_test, y_test)

print(f'Baseline Model - MAE: {mae_baseline:.2f}, RMSE: {rmse_baseline:.2f}')
print(f'Precise Model - MAE: {mae_precise:.2f}, RMSE: {rmse_precise:.2f}')

# Schritt 4: Visualisierung
plot_correlation_matrix(processed_data)

predictions_precise = precise_model.predict(X_test)
plot_prediction_errors(y_test, predictions_precise)
plot_actual_vs_predicted(y_test, predictions_precise)

importances = precise_model.feature_importances_
feature_importances = pd.DataFrame({
    'feature': features,
    'importance': importances
}).sort_values(by='importance', ascending=False)
plot_feature_importances(feature_importances)
