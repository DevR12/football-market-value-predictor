import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error

df = pd.read_csv("data/features_players.csv")

features = df[
    [
        "overall_rating",
        "potential_rating",
        "age",
        "goal_contribution"
    ]
]

target = df["performance_score"]

x_train, x_test, y_train, y_test = train_test_split(
    features,
    target,
    test_size=0.2,
    random_state=42
)

model = RandomForestRegressor(
    n_estimators=600,
    max_depth=16,
    min_samples_split=4,
    random_state=42
)

model.fit(x_train, y_train)

predictions = model.predict(x_test)

print("Model Evaluation\n")

print("R2 Score:", r2_score(y_test, predictions))
print("MAE:", mean_absolute_error(y_test, predictions))

df["predicted_performance"] = model.predict(features)

df["value_efficiency"] = (
    df["predicted_performance"] /
    df["market_value_million_eur"]
)

undervalued_players = df.sort_values(
    by="value_efficiency",
    ascending=False
)

undervalued_players.to_csv(
    "outputs/undervalued_players.csv",
    index=False
)