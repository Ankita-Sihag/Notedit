# ----------------------------------- NOTEDIT ---------------------------------------

import os
from tkinter import *
from tkinter import filedialog, messagebox, simpledialog, colorchooser, ttk, font
from tkinter.font import Font
from PIL import Image, ImageTk

# The current file name
file_name = ""


# ----------------------------------- FILE MENU FUNCTIONS ---------------------------------------


def new_file(event=None):
    global file_name
    ans = messagebox.askquestion("Save file", "Would you like to save this file ? ")
    if ans == "yes":
        save()
    text_area.delete(1.0, END)
    file_name = ""
    root.title("Untitled.txt - Notedit")


def open_file(event=None):
    global file_name
    opened_file = filedialog.askopenfile(title="Select the file to open",
                                         filetypes=(("Text File", "*.txt"), ("All Files", "*.*")))
    if opened_file is not None:
        text_area.delete(1.0, END)
        for line in opened_file:
            text_area.insert(END, line)
        file_name = opened_file.name
        display_name = opened_file.name.split("/")[-1]
        root.title(display_name + " - Notedit")
        opened_file.close()


def save(event=None):
    global file_name
    if file_name == "":
        save_as()
    else:
        file = open(file_name, "w+")
        file.write(text_area.get(1.0, END))
        file.close()


def save_as(event=None):
    global file_name
    file = filedialog.asksaveasfile(defaultextension=".txt",
                                    filetypes=(("Text File", "*.txt"), ("All Files", "*.*")))
    if file is None:
        return
    file_name = file.name
    display_name = str(file.name).split("/")[-1]

    root.title(display_name + " - Notedit")
    file.write(text_area.get("1.0", END))
    file.close()


def rename_file(event=None):
    global file_name
    if file_name == "":
        open_file()

    arr = file_name.split('/')
    path = ""
    for i in range(0, len(arr) - 1):
        path = path + arr[i] + '/'

    new_name = simpledialog.askstring("Rename", "Enter new name")
    if not new_name:
        return
    os.rename(file_name, str(path) + str(new_name))
    root.title(new_name + " - Notedit")


def close(event=None):
    root.quit()


# ----------------------------------- EDIT MENU FUNCTIONS ---------------------------------------


def cut(event=None):
    try:
        copy()
        text_area.delete(index1=SEL_FIRST, index2=SEL_LAST)
    except:
        pass


def copy(event=None):
    try:
        text_area.clipboard_clear()
        text_area.clipboard_append(string=text_area.selection_get())
    except:
        pass


def paste(event=None):
    try:
        print("in paste", text_area.clipboard_get())
        text_area.insert(INSERT, text_area.clipboard_get())
    except Exception as e:
        print(e)


def undo(event=None):
    try:
        text_area.edit_undo()
    except:
        pass


def redo(event=None):
    try:
        text_area.edit_redo()
    except:
        pass


# ----------------------------------- HELP MENU FUNCTIONS ---------------------------------------


