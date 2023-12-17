-- a stored procedure that calculates the average score of a student
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(user_id INT)
BEGIN
    DECLARE av DECIMAL;
    SELECT AVG(score) INTO av
    FROM corrections c
    WHERE c.user_id = user_id;

    UPDATE users
    SET average_score = IFNULL(av, 0)
    WHERE id = user_id;
END$$
DELIMITER ;
