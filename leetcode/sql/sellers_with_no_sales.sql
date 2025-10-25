SELECT s.seller_name 
FROM Seller s 
JOIN Orders o ON o.seller_id = s.seller_id 
GROUP BY s.seller_id, s.seller_name 
HAVING SUM(CASE WHEN YEAR(o.sale_date) = 2020 THEN 1 ELSE 0 END) = 0 
ORDER BY s.seller_name;

#OR

SELECT s.seller_name
FROM Seller s
JOIN (
    SELECT seller_id
    FROM Orders
    WHERE seller_id NOT IN (
        SELECT seller_id
        FROM Orders
        WHERE YEAR(sale_date) = 2020
    )
) AS t2
ON t2.seller_id = s.seller_id
ORDER BY s.seller_name; 


# Finds all sellers who made no sales in 2020.
# First uses GROUP BY + HAVING +SUM to count 2020 sales per seller.
# Second uses a subquery with NOT IN to filter sellers without 2020 sales.
 