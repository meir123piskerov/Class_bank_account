from BankAccount import BankAccount

user_1 = BankAccount("meir",8000)
user_2 = BankAccount("moti",10000)

user_1.__str__()
user_2.__str__()

transfer_money = user_2.transfer_funds(user_1,500)
print(user_1.__str__())
print(user_2.__str__())
