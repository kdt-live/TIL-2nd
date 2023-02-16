-- SELECT customeㄱNumber, amount
-- FROM payments
-- WHERE amount = 위에서 찾은 최대 값
SELECT customerNumber, amount
FROM payments
WHERE amount = (
	SELECT MAX(amount)
	FROM payments
);

-- 미국에 사무실에서 일하는 직원의 이름과 성 조회
-- 미국 사무실 코드를 가지고 있는 목록 
-- 직원 테이블의 officecode가 1, 2, 3 인지 확인 
SELECT lastName, firstName
FROM employees
WHERE officeCode IN 
	(
		SELECT officeCode
		FROM offices
		WHERE country = 'USA'
    );
    

-- orders에는 주문한 고객들만 들어있음 -> NOT IN
-- orders에서 고객 주문 목록을 가져와서
-- customers의 모든 정보와 위에서 가져온 고객 주문 목록을 비교 
-- 결국 위에서 가져온 고객 주문 목록에 포함되지 않는 고객이 범인
SELECT customerName
FROM customers
WHERE customerNumber NOT IN (
	SELECT DISTINCT customerNumber
    FROM orders
);


SELECT customerNumber, amount, contactFirstName
FROM (
	SELECT *
    FROM payments
    INNER JOIN customers USING (customerNumber)
) AS mySub
WHERE amount = (
	SELECT MAX(amount)
	FROM payments
);

-- 서브쿼리를 사용하지 않은 동일한 코드
SELECT L.customerNumber, L.amount, R.contactFirstName 
FROM payments L 
INNER JOIN customers R 
	ON L.customerNumber = R.customerNumber 
WHERE L.amount = (
	SELECT MAX(amount)
    FROM payments
);


SELECT customerNumber, customerName
FROM customers
WHERE EXISTS (
	SELECT *
    FROM orders
    WHERE customers.customerNumber = orders.customerNumber
);

SELECT employeeNumber, firstName, lastName
FROM employees
WHERE EXISTS (
	SELECT *
    FROM offices
    WHERE 
		city = 'Paris' 
        AND employees.officeCode = offices.officeCode
);

SELECT contactFirstName, creditLimit,
	CASE 
		WHEN creditLimit > 100000 THEN 'VIP'
        WHEN creditLimit > 70000 THEN 'Pla'
        ELSE 'Bronze'
    END AS grade
FROM customers;

SELECT orderNumber, status, 
	CASE
		WHEN status = 'In Process' THEN '주문중'
        WHEN status = 'Shipped' THEN '발주완료'
        WHEN status = 'Cancelled' THEN '주문취소'
        ELSE '기타사유'
    END AS details
FROM orders;