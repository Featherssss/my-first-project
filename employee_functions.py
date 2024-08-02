class Employee:
    """生成员工信息"""
    def __init__(self,first,last,salary):
        self.first_name = first.title()
        self.last_name = last.title()
        self.full_name = f"{self.first_name} {self.last_name}"
        self.salary = salary
        
    def show_info(self,):
        print(f"这是员工的信息：\n{self.full_name}\n{self.salary}")
        
    def give_raise(self,add=5000):
        self.salary += add