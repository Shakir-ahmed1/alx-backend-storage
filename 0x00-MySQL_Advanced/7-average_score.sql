-- a stored procedure that calculates the average score of a student
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id_param INT
)
BEGIN
    DECLARE total_score FLOAT DEFAULT 0;
    DECLARE total_projects INT DEFAULT 0;
    DECLARE average_score FLOAT DEFAULT 0;

    -- Calculate total score for the user
    SELECT SUM(score) INTO total_score
    FROM corrections
    WHERE user_id = user_id_param;

    -- Calculate total number of projects
    SELECT COUNT(*) INTO total_projects
    FROM corrections
    WHERE user_id = user_id_param;

    -- Calculate average score
    IF total_projects > 0 THEN
        SET average_score = total_score / total_projects;
    END IF;

    -- Update the users table with the calculated average score
    UPDATE users
    SET average_score = average_score
    WHERE id = user_id_param;
END//

DELIMITER ;
