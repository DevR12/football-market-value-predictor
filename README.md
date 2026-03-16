# Identifying Value-for-Money Football Transfers

## Overview

This project builds a sports analytics pipeline to identify undervalued football players based on their on-field performance relative to their market value.

The analysis focuses on a practical scouting question:

> Which players deliver the most performance for their transfer value?

The project processes player statistics, engineers performance metrics, and ranks players by a value efficiency score to highlight potential value-for-money transfers.


---

## Project Pipeline

The project follows a simple data analytics workflow:

raw dataset ↓ data cleaning ↓ feature engineering ↓ SQL analytics queries ↓ value efficiency analysis ↓ undervalued player ranking


---

## Repository Structure

sports-analytics │ ├── data/ │   raw_players.csv │   clean_players.csv │   features_players.csv │ ├── scripts/ │   clean_data.py │   feature_engineering.py │   value_efficiency_analysis.py │ ├── sql/ │   analytics_queries.sql │ ├── outputs/ │   undervalued_players.csv │ └── README.md


---

## Data Cleaning

The cleaning pipeline standardizes the dataset and ensures all required fields are valid.

Key checks include:

verifying numeric columns

handling missing values

validating ranges for goals, assists, and minutes played

exporting a cleaned dataset for downstream processing


Script:

scripts/clean_data.py

Output:

data/clean_players.csv


---

## Feature Engineering

Additional features were engineered to support analysis.

*Position Grouping*

Player positions were grouped into broader tactical categories:
- attacker
- winger
- midfielder
- defender
- goalkeeper

---

*Goal Contribution*

Goal contribution captures direct attacking involvement.

goal_contribution = goals + assists


---

*Performance Score*

A custom performance metric was created that weights player actions differently depending on position.

Example structure:

performance_score =
(goals × weight) + (assists × weight) + (rating × weight)

Different weights are used for attackers, midfielders, defenders, and goalkeepers.

This produces a normalized performance metric comparable across players.

---

## SQL Analytics

Several analytical queries were run to explore the dataset.

Examples include:
- top players by performance score
- average performance by position group
- club-level performance averages
- age vs performance distribution
- top players per league

---

## Value Efficiency Metric

To evaluate transfer value, a value efficiency metric was designed.

value_efficiency = performance_score / market_value

*Interpretation:*

Higher value efficiency indicates stronger performance relative to cost.

This metric highlights players delivering strong performance while having relatively low transfer value.

---

*Identifying Undervalued Players*

Players are ranked by value efficiency:

value_efficiency (descending)

The top results represent potential value-for-money transfers.

**Output file:**

outputs/value_for_money_transfers.csv

---

*Example Insight*

Using the efficiency metric, the analysis identifies players who:
- perform above their market value
- provide strong on-field impact at lower transfer cost
- could represent attractive transfer opportunities

---

## Technologies Used

Python

Pandas

SQL

---