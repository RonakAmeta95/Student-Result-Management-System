def Marks_maths():
        while True:
            a=int(input("Enter the Marks of Mathematic    :"))
            if a<=100 and a>=0:
                print(a,"/100 Added in Mathematic")
                return a
                break
            else:
                print("Marks should be between 0 to 100")
        
def Marks_phy():
        while True:
            b=int(input("Enter the Marks of Physics       :"))
            if b<=100 and b>=0:
                print(b,"/100 Added in Physic")
                return b
                break
            else:
                print("Marks should be between 0 to 100")
  
def Marks_che():
        while True:
            c=int(input("Enter the Marks of Chemistry     :"))
            if c<=100 and c>=0:
                print(c,"/100 Added in Chemistry")
                return c
                break
            else:
                print("Marks should be between 0 to 100")

def grade(n):
    if n>=250 and n<=300:
        print("    Grade                         = A")
    elif n>=200 and n<=249:
        print("    Grade                         = B")
    elif n>=150 and n<=199:
        print("    Grade                         = C")
    elif n>=100 and n<=149:
        print("    Grade                         = D")
    else:
        print("    Grade                         = E")
        
def res(maths, phy, che):
    if maths >= 33 and phy >= 33 and che >= 33:
        print("    Result                        = PASS")
    else:
        print("    Result                        = FAIL")
        
stu_list=[]
while True:
    print("\n|||||||||||||||||||||--WELCOME--|||||||||||||||||||||||")
    print("|||  CHOOSE:                                        |||")
    print("|||  1. Enter the Data of the Student               |||")
    print("|||  2. Search the Result of the Student            |||")
    print("|||  3. Update the Result of the Student            |||")
    print("|||  4. Delete the Record of the Student            |||")
    print("|||  5. Exit                                        |||")
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||\n")
    ch=input("ENTER YOUR CHOICE:")
    if ch=="1":
        print("\n[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]")
        print("[[-------------------ENTER THE DATA-------------------]]")
        print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]\n")
        Name=input("Enter the Name of the Student    :").upper()
        cl=int(input("Enter the Class of the Student   :"))
        a = Marks_maths()
        b = Marks_phy()
        c = Marks_che()
        list=[Name,cl,a,b,c]
        stu_list.append(list)
    elif ch=="2":
        print("\n--------------------SEARCH RESULT----------------------\n")
        Name=input("Enter Name of the Student        :").upper()
        cl=int(input("Enter Class of the Student       :"))
        for i in stu_list:
            if i[0]==Name and i[1]==cl:
                    print("\n||||||||||||||||||||||||-RESULT-||||||||||||||||||||||||\n")
                    print("    Name of the Student           =",i[0])
                    print("    Class of the Student          =",i[1])
                    print("    Maths Marks of the Student    =",i[2])
                    print("    Physics Marks of the Student  =",i[3])
                    print("    Chemistry Marks of the Student=",i[4])
                    print("    Total Marks of the Student    =",i[2]+i[3]+i[4])
                    grade(i[2]+i[3]+i[4])
                    res(i[2],i[3],[4])
                    print("\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n")
                    print("\n")
                    break
        else:
                print("Data not found!!!!\n")
    elif ch=="3":
        print("\n------------------UPDATE THE RESULT --------------------\n")
        Name=input("\nEnter the Name of the Student    :").upper()
        cl=int(input("Enter the Class of the Student   :"))
        for i in range(0,len(stu_list)):
            l=stu_list[i]
            if l[0]==Name and l[1]==cl:
                a = Marks_maths()
                b = Marks_phy()
                c = Marks_che()
                list_u=[Name,cl,a,b,c]
                stu_list[i]=list_u
                break
        else:
            print("\nData not found!!!\n")
    elif ch=="4":
        print("\n------------------DELETE THE RECORD--------------------\n")
        Name=input("\nEnter the Name of the Student :").upper()
        cl=int(input("Enter the Class of the Student :"))
        for i in stu_list:
            if i[0]==Name and i[1]==cl:
                stu_list.remove(i)
                print("\nData deleted successfully!\n")
                break
        else:
            print("\nData not found!!!!\n")
    
    elif ch=="5":
        print("\n***********Thank You**************")
        break
    else:
        print("\nINVAILD CHOICE!!!\n")