def shortcuts():
    window = Toplevel(root)
    window.title("Shortcuts")
    window.geometry("330x500+60+50")
    window.resizable(False, False)

    heading_label = Label(window, text="Shortcuts", padx=100, pady=20,
                          font=Font(family="Candara", size=16, underline=1))
    heading_label.grid(columnspan=2)

    # New File
    new_name = Label(window, text="New", padx=40, pady=10)
    new_name.grid(row=1, column=0)
    new_shortcut = Label(window, text="Ctrl + N")
    new_shortcut.grid(row=1, column=1)

    # Open File
    open_name = Label(window, text="Open", padx=40)
    open_name.grid(row=2, column=0)
    open_shortcut = Label(window, text="Ctrl + O")
    open_shortcut.grid(row=2, column=1)

    # Save
    save_name = Label(window, text="Save", padx=40, pady=10)
    save_name.grid(row=3, column=0)
    save_shortcut = Label(window, text="Ctrl + S")
    save_shortcut.grid(row=3, column=1)

    # Save As
    save_as_name = Label(window, text="Save As", padx=40)
    save_as_name.grid(row=4, column=0)
    save_as_shortcut = Label(window, text="Ctrl + Shift + S")
    save_as_shortcut.grid(row=4, column=1)

    # Cut
    cut_name = Label(window, text="Cut", padx=40, pady=10)
    cut_name.grid(row=5, column=0)
    cut_shortcut = Label(window, text="Ctrl + X")
    cut_shortcut.grid(row=5, column=1)

    # Copy
    copy_name = Label(window, text="Copy", padx=40)
    copy_name.grid(row=6, column=0)
    copy_shortcut = Label(window, text="Ctrl + C")
    copy_shortcut.grid(row=6, column=1)

    # Paste
    paste_name = Label(window, text="Paste", padx=40, pady=10)
    paste_name.grid(row=7, column=0)
    paste_shortcut = Label(window, text="Ctrl + V")
    paste_shortcut.grid(row=7, column=1)

    # Align left
    left_name = Label(window, text="Align Left", padx=40)
    left_name.grid(row=8, column=0)
    left_shortcut = Label(window, text="Ctrl + Shift + L")
    left_shortcut.grid(row=8, column=1)

    # Align center
    center_name = Label(window, text="Align Center", padx=40, pady=10)
    center_name.grid(row=9, column=0)
    center_shortcut = Label(window, text="Ctrl + Shift + C")
    center_shortcut.grid(row=9, column=1)

    # Align right
    right_name = Label(window, text="Align Right", padx=40)
    right_name.grid(row=10, column=0)
    right_shortcut = Label(window, text="Ctrl + Shift + R")
    right_shortcut.grid(row=10, column=1)

    # Find
    find_name = Label(window, text="Find", padx=40, pady=10)
    find_name.grid(row=11, column=0)
    find_shortcut = Label(window, text="Ctrl + F")
    find_shortcut.grid(row=11, column=1)

    # Replace
    replace_name = Label(window, text="Replace", padx=40)
    replace_name.grid(row=12, column=0)
    replace_shortcut = Label(window, text="Ctrl + R")
    replace_shortcut.grid(row=12, column=1)

    # Exit
    exit_name = Label(window, text="Exit", padx=40, pady=10)
    exit_name.grid(row=13, column=0)
    exit_shortcut = Label(window, text="Alt + F4")
    exit_shortcut.grid(row=13, column=1)


def about():
    window = Toplevel(root)
    window.title("About")
    window.geometry("310x300+60+50")
    window.resizable(False, False)

    text1 = Label(window, justify=CENTER,
                  text="This is a text editor made\n using Tkinter module\n of Python.",
                  pady=50, font="Calibri 15")
    text1.pack()

    text2 = Label(window, justify=CENTER, text="Coded by: ", font="Candara 15")
    text2.pack()

    text3 = Label(window, justify=CENTER, text="Ankita Sihag", font="Candara 15")
    text3.pack()


# ----------------------------------- TOOLS FUNCTIONS ---------------------------------------


def find(event=None):
    value_to_find = simpledialog.askstring("Find", "Enter the text to search")
    if not value_to_find:
        return

    text_area.tag_remove('highlight', '1.0', END)
    text_area.tag_config('highlight', foreground='red')
    list_of_words = value_to_find.split(' ')
    for word in list_of_words:
        index = '1.0'
        while index:
            index = text_area.search(word, index, nocase=1, stopindex=END)
            if index:
                last_index = '%s+%dc' % (index, len(word))
                text_area.tag_add('highlight', index, last_index)
                index = last_index


def perform_replace(window, old_text, new_text, event=None):
    if old_text == "":
        window.destroy()
        return
    index = '1.0'
    while index:
        index = text_area.search(old_text, index, nocase=1, stopindex=END)
        if index:
            last_index = '%s+%dc' % (index, len(old_text))
            text_area.delete(index, last_index)
            text_area.insert(index, new_text)
            index = last_index
    window.destroy()


