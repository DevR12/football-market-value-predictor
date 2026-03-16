import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

def create_position_grp(df):
    def map_position(pos):
        if pos == "ST":
            return "attacker"
        elif pos in ["LW", "RW"]:
            return "winger"
        elif pos in ["CM", "CDM"]:
            return "midfielder"
        elif pos in ["RB", "CB", "LB"]:
            return "defender"
        elif pos == "GK":
            return "goalkeeper"
        else:
            return "other"
    
    df["position_group"] = df["position"].apply(map_position)

    return df

def calculate_perf_score(row):

    minutes = row["minutes_played"]

    if minutes == 0:
        return 0
    
    goals = row["goals"]
    assists = row["assists"]
    rating = row["overall_rating"]

    role = row["position_group"]

    if role == "attacker":
        goal_w, assist_w, rating_w = 4, 3, 0.5

    elif role == "winger":
        goal_w, assist_w, rating_w = 3.5, 3.5, 0.5

    elif role == "midfielder":
        goal_w, assist_w, rating_w = 2, 4, 0.5

    elif role == "defender":
        goal_w, assist_w, rating_w = 1, 2, 1.5

    elif role == "goalkeeper":
        goal_w, assist_w, rating_w = 0, 0, 2.4

    else:
        goal_w, assist_w, rating_w = 2, 2, 0.5

    score = (
        goals * goal_w +
        assists * assist_w +
        rating * rating_w
    ) / minutes

    return score

def create_perf_score(df):
    df["performance_score"] = df.apply(calculate_perf_score, axis=1)
    return df

def create_goal_contri(df):
    df["goal_contribution"] = df["goals"] + df["assists"]
    return df

def create_age_groups(df):

    def age_group(age):
        if age < 23:
            return "young"
        elif age < 30:
            return "prime"
        else:
            return "veteran"

    df["age_group"] = df["age"].apply(age_group)

    return df

def create_exp_indicator(df):
    df["experienced"] = df["matches_played"] >= 65
    return df

def save_data(df, path):
    df.to_csv(path, index=False)

def main():

    print("Loading cleaned dataset...")
    df = pd.read_csv("data/clean_players.csv")

    print("Creating position groups...")
    df = create_position_grp(df)

    print("Creating goal contribution...")
    df = create_goal_contri(df)

    print("Creating performance score...")
    df = create_perf_score(df)

    print("Creating age groups...")
    df = create_age_groups(df)

    print("Creating experience indicator...")
    df = create_exp_indicator(df)

    print("Saving feature dataset...")
    save_data(df, "data/features_players.csv")

    print("Feature engineering completed successfully.")


if __name__ == "__main__":
    main()