CREATE TABLE IF NOT EXISTS Salesman (
    Salesman_ld TEXT PRIMARY KEY,
    name TEXT,
    city TEXT,
    Comission REAL
);

INSERT INTO Salesman (Salesman_ld, name, city, Comission) VALUES
    ('5001', 'James Hoog', 'New York', 0.15),
    ('5002', 'Nail Knite', 'Paris', 0.13),
    ('5003', 'Joseph Hagari', 'Jerusalem', 0.11),
    ('5004', 'Nathan Issac', 'Haifa', 0.14),
    ('5005', 'Roy Emmanuel', 'Rome', 0.13),
    ('5006', 'Nathaniel Smith', 'London', 0.12),
    ('5007', 'Peter Magdalene', 'Cairo', 0.11);

SELECT * FROM Salesman;

CREATE TABLE IF NOT EXISTS ORDERS(
    ord_no TEXT PRIMARY KEY,
    purch_amt REAL,
    ord_date TEXT,
    customer_id TEXT,
    Salesman_id TEXT
);

INSERT INTO Orders (ord_no, purch_amt, ord_date, customer_id, Salesman_id) VALUES
    ('70001',150.5,'2025-04-18', '3002', '5001'),
    ('70002',245.0,'2024-03-09', '3003', '5002'),
    ('70003',325.5,'2024-09-03', '3004', '5003'),
    ('70004',243.5,'2023-04-23', '3005', '5004'),
    ('70005',500.0,'2023-04-15', '3006', '5005');

SELECT * FROM Orders;

SELECT name, Comission
FROM Salesman;



