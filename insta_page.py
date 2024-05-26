class User:
    def __init__(self, userName, password, fullName):
        self.userName = userName 
        self.password = password
        self.fullName = fullName
        self.followers = []
        self.following = []
        self.followRequestsSent = []
        self.followRequestsReceived = []
        self.posts = []
 
    def handlepostscreation(self):
        content = input("Enter the post content: ")
        self.posts.append(content)
        print("Post created successfully")
     
    def handlesviewpost(self):
        if len(self.posts) == 0:
            print("No post is created")
        else:
            i = 1
            for post in self.posts:
                print(f"post {i}: {post}")
                i += 1
                
    def handlesviewpostfollowing(self):
        if len(self.following) == 0:
            print("you are not following anyone")
            return
        psot_found = False
        for username in self.following:
            userObj = dataStore[username]
            print(f"post form {username}: ")
            i = 1
            for post in userObj.posts:
                print(f" {i}. {post}")
                i += 1
            post_found = True
        if not psot_found:
            print("No posts ara available by your following")
        
    def handlesviewpostfollowers(self):
        if len(self.followers) == 0:
            print("you have no followers")
            return
        
        post = False
        for username in self.followers:
            userObj = dataStore[username]
            print(f"post from {username}: ")
            i = 1
            for post in userObj.posts:
                print(f" {i}. {post}")
                i += 1
            post = True
        if not post:
            print("No posts ara available by your followers")
            
        
    def handleSendFollowRequests(self):
        otherUserName = input("Enter user-name to send follow request: ")
        if otherUserName not in dataStore:
            print("User doesn't exist")
            return 
 
        for userName in self.following:
            if userName == otherUserName:
                print("Already you are following")
                return
        self.followRequestsSent.append(otherUserName)
        otherUserObj = dataStore[otherUserName]
        otherUserObj.followRequestsReceived.append(self.userName)
        print("Follow request sent successfully")
 
    def handleAcceptFollowRequests(self):
        if len(self.followRequestsReceived) == 0:
            print("No follow requests got")
            return
 
        for userName in self.followRequestsReceived:
            print("Do you want to confirm request with id: ", userName)
            option = input("Enter y or n: ")
 
            if option == 'y':
                self.followers.append(userName)
                print("Accepted the request successfully")
            else:
                print("Deleted the follow request successfully")
        self.followRequestsReceived = []
 
    def printAllFollowersList(self):
        if len(self.followers) == 0:
            print("No followers")
            return 
 
        for userName in self.followers:
            print(userName)
 
    def printAllFollowingList(self):
        if len(self.following) == 0:
            print("No-one you are following")
            return 
 
        for userName in self.following:
            print(userName)
            
dataStore = {}
 
def displayAndHandleMainMenu(userName):
    while True:
        print("-----------------------------------------------------")
        print("1 - Put follow requests")
        print("2 - Accept follow requests")
        print("3 - Post something")
        print("4 - Print all followers list")
        print("5 - Print all following list")
        print("6 - The is Posts")
        print("7 - view the post by following")
        print("8 - view the post by followers")
        print("9 - Logout")
        option = int(input("Choose the option:"))
        print("-----------------------------------------------------")
        userObj = dataStore[userName]
 
        if option == 1:
            userObj.handleSendFollowRequests()
        elif option == 2:
            userObj.handleAcceptFollowRequests()
        elif option == 3:
            userObj.handlepostscreation()
        elif option == 4:
            userObj.printAllFollowersList()
        elif option == 5:
            userObj.printAllFollowingList()
        elif option == 6:
            userObj.handlesviewpost()
        elif option == 7:
            userObj.handlesviewpostfollowing()
        elif option == 8:
            userObj.handlesviewpostfollowers()
        elif option == 9:
            print("Loggedout successfully")
            break
        else:
            print("Choose appropriate option")
 
 
def handleLogin():
    print("Enter your login details")
    userName = input("Enter your user-name:")
    password = input("Enter your password:")
    if userName not in dataStore:
        print("Please sign-up first before logging in")
    else:
        print("Logged-in Successfully")
        displayAndHandleMainMenu(userName)
 
def handleSignup():
    print("Enter your details to create an account")
    fullName = input("Enter your full-name:")
    userName = input("Enter your user-name:")
    password = input("Enter your password:")
    if userName not in dataStore:
        newUser = User(userName, password, fullName)
        dataStore[userName] = newUser
        print("Account created Successfully")
    else:
        print("User-Name already exists")
 
 
 
while True:
    print("-----------------------------------------------------")
    print("1 - Login")
    print("2 - Singup")
    print("3 - Exit")
    option = int(input("Choose the option:"))
    print("-----------------------------------------------------")
 
    if option == 1: 
        handleLogin() 
    elif option == 2:
        handleSignup()
    elif option == 3:
        print("Thanks for using Instagram")
        exit(0)
    else:
        print("Choose appropriate option")