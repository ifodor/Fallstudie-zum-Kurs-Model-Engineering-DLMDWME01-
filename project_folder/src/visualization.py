import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_correlation_matrix(data):
    """Zeige die Korrelationsmatrix an."""
    correlation_matrix = data.corr()
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Korrelationsmatrix')
    plt.show()

def plot_feature_importances(feature_importances):
    """Zeige die Feature-Importances an."""
    plt.figure(figsize=(10, 6))
    sns.barplot(x='importance', y='feature', data=feature_importances)
    plt.title('Feature Importances')
    plt.show()

def plot_prediction_errors(y_true, predictions):
    """Zeige die Verteilung der Vorhersagefehler an."""
    errors = y_true - predictions
    plt.figure(figsize=(10, 6))
    sns.histplot(errors, kde=True)
    plt.xlabel("Vorhersagefehler")
    plt.title("Verteilung der Vorhersagefehler")
    plt.show()

def plot_actual_vs_predicted(y_true, predictions):
    """Scatterplot der tatsächlichen vs. vorhergesagten Werte."""
    plt.figure(figsize=(10, 6))
    plt.scatter(y_true, predictions, alpha=0.3)
    plt.plot([0, max(y_true)], [0, max(predictions)], color='red', linestyle='--')
    plt.xlabel("Tatsächliche Werte")
    plt.ylabel("Vorhergesagte Werte")
    plt.title("Tatsächliche vs. vorhergesagte Werte")
    plt.show()
