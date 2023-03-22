#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
#Any code taken from other sources is referenced within my code solution.

#Student ID: 20200947

#Date: 04/12/2021

l=[0,20,40,60,80,100,120]
pass_a=[]
defer_a=[]
fail_a=[]
temp_a=[]
tot = 0
c1=0
c2=0
c3=0
c4=0
c5=0

def pass_u():
    global p
    global pass_a
    p=121
    while(True and (p>120 or p not in l)):
        try:
            p = int(input("\nPlease enter your credits at pass: "))
            if(p not in l):
                print("Out of range")
                continue
                

            

        except ValueError:
            print("Integer required")
            continue
    pass_a.append(p)
    return p

    
def defer_u():
    global d
    global defer_a
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
    defer_a.append(d)
    return d


def fail_u():
    global f
    global fail_a
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
    fail_a.append(f)
    return f



def total():
    tot = p+d+f
    if(tot!=120 or tot>120):
        print(tot,"-","Total Incorrect")
        pass_u()
        defer_u()
        fail_u()
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
        temp_a.append("Progress")
        c1=c1+1
    else:
        if(p==100 and (d==20 or f==20)):
            print("PROGRESS(module trailer)")
            temp_a.append("PROGRESS(module trailer)")
            c2=c2+1
        else:
            if(p<100 and f<=60):
                print("DO NOT PROGRESS - module retriever")
                temp_a.append("DO NOT PROGRESS - module retriever")
                c3=c3+1
            else:
                if(p<100 and f>60):
                    print("EXCLUDE")
                    temp_a.append("EXCLUDE")
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
        pass_u()
        defer_u()
        fail_u()
        total()
        results()
        back()
    else:
        if(choice=="Q" or choice=="q"):
            print("\nHorizontal Histogram")
            for a in range(1):
                print("\nProgress"," ",f'{c1:02}', "  :", end=' ')#The " end=' ' " keyword prints the required number stars, according to the for loop, in one line.
                for b in range(c1):
                    print("*", end=' ')
                print("\nTrailer","  ", f'{c2:02}', "  :", end=' ')#The " f'{c2:02}' " keyword is the string formatter. This keyword in this command makes the output to be printed with 2 digits if it has a single digit.
                for c in range(c2):
                    print("*", end=' ')
                print("\nRetriever","", f'{c3:02}', "  :", end=' ')
                for d in range(c3):
                    print("*", end=' ')
                print("\nExcluded"," ", f'{c4:02}', "  :", end=' ')
                for e in range(c4):
                    print("*", end=' ')
            

        else:
            print("Invalid choice")
            back()



def v_histo():
    global c1
    global c2
    global c3
    global c4
    global c5
    print("\n")
    a = str(c1)
    b = str(c2)
    c = str(c3)
    d = str(c4)
    topics=['Progress',a,"|",'Trailer',b,"|",'Retriever',c,"|",'Excluded',d]
    print(' '.join(topics))
    for i in range(max(c1,c2,c3,c4)):
        print("     {0}          {1}            {2}             {3}" . format(
            '*' if i<c1 else " ",
            '*' if i<c2 else " ",
            '*' if i<c3 else " ",
            '*' if i<c4 else " "))
    print("\n")
    print(c5,"number of outcomes in total")

    

def lists():
    global temp_a
    global pass_a
    global defer_a
    global fail_a
    print("\n")
    length=len(pass_a)
    for count in range(length):
        print(temp_a[count]," ","-"," ",str(pass_a[count]),","," "+str(defer_a[count]),","," "+str(fail_a[count]))

