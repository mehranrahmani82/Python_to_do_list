class To_Do_List():
    def __init__(self):
        self.Do_list=[]
        self.Load_From_File()

    def Load_From_File(self):
        try:
            with open("SAVE.txt","r") as f:
                self.Do_list=[line.strip() for line in f.readlines()]
        except FileNotFoundError:
            print("the previous file not exist.please refresh it")
    def Create_Menu(self)-> int:
        f=open("Menu.txt","r")
        content=f.read()
        print(content)
        menu = {"0": self.Seen,"1":self.Access,"2":self.Create_Add,"3":self.Update_The_Unique,"4":self.Delete_The_Unique,"5":self.Insert_The_Unique}
        option=input("Please Enter Your DO_LIST\n")
        action=menu.get(option)
        if action:
            action()
        else:
            return -1
        return 0
    def Save_To_File(self):
        with open("SAVE.txt","w") as f:
            for item in self.Do_list:
                f.write(item+"\n")
    
    def Seen(self):
        if  self.Do_list:
            for priority, item in enumerate(self.Do_list):
                print("-"*30)
                print("|",f' Priority: {priority} ' ,f' Do {item} ',"|")
        else:
            print("You have nothing to do,please create the list")
        
        while True:
            x = input(
                " Please if you done wtih it, Push ENTER or push yes or y to continue\n ")
            if x=="":
                break
        return 0
    
    def Access(self):
        while True:
            if not self.Do_list:
                print("the list is empty please create it")
                break
                
            try:
                x=int(input("Please enter your priority to see it\n"))
            except ValueError:
                print("Please enter your valid priority")
                continue
                
            if -1<x<len(self.Do_list):
                print("the priority   ", f'{x} is ' ,self.Do_list[x])
                break
            else:
                print("the option may not exist or wrong Choose")
        return 0

    def Create_Add(self):
        while True:
            the_DO=input("Please enter your DO . If you not any more Dos please just push ENTER\n")
            if the_DO=="":
                break
            self.Do_list.append(the_DO)
            self.Save_To_File()
            
        return 0
    def Update_The_Unique(self):
        while True:
            if not self.Do_list:
                print("the list is empty please create it")
                break
            try:
                x=int(input("Please enter your priority to Updating\n"))
            except ValueError:
                print("Please enter your valid priority")
                continue
            if not -1 < x < len(self.Do_list):
                print("the option may not exist or wrong Choose")
                continue
            the_DO=input("Please enter your Do\n")
            self.Do_list[x]=the_DO
            self.Save_To_File()
            x = input(
                "If you not any more Update please just push ENTER. or push yes or y to continue\n")
            if x == "":
                break
        return 0

    def Delete_The_Unique(self):
        while True:
            if not self.Do_list:
                print("the list is empty please create it")
                break
            try:
                x=int(input("please enter your priority to Delete\n"))
            except:
                print("Please enter your valid priority")
                continue
            if not -1 < x < len(self.Do_list):
                print("the option may not exist or wrong Choose")
                continue
            the_DO=self.Do_list.pop(x)
            self.Save_To_File()
            print(f' the Priority {x} with Do { the_DO } was removed')
            x = input(
                " If you not any more Deleting please just push ENTER or push yes or y to continue\n")
            if x == "":
                break
        return 0
    def Insert_The_Unique(self):
        while True:
            try:
                x = int(input("please enter your priority to Insert\n"))
            except ValueError:
                print("Please enter your valid priority")
                continue
            if not -1 < x <= len(self.Do_list):
                print("the option may not exist or wrong Choose")
                continue
            the_new_DO=input("Pleae enter your NEW DO\n")
            self.Do_list.insert(x,the_new_DO)
            self.Save_To_File()
            x = input(
                " If you not any more Inserting please just push ENTER or push yes or y to continue\n")
            if x == "":
                break
        return 0
    
        
        

ob1=To_Do_List()

while True:
    req=ob1.Create_Menu()
    if req==-1:
        break