def replace(event=None):
    window = Toplevel(root)
    window.title("Replace")
    window.geometry("300x300+400+200")

    old_label = Label(window, text="Enter the text to be replaced: ", font="Calibri 12", padx=10, pady=20)
    old_label.pack()
    old_input = Entry(window, font="Calibri 12")
    old_input.pack()
    old_input.focus()

    new_label = Label(window, text="Enter the new text: ", font="Calibri 12", padx=10, pady=20)
    new_label.pack()
    new_input = Entry(window, font="Calibri 12")
    new_input.pack()

    bottom_frame = Frame(window, padx=10, pady=20)
    bottom_frame.pack()
    ok_button = Button(bottom_frame, text="Ok", font="Calibri 12", borderwidth=2, padx=10,
                       command=lambda: perform_replace(window, old_input.get(), new_input.get()))
    ok_button.grid(row=0, column=0, padx=10)
    window.bind('<Return>', lambda x: perform_replace(window, old_input.get(), new_input.get(), x))

    cancel_button = Button(bottom_frame, text="Cancel", font="Calibri 12", borderwidth=2, command=window.destroy)
    cancel_button.grid(row=0, column=1, padx=10)


def enter_tool(name, shortcut, event=None):
    tool_hover_name.config(text=name)
    tool_hover_shortcut.config(text=shortcut)


def leave_tool(event=None):
    tool_hover_name.config(text="")
    tool_hover_shortcut.config(text="")


# ----------------------------------- FORMAT FUNCTIONS ---------------------------------------


def change_font(event=None):
    text_area.config(font=Font(family=font_family.get(), size=size.get()))


def change_size(event=None):
    text_area.config(font=Font(family=font_family.get(), size=size.get()))


def change_text_color():
    color = colorchooser.askcolor(title="Choose text color", initialcolor="black")[1]
    text_area.config(foreground=color)
    text_area.config(insertbackground=color)


def change_background_color():
    color = colorchooser.askcolor(title="Choose background color", initialcolor="white")[1]
    text_area.config(background=color)


def remove_align_tags():
    align_tags = text_area.tag_names()
    if "CENTER" in align_tags:
        text_area.tag_remove("CENTER", "1.0", END)
    if "LEFT" in align_tags:
        text_area.tag_remove("LEFT", "1.0", END)
    if "RIGHT" in align_tags:
        text_area.tag_remove("RIGHT", "1.0", END)


def left_align(event=None):
    remove_align_tags()
    text_area.tag_configure("LEFT", justify="left")
    text_area.tag_add("LEFT", 1.0, END)


def center_align(event=None):
    remove_align_tags()
    text_area.tag_configure("CENTER", justify="center")
    text_area.tag_add("CENTER", 1.0, END)


def right_align(event=None):
    remove_align_tags()
    text_area.tag_configure("RIGHT", justify="right")
    text_area.tag_add("RIGHT", 1.0, END)


def enter_format_button(name, shortcut, event=None):
    format_hover_name.config(text=name)
    format_hover_shortcut.config(text=shortcut)


def leave_format_button(event=None):
    format_hover_name.config(text="")
    format_hover_shortcut.config(text="")


# ----------------------------------- ROOT ---------------------------------------


root = Tk()

root.title("Untitled - Notedit")
root.geometry("550x500+320+60")

# ----------------------------------- MENU ---------------------------------------


main_menu = Menu(root)
root.config(menu=main_menu)

# ----------------------------------- FILE MENU ---------------------------------------


file_menu = Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="File", menu=file_menu)

# New
file_menu.add_command(label="New", command=new_file)
root.bind('<Control-N>', new_file)
root.bind('<Control-n>', new_file)

# Open
file_menu.add_command(label="Open", command=open_file)
root.bind('<Control-O>', open_file)
root.bind('<Control-o>', open_file)

file_menu.add_separator()

# Save
file_menu.add_command(label="Save", command=save)
root.bind('<Control-Key-S>', save)
root.bind('<Control-Key-s>', save)

# Save as
file_menu.add_command(label="Save As", command=save_as)
root.bind('<Control-Shift-S>', save_as)
root.bind('<Control-Shift-s>', save_as)

# Rename
file_menu.add_command(label="Rename", command=rename_file)

file_menu.add_separator()

# Exit
file_menu.add_command(label="Exit", command=close)
root.bind('<Alt-F4>', close)

# ----------------------------------- EDIT MENU ---------------------------------------


edit_menu = Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="Edit", menu=edit_menu)

# Cut
edit_menu.add_command(label="Cut", command=cut)

# Copy
edit_menu.add_command(label="Copy", command=copy)

# Paste
edit_menu.add_command(label="Paste", command=paste)

edit_menu.add_separator()

# Undo
edit_menu.add_command(label="Undo", command=undo)

# Redo
edit_menu.add_command(label="Redo", command=redo)

