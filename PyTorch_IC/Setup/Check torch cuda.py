import torch
print("\033c") # Clear the screen/terminal
print("Is PyTorch avaialble and working?")
print("x = torch.rand(5, 3)")
x = torch.rand(5, 3)
print(str(x) + '\n')

print("Is cuda avaialble?")
print("torch.cuda.is_available()")
y = torch.cuda.is_available()
print(str(y) + '\n')
print("If both the above questions have been answered then PyTorch with cuda is avaialble and ready.")
