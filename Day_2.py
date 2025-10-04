Sum of two numbers (input).
num1=int(input("enter first number :"))
num2=int(input("enter second number :"))
sum=num1+num2
print("the sum of two number is :",sum)

# Even/Odd checker.

num=int(input("enter a number :"))
if num%2==0:
    print(num,"is even number ! ")
else:
    print(num,"is odd number !")

# Calculator: ask two numbers and an operator (+ - * / % // **) and print result (handle division by zero).


num1=int(input("enter first number : "))
num2=int(input("enter second number : "))
operater = input("enter operater (+ - * / % // **) :")
if operater=="+":
    print("the sum is :",num1+num2)
elif operater=="-":
    print("the subtraction is :",num1-num2)
elif operater=="*":
    print("the multiplication is :",num1*num2)
elif operater=="/":
    if num2 == 0:
        print("Error: Division by zero is not allowed!")
    else:
        print("The division is:", num1 / num2)
elif operater=="%":
    if num2 == 0:
        print ("Error: Modulus by zero is not allowed !")
    else:
        print("the modulus is :",num1%num2)
elif operater=="//":
    if num2==0:
        print("Error : florr division by zero is not aloowed ! ")
    else:
        print("the floor division is :",num1//num2)


elif operater=="**":
    print("the exponent is :",num1**num2)
else:
    print("invalid operater !")

# 4. Largest of three numbers (use if only, no max() builtin).
 
num1=int(input("enter first number : "))
num2=int(input("enter second number : "))
num3=int(input("enter third number : "))
if num1>num2 and num1>num3:
    print(num1,"is the largest number ! ")
elif num2>num1 and num2>num3:
    print (num2,"is the largest number ! ")
elif num3>num1 and num3>num2:
    print (num3,"is the largest number ! ")
else:
    print("all are equal ! ")



# 5. Grade calculator
marks=int(input("enter your marks out of 100 : "))
if marks>=90 and marks<=100:
    print("your grade is A+ ! ")
elif marks>100:
    print("invalid input marks ! ,marks shoul be between 0 to 100 ! ")
elif marks>=80 and marks<=90:
    print("your grade id A ! ")
elif marks>=70 and marks<=80:
    print("your grade is B ! ")
elif marks>=60 and marks<=70:
    print("your grade is c ! ")
elif marks>=50 and marks<=60:
    print("your grade is D ! ")
else:
    print("try next time ! good luck !")


# 6. Simple login simulator: store username, password variables and ask input, print success/fail.
username="hifzan"
password="hifzan123"
input_username=str(input("enter your username : "))
input_password=str(input("enter your password :  "))
if input_username==username and input_password==password:
    print("login sucessfull :")
if input_username!=username or input_password!=password:
     print("login fails ")

# 7. BMI calculator: input weight(kg) and height(m) → BMI = weight / (height**2) → print category.
input_weight=float(input("enter your weight in kg : "))
input_hieght=float(input("enter you hieght in meter : "))
BMI=input_weight/input_hieght**2
if BMI<18.5:
    print("your BMI is ",BMI,"and your underwight ! ")
elif BMI>=18.5 and BMI<24.9:
    print("your BMI is ",BMI, "and you normal weight ! ")
elif BMI>=25 and BMI<29.9:
    print("your BMI is ",BMI,"and you are overweight ! ")
elif BMI>=30:
    print("your BMI is ",BMI,"and you are obese ! ")

