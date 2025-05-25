class Employee:
    def __init__(self,name,salary,ssn):
         self.name = name       # public variable
         self._salary =  salary   #protected variable(semi private )
         self.__ssn = ssn #private variable not access outside the class

if __name__ == "__main__":
     emp = Employee("Saqib", 50000, "123-45-6789")
     #access public variable 
     print("Public variable :", emp.name)
     #access protected variable 
     print("Protected  variable :", emp._salary)
     #access private variable 
     try:
          print("Private  variable :", emp.__ssn)
     except AttributeError:
         print("cannot access private variable __ssn.")
     
     