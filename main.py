from tkinter import Tk, Entry, END, Button

root = Tk()

root.title("Basic Calculator")

# locking the size of window make it unchangeable
root.resizable(False, False)

# input field or Entry
display = Entry(root, width=42, borderwidth=3, bg='#322e2f', fg='#FFFFFF')
display.grid(row=0, column=0, columnspan=4, )


# adding string characters to Entry
def letter_add(letter):
    current = display.get()
    display.delete(0, END)
    display.insert(0, str(current) + str(letter))


# to delete all thing in Entry
def var_clear_all():
    display.delete(0, END)


# to delete one character from right
def clear_one():
    current = display.get()
    display.delete(0, END)
    display.insert(0, current[0:-1])


# using eval function to do the calculating
def calculating():
    current_num = display.get()
    answer = eval(current_num)
    display.delete(0, END)
    display.insert(0, str(answer))


# number buttons with the same function
button_1 = Button(root, borderwidth=3, text='1', font='bold', command=lambda: letter_add(1), bg='#e2d810', fg='#000000')
button_2 = Button(root, borderwidth=3, text='2', font='bold', command=lambda: letter_add(2), bg='#e2d810', fg='#000000')
button_3 = Button(root, borderwidth=3, text='3', font='bold', command=lambda: letter_add(3), bg='#e2d810', fg='#000000')
button_4 = Button(root, borderwidth=3, text='4', font='bold', command=lambda: letter_add(4), bg='#e2d810', fg='#000000')
button_5 = Button(root, borderwidth=3, text='5', font='bold', command=lambda: letter_add(5), bg='#e2d810', fg='#000000')
button_6 = Button(root, borderwidth=3, text='6', font='bold', command=lambda: letter_add(6), bg='#e2d810', fg='#000000')
button_7 = Button(root, borderwidth=3, text='7', font='bold', command=lambda: letter_add(7), bg='#e2d810', fg='#000000')
button_8 = Button(root, borderwidth=3, text='8', font='bold', command=lambda: letter_add(8), bg='#e2d810', fg='#000000')
button_9 = Button(root, borderwidth=3, text='9', font='bold', command=lambda: letter_add(9), bg='#e2d810', fg='#000000')
button_0 = Button(root, borderwidth=3, text='0', font='bold', command=lambda: letter_add(0), bg='#e2d810', fg='#000000')

# symbol buttons
button_plus = Button(root, borderwidth=3, text='+', font='bold', command=lambda: letter_add("+"), bg='#6b7b8c')
button_mines = Button(root, borderwidth=3, text='-', font='bold', command=lambda: letter_add("-"), bg='#6b7b8c')
button_decimal = Button(root, borderwidth=3, text='.', font='bold', command=lambda: letter_add("."), bg='#6b7b8c')
button_multi = Button(root, borderwidth=3, text='*', font='bold', command=lambda: letter_add("*"), bg='#6b7b8c')
button_div = Button(root, borderwidth=3, text='/', font='bold', command=lambda: letter_add("/"), bg='#6b7b8c')
# these buttons got different functions
button_clear = Button(root, borderwidth=3, text='AC', font='bold', command=var_clear_all, bg='#3b4d61', fg='#FFFFFF')
button_equal = Button(root, borderwidth=3, text='=', font='bold', command=calculating, bg='#3b4d61', fg='#FFFFFF')
button_clear_one = Button(root, borderwidth=3, text='C', font='bold', command=clear_one, bg='#3b4d61', fg='#FFFFFF')

# all the buttons to show
button_1.grid(row=3, column=0, ipadx=15, ipady=17, padx=2, pady=2)
button_2.grid(row=3, column=1, ipadx=15, ipady=17, padx=2, pady=2)
button_3.grid(row=3, column=2, ipadx=15, ipady=17, padx=2, pady=2)
button_4.grid(row=2, column=0, ipadx=15, ipady=17, padx=2, pady=2)
button_5.grid(row=2, column=1, ipadx=15, ipady=17, padx=2, pady=2)
button_6.grid(row=2, column=2, ipadx=15, ipady=17, padx=2, pady=2)
button_7.grid(row=1, column=0, ipadx=15, ipady=17, padx=2, pady=2)
button_8.grid(row=1, column=1, ipadx=15, ipady=17, padx=2, pady=2)
button_9.grid(row=1, column=2, ipadx=15, ipady=17, padx=2, pady=2)
button_0.grid(row=4, column=0, ipadx=15, ipady=17, padx=2, pady=2)

button_clear.grid(row=1, column=3, ipadx=10, ipady=57, padx=2, pady=2, rowspan=2)
button_plus.grid(row=4, column=1, ipadx=15, ipady=17, padx=2, pady=2)
button_mines.grid(row=4, column=2, ipadx=15, ipady=17, padx=2, pady=2)
button_multi.grid(row=4, column=3, ipadx=20, ipady=17, padx=2, pady=2)
button_equal.grid(row=5, column=2, ipadx=50, ipady=17, padx=2, pady=2, columnspan=3)
button_decimal.grid(row=5, column=0, ipadx=18, ipady=17, padx=2, pady=2)
button_clear_one.grid(row=3, column=3, ipadx=17, ipady=17, padx=2, pady=2)
button_div.grid(row=5, column=1, ipadx=18, ipady=17, padx=2, pady=2)

root.mainloop()
