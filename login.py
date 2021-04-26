import json
import os
out_dict={}
dict2={}
dict1={}
list1=[]
if os.path.exists("userdetails.json"):
    pass
else:
    f=open("userdetails.json","x")
    f.close()
user=input("would you want to login/signup: ")
if user=="signup":
    name=input("enter your name: ")
    password=input("enter your password: ")
    l, u, p, d = 0, 0, 0, 0
    for i in password:
        if (i.islower()):
            l+=1      
        if (i.isupper()):
            u+=1     
        if (i.isdigit()):
            d+=1           
        if(i=='@'or i=='$' or i=='_'):
            p+=1
    try:
        with open("userdetails.json","r") as output :
            user_data=json.load(output)
            for i in user_data["userinfo"]:
                pass 
    except:
        pass  
    if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(password)):
        password2=input("enter your confirm password: ")
        if password==password2:
            if os.stat("userdetails.json").st_size==0:
            # if i["user_name"] != name   and  i["user_password"]!= password:
                print("You Signed Up Succsefully")
                discreaption=input("enter your discreaption=")
                gender=input("enter your sex")
                hobbies=input("enter your hobbies")
                birth=input("enter your date of b")
                dict2["description"]=discreaption
                dict2["hobbies"]=hobbies
                dict2["birth"]=birth
                dict2["gender"]=gender
                out_dict["user_name"]=name
                out_dict["user_password"]=password
                out_dict["profile"]=dict2
                list1.append(out_dict)
                dict1["userinfo"]=list1
                try:
                    with open("userdetails.json","r+")as f:
                        j=f.read()
                        fs=json.loads(j)
                        for i in fs:
                            if i == "userinfo":
                                s=fs[i]
                                s.append(out_dict.copy())
                                dict1["userinfo"]=s
                                json.dumps(dict1,f)
                                f.close()
                except:
                    with open("userdetails.json","w") as fil:
                        fil.write(json.dumps(dict1,indent=4))
            else:
                if i["user_name"] != name   and  i["user_password"]!= password:
                    print("You Signed Up Succsefully")
                    discreaption=input("enter your discreaption=")
                    gender=input("enter your sex")
                    hobbies=input("enter your hobbies")
                    birth=input("enter your date of b")
                    dict2["description"]=discreaption
                    dict2["hobbies"]=hobbies
                    dict2["birth"]=birth
                    dict2["gender"]=gender
                    out_dict["user_name"]=name
                    out_dict["user_password"]=password
                    out_dict["profile"]=dict2
                    list1.append(out_dict)
                    dict1["userinfo"]=list1
                    try:
                        with open("userdetails.json","r+")as f:
                            j=f.read()
                            fs=json.loads(j)
                            for i in fs:
                                if i == "userinfo":
                                    s=fs[i]
                                    s.append(out_dict.copy())
                                    dict1["userinfo"]=s
                                    json.dumps(dict1,f)
                                    f.close()
                    except:
                        with open("userdetails.json","w") as fil:
                            fil.write(json.dumps(dict1,indent=4))
                else:
                    print("Already Exsist")
                
        else:
            print("both password are wrong")
elif user == "login":
    name=input("enter your name: ")
    password=input("enter your password: ")
    with open("userdetails.json","r")as file1:
        data1=json.load(file1)
        for element in data1["userinfo"]:
            if element["user_name"]==name and element["user_password"]==password:
                print(name+"You Logged in Succesfully")
                print("PROFILE........")
                print("Username",name)
                print("gender",":",element["profile"]["gender"])
                print("Bio",":",element["profile"]["description"])
                print("Hobbie",":",element["profile"]["hobbies"])
                print("D_o_b",":",element["profile"]["birth"])
                break
        else:
            print("Password and Username are Invalid")
                





    
