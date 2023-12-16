-- trigger that activates when inserting orders
DELIMITER $$

CREATE TRIGGER items_after_insert
        AFTER INSERT ON orders
        FOR EACH ROW
BEGIN
        UPDATE items
        SET quantity = quantity - NEW.number
	WHERE name = NEW.item_name;
END $$
DELIMITER ;
