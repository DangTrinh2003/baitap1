import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg

win = tk.Tk()
win.title("Python GUI")



mighty = ttk.LabelFrame(win, text=' Mighty Python ')
mighty.grid(column=0, row=0, padx=8, pady=4)

ttk.Label(mighty, text="Enter a name:").grid(column=0, row=0, sticky='W')
name = tk.StringVar()
name_entered = ttk.Entry(mighty, width=12, textvariable=name)
name_entered.grid(column=0, row=1, sticky='W')

ttk.Label(mighty, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
number_chosen = ttk.Combobox(mighty, width=12, textvariable=number, state='readonly')
number_chosen['values'] = (1, 2, 4, 42, 100)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)

def click_me():
    action.configure(text=f'Hello {name.get()} {number.get()}')

action = ttk.Button(mighty, text="Click Me!", command=click_me)
action.grid(column=2, row=1)

chVarDis = tk.IntVar()
check1 = tk.Checkbutton(mighty, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(mighty, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(mighty, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)

COLOR1 = "Blue"
COLOR2 = "Gold"
COLOR3 = "Red"

radVar = tk.IntVar()
radVar.set(2)

def radCall():
    radSel = radVar.get()
    if radSel == 1:
        win.configure(background=COLOR1)
    elif radSel == 2:
        win.configure(background=COLOR2)
    elif radSel == 3:
        win.configure(background=COLOR3)

rad1 = tk.Radiobutton(mighty, text=COLOR1, variable=radVar, value=1, command=radCall)
rad1.grid(column=0, row=6, sticky=tk.W, columnspan=3)

rad2 = tk.Radiobutton(mighty, text=COLOR2, variable=radVar, value=2, command=radCall)
rad2.grid(column=1, row=6, sticky=tk.W, columnspan=3)

rad3 = tk.Radiobutton(mighty, text=COLOR3, variable=radVar, value=3, command=radCall)
rad3.grid(column=2, row=6, sticky=tk.W, columnspan=3)

scrol_w = 30
scrol_h = 3
scr = scrolledtext.ScrolledText(mighty, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, row=5, columnspan=3, padx=10, pady=10)



name_entered.focus()

# Creating a Menu Bar
menu_bar = Menu(win)
win.config(menu=menu_bar)

# Create menu and add menu items
file_menu = Menu(menu_bar, tearoff=0)  # create File menu
file_menu.add_command(label="New")  
menu_bar.add_cascade(label="File", menu=file_menu)  # add File menu to menu bar and give it a label
file_menu.add_separator()
file_menu.add_command(label="Exit", command=win.quit)




def _msgBox():  
    msg.showinfo('Python Message Info Box', 'A Python GUI created  using tkinter:\nThe year is 2019.')


# Add Help menu
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=_msgBox) #display message when clicked






# Thêm các buttons và chức năng tính toán
def calculate(operation):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if operation == 'add':
            result.set(num1 + num2)
        elif operation == 'subtract':
            result.set(num1 - num2)
        elif operation == 'multiply':
            result.set(num1 * num2)
        elif operation == 'divide':
            if num2 == 0:
                result.set("Error! Division by zero.")
            else:
                result.set(num1 / num2)
    except ValueError:
        result.set("Invalid Input")


calc_frame = ttk.LabelFrame(win, text="Simple Calculator")
calc_frame.grid(column=0, row=8, padx=8, pady=4)

# Labels and Entries
ttk.Label(calc_frame, text="Number 1:").grid(column=0, row=0, sticky=tk.W)
entry_num1 = ttk.Entry(calc_frame, width=10)
entry_num1.grid(column=1, row=0)

ttk.Label(calc_frame, text="Number 2:").grid(column=0, row=1, sticky=tk.W)
entry_num2 = ttk.Entry(calc_frame, width=10)
entry_num2.grid(column=1, row=1)

# Buttons for operations
ttk.Button(calc_frame, text="+", command=lambda: calculate('add')).grid(column=2, row=0)
ttk.Button(calc_frame, text="-", command=lambda: calculate('subtract')).grid(column=3, row=0)
ttk.Button(calc_frame, text="*", command=lambda: calculate('multiply')).grid(column=2, row=1)
ttk.Button(calc_frame, text="/", command=lambda: calculate('divide')).grid(column=3, row=1)

# Display result
result = tk.StringVar()
ttk.Label(calc_frame, text="Result:").grid(column=0, row=2, sticky=tk.W)
ttk.Label(calc_frame, textvariable=result).grid(column=1, row=2, sticky=tk.W)

# Thêm nút Reset để xóa các trường nhập và kết quả
def reset():
    entry_num1.delete(0, 'end')
    entry_num2.delete(0, 'end')
    result.set("")

# Thêm nút Reset trong phần máy tính
ttk.Button(calc_frame, text="Reset", command=reset).grid(column=4, row=0)


def change_theme(theme):
    style = ttk.Style()
    if theme == 'dark':
        style.theme_use('clam')
        win.configure(background='black')
    else:
        style.theme_use('default')
        win.configure(background='white')

# Thêm lựa chọn theme trong menu
theme_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Theme", menu=theme_menu)
theme_menu.add_command(label="Dark Mode", command=lambda: change_theme('dark'))
theme_menu.add_command(label="Light Mode", command=lambda: change_theme('light'))

win.mainloop()
