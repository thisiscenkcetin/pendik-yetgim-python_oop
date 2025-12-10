
import tkinter as tk

def tıklama(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(str(entry.get()))
            entry_var.set(result)

        except Exception as e:
            entry_var.set("Hata")
        
    elif text == "c":
        entry_var.set("")
    
    else:
        entry_var.set(entry_var.get() + text)


root = tk.Tk()

root.title("Hesap Makinesi")


entry_var = tk.StringVar()

entry = tk.Entry(root,textvar=entry_var,font="Arial 20",justify="right")

entry.pack(fill=tk.X,padx=10,pady=10,ipady=10)

frame = tk.Frame(root)

frame.pack(padx=10,pady=5)


buttons = [
    ["7","8","9","/"],
    ["4","5","6","*"],
    ["1","2","3","-"],
    ["c","0","=","+"]
]


for row_list in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack()

    for char in row_list:
        btn = tk.Button(row_frame,text=char,font="Arial 18",width=4,height=2)
        btn.pack(side=tk.LEFT,padx=5,pady=5)
        btn.bind("<Button-1>",tıklama)

root.mainloop()



