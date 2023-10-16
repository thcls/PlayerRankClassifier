import pandas as pd
from assets.scripts.data import *
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from assets.scripts.data import allKeys, getJsonData, getSample

#dataList = getTestList("PlayerRankClassifier/assets/data/json/val_stats_full.json", 2500, "")
dataList = getSample("assets/data/json/val_stats_full.json", 10, "BR")

# DataFrame
df = pd.DataFrame(dataList)

# Dividindo os dados em recursos (X) e rótulos (y)
X = df.drop(allKeys(), axis=1)
y = df['rating']

# Divisão
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

random_forest = RandomForestClassifier(n_estimators=140, random_state=42)

# Validação cruzada
scores = cross_val_score(random_forest, X, y, cv=10)
print("Acurácia da validação cruzada: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

# Treinamento
random_forest.fit(X_train, y_train)

# Previsões
y_pred = random_forest.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')
confusion = confusion_matrix(y_test, y_pred)

print("Acurácia:", accuracy)
print("Precisão:", precision)
print("Revocação (Recall):", recall)
print("F1-Score:", f1)
print("Matriz de Confusão:")
print(confusion)
