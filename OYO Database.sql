Create database OYO;
Use OYO;

-- Create tables
CREATE TABLE Hotel (
    HID INT PRIMARY KEY,
    Hname VARCHAR(50),
    Rating FLOAT,
    Address VARCHAR(50),
    No_of_Rooms INT,
    Contact_Number VARCHAR(20)
);

CREATE TABLE Room (
    Room_no INT PRIMARY KEY,
    RID INT,
    Room_Type VARCHAR(20),
    Price INT,
    Description VARCHAR(50),
    FOREIGN KEY (RID) REFERENCES Hotel(HID)
);

CREATE TABLE Customer (
    CID INT PRIMARY KEY,
    Cname VARCHAR(50),
    contact VARCHAR(20),
    Address VARCHAR(50),
    Registration_Date DATE
);

CREATE TABLE Booking (
    BID INT PRIMARY KEY,
    HID INT,
    CID INT,
    Price_Per_hour INT,
    RID INT,
    Check_Out DATE,
    Check_In DATE,
    FOREIGN KEY (HID) REFERENCES Hotel(HID),
    FOREIGN KEY (CID) REFERENCES Customer(CID),
    FOREIGN KEY (RID) REFERENCES Room(Room_no)
);

CREATE TABLE Payment (
    PID INT PRIMARY KEY,
    CID INT,
    Payment_Mode VARCHAR(20),
    Amount INT,
    Status VARCHAR(20),
    Date DATE,
    BID INT,
    FOREIGN KEY (CID) REFERENCES Customer(CID),
    FOREIGN KEY (BID) REFERENCES Booking(BID)
);

-- Insert into Hotel
INSERT INTO Hotel (HID, Hname, Rating, Address, No_of_Rooms, Contact_Number)
VALUES
    (1, 'Hotel Leela', 4.5, 'Mumbai', 100, '022-12345678'),
    (2, 'Hotel Taj', 4.8, 'Delhi', 150, '011-98765432'),
    (3, 'Hotel Oberoi', 4.9, 'Bangalore', 120, '080-11122233'),
    (4, 'Hotel Hyatt', 4.7, 'Hyderabad', 110, '040-33344444'),
    (5, 'Hotel Marriott', 4.6, 'Chennai', 130, '044-55566666');

-- Insert into Room
INSERT INTO Room (Room_no, RID, Room_Type, Price, Description)
VALUES
    ('101', 1, 'Single', 2000, 'Non-AC'),
    ('102', 1, 'Double', 3000, 'AC'),
    ('103', 2, 'Single', 2500, 'Non-AC'),
    ('104', 2, 'Double', 3500, 'AC'),
    ('105', 3, 'Single', 2200, 'Non-AC'),
    ('106', 3, 'Double', 3200, 'AC'),
    ('107', 4, 'Single', 2300, 'Non-AC'),
    ('108', 4, 'Double', 3300, 'AC'),
    ('109', 5, 'Single', 2000, 'Non-AC'),
    ('110', 5, 'Double', 3000, 'AC');

-- Insert into Customer
INSERT INTO Customer (CID, Cname, contact, Address, Registration_Date)
VALUES
    (1, 'Saurav', '9876543210', 'Mumbai', '2022-01-01'),
    (2, 'Uttam', '1112223333', 'Delhi', '2022-02-01'),
    (3, 'Hardik', '3334445555', 'Bangalore', '2022-03-01'),
    (4, 'Japjot', '4445556666', 'Hyderabad', '2022-04-01'),
    (5, 'Vansh', '5556667777', 'Chennai', '2022-05-01'),
    (6, 'Tarun', '6667778888', 'Mumbai', '2022-06-01'),
    (7, 'Rashmi', '7778889999', 'Delhi', '2022-07-01'),
    (8, 'Sashaki', '8889990000', 'Bangalore', '2022-08-01'),
    (9, 'Raj', '9990001111', 'Hyderabad', '2022-09-01'),
    (10, 'Rahul', '0001112222', 'Chennai', '2022-10-01');

-- Insert into Booking
INSERT INTO Booking (BID, HID, CID, Price_Per_hour, RID, Check_Out, Check_In)
VALUES
    (1, 1, 1, 100, 101, '2022-01-15', '2022-01-10'),
    (2, 2, 2, 120, 103, '2022-02-15', '2022-02-10'),
    (3, 3, 3, 110, 105, '2022-03-15', '2022-03-10'),
    (4, 4, 4, 130, 107, '2022-04-15', '2022-04-10'),
    (5, 5, 5, 140, 109, '2022-05-15', '2022-05-10'),
    (6, 1, 6, 100, 101, '2022-06-15', '2022-06-10'),
    (7, 2, 7, 120, 103, '2022-07-15', '2022-07-10'),
    (8, 3, 8, 110, 105, '2022-08-15', '2022-08-10'),
    (9, 4, 9, 130, 107, '2022-09-15', '2022-09-10'),
    (10, 5, 10, 140, 109, '2022-10-15', '2022-10-10');

-- Insert into Payment
INSERT INTO Payment (PID, CID, Payment_Mode, Amount, Status, Date, BID)
VALUES
    (1, 1, 'Credit Card', 1000, 'Paid', '2022-01-15', 1),
    (2, 2, 'Debit Card', 1200, 'Paid', '2022-02-15', 2),
    (3, 3, 'Cash', 1100, 'Paid', '2022-03-15', 3),
    (4, 4, 'Credit Card', 1300, 'Paid', '2022-04-15', 4),
    (5, 5, 'Debit Card', 1400, 'Paid', '2022-05-15', 5),
    (6, 1, 'Credit Card', 1000, 'Paid', '2022-06-15', 6),
    (7, 2, 'Debit Card', 1200, 'Paid', '2022-07-15', 7),
    (8, 3, 'Cash', 1100, 'Paid', '2022-08-15', 8),
    (9, 4, 'Credit Card', 1300, 'Paid', '2022-09-15', 9),
    (10, 5, 'Debit Card', 1400, 'Paid', '2022-10-15', 10);
    
-- Select statements
SELECT * FROM Hotel;
SELECT * FROM Room;
SELECT * FROM Customer;
SELECT * FROM Booking;
SELECT * FROM Payment;