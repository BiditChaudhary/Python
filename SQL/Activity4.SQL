CREATE TABLE IF NOT EXISTS Product (
    PRO_ID INTEGER PRIMARY KEY,
    PRO_NAME TEXT,
    PRO_PRICE INTEGER,
    PRO_COM FLOAT
);

INSERT INTO Product (PRO_ID, PRO_NAME, PRO_PRICE, PRO_COM)
VALUES
    (101,'Motherboard',3200,15),
    (102,'Keyboard',450,16),
    (103,'Speaker',250,14),
    (104,'ZipDrive',250,13),
    (105,'Mouse',120,16);


SELECT * FROM Product

SELECT * FROM Product WHERE PRO_PRICE = (SELECT min (PRO_PRICE) from Product)

SELECT * FROM Product WHERE PRO_PRICE = (SELECT max (PRO_PRICE) from Product)

