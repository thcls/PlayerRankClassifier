from assets.scripts.data import *
import pandas as pd
import numpy as np
import json
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

dataList = getSample("assets/data/json/val_stats_full.json", 20, "BR")

# DataFrame
df = pd.DataFrame(dataList)

# Dividindo os dados em recursos (X) e rótulos (y)
X = df.drop(allKeys(), axis=1)
y = df['rating']

# Normalizar os recursos
scaler = StandardScaler()
X = scaler.fit_transform(X)

n_splits = 10

kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)

# Listas para armazenar métricas de avaliação
accuracy_scores = []
precision_scores = []
recall_scores = []
f1_scores = []

# Divisão
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Folds
for train_index, test_index in kf.split(X_train):
    X_fold_train, X_fold_val = X_train[train_index], X_train[test_index]
    y_fold_train, y_fold_val = y_train.iloc[train_index], y_train.iloc[test_index]

    k = 2
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_fold_train, y_fold_train)
    previsoes = knn.predict(X_fold_val)

    accuracy_scores.append(accuracy_score(y_fold_val, previsoes))
    precision_scores.append(precision_score(y_fold_val, previsoes, average='micro'))
    recall_scores.append(recall_score(y_fold_val, previsoes, average='micro'))
    f1_scores.append(f1_score(y_fold_val, previsoes, average='micro'))

# Métricas
mean_accuracy = np.mean(accuracy_scores)
mean_precision = np.mean(precision_scores)
mean_recall = np.mean(recall_scores)
mean_f1 = np.mean(f1_scores)

print("Média de Acurácia:", mean_accuracy)
print("Média de Precisão:", mean_precision)
print("Média de Recall:", mean_recall)
print("Média de F1-score:", mean_f1)
