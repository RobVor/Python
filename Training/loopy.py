mylist = [1,2,3,4,5]

for i in mylist:
    if i > 2:
        print(i)

password = ''
while password != 'python123':
    password = input("Please enter the password: ")
    if password == 'python123':
        print("Success")
    else:
        print("Please try again")

Names = ["James", "John", "Jack"]
emails = ["gmail", "hotmail", "yahoo"]

for i,j in zip(Names, emails):
    print(i,j)