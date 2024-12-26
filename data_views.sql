
-- create Professor View
create view ProfessorView as
select ProfessorID, FirstName, LastName, Gender, BirthDate, FacultyID, Salary, ExitDate, ManagerID
	from Employee 
		inner join Person on Person.PersonID = Employee.PersonID
		inner join Professor on Professor.EmployeeID = Employee.EmployeeID;




-- create student view 
create view StudentView as
select StudentID, FirstName, LastName, GPA, Gender, BirthDate, FacultyID
from Person inner join Student
on Student.PersonID = Person.PersonID;


-- create worker view
create view WorkerView as 
select WorkerID, FirstName, LastName, Gender, BirthDate, FacultyID, Salary, ExitDate
from Employee 
	inner join Person on Person.PersonID = Employee.PersonID
	inner join Worker on Worker.EmployeeID = Employee.EmployeeID;



	
-- create Adminstrator view
create view AdminstratorView as 
select AdminstratorID, FirstName, LastName, Gender, BirthDate, FacultyID, Salary, ExitDate
from Employee 
	inner join Person on Person.PersonID = Employee.PersonID
	inner join Administrator on Administrator.EmployeeID = Employee.EmployeeID;