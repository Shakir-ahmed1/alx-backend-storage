-- calculates the weighted average for all users
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE user_id_param INT;
    
    -- Declare a cursor to iterate over user IDs
    DECLARE user_cursor CURSOR FOR
        SELECT id FROM users;
    
    -- Open the cursor
    OPEN user_cursor;
    
    -- Start fetching user IDs
    user_loop: LOOP
        -- Fetch the next user ID
        FETCH user_cursor INTO user_id_param;
        
        -- Exit the loop if no more rows to fetch
        IF user_id_param IS NULL THEN
            LEAVE user_loop;
        END IF;
        
        -- Call the ComputeAverageWeightedScoreForUser procedure for the current user
        CALL ComputeAverageWeightedScoreForUser(user_id_param);
    END LOOP;
    
    -- Close the cursor
    CLOSE user_cursor;
    
END //

DELIMITER ;