# ----------------------------------- VIEW MENU ---------------------------------------


view_menu = Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="View", menu=view_menu)

# Text Color
view_menu.add_command(label="Text Color", command=change_text_color)

# Background Color
view_menu.add_command(label="Background Color", command=change_background_color)

view_menu.add_separator()

# Align Left
view_menu.add_command(label="Align Left", command=left_align)
root.bind('<Control-Shift-L>', left_align)
root.bind('<Control-Shift-l>', left_align)

# Align Center
view_menu.add_command(label="Align Center", command=center_align)
root.bind('<Control-Shift-C>', center_align)
root.bind('<Control-Shift-c>', center_align)

# Align Right
view_menu.add_command(label="Align Right", command=right_align)
root.bind('<Control-Shift-R>', right_align)
root.bind('<Control-Shift-r>', right_align)

# ----------------------------------- TOOLS MENU ---------------------------------------


tools_menu = Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="Tools", menu=tools_menu)

# Find
tools_menu.add_command(label="Find", command=find)
root.bind('<Control-F>', find)
root.bind('<Control-f>', find)

# Replace
tools_menu.add_command(label="Replace", command=replace)
root.bind('<Control-R>', replace)
root.bind('<Control-r>', replace)

# ----------------------------------- HELP MENU ---------------------------------------


help_menu = Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="Help", menu=help_menu)

# Shortcuts
help_menu.add_command(label="Shortcuts", command=shortcuts)

help_menu.add_separator()

# About
help_menu.add_command(label="About", command=about)

# ----------------------------------- TOOL BAR ---------------------------------------


tool_bar = Frame(root, pady=2, highlightbackground="black", highlightthickness=1)
tool_bar.pack(side=TOP, fill=X)

# New File
new_file_img = Image.open("Images/New File.png")
new_file_img = new_file_img.resize((18, 18), Image.ANTIALIAS)
new_file_img = ImageTk.PhotoImage(new_file_img)
new_file_btn = Button(command=new_file, image=new_file_img, borderwidth=2)
new_file_btn.pack(in_=tool_bar, side=LEFT, padx=4, pady=4)
new_file_btn.bind('<Enter>', lambda x: enter_tool("New File", "Ctrl + N", x))
new_file_btn.bind('<Leave>', leave_tool)

# Open file
open_file_img = Image.open("Images/Open.png")
open_file_img = open_file_img.resize((18, 18), Image.ANTIALIAS)
open_file_img = ImageTk.PhotoImage(open_file_img)
open_file_btn = Button(command=open_file, image=open_file_img, borderwidth=2)
open_file_btn.pack(in_=tool_bar, side=LEFT, padx=4, pady=4)
open_file_btn.bind('<Enter>', lambda x: enter_tool("Open File", "Ctrl + O", x))
open_file_btn.bind('<Leave>', leave_tool)

# Save
save_file_img = Image.open("Images/Save.png")
save_file_img = save_file_img.resize((18, 18), Image.ANTIALIAS)
save_file_img = ImageTk.PhotoImage(save_file_img)
save_file_btn = Button(command=save, image=save_file_img, borderwidth=2)
save_file_btn.pack(in_=tool_bar, side=LEFT, padx=4, pady=4)
save_file_btn.bind('<Enter>', lambda x: enter_tool("Save", "Ctrl + S", x))
save_file_btn.bind('<Leave>', leave_tool)

# Blank space
line = Label(text="", height=1, width=1)
line.pack(in_=tool_bar, side=LEFT)

# Cut
cut_img = Image.open("Images/Cut.png")
cut_img = cut_img.resize((18, 18), Image.ANTIALIAS)
cut_img = ImageTk.PhotoImage(cut_img)
cut_btn = Button(command=cut, image=cut_img, borderwidth=2)
cut_btn.pack(in_=tool_bar, side=LEFT, padx=4, pady=4)
cut_btn.bind('<Enter>', lambda x: enter_tool("Cut", "Ctrl + X", x))
cut_btn.bind('<Leave>', leave_tool)

