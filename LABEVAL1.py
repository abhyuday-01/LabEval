
def add_c(contact):
    name=input("enter name:")
    phn=input("enter phn no.:")
    email=input("enter email(if no email enter *):")
    contact[name]=[phn,email]
    print("contact added")

def update_c(contact):
    name=input("enter name:")
    i=int(input("what you want to update?(0 for phone no., 1 for email)"))
    if i:
        e=input("enter email(if no email enter *):")
        contact[name][1]=e
    else:
        phn=input("enter phn no.:")
        contact[name][0]=phn
    print("contact updated")
    
def delete_c(contact):
    name=input("enter name:")
    contact.pop(name)
    print("contact deleted")

def list_c(contact):
    for i in contact.items():
        print(i)

def search_c(contact):
    i=int(input("what you want to search from?(0 for name, 1 for email):"))
    if i:
        e=input("enter email:")
        found=0
        for i in contact.keys():
            if contact[i][1]==e:
                print(i,contact[i])
                found=1
                break
        if found==0:
            print("Not found")
    else:
        name=input("enter name:")
        if name in contact.keys():
            print(name,contact[name])
        else:
            print("Not found")
            
def listByInitial(contact):
    a=input("enter initial alphabet")
    a=a.lower()
    for i in contact.keys():
        if i[0]==a or i[0]==a.upper():
            print(i,contact[i])

con={}
while True:
    i=int(input("Welcome \n What you want to do? \n 1. add contact \n 2. update contact \n 3. delete contact \n 4. list contact \n 5. search contact \n 6. list by initial\n enter index of task and 7 for exit\n"))
    if i==1:
        add_c(con)
    elif i==2:
        update_c(con)
    elif i==3:
        delete_c(con)
    elif i==4:
        list_c(con)
    elif i==5:
        search_c(con)
    elif i==6:
        listByInitial(con)
    elif i==7:
        break
    
                
