DROP TABLE IF EXISTS users;

CREATE TABLE users (
	id INT AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
); 

DROP TABLE articles;

CREATE TABLE articles (
	id INT AUTO_INCREMENT,
    title VARCHAR(50) NOT NULL,
    content VARCHAR(100) NOT NULL,
    userId INT NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO
	users (name)
VALUES
	('권미자'),
    ('류준하'),
    ('정영식');

INSERT INTO
	articles (title, content, userId)
VALUES
	('제목1', '내용1', 1),
    ('제목2', '내용2', 2),
    ('제목3', '내용3', 4);
    
SELECT * FROM users;
SELECT * FROM articles;


SELECT articles.id, title, content, name
FROM articles
INNER JOIN users
	ON articles.userId = users.id;

SELECT 
	productCode, productName, textDescription
FROM
	products
INNER JOIN productlines
	ON products.productLine = productlines.productLine;

SELECT
	orders.orderNumber, status, priceEach
FROM
	orders
INNER JOIN orderdetails
	ON orders.orderNumber = orderdetails.orderNumber;
    
    
SELECT
	t1.orderNumber, 
    status, 
    SUM(priceEach * quantityOrdered) AS totalSales
FROM
	orders AS t1
INNER JOIN orderdetails AS t2
	ON t1.orderNumber = t2.orderNumber
GROUP BY
	orderNumber;
    
SELECT contactFirstName, orderNumber, status
FROM customers
LEFT JOIN orders
	ON customers.customerNumber = orders.customerNumber;
    
SELECT contactFirstName, orderNumber, status
FROM customers
LEFT JOIN orders
	ON customers.customerNumber = orders.customerNumber
WHERE orderNumber IS NULL;

SELECT employeeNumber, firstName, customerNumber, contactFirstName
FROM customers
RIGHT JOIN employees
	ON employees.employeeNumber = customers.salesRepEmployeeNumber;
    
SELECT employeeNumber, firstName, customerNumber, contactFirstName
FROM customers
RIGHT JOIN employees
	ON employees.employeeNumber = customers.salesRepEmployeeNumber
WHERE customerNumber IS NULL;