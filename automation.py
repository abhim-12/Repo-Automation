import time
from selenium import webdriver
from tkinter import *
from functools import partial
from tkinter.ttk import *

def runBrowser(uname,pwd,repo_name):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    driver = webdriver.Chrome('D:\Abhi\Drivers\chromedriver',options=options)
    driver.get('http://www.github.com/login')

    login = driver.find_element_by_id('login_field')
    time.sleep(5)
    login.send_keys(uname)

    password = driver.find_element_by_id('password')
    password.send_keys(pwd)
    password.submit()
    time.sleep(5)

    driver.get('http://www.github.com/new')
    repo_box = driver.find_element_by_id('repository_name')
    repo_box.send_keys(repo_name)
    time.sleep(5)  
    checkbox  = driver.find_element_by_id("repository_auto_init")
    checkbox.click()
    repo_box.submit()
    time.sleep(5)
    prog = "Success"                                                          
    driver.quit()    

def validateLogin(username, password,repo):
    runBrowser(username.get(),password.get(),repo.get())
    prog.set("Success")
    return

#window
tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('Github Login')
p1 = PhotoImage(file = 'git-logo.png') 
tkWindow.iconphoto(False,p1)

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)

#new repository name
repoLabel = Label(tkWindow,text="Repository Name").grid(row=2, column=0)  
repo = StringVar()
repoEntry = Entry(tkWindow, textvariable=repo).grid(row=2, column=1)

validateLogin = partial(validateLogin, username, password,repo)

#login button
createButton = Button(tkWindow, text="Create", command=validateLogin).grid(row=4, column=0)  

#Update completion
prog = StringVar()
progress = Label(tkWindow, textvariable=prog,font=('Helvetica', 16, 'bold')).grid(row=7, column=0)

tkWindow.mainloop()

   



