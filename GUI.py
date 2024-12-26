import tkinter as tk
from tkinter import ttk, messagebox
import pyodbc

# Database connection setup
def connect_to_db():
    connection = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=AHMED;"
    "Database=University;"
    "Trusted_Connection=yes;"
    )
    return connection

def execute_query(query, params=()):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        messagebox.showerror("Database Error", str(e))
        return False

def fetch_data(query):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()
        return rows
    except Exception as e:
        messagebox.showerror("Database Error", str(e))
        return []

# GUI Components
class UniversityApp:
    def __init__(self, root):
        self.root = root
        self.root.title("University Database Management")
        self.root.geometry("500x600")

        # Main Tabs
        self.tab_control = ttk.Notebook(root)

        self.tab_insert_student = ttk.Frame(self.tab_control)
        self.tab_insert_professor = ttk.Frame(self.tab_control)
        self.tab_insert_worker = ttk.Frame(self.tab_control)
        self.tab_insert_admin = ttk.Frame(self.tab_control)

        self.tab_control.add(self.tab_insert_student, text="Insert Student")
        self.tab_control.add(self.tab_insert_professor, text="Insert Professor")
        self.tab_control.add(self.tab_insert_worker, text="Insert Worker")
        self.tab_control.add(self.tab_insert_admin, text="Insert Administrator")

        self.tab_control.pack(expand=1, fill="both")

        # Populate tabs with forms
        self.create_student_form()
        self.create_professor_form()
        self.create_worker_form()
        self.create_admin_form()



    def create_student_form(self):
        ttk.Label(self.tab_insert_student, text="First Name").grid(row=0, column=0)
        self.student_first_name = ttk.Entry(self.tab_insert_student)
        self.student_first_name.grid(row=0, column=1)

        ttk.Label(self.tab_insert_student, text="Middle Name").grid(row=1, column=0)
        self.student_mid_name = ttk.Entry(self.tab_insert_student)
        self.student_mid_name.grid(row=1, column=1)

        ttk.Label(self.tab_insert_student, text="Last Name").grid(row=2, column=0)
        self.student_last_name = ttk.Entry(self.tab_insert_student)
        self.student_last_name.grid(row=2, column=1)

        ttk.Label(self.tab_insert_student, text="Gender").grid(row=3, column=0)
        self.student_gender = ttk.Entry(self.tab_insert_student)
        self.student_gender.grid(row=3, column=1)

        ttk.Label(self.tab_insert_student, text="Birth Date (YYYY-MM-DD)").grid(row=4, column=0)
        self.student_birth_date = ttk.Entry(self.tab_insert_student)
        self.student_birth_date.grid(row=4, column=1)

        ttk.Label(self.tab_insert_student, text="Faculty ID").grid(row=5, column=0)
        self.student_faculty_id = ttk.Entry(self.tab_insert_student)
        self.student_faculty_id.grid(row=5, column=1)

        ttk.Label(self.tab_insert_student, text="GPA").grid(row=6, column=0)
        self.student_gpa = ttk.Entry(self.tab_insert_student)
        self.student_gpa.grid(row=6, column=1)

        ttk.Button(self.tab_insert_student, text="Insert Student", command=self.insert_student).grid(row=7, column=0, columnspan=2)
        ttk.Button(self.tab_insert_student, text="Show Students", command=self.show_students).grid(row=8, column=0, columnspan=2)

    def insert_student(self):
        # Get data from fields
        first_name = self.student_first_name.get()
        mid_name = self.student_mid_name.get()
        last_name = self.student_last_name.get()
        gender = self.student_gender.get()
        birth_date = self.student_birth_date.get()
        faculty_id = self.student_faculty_id.get()
        gpa = self.student_gpa.get()

        # Insert into Person table first
        person_query = """
        INSERT INTO Person (FirstName, MidName, LastName, Gender, BirthDate, FacultyID)
        VALUES (?, ?, ?, ?, ?, ?)"""
        if execute_query(person_query, (first_name, mid_name, last_name, gender, birth_date, faculty_id)):
            # Get last inserted PersonID
            conn = connect_to_db()
            cursor = conn.cursor()
            cursor.execute("SELECT SCOPE_IDENTITY()")
            person_id = cursor.fetchone()[0]
            conn.close()

            # Insert into Student table
            student_query = """
            INSERT INTO Student (GPA, PersonID) VALUES (?, ?)"""
            if execute_query(student_query, (gpa, person_id)):
                messagebox.showinfo("Success", "Student inserted successfully!")

    def show_students(self):
        rows = fetch_data("select StudentID, FirstName, LastName, GPA, Gender, BirthDate, FacultyID from Person inner join Student on Student.PersonID = Person.PersonID;")
        self.display_data(rows, ["StudentID", "FirstName", "LastName", "GPA", "Gender", "BirthDate", "FacultyID"])

    def display_data(self, rows, columns):
        data_window = tk.Toplevel(self.root)
        data_window.title("Data Viewer")
        tree = ttk.Treeview(data_window, columns=columns, show='headings')

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150)

        for row in rows:
            tree.insert('', tk.END, values=row)

        tree.pack(expand=True, fill=tk.BOTH)



    def create_professor_form(self):
        ttk.Label(self.tab_insert_professor, text="First Name").grid(row=0, column=0)
        self.professor_first_name = ttk.Entry(self.tab_insert_professor)
        self.professor_first_name.grid(row=0, column=1)

        ttk.Label(self.tab_insert_professor, text="Middle Name").grid(row=1, column=0)
        self.professor_mid_name = ttk.Entry(self.tab_insert_professor)
        self.professor_mid_name.grid(row=1, column=1)

        ttk.Label(self.tab_insert_professor, text="Last Name").grid(row=2, column=0)
        self.professor_last_name = ttk.Entry(self.tab_insert_professor)
        self.professor_last_name.grid(row=2, column=1)

        ttk.Label(self.tab_insert_professor, text="Gender").grid(row=3, column=0)
        self.professor_gender = ttk.Entry(self.tab_insert_professor)
        self.professor_gender.grid(row=3, column=1)

        ttk.Label(self.tab_insert_professor, text="Birth Date (YYYY-MM-DD)").grid(row=4, column=0)
        self.professor_birth_date = ttk.Entry(self.tab_insert_professor)
        self.professor_birth_date.grid(row=4, column=1)

        ttk.Label(self.tab_insert_professor, text="Faculty ID").grid(row=5, column=0)
        self.professor_faculty_id = ttk.Entry(self.tab_insert_professor)
        self.professor_faculty_id.grid(row=5, column=1)

        ttk.Label(self.tab_insert_professor, text="Salary").grid(row=6, column=0)
        self.professor_salary = ttk.Entry(self.tab_insert_professor)
        self.professor_salary.grid(row=6, column=1)

        ttk.Label(self.tab_insert_professor, text="Manager ID").grid(row=7, column=0)
        self.professor_manager_id = ttk.Entry(self.tab_insert_professor)
        self.professor_manager_id.grid(row=7, column=1)

        ttk.Button(self.tab_insert_professor, text="Insert Professor", command=self.insert_professor).grid(row=8, column=0, columnspan=2)
        ttk.Button(self.tab_insert_professor, text="Show Professors", command=self.show_professors).grid(row=9, column=0, columnspan=2)

    def insert_professor(self):
        # Get data from fields
        first_name = self.professor_first_name.get()
        mid_name = self.professor_mid_name.get()
        last_name = self.professor_last_name.get()
        gender = self.professor_gender.get()
        birth_date = self.professor_birth_date.get()
        faculty_id = self.professor_faculty_id.get()
        salary = self.professor_salary.get()
        manager_id = self.professor_manager_id.get()

        # Insert into Person table first
        person_query = """
        INSERT INTO Person (FirstName, MidName, LastName, Gender, BirthDate, FacultyID)
        VALUES (?, ?, ?, ?, ?, ?)"""
        if execute_query(person_query, (first_name, mid_name, last_name, gender, birth_date, faculty_id)):
            # Get last inserted PersonID
            conn = connect_to_db()
            cursor = conn.cursor()
            cursor.execute("SELECT SCOPE_IDENTITY()")
            person_id = cursor.fetchone()[0]
            conn.close()

            # Insert into Employee table
            employee_query = """
            INSERT INTO Employee (Salary, ExitDate, PersonID, ManagerID) VALUES (?, NULL, ?, ?)"""
            if execute_query(employee_query, (salary, person_id, manager_id)):
                # Get last inserted EmployeeID
                conn = connect_to_db()
                cursor = conn.cursor()
                cursor.execute("SELECT SCOPE_IDENTITY()")
                employee_id = cursor.fetchone()[0]
                conn.close()

                # Insert into Professor table
                professor_query = """
                INSERT INTO Professor (EmployeeID) VALUES (?)"""
                if execute_query(professor_query, (employee_id,)):
                    messagebox.showinfo("Success", "Professor inserted successfully!")

    def show_professors(self):
        rows = fetch_data("select ProfessorID, FirstName, LastName, Gender, BirthDate, FacultyID, Salary, ExitDate, ManagerID from Employee inner join Person on Person.PersonID = Employee.PersonID inner join Professor on Professor.EmployeeID = Employee.EmployeeID;")
        self.display_data(rows, ["ProfessorID", "FirstName", "LastName", "Gender", "BirthDate", "FacultyID", "Salary", "ExitDate", "ManagerID"])



    def create_worker_form(self):
        ttk.Label(self.tab_insert_worker, text="First Name").grid(row=0, column=0)
        self.worker_first_name = ttk.Entry(self.tab_insert_worker)
        self.worker_first_name.grid(row=0, column=1)

        ttk.Label(self.tab_insert_worker, text="Middle Name").grid(row=1, column=0)
        self.worker_mid_name = ttk.Entry(self.tab_insert_worker)
        self.worker_mid_name.grid(row=1, column=1)

        ttk.Label(self.tab_insert_worker, text="Last Name").grid(row=2, column=0)
        self.worker_last_name = ttk.Entry(self.tab_insert_worker)
        self.worker_last_name.grid(row=2, column=1)

        ttk.Label(self.tab_insert_worker, text="Gender").grid(row=3, column=0)
        self.worker_gender = ttk.Entry(self.tab_insert_worker)
        self.worker_gender.grid(row=3, column=1)

        ttk.Label(self.tab_insert_worker, text="Birth Date (YYYY-MM-DD)").grid(row=4, column=0)
        self.worker_birth_date = ttk.Entry(self.tab_insert_worker)
        self.worker_birth_date.grid(row=4, column=1)

        ttk.Label(self.tab_insert_worker, text="Salary").grid(row=5, column=0)
        self.worker_salary = ttk.Entry(self.tab_insert_worker)
        self.worker_salary.grid(row=5, column=1)

        ttk.Label(self.tab_insert_worker, text="Exit Date (YYYY-MM-DD)").grid(row=6, column=0)
        self.worker_exit_date = ttk.Entry(self.tab_insert_worker)
        self.worker_exit_date.grid(row=6, column=1)

        ttk.Label(self.tab_insert_worker, text="Manager ID").grid(row=7, column=0)
        self.worker_manager_id = ttk.Entry(self.tab_insert_worker)
        self.worker_manager_id.grid(row=7, column=1)

        ttk.Button(self.tab_insert_worker, text="Insert Worker", command=self.insert_worker).grid(row=8, column=0, columnspan=2)
        ttk.Button(self.tab_insert_worker, text="Show Workers", command=self.show_workers).grid(row=9, column=0, columnspan=2)

    def insert_worker(self):
        # Get data from fields
        first_name = self.worker_first_name.get()
        mid_name = self.worker_mid_name.get()
        last_name = self.worker_last_name.get()
        gender = self.worker_gender.get()
        birth_date = self.worker_birth_date.get()
        salary = self.worker_salary.get()
        exit_date = self.worker_exit_date.get()
        manager_id = self.worker_manager_id.get()

        # Insert into Person table first
        person_query = """
        INSERT INTO Person (FirstName, MidName, LastName, Gender, BirthDate, FacultyID)
        VALUES (?, ?, ?, ?, ?, NULL)"""
        if execute_query(person_query, (first_name, mid_name, last_name, gender, birth_date)):
            # Get last inserted PersonID
            conn = connect_to_db()
            cursor = conn.cursor()
            cursor.execute("SELECT SCOPE_IDENTITY()")
            person_id = cursor.fetchone()[0]
            conn.close()

            # Insert into Employee table
            employee_query = """
            INSERT INTO Employee (Salary, ExitDate, PersonID, ManagerID) VALUES (?, ?, ?, ?)"""
            if execute_query(employee_query, (salary, exit_date, person_id, manager_id)):
                # Get last inserted EmployeeID
                conn = connect_to_db()
                cursor = conn.cursor()
                cursor.execute("SELECT SCOPE_IDENTITY()")
                employee_id = cursor.fetchone()[0]
                conn.close()

                # Insert into Worker table
                worker_query = """
                INSERT INTO Worker (EmployeeID) VALUES (?)"""
                if execute_query(worker_query, (employee_id,)):
                    messagebox.showinfo("Success", "Worker inserted successfully!")

    def show_workers(self):
        rows = fetch_data("select WorkerID, FirstName, LastName, Gender, BirthDate, FacultyID, Salary, ExitDate from Employee  inner join Person on Person.PersonID = Employee.PersonID inner join Worker on Worker.EmployeeID = Employee.EmployeeID;")
        self.display_data(rows, ["WorkerID", "FirstName", "LastName", "Gender", "BirthDate", "FacultyID", "Salary", "ExitDate"])



    def create_admin_form(self):
        ttk.Label(self.tab_insert_admin, text="First Name").grid(row=0, column=0)
        self.admin_first_name = ttk.Entry(self.tab_insert_admin)
        self.admin_first_name.grid(row=0, column=1)

        ttk.Label(self.tab_insert_admin, text="Middle Name").grid(row=1, column=0)
        self.admin_mid_name = ttk.Entry(self.tab_insert_admin)
        self.admin_mid_name.grid(row=1, column=1)

        ttk.Label(self.tab_insert_admin, text="Last Name").grid(row=2, column=0)
        self.admin_last_name = ttk.Entry(self.tab_insert_admin)
        self.admin_last_name.grid(row=2, column=1)

        ttk.Label(self.tab_insert_admin, text="Gender").grid(row=3, column=0)
        self.admin_gender = ttk.Entry(self.tab_insert_admin)
        self.admin_gender.grid(row=3, column=1)

        ttk.Label(self.tab_insert_admin, text="Birth Date (YYYY-MM-DD)").grid(row=4, column=0)
        self.admin_birth_date = ttk.Entry(self.tab_insert_admin)
        self.admin_birth_date.grid(row=4, column=1)

        ttk.Label(self.tab_insert_admin, text="Salary").grid(row=5, column=0)
        self.admin_salary = ttk.Entry(self.tab_insert_admin)
        self.admin_salary.grid(row=5, column=1)

        ttk.Label(self.tab_insert_admin, text="Exit Date (YYYY-MM-DD)").grid(row=6, column=0)
        self.admin_exit_date = ttk.Entry(self.tab_insert_admin)
        self.admin_exit_date.grid(row=6, column=1)

        ttk.Label(self.tab_insert_admin, text="Manager ID").grid(row=7, column=0)
        self.admin_manager_id = ttk.Entry(self.tab_insert_admin)
        self.admin_manager_id.grid(row=7, column=1)

        ttk.Button(self.tab_insert_admin, text="Insert Administrator", command=self.insert_admin).grid(row=8, column=0, columnspan=2)
        ttk.Button(self.tab_insert_admin, text="Show Administrators", command=self.show_administrators).grid(row=9, column=0, columnspan=2)

    def insert_admin(self):
        # Get data from fields
        first_name = self.admin_first_name.get()
        mid_name = self.admin_mid_name.get()
        last_name = self.admin_last_name.get()
        gender = self.admin_gender.get()
        birth_date = self.admin_birth_date.get()
        salary = self.admin_salary.get()
        exit_date = self.admin_exit_date.get()
        manager_id = self.admin_manager_id.get()

        # Insert into Person table first
        person_query = """
        INSERT INTO Person (FirstName, MidName, LastName, Gender, BirthDate, FacultyID)
        VALUES (?, ?, ?, ?, ?, NULL)"""
        if execute_query(person_query, (first_name, mid_name, last_name, gender, birth_date)):
            # Get last inserted PersonID
            conn = connect_to_db()
            cursor = conn.cursor()
            cursor.execute("SELECT SCOPE_IDENTITY()")
            person_id = cursor.fetchone()[0]
            conn.close()

            # Insert into Employee table
            employee_query = """
            INSERT INTO Employee (Salary, ExitDate, PersonID, ManagerID) VALUES (?, ?, ?, ?)"""
            if execute_query(employee_query, (salary, exit_date, person_id, manager_id)):
                # Get last inserted EmployeeID
                conn = connect_to_db()
                cursor = conn.cursor()
                cursor.execute("SELECT SCOPE_IDENTITY()")
                employee_id = cursor.fetchone()[0]
                conn.close()

                # Insert into Administrator table
                admin_query = """
                INSERT INTO Administrator (EmployeeID) VALUES (?)"""
                if execute_query(admin_query, (employee_id,)):
                    messagebox.showinfo("Success", "Administrator inserted successfully!")
    
    def show_administrators(self):
        rows = fetch_data("select AdminstratorID, FirstName, LastName, Gender, BirthDate, FacultyID, Salary, ExitDate from Employee inner join Person on Person.PersonID = Employee.PersonID inner join Administrator on Administrator.EmployeeID = Employee.EmployeeID;")
        self.display_data(rows, ["AdminstratorID", "FirstName", "LastName", "Gender", "BirthDate", "FacultyID", "Salary", "ExitDate"])



if __name__ == "__main__":
    root = tk.Tk()
    app = UniversityApp(root)
    root.mainloop()
