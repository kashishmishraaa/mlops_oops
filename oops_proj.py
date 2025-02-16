class chatbook:
    __id=1
    def __init__(self):
        self.id=chatbook.__id
        chatbook.__id+=1
        self.__username="username"
        self.user_id=0
        self.user_id+=1
        self.password=""
        self.loggedin=False
        #self.menu()
    @staticmethod
    def get_id():
        return chatbook.__id
    @staticmethod
    def set_id(val):
        chatbook.__id=val
        return chatbook.__id

    def get_name(self):    #getter method
        return self.__username
    def set_name(self,value):  #setter value
        self.__username=value

    def menu(self):

        user_input=input("""welcome to chatbook, how would you like to proceed?
                         1.press 1 to signup
                         2. press 2 to signin
                         3. press 3 to write to post
                         4. press 4 to message a friend
                         5. press any other key to exit: """)
        if user_input=="1":
            self.signup()
        if user_input=="2":
            self.signin()
        elif user_input=="3":
            self.mypost()
        elif user_input=="4":
            self.sendmsg()
        else:
            exit()
    def signup(self):
        email=input("enter your email here: ")
        pswd=input("enter your password here: ")
        self.username=email
        self.password=pswd
        print("you have signed up successfully")
        print("\n")
        self.menu()
    def signin(self):
        if self.username=="" and self.password=="":
            print("please signup first by pressing 1 in the main menu")
        else:
            uname=input("please enter your email/username: ")
            pswd=input("please enter your password: ")
            if self.username==uname and self.password==pswd:
                print("you have logged in successfully !!")
                self.loggedin=True
            else:
                print("please enter correct username/password !")
        print("\n")
        self.menu()
    def mypost(self):
        if self.loggedin==True:
            text=input("enter your message here: ")
            print(f"following content has been posted: {text}")
        else:
            print("you need to signin first to post something")
        print("\n")
        self.menu()
    def sendmsg(self):
        if self.loggedin==True:
            text=input("enter your message here")
            frnd=input("whom to send the message?: ")
            print(f"your message has been sent to {frnd}")
        else:
            print("you need to signin first to post something")
        print("\n")
        self.menu() 

    
obj=chatbook()