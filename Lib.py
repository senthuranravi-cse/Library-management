
mBooks=[["1001"," A Brief History of Time-Stephen Hawking",3],["1002","The Universe in a Nutshell-Stephen Hawking",3],["1003","The Selfish Gene-Richard Dawkins",3],["1004","The History of Pi-Petre Peckmann",3],["1005","The Universal History of Numbers-Ifragh",3]]
mStudentDetail=[["CS01",[]],["CS02",[]],["CS03",[]],["CS04",[]],["CS05",[]],["CS06",[]],["CS07",[]],["CS08",[]],["CS09",[]],["CS10",[]]]

def detailBook(bn): #fun1
    for i in mBooks:
            for j in i:
                if bn == j :
                    print("Book Name and Author name: ",i[1])
                    print("Book Count : ",i[2])
                    return True
    return False

def lentBook(sid): #fun2
    for i in mStudentDetail:
            if sid.upper() == i[0] :
                bn=(input("Enter the Book Number : "))
                for j in mBooks :
                    if j[0] == bn :
                        if j[2] > 0 :
                            i[1].append(bn)
                            j[2] = j[2]-1
                            print("DONE!! Student",i[0],"take the Book.",bn)
                            return True
                        else :
                            print("Book",bn,"is not available in Library..!!")
                            return True
    return False

def returnBook(sid): #fun3
    for i in mStudentDetail:
            if sid.upper() == i[0] :
                bn=(input("Enter the Book Number : "))
                for j in mBooks :
                    if j[0] == bn :
                        if bn in i[1]:
                            i[1].remove(bn)
                            j[2] = j[2]+1
                            print("DONE!! Student",i[0],"return the Book.",bn)
                            return True
                        else :
                            print("Student",i[0],"already returned the Book..!!")
                            return True
    return False


print("======>>> Simple Library Management!! <<<=====")
while True : #infinite loop
    n=(input("\nMENU\n\n1.Book Details\n2.Lent Book\n3.Return Book\n"))
    if n=='1':
        bn=(input("Enter the Book Number : "))
        if not detailBook(bn) : # control goes to fun1
            print("ERROR : Invalid Book Number..!!")
    elif n=='2':
        sid=(input("Enter the Student ID : "))
        if not lentBook(sid) : # control goes to fun2
            print("ERROR : Invalid Book or Student Detail..!!")
    elif n=='3':
        sid=(input("Enter the Student ID : "))
        if not returnBook(sid) : # control goes to fun3
            print("ERROR : Invalid Book or Student Detail..!!")
    else:
        print("please choose correct option")
