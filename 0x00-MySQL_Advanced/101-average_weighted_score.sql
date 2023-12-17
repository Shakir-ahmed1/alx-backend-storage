-- calculates the weighted average for all users
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    -- Temporary table to store weighted scores
    CREATE TEMPORARY TABLE IF NOT EXISTS weighted_scores (
        user_id INT NOT NULL,
        weighted_score FLOAT DEFAULT 0,
        total_weight INT DEFAULT 0
    );

    -- Calculate weighted scores for each user and project
    INSERT INTO weighted_scores (user_id, weighted_score, total_weight)
    SELECT c.user_id, SUM(c.score * p.weight) AS weighted_score, SUM(p.weight) AS total_weight
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    GROUP BY c.user_id;

    -- Update the average_score in the users table
    UPDATE users u
    JOIN weighted_scores ws ON u.id = ws.user_id
    SET u.average_score = ws.weighted_score / ws.total_weight;

    -- Drop the temporary table
    DROP TABLE weighted_scores;
END //
DELIMITER ;

