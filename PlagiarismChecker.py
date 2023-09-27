from tkinter import *
from tkinter import filedialog, messagebox
from difflib import SequenceMatcher

master = Tk()
master.title("Plagiarism Checker")
master.geometry("500x500")
master.configure(background="#B1D4E0")

file_list = []


def choose_file():
    global file_list
    if len(file_list) == 2:
        messagebox.showwarning(title="Warning", message="2 files already chosen.")
    else:
        path = filedialog.askopenfilename()
        if len(file_list) < 2:
            file_list.append(path)


def check_plagiarism():
    global file_list
    if len(file_list) < 2:
        messagebox.showerror(message="Select 2 files")
    else:
        with open(file_list[0]) as file1, open(file_list[1]) as file2:
            file1_data = file1.read()
            file2_data = file2.read()

            plag = SequenceMatcher(None, file1_data, file2_data).ratio()*100
            num = round(plag, 3)
            display_message = "Plagiarism Percentage: " + str(num)
            label2.config(text=display_message)


def clear():
    label2.config(text="")
    file_list.clear()


label1 = Label(master, bg="#B1D4E0", fg="#003060", text="Plagiarism Checker", font="Courier 20 bold")
label1.place(x=100, y=20)

button1 = Button(master, bg="#003060", fg="#B1D4E0", text="Choose File 1", font="Courier 14", relief=RAISED, command=choose_file)
button1.place(x=50, y=100)

button2 = Button(master, bg="#003060", fg="#B1D4E0", text="Choose File 2", font="Courier 14", relief=RAISED, command=choose_file)
button2.place(x=270, y=100)

button3 = Button(master, bg="#003060", fg="#B1D4E0", text="Check", font="Courier 14", relief=RAISED, command=check_plagiarism)
button3.place(x=160, y=180)

button4 = Button(master, bg="#003060", fg="#B1D4E0", text="Clear", font="Courier 14", relief=RAISED, command=clear)
button4.place(x=250, y=180)

label2 = Label(master, fg="#003060", font="Courier 14", width=34, height=3)
label2.place(x=50, y=260)

master.mainloop()
