-- Creaet The Database
create database University;

----------------------
-- Create The Tables--
----------------------

-- Create the Faculty table
CREATE TABLE Faculty (
    FacultyID INT identity PRIMARY KEY,
    Name NVARCHAR(100),
    PhoneNumber NVARCHAR(14),
    Email NVARCHAR(100)
);

-- Create the Person table
CREATE TABLE Person (
    PersonID INT identity PRIMARY KEY,
    FirstName NVARCHAR(100),
    MidName NVARCHAR(100),
    LastName NVARCHAR(100),
    Gender NVARCHAR(1),
    BirthDate DATE,
    FacultyID INT FOREIGN KEY REFERENCES Faculty(FacultyID)
);



-- Create the Phone table
CREATE TABLE Phone (
    PhoneID INT identity PRIMARY KEY,
    PhoneNumber1 NVARCHAR(13),
    PhoneNumber2 NVARCHAR(13),
    PersonID INT FOREIGN KEY REFERENCES Person(PersonID)
);

-- Create the Employee table
CREATE TABLE Employee (
    EmployeeID INT identity PRIMARY KEY,
    Salary FLOAT,
    ExitDate DATE,
    PersonID INT FOREIGN KEY REFERENCES Person(PersonID),
    ManagerID INT FOREIGN KEY REFERENCES Employee(EmployeeID)
);

-- Create the Student table
CREATE TABLE Student (
    StudentID INT identity PRIMARY KEY,
    GPA FLOAT,
    PersonID INT FOREIGN KEY REFERENCES Person(PersonID)
);

-- Create the Course table
CREATE TABLE Course (
    CourseID INT identity PRIMARY KEY,
    Name NVARCHAR(100),
    Title NVARCHAR(100),
    CreditHours INT,
    DeptName NVARCHAR(100),
    FacultyID INT FOREIGN KEY REFERENCES Faculty(FacultyID)
);

-- Create the Enrollment table
CREATE TABLE Enrollment (
    EnrollmentID INT identity PRIMARY KEY,
    EnrollmentDate DATE,
    CourseID INT FOREIGN KEY REFERENCES Course(CourseID),
    StudentID INT FOREIGN KEY REFERENCES Student(StudentID)
);

-- Create the Professor table
CREATE TABLE Professor (
    ProfessorID INT identity PRIMARY KEY,
    EmployeeID INT FOREIGN KEY REFERENCES Employee(EmployeeID)
);


-- Create the Teachment table
CREATE TABLE Teachment (
    TeachmentID INT identity PRIMARY KEY,
    ProfessorID INT FOREIGN KEY REFERENCES Professor(ProfessorID),
    EnrollmentID INT FOREIGN KEY REFERENCES Enrollment(EnrollmentID),
    LectureDay NVARCHAR(20),
    LectureRoom INT
);

-- Create the Worker table
CREATE TABLE Worker (
    WorkerID INT identity PRIMARY KEY,
    EmployeeID INT FOREIGN KEY REFERENCES Employee(EmployeeID)
);

-- Create the Administrator table
CREATE TABLE Administrator (
    AdminstratorID INT identity PRIMARY KEY,
    EmployeeID INT FOREIGN KEY REFERENCES Employee(EmployeeID)
);

