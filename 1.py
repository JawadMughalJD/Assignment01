Name = input("Enter your name: ")

a= len(Name)

for i in range (0,a):
    for j in range (0,i):
        print (" ", end=" ")
    print(Name[i])
    
for i in range (a-2,-1,-1):
    for j in range (0,i):
        print (" ", end=" ")
    print(Name[i])