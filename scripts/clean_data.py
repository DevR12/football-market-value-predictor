import pandas as pd

def load_data(path):
    """Load raw dataset"""
    df = pd.read_csv(path)
    return df

def validate_numeric_columns(df):
    numeric_cols = ["age",
                    "overall_rating",
                    "potential_rating",
                    "matches_played",
                    "goals",
                    "assists",
                    "minutes_played",
                    "market_value_million_eur",
                    "contract_years_left"]
    
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    
    return df

def standard_categorical_cols(df):
    categorical_cols = ["player_name",
                        "nationality",
                        "club",
                        "position",
                        "injury_prone",
                        "transfer_risk_level"]
    
    for col in categorical_cols:
        df[col] = df[col].astype(str).str.strip()
    
    return df

def range_validation(df):
    df = df[(df["age"] >= 16) & (df["age"] <= 45)]
    df = df[df["goals"] >= 0]
    df = df[df["assists"] >= 0]
    df = df[df["matches_played"] >= 0]
    df = df[df["minutes_played"] >= 0]
    df = df[df["market_value_million_eur"] >= 0]

    return df

def logic_checks(df):
    # players with matches == 0 but goals or assists > 0
    inconsistent = (df["matches_played"] == 0) & (
        (df["goals"] > 0) | (df["assists"] > 0)
    )

    df = df[~inconsistent]

    return df

def remove_duplicates(df):
    df = df.drop_duplicates(subset="player_id")
    return df

def save_clean_data(df, path):
    df.to_csv(path, index=False)

def main():

    print("Loading raw dataset...")
    df = load_data("data/raw_players.csv")

    print("Validating numeric columns...")
    df = validate_numeric_columns(df)

    print("Standardizing categorical columns...")
    df = standard_categorical_cols(df)

    print("Applying range validation...")
    df = range_validation(df)

    print("Checking logical consistency...")
    df = logic_checks(df)

    print("Removing duplicates...")
    df = remove_duplicates(df)

    print("Saving cleaned dataset...")
    save_clean_data(df, "data/clean_players.csv")

    print("Cleaning pipeline completed successfully.")


if __name__ == "__main__":
    main()