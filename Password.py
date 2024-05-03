from cryptography.fernet import Fernet
import tkinter as tk
import customtkinter
import sys

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)
  
def lihat():
    
    root.geometry("720x720")
    
    frame = customtkinter.CTkFrame(root, width=650, height=650, corner_radius=10)
    frame.grid(row=0, column=0 ,pady=10, padx=10, sticky="ns")

    post = customtkinter.CTkLabel(frame, text="Safe Note Manager", font=customtkinter.CTkFont(size=25, weight="bold"), width=650)
    post.grid(row=0, column=1, padx=10, pady=(10,5))
    desc = customtkinter.CTkLabel(frame, text="Simpan Catatan Dengan Aman", font=customtkinter.CTkFont(size=10), width=650)
    desc.grid(row=1, column=1, padx=2, pady=1)

    btnframe = customtkinter.CTkFrame(frame, width=300, corner_radius=2)
    btnframe.grid(row=2, column=0, columnspan=3, pady=(15,5))

    btn1 = customtkinter.CTkButton(btnframe, width=100, text="Tambah Catatan", command=tambah).grid(row=0, column=0, padx=5, pady=5)
    btn2 = customtkinter.CTkButton(btnframe, width=100, text="Lihat Catatan", command=lihat).grid(row=0, column=1, padx=5, pady=5)
    btn3 = customtkinter.CTkButton(btnframe, width=100, text="Keluar", command=keluar).grid(row=0, column=2, padx=5, pady=5)
    
    hstrframe = customtkinter.CTkFrame(frame, width= 650, height= 400)
    hstrframe.grid(row = 3, column = 1, pady= (10,10), padx= 10)
    hstrlabel = customtkinter.CTkLabel(hstrframe, width= 650, text= "Data Catatan")
    hstrlabel.grid(row = 0, column = 0, padx = 5, pady = 1, sticky = "n")
    history_text = customtkinter.CTkTextbox(hstrframe, width= 650, height= 500)
    history_text.grid(row = 1, column = 0, padx = 5, pady = (1,5))

    
    with open('Password.txt', 'r') as f:
        for line in f.readlines():
            data = line.strip()
            user, passw = data.split("|")
            decrypted_passw = fer.decrypt(passw.encode()).decode()
            text_to_insert = f"Nama Data: {user} | Data: {decrypted_passw}\n"
            history_text.insert(tk.END, text_to_insert)

def tambah():
    
    def submit():
        nama = entry_displayr.get()
        pwd = entry_displayk.get(0.1,"end")
        with open('Password.txt', 'a') as f:
            f.write(nama + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
        
        entry_displayr.delete(0, "end")
        entry_displayk.delete(0.1, "end")
    
    root.geometry("720x720")
    
    frame = customtkinter.CTkFrame(root, width=650, height=650, corner_radius=10)
    frame.grid(row=0, column=0 ,pady=10, padx=10, sticky="ns")

    post = customtkinter.CTkLabel(frame, text="Safe Note Manager", font=customtkinter.CTkFont(size=25, weight="bold"), width=650)
    post.grid(row=0, column=1, padx=10, pady=(10,5))
    desc = customtkinter.CTkLabel(frame, text="Simpan Catatan Dengan Aman", font=customtkinter.CTkFont(size=10), width=650)
    desc.grid(row=1, column=1, padx=2, pady=1)

    btnframe = customtkinter.CTkFrame(frame, width=300, corner_radius=2)
    btnframe.grid(row=2, column=0, columnspan=3, pady=(15,5))

    btn1 = customtkinter.CTkButton(btnframe, width=100, text="Tambah Catatan", command=tambah).grid(row=0, column=0, padx=5, pady=5)
    btn2 = customtkinter.CTkButton(btnframe, width=100, text="Lihat Catatan", command=lihat).grid(row=0, column=1, padx=5, pady=5)
    btn3 = customtkinter.CTkButton(btnframe, width=100, text="Keluar", command=keluar).grid(row=0, column=2, padx=5, pady=5)
    
    entryframe = customtkinter.CTkFrame(frame, width= 300, corner_radius= 0.5)
    entryframe.grid(row = 3, column = 1, pady = 5, padx = 5)
    entry_displayr = customtkinter.CTkEntry(entryframe, height=30, width=300, corner_radius=5, placeholder_text="Nama Data")
    entry_displayr.grid(row=1, column=0, padx=10, pady=5)
    entry_displayk = customtkinter.CTkTextbox(entryframe, height=250, width=300, corner_radius=5)
    entry_displayk.grid(row=2, column=0, padx=10, pady=5)
    
    btn4 = customtkinter.CTkButton(frame, width=100, text="Submit", command=submit).grid(row=4, column=1)


def keluar():
    root.destroy()
        
    
# GUI ---------------------------------------------------------------------------------------------------------------

root = customtkinter.CTk()
root.title("Safe Note Manager")
root.geometry("400x200")
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

frame = customtkinter.CTkFrame(root, width=350, height=350, corner_radius=10)
frame.grid(row=0, column=0 ,pady=10, padx=10, sticky="ns")

post = customtkinter.CTkLabel(frame, text="Safe Note Manager", font=customtkinter.CTkFont(size=25, weight="bold"), width=325)
post.grid(row=0, column=1, padx=10, pady=(10,5))
desc = customtkinter.CTkLabel(frame, text="Simpan Catatan Dengan Aman", font=customtkinter.CTkFont(size=10), width=325)
desc.grid(row=1, column=1, padx=2, pady=1)

btnframe = customtkinter.CTkFrame(frame, width=300, corner_radius=2)
btnframe.grid(row=2, column=0, columnspan=3, pady=(15,5))

btn1 = customtkinter.CTkButton(btnframe, width=100, text="Tambah Catatan", command=tambah).grid(row=0, column=0, padx=5, pady=5)
btn2 = customtkinter.CTkButton(btnframe, width=100, text="Lihat Catatan", command=lihat).grid(row=0, column=1, padx=5, pady=5)
btn3 = customtkinter.CTkButton(btnframe, width=100, text="Keluar", command=keluar).grid(row=0, column=2, padx=5, pady=5)

name = customtkinter.CTkLabel(frame, text="227006051 Fahri Aminuddin Abdillah", font=customtkinter.CTkFont(size=10), width=325)
name.grid(row=5, column=1)

root.mainloop()