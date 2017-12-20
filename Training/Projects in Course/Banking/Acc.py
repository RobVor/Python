"""Having a look at another approach to OOP classes"""

class BACC:
    """DocString: This creates a base class bank account."""

    def __init__(self, file_path):
        self.file_path = file_path
        with open(file_path, "r") as file:
            file.seek(0)
            self.balance = int(file.read())

    def Withdraw(self, amount):                     # Method
        self.balance -= amount

    def Deposit(self, amount):
        self.balance += amount

#    def Bank(self):                                # Method can close the file and write. Needs to be called
#        with open(self.file_path, "w") as file:
#            file.write(str(self.balance))

    def __del__(self):                              # __del__ can be used to close the file, but, since python 3.4 del terminates all built-in methods ## Destructor
                                                    # before closing, so this will fail on exits, but will work on clearing a class call
        with open(self.file_path, "w") as file:
            file.write(str(self.balance))

class CBACC(BACC):                                  # Inherited classes/Sub Class
    """ DocString: This class creates an Inherited bank account called 'checking' of the base class bank account"""

    AccType = "Checking"                            # Class variable/Attribute

    def __init__(self, file_path):                  # Constructor
        BACC.__init__(self, file_path)

    def Transfer(self, amount):                     # Sub Class method
        self.balance -= amount                      # Instance variables

### Calling the class
# Account = BACC("balance.txt")                     # Instantiation of a class
# print(Account.balance)

# Account.Withdraw(100)
# print(Account.balance)

# Account.Deposit(250)
# print(Account.balance)

#Account.Bank()                                     # Calling the close method to commit changes
# Account = None                                    # Clearing a class call by setting the object to none. This calls the __del__ method correctly.

### Inherited classes

CheckAccount = CBACC("balance.txt")                 # Instantiation of a class (Inherited)
print(CheckAccount.balance)

CheckAccount.Transfer(500)
print(CheckAccount.balance)

print(CheckAccount.AccType)
print(CheckAccount.__doc__)                         # Docstring call

CheckAccount = None