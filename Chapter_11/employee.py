class Employee:
    """Represent an employee"""
    def __init__(self, first, last, annual_salary):
        """Define the attributes"""
        self.first = first
        self.last = last
        self.annual_salary = annual_salary
    
    def give_raise(self, promotion: int = 5000):
        """Raise the annual salary"""
        
        self.annual_salary += promotion
        print(self.annual_salary)
