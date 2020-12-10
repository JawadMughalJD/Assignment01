RollNo = []
Name = []
Age = []
Marks = []

n = int(input ("How many records you want to enter: "))
print(end="\n")

for i in range (0,n):
    rollno = (input("Enter Roll no: "))
    name = (input("Enter Name: "))
    age = int(input("Enter Age: "))

    marks = int(input("Enter Marks: "))
    while(marks > 100 or marks < 0):
        marks = int(input("Enter Marks Again: "))  

    print(end="\n")
    RollNo.append(rollno)
    Name.append(name)
    Age.append(age)
    Marks.append(marks)
 
print("Roll numbers: ",RollNo)
print("Names: ",Name)
print("Ages: ",Age)
print("Marks: ",Marks)

Average = sum(Marks)/len(Marks)
lowest = min(Marks)
highest = max(Marks)

print(end="\n")
print("Average marks are: ",Average)
print("Lowest marks are: ",lowest)
print("Highest marks are: ",highest)
