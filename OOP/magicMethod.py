# class Book():
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
    
#     def __str__(self) -> str:
#         return f"{self.title} by {self.author}"
    
#     def __len__(self):
#         return self.pages
    
#     def __del__(self):
#         print("A book object has been delete")

# b = Book("Python", "Bang", 20)

# print(b)
# del b







class Account():
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, def_amt):
        self.balance += def_amt
        print(f"Added {def_amt} to the balance")
 
    def withdrawal(self, wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print("Withdrawal accepted")
        else:
            print("Sorry not enough funds")

    def __str__(self) -> str:
        return f"Owner: {self.owner} \nBalance: {self.balance}"

a = Account("Bang", 500)
    
print(a.owner)
print(a.balance)

print(a)
print(a.deposit(100))

print(a.withdrawal(400))
print(a)