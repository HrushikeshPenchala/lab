import pandas as pd
from sklearn.feature_selection import mutual_info_classif

data = pd.DataFrame({
    "Outlook": ["Sunny", "Sunny", "Rainy", "Rainy", "Sunny", "Rainy"],
    "Play": ["No", "No", "Yes", "Yes", "Yes", "No"]
})

# Convert categories to numbers
x = data["Outlook"].map({"Sunny": 0, "Rainy": 1}).values.reshape(-1, 1)
y = data["Play"].map({"No": 0, "Yes": 1})

# Calculate Information Gain
gain = mutual_info_classif(
    x, y,
    discrete_features=True,
    random_state=0
)

print("Information Gain:", round(gain[0], 3))