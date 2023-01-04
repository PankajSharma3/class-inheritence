# class Employee():
#     no_of_leaves=8
#     def __init__(self,name,salary,role):
#         self.name=name
#         self.salary=salary
#         self.role=role
#     @classmethod
#     def f(cls,leaves):
#         cls.no_of_leaves=leaves
# class p(Employee):
#     pass     
# harry=Employee("Harry",255,"Instructor")
# rohan=Employee("Rohan",223,"Instructor")
# pankaj=Employee("Pankaj",223,"Instructor")
# print(pankaj.name)
class Electronics():
    a=100
    print(a,"is number of elsctronic devices used")
class Pocket(Electronics):
    b=12
    print(b,"is inserted in the pocket")
class Phone(Pocket):
    c="Apple"
    print(c,"This is inserted in the pocket")
pankaj=Electronics()
akash=Pocket()
ankit=Phone()
print(akash.b)