-- calculates the weighted average for all users
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE user_id_param INT;
    
    DECLARE user_cursor CURSOR FOR
        SELECT id FROM users;
    
    DECLARE total_weighted_score FLOAT;
    DECLARE total_weight INT;
    
    OPEN user_cursor;
    
    user_loop: LOOP
        FETCH user_cursor INTO user_id_param;
        
        IF user_id_param IS NULL THEN
            LEAVE user_loop;
        END IF;
        
        SELECT SUM(c.score * p.weight), SUM(p.weight)
        INTO total_weighted_score, total_weight
        FROM corrections c
        JOIN projects p ON c.project_id = p.id
        WHERE c.user_id = user_id_param;
        
        IF total_weight > 0 THEN
            UPDATE users
            SET average_score = total_weighted_score / total_weight
            WHERE id = user_id_param;
        ELSE
            UPDATE users
            SET average_score = 0
            WHERE id = user_id_param;
        END IF;
    END LOOP;
    
    CLOSE user_cursor;
    
END //

DELIMITER ;

