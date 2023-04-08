import tkinter

def nothing():
    print("testing")
    


class ActiveDirectoryToolBox():
    
    def adAccountMenuCanvas():
        pass
    
    
    rootCanvas = tkinter.Tk()

    rootCanvas.title("AD Toolbox")
    rootCanvas.geometry('400x400')
    rootCanvas.resizable(False,False)
    rootCanvas.eval('tk::PlaceWindow . center')


    mainMenuNavBar = tkinter.Menu(rootCanvas)
    
    fileMenu = tkinter.Menu(mainMenuNavBar, tearoff=0)
    fileMenu.add_command(label="Save State", command=nothing)
    fileMenu.add_command(label="Notes", command=nothing)
    fileMenu.add_command(label="Exit", command=rootCanvas.quit)
    mainMenuNavBar.add_cascade(label="File", menu=fileMenu)
    
    
    mainMenuNavBar.add_command(label="Accounts", command=adAccountMenuCanvas)
    mainMenuNavBar.add_command(label="Computers", command=nothing)
    mainMenuNavBar.add_command(label="Groups", command=nothing)
    
    label = tkinter.Label(rootCanvas, text="hello world")
    label.pack()


    rootCanvas.config(menu=mainMenuNavBar)
    rootCanvas.mainloop()



###########################################################################################################################
ActiveDirectoryToolBox()
