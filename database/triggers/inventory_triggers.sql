DELIMITER //

CREATE TRIGGER after_product_update
AFTER UPDATE ON products
FOR EACH ROW
BEGIN
    IF OLD.stock_quantity != NEW.stock_quantity THEN
        INSERT INTO inventory_logs (product_id, change_amount, reason)
        VALUES (NEW.id, NEW.stock_quantity - OLD.stock_quantity, 'Stock update');
    END IF;
END //

DELIMITER ;
