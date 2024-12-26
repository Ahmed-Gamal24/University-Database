-----------------------------------------
-- Insert Data In The Tables As Example
-----------------------------------------

-- Insert data into Faculty table
INSERT INTO Faculty ( Name, PhoneNumber, Email) VALUES
('Electronic Engineering', '0122656512', 'Elwahida@gmail.com');

-- Insert data into Person table
INSERT INTO Person ( FirstName, MidName, LastName, Gender, BirthDate, FacultyID) VALUES
( 'Ahmed', 'Gamal', 'Mohamed', 'M', '2004-04-26', NULL),
( 'Mohamed', 'Ahmed', 'Ali', 'M', '2004-02-26', NULL),
( 'Elhousiny', 'Ebrahim', 'Khattab', 'M', '2000-02-26', 1),
( 'Aymen', 'Sayed', 'Emera', 'M', '1999-02-26', NULL),
( 'Yasser', 'Mohamed', 'Ahmed', 'M', '1998-04-20', NULL),
( 'Ali', 'Mohamed', 'Ali', 'M', '1888-03-16', NULL);

-- Insert data into Phone table
INSERT INTO Phone ( PhoneNumber1, PhoneNumber2, PersonID) VALUES
( '010256568', NULL, 3),
( '012587978', NULL, 3),
( '010365686', NULL, 4);

-- Insert data into Employee table
INSERT INTO Employee ( Salary, ExitDate, PersonID, ManagerID) VALUES
( 4000, NULL, 3, 2),
( 5000, NULL, 4, NULL),
( 8000, NULL, 5, NULL),
( 6000, NULL, 6, NULL);

-- Insert data into Student table
INSERT INTO Student ( GPA, PersonID) VALUES
(3.2, 1),
( 2.9, 2);

-- Insert data into Course table
INSERT INTO Course ( Name, Title, CreditHours, DeptName, FacultyID) VALUES
( 'Database', 'Database', 3, 'CSE', 1);

-- Insert data into Enrollment table
INSERT INTO Enrollment ( EnrollmentDate, CourseID, StudentID) VALUES
( '2024-10-18', 1, 1),
( '2024-10-18', 1, 2);

-- Insert data into Professor table
INSERT INTO Professor ( EmployeeID) VALUES
(1);

-- Insert data into Teachment table
INSERT INTO Teachment ( ProfessorID, EnrollmentID, LectureDay, LectureRoom) VALUES
(1, 1, 'Sunday', 4),
(1, 2, 'Sunday', 4);

-- Insert data into Worker table
INSERT INTO Worker ( EmployeeID) VALUES
(4);

-- Insert data into Administrator table
INSERT INTO Administrator ( EmployeeID) VALUES
(3);

