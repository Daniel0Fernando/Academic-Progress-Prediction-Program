#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
#Any code taken from other sources is referenced within my code solution.

#Student ID: 20200947

#Date: 04/12/2021


l=[0,20,40,60,80,100,120]
global tot
global c1
global c2
global c3
global c4
global c5
tot = 0
c1=0
c2=0
c3=0
c4=0
c5=0

def pass_c():
    global p
    p=121
    while(True and (p>120 or p not in l)):
        try:
            p = int(input("\nPlease enter your credits at pass: "))
            if(p not in l):
                print("Out of range")
                continue

            

        except ValueError:
            print("Integer required")
    return p
def defer_c():
    global d
    d=121
    while(True and (d>120 or d not in l)):
        try:
            d = int(input("Please enter your credits at defer: "))
            if(d not in l):
                print("Out of range")
                continue

            

        except ValueError:
            print("Integer required")
            continue
    return d
def fail_c():
    global f
    f=121
    while(True and (f>120 or f not in l)):
        try:
            f = int(input("Please enter your credits at fail: "))
            if(f not in l):
                print("Out of range")
                continue

            

        except ValueError:
            print("Integer required")
            continue
    return f
def total():
    tot = p+d+f
    if(tot!=120 or tot>120):
        print(tot,"-","Total Incorrect")
        pass_c()
        defer_c()
        fail_c()
        total()

def results():
    global p
    global d
    global f
    global c1
    global c2
    global c3
    global c4
    global c5
    if(p==120):
        print("PROGRESS")
        c1=c1+1
    else:
        if(p==100 and (d==20 or f==20)):
            print("PROGRESS(module trailer)")
            c2=c2+1
        else:
            if(p<100 and f<=60):
                print("DO NOT PROGRESS - module retriever")
                c3=c3+1
            else:
                if(p<100 and f>60):
                    print("EXCLUDE")
                    c4=c4+1
    c5=c1+c2+c3+c4
def back():
    global c1
    global c2
    global c3
    global c4
    global c5
    print("---------------------------------------------------------------")
    print("\nWould you like to enter another set of data?\nEnter 'Y' for yes or 'Q' to quit and view results: ")
    print("REPLY WITH CAPITAL LETTERS")
    choice=input("\nEnter your choice Y or Q = ")
    if(choice=="Y" or choice=="y"):
        pass_c()
        defer_c()
        fail_c()
        total()
        results()
        back()
    else: 
        if(choice=="Q" or choice=="q"):
            print("\nHorizontal Histogram")
            for a in range(1):
                print("\nProgress"," ",f'{c1:02}', "  :", end=' ')
                for b in range(c1):
                    print("*", end=' ')
                print("\nTrailer","  ", f'{c2:02}', "  :", end=' ')
                for c in range(c2):
                    print("*", end=' ')
                print("\nRetriever","", f'{c3:02}', "  :", end=' ')
                for d in range(c3):
                    print("*", end=' ')
                print("\nExcluded"," ", f'{c4:02}', "  :", end=' ')
                for e in range(c4):
                    print("*", end=' ')
            print("\n")
            print("\n",c5,"outcomes in total")
        else:
            print("Invalid choice")
            back()
