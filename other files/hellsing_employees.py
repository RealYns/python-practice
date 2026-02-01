from employee import Employee

employee1 = Employee('walter', 'hellsing', 50000)
employee1.give_raise(6000)

print("First name:", employee1.first)
print("Last name:", employee1.last)
print("Annual salary:", employee1.salary)