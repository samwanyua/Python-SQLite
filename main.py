class Employee:

    def __init__(self, first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property # we're able to access 'email' like an attribute i.e emp_1.email .. instead of emp_1.email()
    def email(self):
        return f"{self.first}.{self.last}@email.com"
    
    @property
    def full_name(self):
        return f"{self.first} {self.last}"
    
    def __repr__(self):
        return f"Employee - {self.first}, {self.last}, {self.pay}"