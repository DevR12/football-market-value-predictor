-- top players by perf score
SELECT
    player_name,
    club,
    position,
    performace_score
FROM players
ORDER BY performance_score DESC
LIMIT 10;

-- avg perf by position group
SELECT
    position_group,
    AVG(performace_score) AS avg_performance
FROM players
GROUP BY position_group
ORDER BY avg_performance DESC;

-- best clubs by rating
SELECT 
    club,
    AVG(overall_rating) AS avg_rating
FROM players
GROUP BY club
ORDER BY avg_rating DESC
LIMIT 10;

-- perf by age group
SELECT 
    club,
    AVG(overall_rating) AS avg_rating
FROM players
GROUP BY club
ORDER BY avg_rating DESC
LIMIT 10;

-- top player in each position grp
SELECT *
FROM (
    SELECT 
        player_name,
        position_group,
        club,
        performance_score,
        ROW_NUMBER() OVER (
            PARTITION BY position_group
            ORDER BY performance_score DESC
        ) AS rank_in_position
    FROM players
) ranked_players
WHERE rank_in_position = 1;

-- players with highest goal contributions
SELECT 
    player_name,
    club,
    goals,
    assists,
    goal_contribution
FROM players
ORDER BY goal_contribution DESC
LIMIT 10;

-- exp vs inexp perf
SELECT 
    experienced,
    AVG(performance_score) AS avg_performance
FROM players
GROUP BY experienced;