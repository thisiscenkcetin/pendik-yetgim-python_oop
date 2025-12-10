import tkinter as tk
from tkinter import messagebox
from models import Session,Todo

def görevleri_yenile():
    listbox.delete(0,tk.END)

    session = Session()
    görevler = session.query(Todo).all()

    for g in görevler:
        durum = "✔️" if g.is_done else "❌"
        listbox.insert(tk.END,f"{g.id} - {g.title} - {durum}")

    session.close()

def görev_ekle():
    baslik = entry.get()

    if baslik.strip() == "":
        messagebox.showwarning("Uyarı","Görev başlığı boş olamaz")
        return
    
    session = Session()
    yeni_görev = Todo(title=baslik)
    session.add(yeni_görev)
    session.commit()
    session.close()
    entry.delete(0,tk.END)
    görevleri_yenile()



def görev_tamamla():
    secim = listbox.curselection()

    if not secim:
        return 

    satır = listbox.get(secim[0])
    görev_id = int(satır.split("-")[0].strip())
    session = Session()
    görev = session.query(Todo).get(görev_id)

    if görev:
        görev.is_done = True
        session.commit()
    
    session.close()
    görevleri_yenile()

def görev_sil():
    secim = listbox.curselection(),

    if not secim:
        return 
    
    satır = listbox.get(secim[0])

    görev_id = int(satır.split("-")[0].strip())

    session = Session()

    görev = session.query(Todo).get(görev_id)

    if görev:
        session.delete(görev)

        session.commit()
    
    session.close()

    görevleri_yenile()


root = tk.Tk()

root.title("To-Do Ugulaması")

entry = tk.Entry(root,font="Arial 14")

entry.pack(padx=10,pady=10,fill=tk.X)

btn_frame = tk.Frame(root)

btn_frame.pack(pady=5)

tk.Button(btn_frame,text="Ekle",command=görev_ekle,width=10).grid(row=0,column=0,padx=5)

tk.Button(btn_frame,text="Tamamla",command=görev_tamamla,width=10).grid(row=0,column=1,padx=5)

tk.Button(btn_frame,text="sil",command=görev_sil,width=10).grid(row=0,column=2,padx=5)

listbox = tk.Listbox(root,font="Arial 12",height=10)

listbox.pack(padx=10,pady=10,fill=tk.BOTH,expand=True)


görevleri_yenile()

root.mainloop()
