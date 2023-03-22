#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
#Any code taken from other sources is referenced within my code solution.

#Student ID: 20200947

#Date: 04/12/2021

l=[0,20,40,60,80,100,120]
global c1
global c2
global c3
global c4
global c5
c1=0
c2=0
c3=0
c4=0
c5=0
def pass_user():
    global tot
    global p
    tot = 0
    p=121
    while(True and (p>120 or p not in l)):
        try:
            p = int(input("\nPlease enter your credits at pass: "))
            if(p not in l):
                print("Out of range")
                continue
            else: 
                tot = tot + p
            

        except ValueError:
            print("Integer required")
    return tot 
    return p
def defer_user():
    global tot
    global d
    d=121
    while(True and (d>120 or d not in l)):
        try:
            d = int(input("Please enter your credits at defer: "))
            if(d not in l):
                print("Out of range")
                continue
            else: 
                tot = tot + d
            

        except ValueError:
            print("Integer required")
            continue
    return tot
    return d
def fail_user():
    global tot
    global f
    f=121
    while(True and (f>120 or f not in l)):
        try:
            f = int(input("Please enter your credits at fail: "))
            if(f not in l):
                print("Out of range")
                continue
            else: 
                tot = tot + f
            

        except ValueError:
            print("Integer required")
            continue
    return tot
    return f
def total():
    global tot
    while(tot>120 or tot!=120 ):
        print("Total Incorrect")
        pass_user()
        defer_user()
        fail_user()
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
        print("\nPROGRESS")
        c1=c1+1
    else:
        if(p==100 and (d==20 or f==20)):
            print("\nPROGRESS(module trailer)")
            c2=c2+1
        else:
            if(p<100 and f<=60):
                print("\nDO NOT PROGRESS - module retriever")
                c3=c3+1
            else:
                if(p<100 and f>60):
                    print("\nEXCLUDE")
                    c4=c4+1
    c5=c1+c2+c3+c4
