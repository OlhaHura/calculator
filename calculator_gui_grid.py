import tkinter as tk
import tkinter.font as tkFont

root = tk.Tk()

font_main = tkFont.Font(font="Courier", size=20)

frame_one = tk.Frame(root)
frame_one.grid(column=0, row=0)

frame_two = tk.Frame(root)
frame_two.grid(column=0, row=1)



all_row = []

def show_pressed_button(event, text):
    all_row.append(text)
    display.configure(text=all_row)

def button_equally_pressed(event):
    display.configure(text=eval(''.join(all_row)))
    all_row.clear()

def button_c_pressed(event):
    all_row.pop(-1)
    display.configure(text=all_row)


display = tk.Label(frame_one, bg='white', text='0', font=font_main, justify=tk.RIGHT, width=17)
display.grid(row=0, padx=1, pady=1)


button_c = tk.Button(frame_one, text='C', font=font_main, width=3, height=1)
button_c.bind("<Button-1>", button_c_pressed)
button_c.grid(column=3, row=0)


button_one = tk.Button(frame_two, text='1', font=font_main, width=3, height=1)
button_one.bind("<Button-1>", lambda event, text='1':show_pressed_button(event, text))
button_one.grid(column=0, row=4)


button_two = tk.Button(frame_two,text='2', font=font_main, width=3, height=1)
button_two.bind("<Button-1>", lambda event, text='2':show_pressed_button(event, text))
button_two.grid(column=1, row=4)


button_three = tk.Button(frame_two,text='3', font=font_main, width=3, height=1)
button_three.bind("<Button-1>", lambda event, text='3':show_pressed_button(event, text))
button_three.grid(column=2, row=4)


button_plus = tk.Button(frame_two,text='+', font=font_main, width=3, height=1)
button_plus.bind("<Button-1>", lambda event, text='+':show_pressed_button(event, text))
button_plus.grid(column=3, row=4)


button_four = tk.Button(frame_two,text='4', font=font_main, width=3, height=1)
button_four.bind("<Button-1>", lambda event, text='4':show_pressed_button(event, text))
button_four.grid(column=0, row=3)


button_five = tk.Button(frame_two,text='5', font=font_main, width=3, height=1)
button_five.bind("<Button-1>", lambda event, text='5':show_pressed_button(event, text))
button_five.grid(column=1, row=3)


button_six = tk.Button(frame_two,text='6', font=font_main, width=3, height=1)
button_six.bind("<Button-1>", lambda event, text='6':show_pressed_button(event, text))
button_six.grid(column=2, row=3)


button_minus = tk.Button(frame_two, text='-', font=font_main, width=3, height=1)
button_minus.bind("<Button-1>", lambda event, text='-':show_pressed_button(event, text))
button_minus.grid(column=3, row=3)


button_seven = tk.Button(frame_two, text='7', font=font_main, width=3, height=1)
button_seven.bind("<Button-1>", lambda event, text='7':show_pressed_button(event, text))
button_seven.grid(column=0, row=2)


button_eight = tk.Button(frame_two,text='8', font=font_main, width=3, height=1)
button_eight.bind("<Button-1>", lambda event, text='8':show_pressed_button(event, text))
button_eight.grid(column=1, row=2)


button_nine = tk.Button(frame_two,text='9', font=font_main, width=3, height=1)
button_nine.bind("<Button-1>", lambda event, text='9':show_pressed_button(event, text))
button_nine.grid(column=2, row=2)


button_multiply = tk.Button(frame_two,text='*', font=font_main, width=3, height=1)
button_multiply.bind("<Button-1>", lambda event, text='*':show_pressed_button(event, text))
button_multiply.grid(column=3, row=2)


button_zero = tk.Button(frame_two, text='0', font=font_main, width=3, height=1)
button_zero.bind("<Button-1>", lambda event, text='0':show_pressed_button(event, text))
button_zero.grid(column=0, row=5)


button_dot = tk.Button(frame_two, text='.', font=font_main, width=3, height=1)
button_dot.bind("<Button-1>", lambda event, text='.':show_pressed_button(event, text))
button_dot.grid(column=1, row=5)


button_equally = tk.Button(frame_two, text='=', font=font_main, bg='grey', width=3, height=1)
button_equally.bind("<Button-1>", button_equally_pressed)
button_equally.grid(column=2, row=5)


button_division = tk.Button(frame_two, text='/', font=font_main, width=3, height=1)
button_division.bind("<Button-1>", lambda event, text='/':show_pressed_button(event, text))
button_division.grid(column=3, row=5)




root.mainloop()
