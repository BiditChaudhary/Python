CREATE TABLE IF NOT EXISTS Students (
    ROLL_NO TEXT PRIMARY KEY,
    NAME TEXT NOT NULL,
    ADDRESS TEXT,
    PHONE TEXT,
    AGE INTEGER
);

INSERT INTO Students (ROLL_NO, NAME, ADDRESS, PHONE, AGE) VALUES
('1', 'RAM', 'Kathmandu', '9841365786', 19),
('2', 'PRASHANT', 'Pokhara', '9841785748', 18),
('3', 'UTSAV', 'Chitwan', '984157437', 18),
('4', 'JOSEPH', 'Jhapa', '984153048', 22),
('5', 'ROHIT', 'Birjung', '9841485067',20);

SELECT * FROM Students;

SELECT * FROM Students WHERE AGE = 19 AND ADDRESS = 'Kathmandu'

SELECT * FROM Students WHERE NAME = 'RAM' AND AGE = 19

SELECT * FROM Students WHERE NAME = 'PRASHANT' OR NAME = 'JOSEPH'

SELECT * FROM Students WHERE NAME = 'RAM' OR AGE = 18

SELECT * FROM Students WHERE NAME = 'RAM' OR NAME = 'RAMESH' AND AGE = 19