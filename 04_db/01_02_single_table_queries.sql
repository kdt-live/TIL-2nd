-- 03. Filtering data
SELECT DISTINCT
  lastName
FROM
  employees
ORDER BY
  lastName;

SELECT
  lastName
FROM
  employees
ORDER BY
  lastName;

SELECT DISTINCT
  lastName
FROM
  employees
ORDER BY
  lastName;

SELECT 
  lastName, firstName, officeCode
FROM
  employees
WHERE
  officeCode = 1;

SELECT 
  lastName, firstName, jobTitle
FROM
  employees
WHERE
  jobTitle != 'Sales Rep';

SELECT 
  lastName, firstName, officeCode, jobTitle
FROM
  employees
WHERE
  officeCode >= 1
  AND jobTitle = 'Sales Rep';

SELECT 
  lastName, firstName, officeCode, jobTitle
FROM
  employees
WHERE
  officeCode < 5
  OR jobTitle != 'Sales Rep';

SELECT 
  lastName, firstName, officeCode
FROM
  employees
WHERE
  officeCode BETWEEN 1 AND 4;
-- WHERE
--   officeCode >= 1
--   AND officeCode <= 4;

SELECT 
  lastName, firstName, officeCode
FROM
  employees
WHERE
  officeCode BETWEEN 1 AND 4
ORDER BY officeCode;

SELECT 
  lastName, firstName, officeCode
FROM
  employees
WHERE
  officeCode IN (1, 3, 4);
-- WHERE
--   officeCode = 1
--   OR officeCode = 3
--   OR officeCode = 4;

SELECT 
  lastName, firstName, officeCode
FROM
  employees
WHERE
  officeCode NOT IN (1, 3, 4);

SELECT 
  lastName, firstName
FROM
  employees
WHERE
  lastName LIKE '%son';

SELECT 
  lastName, firstName
FROM
  employees
WHERE
  firstName LIKE '___y';

SELECT 
  contactFirstName, creditLimit
FROM
  customers
ORDER BY creditLimit DESC
LIMIT 7;


SELECT 
  contactFirstName, creditLimit
FROM
  customers
ORDER BY 
  creditLimit DESC
LIMIT 3, 4;
-- LIMIT 5 OFFSET 3;



-- 04. Grouping data
SELECT 
  c1, c2,..., cn, aggregate_function(ci)
FROM
  table_name
GROUP BY 
  c1, c2, ..., cn;

SELECT
  jobTitle
FROM
  employees
GROUP BY
  jobTitle;

SELECT 
  jobTitle, COUNT(*)
FROM
  employees
GROUP BY 
  jobTitle;

SELECT
  country,
  AVG(creditLimit)
FROM
  customers
GROUP BY
  country
ORDER BY
  AVG(creditLimit) DESC;

SELECT
  country,
  AVG(creditLimit) AS avgOfCreditLimit
FROM
  customers
GROUP BY
  country
ORDER BY
  avgOfCreditLimit DESC;

SELECT
  country,
  AVG(creditLimit)
FROM
  customers
WHERE 
  AVG(creditLimit) > 80000
GROUP BY
  country;

SELECT
  country,
  AVG(creditLimit)
FROM
  customers
GROUP BY
  country
HAVING
  AVG(creditLimit) > 80000;
