DELIMITER //

CREATE PROCEDURE CalculateOrderTotal(IN orderId INT)
BEGIN
    DECLARE total DECIMAL(10, 2);

    SELECT SUM(quantity * price_at_purchase) INTO total
    FROM order_items
    WHERE order_id = orderId;

    UPDATE orders
    SET total_amount = IFNULL(total, 0)
    WHERE id = orderId;
END //

DELIMITER ;
