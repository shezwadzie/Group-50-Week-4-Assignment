
# predict_issue_priority.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load Dataset
data = pd.read_csv("https://raw.githubusercontent.com/jbrownlee/Datasets/master/breast-cancer.csv", header=None)

# 2. Add column names (based on dataset)
data.columns = ["Class", "age", "menopause", "tumor-size", "inv-nodes", "node-caps", "deg-malig", "breast", "breast-quad", "irradiat"]

# 3. Convert categorical to numerical
for col in data.columns:
    if data[col].dtype == 'object':
        le = LabelEncoder()
        data[col] = le.fit_transform(data[col])

# 4. Split into features and labels
X = data.drop("Class", axis=1)
y = data["Class"]

# 5. Split into train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6. Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# 7. Predict and Evaluate
y_pred = model.predict(X_test)
print("✅ Accuracy:", accuracy_score(y_test, y_pred))
print("\n📊 Classification Report:\n", classification_report(y_test, y_pred))

# 8. Visualize feature importance
feature_imp = pd.Series(model.feature_importances_, index=X.columns)
sns.barplot(x=feature_imp, y=feature_imp.index)
plt.title("Feature Importance")
plt.tight_layout()
plt.savefig("feature_importance.png")
print("📈 Feature importance chart saved as 'feature_importance.png'")
