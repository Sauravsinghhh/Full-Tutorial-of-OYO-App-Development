# Full-Tutorial-of-OYO-App-Development
Team Introduction<br>
Welcome to our OYO Clone Project repository! We are a team passionate about creating a streamlined accommodation booking experience. Let us introduce ourselves:
<br>•	Team Members:
<br>Saurav Singh
<br>	Rashmi
<br>Hardik
<br>
# Project Introduction<br>
This repository hosts the Phase One development of our OYO Clone application. Currently, we have implemented:<br>
•	Backend:
 Developed in Python, our backend handles the core functionalities of our application.<br>
•	Database: 
Utilizing SQL, we've designed a database schema to store essential data for bookings and users.<br>
•	Frontend: 
Initial UI design featuring a home page and login interface using tkinter.<br>

Please note, this is an ongoing project and represents only the initial phase of development.
<br>
# Backend and Database Connectivity<br>
To access the backend and database functionalities:<br>
Step 1 -.	Database Connectivity:
Our backend (backend.py) connects to the SQL database using Mysql workbench..
Modify the database connection string  by using your password in backend.py to match your SQL setup.
<br>
Step2- .	Data Identifier:
Identifier structure:
Enter an identifier (hotel name, customer name, contact, address, booking ID, payment ID): {here you have to enter what details you are searching for} 
For example :<br>
•	If you enter name of hotel “hotel Taj” it will show the details of the taj hotel i.e.<br>
o	Details:
(HID-2, Hotel Name -'Hotel Taj', Hotel Rating - 4.8, Hotel Location- 'Delhi', Total Rooms-  150,Contact- '011-98765432')<br>
<br>
•	Entering customer name “ Rashmi” , it will show the customer details i.e.<br>
o	Details:<br>
(CID-7,CName- 'Rashmi',Contact- '7778889999',Stay Location- 'Delhi', Checkin Time- (YY-MM-DD))
<br>
# Database Overview
We have structured our SQL database to support the following functionalities:<br>
•	Tables:<br>
o	Hotels: <br>
Stores hotel information including name, address, and contact and ratings of the hotel.<br> 
o	Customer: <br>
Manages customer data such as name , contact information and registration date.<br>
o	Booking: <br>
Tracks booking details with references to customers and hotels.<br>
o	Room: <br>
Provides the details of every room.<br>
o	Payment: <br>
Account for the payment details reference to the customer and booking.<br>

# Frontend Overview<br>
Our frontend (tkinter-based) demonstrates the user interface conceptually. <br>
•	Limitations:<br>
The frontend UI in this repository is for demonstration purposes.
Direct functionality may not work on your local machine without appropriate requirements of the interface , backend and database setup.
