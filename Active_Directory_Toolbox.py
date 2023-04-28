import tkinter
import time
import os
from pyad import *
    

class ActiveDirectoryToolBox():

    
    def __init__(self) -> None:

        environmentDomain = os.environ['userdnsdomain']

        def getADLoginCredentials(canvas):

            credentials = {'username': '', 'password': ''}

            def obtainDetails():
                credentials["username"] = loginUsernameTextbox.get()
                credentials['password'] = loginPasswordTextbox.get()
                pyad.set_defaults(ldap_server=environmentDomain, username=credentials['username'], password=credentials['password'])
                loginCredentialsPopUp.destroy()

            loginCredentialsPopUp = tkinter.Toplevel(canvas)
            loginCredentialsPopUp.geometry("220x150")
            loginCredentialsPopUp.resizable(False, False)
            loginCredentialsPopUp.title("Login")
            loginCredentialsPopUp.geometry(f'+{canvas.winfo_rootx()+80}+{canvas.winfo_rooty()+80}')
            

            credentialWidgetsFrame = tkinter.Frame(loginCredentialsPopUp, height=150, width=150, bg="#c7c7c7")
            credentialWidgetsFrame.pack(anchor="center", expand=True, fill="both")

            loginUsernameLabel = tkinter.Label(credentialWidgetsFrame, text="Username: ", font=("Arial", 10), bg="#c7c7c7")
            loginUsernameTextbox = tkinter.Entry(credentialWidgetsFrame)
            loginPasswordLabel = tkinter.Label(credentialWidgetsFrame, text="Psssword: ", font=("Arial", 10), bg="#c7c7c7")
            loginPasswordTextbox = tkinter.Entry(credentialWidgetsFrame, show='*')
            loginCredentialsAccept = tkinter.Button(credentialWidgetsFrame, text="Use Credentials", command=obtainDetails)

            loginUsernameLabel.pack()
            loginUsernameTextbox.pack()
            loginPasswordLabel.pack(pady=(10,0))
            loginPasswordTextbox.pack()
            loginCredentialsAccept.pack(pady=(10,5))


            
        

        def clearFrame(frame):
            for widget in frame.winfo_children():
                widget.destroy()

        def adAccountMenuWidgets():
            clearFrame(self.mainFrame)

            def verifyIdentityExists():
                try: 
                    print(adsearch.by_upn(f"{adAccountIdentityTextboxWidget.get()}@{environmentDomain}"))
                    return True
                except:
                    print ("Account not found")
                    return False

            def unlockIdenity():
                pass

            def disableIdenity():
                pass

            def createAlias():
                pass

            

            titleLabel = tkinter.Label(self.mainFrame, text="Account Management", font=("Arial", 15))
            titleLabel.pack(pady=5)

            adAccountIdentityTextboxLabel = tkinter.Label(self.mainFrame, text="Account Identity", font=("Arial", 8))
            adAccountIdentityTextboxLabel.pack(side=tkinter.LEFT)

            adAccountIdentityTextboxWidget = tkinter.Entry(self.mainFrame)
            adAccountIdentityTextboxWidget.pack(side=tkinter.LEFT)

            accountIdentityOptionsFrame = tkinter.Frame(height=50, width=370, bg="#c7c7c7", bd=2)
            accountIdentityOptionsFrame.pack(pady=5, anchor="center")

            unlockAccountButton = tkinter.Button(accountIdentityOptionsFrame, text="Unlock", command=unlockIdenity)
            unlockAccountButton.pack(side=tkinter.LEFT)

            diableAccountButton = tkinter.Button(accountIdentityOptionsFrame, text="Disable", command=disableIdenity)
            diableAccountButton.pack(side=tkinter.LEFT, padx=(5,5))

            createAliasButton = tkinter.Button(accountIdentityOptionsFrame, text="New Alias", command=createAlias)
            createAliasButton.pack(side=tkinter.LEFT)

            





        
        def adComputerMenuWidgets():
            clearFrame(self.mainFrame)

            titleLabel = tkinter.Label(self.mainFrame, text="Computer Management", font=("Arial", 15))
            titleLabel.pack()

        def adGroupMenuWidgets():
            clearFrame(self.mainFrame)

            titleLabel = tkinter.Label(self.mainFrame, text="Group Management", font=("Arial", 15))
            titleLabel.pack()

        def nothing():
            print("testing")


        self.rootCanvas = tkinter.Tk()

        self.rootCanvas.title("AD Toolbox")
        self.rootCanvas.geometry('400x400')
        self.rootCanvas.resizable(False,False)
        self.rootCanvas.eval('tk::PlaceWindow . center')


        self.mainFrame = tkinter.Frame(self.rootCanvas)
        self.mainFrame.pack()
        self.mainMenuNavBar = tkinter.Menu(self.rootCanvas)

        
        fileMenu = tkinter.Menu(self.mainMenuNavBar, tearoff=0)
        fileMenu.add_command(label="Save State", command=nothing)
        fileMenu.add_command(label="Notes", command=nothing)
        fileMenu.add_command(label="Exit", command=self.rootCanvas.quit)
        self.mainMenuNavBar.add_cascade(label="File", menu=fileMenu)

        
        
        self.mainMenuNavBar.add_command(label="Accounts", command=adAccountMenuWidgets)
        self.mainMenuNavBar.add_command(label="Computers", command=adComputerMenuWidgets)
        self.mainMenuNavBar.add_command(label="Groups", command=adGroupMenuWidgets)
        self.rootCanvas.config(menu=self.mainMenuNavBar)


        getADLoginCredentials(self.rootCanvas)        
        adAccountMenuWidgets()                  
        self.rootCanvas.mainloop()
    
    

    


###########################################################################################################################
ActiveDirectoryToolBox()
