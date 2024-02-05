# დავალება 17

# შემსრულებელი: გიორგი ცუცქირიძე

# ბიბლიოთეკების შემოტანა

## სავარჯიშო 1

# შექმენი კლასიm რომელსაც ექნება public, protected და private
# პარამეტრები. გამოიყენე @property დეკორატორი და ასევე შექმენი
# setter და  getter დეკორატორებიანი ფუნქციები პარამეტრებზე 
# წვდომისა და რედაქტირებისთვის.


class Employee:
    def __init__(self, emp_name, emp_lastname, emp_ID, emp_email):
        self.emp_name = emp_name
        self.emp_lastname = emp_lastname
        self._emp_ID = emp_ID
        self.__emp_email = emp_email

    @property
    def emp_ID(self):
        return self._emp_ID

    @emp_ID.setter
    def emp_ID(self, value):
        self._emp_ID = value

    @emp_ID.getter
    def emp_ID(self):
        print("getting infromation about employee's ID")
        return self._emp_ID

    @property
    def emp_email(self):
        return self.__emp_email
  
    @emp_email.setter
    def emp_email(self, value):
        assert "@" in value, "Enter correct email address!"
        self.__emp_email = value

    def print_emp_data(self):
        print(f"Name of the Employee: {self.emp_name}\n"
              f"Lastname of the Employee: {self.emp_lastname}\n"
              f"ID of the Employee: {self.emp_ID}\n"
              f"E-mail of the Employee: {self.__emp_email}\n"
              )

# შემოწმება

emp1 = Employee("Giorgi", "Tsutskiridze", "38001039110", "giorgi.tsu@gmail.com")
print(emp1.emp_name)
print(emp1.emp_ID)
emp1.emp_ID = "38001039111"
print(emp1.emp_ID)
print(emp1.emp_email)
# emp1.emp_email = "giorgi.tsugmail.com"  # Uncomment to check
emp1.print_emp_data()


## სავარჯიშო 2

# შექმენი მისი შვილობილი კლასი და შეუცვალე რაიმე არსებული მეთოდი.


class EmployeeDivision(Employee):

    def __init__(self, emp_name, emp_lastname, emp_ID, emp_email, emp_division):
        super().__init__(emp_name, emp_lastname, emp_ID, emp_email)
        self.emp_division = emp_division

    def print_emp_data(self):
        print(f"Name of the Employee: {self.emp_name}\n"
              f"Lastname of the Employee: {self.emp_lastname}\n"
              f"ID of the Employee: {self.emp_ID}\n"
              f"E-mail of the Employee: {self.emp_email}\n"
              f"Division of the Employee: {self.emp_division}\n"
               )

# შემოწმება

emp1 = EmployeeDivision("Beso", "Navrozashvili", "54006539220", "besarion.NVR@gmail.com", "HR")
emp1.print_emp_data()




#------------------------------------------------------------------#