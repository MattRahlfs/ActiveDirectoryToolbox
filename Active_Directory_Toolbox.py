import tkinter
import time
    

class ActiveDirectoryToolBox():
    
    
    def __init__(self) -> None:

        def clearFrame(frame):
            for widget in frame.winfo_children():
                widget.destroy()

        def adAccountMenuWidgets():
            clearFrame(self.mainFrame)
            titleLabel = tkinter.Label(self.mainFrame, text="Account Management", font=("Arial", 15))
            titleLabel.pack(pady=5)

            adAccountIdentityTextboxLabel = tkinter.Label(self.mainFrame, text="Account Identity", font=("Arial", 8))
            adAccountIdentityTextboxLabel.pack(side=tkinter.LEFT, padx=5)

            adAccountIdentityTextboxWidget = tkinter.Entry(self.mainFrame)
            adAccountIdentityTextboxWidget.pack()

            getAccount=tkinter.Button(self.mainFrame, text="acc info")
            getAccount.pack()

        
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



        adAccountMenuWidgets()                  
        self.rootCanvas.mainloop()
    
    

    


###########################################################################################################################
ActiveDirectoryToolBox()
