-- adding corrections using procedure
DELIMITER $$
CREATE PROCEDURE AddBonus(user_id INT, project_name VARCHAR(255), score INT)
BEGIN
   DECLARE pro INT;
   SET pro = (SELECT id FROM projects WHERE name = project_name);
   IF pro IS NULL THEN
	INSERT INTO projects (name) VALUES (project_name);
	SET Pro = LAST_INSERT_ID();
   END IF;
   INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, pro, score);
END$$
DELIMITER ;
