# Question 1
a=int(input("marks of the students"))
if a>80:
    print("Grade score A")
elif 60<a<80:
    print("Grade score B")
elif 50<a<60:
      print("Grade score C")
elif 45<a<50:
    print("Grade score D")
elif 25<a<45:
      print("Grade score E")
else:
      print( "Grade score F")


# Question 2
n1= int(input("Enter the year"))
if n1%4==0 or n1%100==0 and n1%400==0:
   print("is a leap year")
else:
    print("is not a leap year")


# Question 4
x = 200
for i in range(x):
    if i % 5 == 2:
        if i % 6 == 3:
            if i % 7 ==2:
                print(i, 'candies are in the bowl')






