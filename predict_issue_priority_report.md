# 🧠 Predictive Analytics for Resource Allocation

## 🔍 Task Overview
This task focuses on using a Random Forest machine learning model to predict issue priority (represented by breast cancer classifications) using the Breast Cancer dataset from Kaggle. The goal is to apply AI in decision-making for resource allocation, like prioritizing health cases.

---

## 📊 Dataset
- **Source**: Breast Cancer Dataset (UCI / Kaggle)
- **Features**: Age, Menopause, Tumor Size, Lymph Node Info, etc.
- **Label**: Class (problem recurrence or not)

---

## 🛠️ Method
- Preprocessed data (handled categorical features with Label Encoding)
- Split data into training (80%) and testing (20%)
- Trained a **Random Forest Classifier**
- Evaluated performance using:
  - Accuracy Score
  - Classification Report (Precision, Recall, F1-score)
- Visualized feature importance using Seaborn

---

## ✅ Results
- **Accuracy**: ~91%
- Classification metrics showed strong prediction performance.
- Feature importance chart saved as: `feature_importance.png`

---

## ⚖️ Ethical Reflection
- **Bias Risk**: If the dataset underrepresents certain patient groups (age ranges, ethnicities), the model may generalize poorly in real-world settings.
- **Fairness Tools**:
  - IBM's AI Fairness 360 could be used to audit feature bias.
  - Better data diversity would ensure fairer predictions.

---

## 📁 Files in This Task
- `predict_issue_priority.py` (Python script)
- `feature_importance.png` (generated chart)
- `predict_issue_priority_report.md` (this file)

---

✅ *Task Completed by Member 4*
