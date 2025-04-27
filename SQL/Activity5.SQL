CREATE TABLE IF NOT EXISTS ProductS (
    PRO_ID TEXT PRIMARY KEY,
    PRO_NAME TEXT,
    SUP_ID TEXT,
    CAT_ID TEXT,
    UNIT INTEGER,
    PRICE REAL
);

INSERT INTO ProductS(PRO_ID, PRO_NAME, SUP_ID, CAT_ID, UNIT, PRICE) VALUES
    ("101","Chais", "100", "1", 50, 18),
    ("102","Chang", "101","2", 50, 19),
    ("103","Aniseed Syrup", "102","3", 50, 10),
    ("104","Anton Seasoning", "103","4", 50, 22),
    ("105","Chef Anton Syrup Mix", "104", "5", 50, 21.35);

SELECT * FROM ProductS

Select count (*) FROM Products

Select count (PRO_ID) FROM Products

Select AVG (PRICE) FROM Products

Select Sum (PRICE) FROM Products

SELECT Sum (UNIT) FROM Products

SELECT DISTINCT (PRO_NAME) FROM Products