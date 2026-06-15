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

CREATE TRIGGER after_order_item_insert
AFTER INSERT ON order_items
FOR EACH ROW
BEGIN
    UPDATE products
    SET stock_quantity = stock_quantity - NEW.quantity
    WHERE id = NEW.product_id;
END //

DELIMITER ;

