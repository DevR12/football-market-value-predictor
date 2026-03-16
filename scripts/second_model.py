import pandas as pd

df = pd.read_csv("data/features_players.csv")

df["value_efficiency"] = (
    df["performance_score"] /
    df["market_value_million_eur"]
)

top_performers = df.sort_values(
    by="performance_score",
    ascending=False
)

undervalued_players = df.sort_values(
    by="value_efficiency",
    ascending=False
)

print("Top Performing Players\n")

print(
    top_performers[
        ["player_name","club","position","performance_score"]
    ].head(10)
)

print("\nMost Undervalued Players\n")

print(
    undervalued_players[
        [
            "player_name",
            "club",
            "position",
            "performance_score",
            "market_value_million_eur",
            "value_efficiency"
        ]
    ].head(10)
)

undervalued_players.to_csv(
    "outputs/value_for_money_transfers.csv",
    index=False
)