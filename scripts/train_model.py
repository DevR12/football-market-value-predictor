import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

df = pd.read_csv("data/features_players.csv")

features = df[
    [
        "overall_rating",
        "potential_rating",
        "performance_score"
    ]
]

target = df["market_value_million_eur"]

x_train, x_test, y_train, y_test = train_test_split(
    features,
    target,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()
model.fit(x_train, y_train)

coefficients = pd.Series(
    model.coef_,
    index=features.columns
)
print("Linear Coefficients")
print(coefficients.sort_values(ascending=False))
print("\n")

predictions = model.predict(x_test)

print("Model Evaluation")
print(f"R2 Score: {r2_score(y_test, predictions):.4f}")
print(f"MAE:      {mean_absolute_error(y_test, predictions):.4f} Million EUR")
print("\n")

df["predicted_market_value"] = model.predict(features)
df["value_gap"] = df["predicted_market_value"] - df["market_value_million_eur"]

undervalued_players = df.sort_values(
    by="value_gap",
    ascending=False
)

undervalued_players.to_csv(
    "outputs/undervalued_players.csv",
    index=False
)

print("Successfully exported undervalued_players.csv")