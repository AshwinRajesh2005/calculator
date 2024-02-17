
def addition(a,b):
    return a+b
def subraction(a,b):
    return a-b
def multipication(a,b):
    return a*b
def division(a,b):
    return a//b
while True:
    print("\n CALCULATOR")
    print("1. addition")
    print("2. subrsction")
    print("3. multipication")
    print("4. division")
    print("5. EXIT")
    choice_the_number_to_solve=input("enter the artimetic operation number:")

    if choice_the_number_to_solve=='1':
         a=int(input("enter the a number:"))
         b=int(input("enter the b number:"))
         print(str(a)+"+"+str(b)+"="+str(addition(a,b)))
    elif choice_the_number_to_solve=='2':
         a=int(input("enter the a number:"))
         b=int(input("enter the b number:"))
         print(str(a)+"-"+str(b)+"="+str(subraction(a,b)))
    elif choice_the_number_to_solve=='3':
         a=int(input("enter the a number:"))
         b=int(input("enter the b number:"))
         print(str(a)+"*"+str(b)+"="+str(multipication(a,b)))
    elif choice_the_number_to_solve=='4':
         a=int(input("enter the a number:"))
         b=int(input("enter the b number:"))
         print(str(a)+"/"+str(b)+"="+str(divison(a,b)))
    elif choice_the_number_to_solve=='5':
         print("thanks you and please visit again")
    else:
         print("invalid option try again")
