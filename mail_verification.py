# Email verification --> using string

email = input("Enter the mail : ") #g@g.in abhi626508.com

k,j,d=0,0,0

if len(email)>=6:
    if email[0].isalpha():
        if ("@"in email) and (email.count("@")==1):
            if (email[-4]==".")^(email[-3]=="."):
                for i in email:
                    if i ==i.isspace():
                        k=1
                    elif i.isspace():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d==1
                        
                if k==1 or j==1 or d==1:
                    print("wrong Email") #5 
            else:
                print("Wrong email")  #4
        else:
            print("Wrong mail") #3
    else:
        print("Wrong mail") #2
else:
    print("Wrong mail")  #1