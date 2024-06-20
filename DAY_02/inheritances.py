class faculty:
    def __init__(self,f_name,department,f_id):
        self.f_name=f_name
        self.department=department
        self.f_id=f_id
    
    def print_info(self):
        print("faculty information=",self.f_name,self.department,self.f_id)
obj=faculty("Ashish","computer_science",1001)
obj.print_info()


class cse(faculty):
    pass
obj1=cse("jyoti_mam","computer_science",1002)
obj1.print_info()
