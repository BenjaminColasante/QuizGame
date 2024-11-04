
import math
import random


def elementary_school_quiz(flag, n):

    ''' (number,number)->number
     Returns the number of questions answered correctly after given n, and flag.
     Precondition: flag is 0 or 1, n is 1 or 2
     '''
    if flag == 0:
        a = random.randint(0,10)
        b = random.randint(0,10)
        score = 0
        if n == 1:
            c = int(input("Question 1:\n2 to what is " + str(2**a) + " i.e. what is the result of log_2 (" + str(2**a) + ") "))
            if a == c:
                return score+1
            else:
                return 0
        elif n == 2:
            d = int(input("Question 1:\n2 to what is " + str(2**a) + " i.e. what is the result of log_2 (" + str(2**a) + ") "))
            e = int(input("Question 2:\n2 to what is " + str(2**b) + " i.e. what is the result of log_2 (" + str(2**b) + ") "))
            if a == d and b == e:
                return score+2
            elif a == d or b == e:
                return score+1
            else:
                return score
    elif flag == 1:
        a = random.randint(0,10)
        b = random.randint(0,10)
        score = 0
        if n == 1:
            c = int(input("Question 1:\nWhat is the result of 2^"+str(a)+"? "))
            if c == 2**a:
                return score+1
            else:
                return 0
        elif n == 2:
            d = int(input("Question 1:\nWhat is the result of 2^"+str(a)+"? "))
            e = int(input("Question 2:\nWhat is the result of 2^"+str(b)+"? "))
            if d == 2**a and e == 2**b:
                return score+2
            elif d == 2**a or e == 2**b:
                return score+1
            else:
                return score
        
        



def high_school_quiz(a,b,c):

    ''' (number,number,number)->None
     Prints the solutions to the quadratic equation with given, a, b, and c
     Precondition: None
     '''
    if a == 0:
        if b == 0:
            if c == 0:
                print("The quadratic equation 0.0·x + 0.0 = 0\nis satisfied for all numbers x")
            else:
                print("The quadratic equation 0.0·x + "+str(c)+" = 0\nis satisfied for no numbers x")
        else:
            x = -c/b
            print("The linear equation "+str(b)+"·x + "+str(c)+" = 0\nhas the following root/solution: "+str(x))
    else:
        d = b**2 - 4*a*c
        if d > 0:
            root1 = (-b+(math.sqrt((b**2)-(4)*(a)*(c))))/(2*a)
            root2 = (-b-(math.sqrt((b**2)-(4)*(a)*(c))))/(2*a)
            print("The quadratic equation "+str(a)+"·x^2 + "+str(b)+"·x + "+str(c)+" = 0\nhas the following real roots:\n"+str(root1)+" and "+str(root2))
        elif d == 0:
            root1 = -b/(2*a)
            print("The quadratic equation "+str(a)+"·x^2 + "+str(b)+"·x + "+str(c)+" = 0\nhas only one solution, a real root:\n"+str(root1))
        else:
            root1 = (math.sqrt(-(b**2-4*a*c)))/(2*a)
            root2 = -b/(2*a)
            print("The quadratic equation "+str(a)+"·x^2 + "+str(b)+"·x + "+str(c)+" = 0\nhas the following two complex roots:\n"+str(root2)+" + i "+str(root1)+"\nand\n"+str(root2)+" - i "+str(root1))


print("*******************************************")
print("*                                         *")
print("*  __Welcome to my math quiz-generator__  *")
print("*                                         *")
print("*******************************************\n")

name=input("What is your name? ")

status=input("Hi "+name+". Are you in? Enter \n1 for elementary school\n2 for high school or\n3 or other character(s) for none of the above?\n")

if status=='1':

    top_edge = ((len(name)+72)*"*")
    side_edge = ("* " + ((len(name)+68))*" " + " *")
    print("")
    print(top_edge)
    print(side_edge)
    print("*  __" + name + ", welcome to my quiz-generator for elementary school students.__  *")
    print(side_edge)
    print(str(top_edge) + "\n")

    flag = int(input(str(name)+" what would you like to practice? Enter\n0 for inverse of exponentiation\n1 for exponentiation\n"))
    if flag == 0:
        n = int(input("How many practice questions would you like to do? Enter 0, 1, or 2: "))
        if n == 1:
            print(str(name)+", here is your 1 question:")
            result = elementary_school_quiz(flag, n)
            if result == 1:
                print("Congratulations "+str(name)+"! You'll probably get an A tomorrow.")
            else:
                print("I think you need some more practice "+str(name)+".")
        elif n == 2:
            print(str(name)+", here is your 2 questions:")
            result = elementary_school_quiz(flag, n)
            if result == 2:
                print("Congratulations "+str(name)+"! You'll probably get an A tomorrow.")
            elif result == 1:
                print("You did ok "+str(name)+", but I know you can do better.")
            else:
                print("I think you need some more practice "+str(name)+".")
        elif n == 0:
            print("Zero questions. OK. Goodbye")
        else:
            print("Only 0,1, or 2 are valid choices for the number of questions.")


    elif flag == 1:
        n = int(input("How many practice questions would you like to do? Enter 0, 1, or 2: "))
        if n == 1:
            print(str(name)+", here is your 1 question:")
            result = elementary_school_quiz(flag, n)
            if result == 1:
                print("Congratulations "+str(name)+"! You'll probably get an A tomorrow.")
            else:
                print("I think you need some more practice "+str(name)+".")
        elif n == 2:
            print(str(name)+", here is your 2 questions:")
            result = elementary_school_quiz(flag, n)
            if result == 2:
                print("Congratulations "+str(name)+"! You'll probably get an A tomorrow.")
            elif result == 1:
                print("You did ok "+str(name)+", but I know you can do better.")
            else:
                print("I think you need some more practice "+str(name)+".")
        elif n == 0:
            print("Zero questions. OK. Goodbye")
        else:
            print("Only 0,1, or 2 are valid choices for the number of questions.")
    else:
        print("Invalid choice. Only 0 or 1 is accepted.")
            
            

            
            

elif status=='2':

    top_edge = ((len(name)+61)*"*")
    side_edge = ("* " + ((len(name)+57))*" " + " *")
    print("")
    print(top_edge)
    print(side_edge)
    print("*  __quadratic equation, a·x^2 + b·x + c= 0, solver for " + str(name)+"__  *")
    print(side_edge)
    print(str(top_edge) + "\n")
    
    flag=True
    while flag:
        question= input(name.strip() +", would you like a quadratic equation solved? ")

        question = question.lower().strip()

        if question!="yes":
            flag=False
        else:
            print("Good choice!")

            a = float(input("Enter a number the coefficient a: "))
            b = float(input("Enter a number the coefficient b: "))
            c = float(input("Enter a number the coefficient c: "))
            result = high_school_quiz(a,b,c)
 
else:

    print(str(name)+" you are not a target audience for this software.")

print("Good bye "+name+"!")