# Copy
copy_img = Image.open("Images/Copy.png")
copy_img = copy_img.resize((18, 18), Image.ANTIALIAS)
copy_img = ImageTk.PhotoImage(copy_img)
copy_btn = Button(command=copy, image=copy_img, borderwidth=2)
copy_btn.pack(in_=tool_bar, side=LEFT, padx=4, pady=4)
copy_btn.bind('<Enter>', lambda x: enter_tool("Copy", "Ctrl + C", x))
copy_btn.bind('<Leave>', leave_tool)

# Paste
paste_img = Image.open("Images/Paste.png")
paste_img = paste_img.resize((18, 18), Image.ANTIALIAS)
paste_img = ImageTk.PhotoImage(paste_img)
paste_btn = Button(command=paste, image=paste_img, borderwidth=2)
paste_btn.pack(in_=tool_bar, side=LEFT, padx=4, pady=4)
paste_btn.bind('<Enter>', lambda x: enter_tool("Paste", "Ctrl + V", x))
paste_btn.bind('<Leave>', leave_tool)

# Blank space
line = Label(text="", height=1, width=1)
line.pack(in_=tool_bar, side=LEFT)

# Undo
undo_img = Image.open("Images/Undo.png")
undo_img = undo_img.resize((18, 18), Image.ANTIALIAS)
undo_img = ImageTk.PhotoImage(undo_img)
undo_btn = Button(command=undo, image=undo_img, borderwidth=2)
undo_btn.pack(in_=tool_bar, side=LEFT, padx=4, pady=4)
undo_btn.bind('<Enter>', lambda x: enter_tool("Undo", "Ctrl + Z", x))
undo_btn.bind('<Leave>', leave_tool)

# Redo
redo_img = Image.open("Images/Redo.png")
redo_img = redo_img.resize((18, 18), Image.ANTIALIAS)
redo_img = ImageTk.PhotoImage(redo_img)
redo_btn = Button(command=redo, image=redo_img, borderwidth=2)
redo_btn.pack(in_=tool_bar, side=LEFT, padx=4, pady=4)
redo_btn.bind('<Enter>', lambda x: enter_tool("Redo", "Ctrl + Y", x))
redo_btn.bind('<Leave>', leave_tool)

# Blank Space
line = Label(text="", height=1, width=1)
line.pack(in_=tool_bar, side=LEFT)

# Find
search_img = Image.open("Images/Search.png")
search_img = search_img.resize((18, 18), Image.ANTIALIAS)
search_img = ImageTk.PhotoImage(search_img)
search_btn = Button(command=find, image=search_img, borderwidth=2)
search_btn.pack(in_=tool_bar, side=LEFT, padx=4, pady=4)
search_btn.bind('<Enter>', lambda x: enter_tool("Find", "Ctrl + F", x))
search_btn.bind('<Leave>', leave_tool)

# Replace
replace_img = Image.open("Images/Replace.png")
replace_img = replace_img.resize((18, 18), Image.ANTIALIAS)
replace_img = ImageTk.PhotoImage(replace_img)
replace_btn = Button(command=replace, image=replace_img, borderwidth=2)
replace_btn.pack(in_=tool_bar, side=LEFT, padx=4, pady=4)
replace_btn.bind('<Enter>', lambda x: enter_tool("Replace", "Ctrl + R", x))
replace_btn.bind('<Leave>', leave_tool)

# name and shortcut
tool_right_frame = Frame(tool_bar, padx=2)
tool_right_frame.pack(side=RIGHT, fill=Y)

tool_hover_name = Label(tool_right_frame, text="")
tool_hover_name.grid(row=0, column=0)

tool_hover_shortcut = Label(tool_right_frame, text="")
tool_hover_shortcut.grid(row=1, column=0)

# ----------------------------------- FORMAT BAR ---------------------------------------


format_bar = Frame(root, pady=2, highlightbackground="black", highlightthickness=1)
format_bar.pack(side=TOP, fill=X)

# Font family
all_fonts = font.families()
font_family = ttk.Combobox(format_bar, state="readonly", values=all_fonts)
font_family.set('Calibri')
font_family.pack(in_=format_bar, side=LEFT, padx=4, pady=4)
font_family.bind('<<ComboboxSelected>>', change_font)
font_family.bind('<Enter>', lambda x: enter_format_button("Font Family", "", x))
font_family.bind('<Leave>', leave_format_button)

# Size
all_sizes = [8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 24, 26, 28, 36, 48, 72]
size = ttk.Combobox(format_bar, state="readonly", values=all_sizes, width=5)
size.set('11')
size.pack(in_=format_bar, side=LEFT, padx=4, pady=4)
size.bind('<<ComboboxSelected>>', change_size)
size.bind('<Enter>', lambda x: enter_format_button("Font Size", "", x))
size.bind('<Leave>', leave_format_button)

# Blank space
line = Label(text="", height=1, width=1)
line.pack(in_=format_bar, side=LEFT)

# Text color
text_color_img = Image.open("Images/Text.png")
text_color_img = text_color_img.resize((18, 18), Image.ANTIALIAS)
text_color_img = ImageTk.PhotoImage(text_color_img)
text_color_btn = Button(command=change_text_color, image=text_color_img, borderwidth=2)
text_color_btn.pack(in_=format_bar, side=LEFT, padx=4, pady=4)
text_color_btn.bind('<Enter>', lambda x: enter_format_button("Text Color", "", x))
text_color_btn.bind('<Leave>', leave_format_button)

# Background color
background_color_img = Image.open("Images/Background.png")
background_color_img = background_color_img.resize((18, 18), Image.ANTIALIAS)
background_color_img = ImageTk.PhotoImage(background_color_img)
background_color_btn = Button(command=change_background_color, image=background_color_img, borderwidth=2)
background_color_btn.pack(in_=format_bar, side=LEFT, padx=4, pady=4)
background_color_btn.bind('<Enter>', lambda x: enter_format_button("Background Color", "", x))
background_color_btn.bind('<Leave>', leave_format_button)

# Blank space
line = Label(text="", height=1, width=1)
line.pack(in_=format_bar, side=LEFT)

# Align left
left_img = Image.open("Images/Left.png")
left_img = left_img.resize((18, 18), Image.ANTIALIAS)
left_img = ImageTk.PhotoImage(left_img)
left_btn = Button(command=left_align, image=left_img, borderwidth=2)
left_btn.pack(in_=format_bar, side=LEFT, padx=4, pady=4)
left_btn.bind('<Enter>', lambda x: enter_format_button("Align Left", "Ctrl + Shift + L", x))
left_btn.bind('<Leave>', leave_format_button)

# Align center
center_img = Image.open("Images/Center.png")
center_img = center_img.resize((18, 18), Image.ANTIALIAS)
center_img = ImageTk.PhotoImage(center_img)
center_btn = Button(command=center_align, image=center_img, borderwidth=2)
center_btn.pack(in_=format_bar, side=LEFT, padx=4, pady=4)
center_btn.bind('<Enter>', lambda x: enter_format_button("Align center", "Ctrl + Shift + C", x))
center_btn.bind('<Leave>', leave_format_button)

# Align right
right_img = Image.open("Images/Right.png")
right_img = right_img.resize((18, 18), Image.ANTIALIAS)
right_img = ImageTk.PhotoImage(right_img)
right_btn = Button(command=right_align, image=right_img, borderwidth=2)
right_btn.pack(in_=format_bar, side=LEFT, padx=4, pady=4)
right_btn.bind('<Enter>', lambda x: enter_format_button("Align right", "Ctrl + Shift + R", x))
right_btn.bind('<Leave>', leave_format_button)

# name and shortcut
format_right_frame = Frame(format_bar, padx=2)
format_right_frame.pack(side=RIGHT, fill=Y)

format_hover_name = Label(format_right_frame, text="")
format_hover_name.grid(row=0, column=0)

format_hover_shortcut = Label(format_right_frame, text="")
format_hover_shortcut.grid(row=1, column=0)

# ----------------------------------- TEXT AREA ---------------------------------------


bottom_frame = Frame(root, padx=2, pady=2, borderwidth=2, relief=SUNKEN)
bottom_frame.pack(fill=BOTH, expand=1)

scroll_bar = Scrollbar(bottom_frame)
scroll_bar.pack(side=RIGHT, fill=Y)

text_area = Text(bottom_frame, undo=True, font=Font(family="Calibri", size=11), wrap=WORD,
                 yscrollcommand=scroll_bar.set)
text_area.pack(fill=BOTH, expand=1)
text_area.focus()

scroll_bar.config(command=text_area.yview)

root.mainloop()

# ---------------------------------------------------------------------------------------
