# coding:utf-8
from random import randint, choice
from tkinter import *
from tkinter import messagebox
import webbrowser
import string
import pyperclip


def generate_password():
    password_min = 8
    password_max = 12
    all_chars = string.ascii_letters + string.digits + string.punctuation + string.digits
    password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)


def copy_password():
    if not password_entry.get() == "":
        pyperclip.copy(password_entry.get())
        messagebox.showinfo(title="Copié",
                            message="Votre mot de passe a été copié dans le presse-papiers.")
    else:
        if messagebox.askyesno("Erreur", "Il n'y a pas de mot de passe à copier. Voulez-vous en créer un?"):
            generate_password()
            pyperclip.copy(password_entry.get())
            messagebox.showinfo(title="Copié",
                                message="Votre mot de passe a été copié dans le presse-papiers.")
        else:
            messagebox.showinfo("Annulation", "Le mot de passe n'a pas été copié.")


def site():
    question = messagebox.askokcancel("Redirection", "Vous allez être redirigé vers un site internet.")
    if question:
        webbrowser.open_new("http://mot-de-passe.org")
    else:
        messagebox.showinfo("Annulation", "Vous ne serez pas redirigé vers le site internet.")


def save_password():
    if not password_entry.get() == "":
        with open("passwords.txt", "a") as file:
            file.write(password_entry.get())
        messagebox.showinfo(title="Enregistré",
                            message="Votre mot de passe a été enregistré dans le fichier passwords.txt qui est dans les même répertoire que cette application.")
    else:
        question = messagebox.askyesno(title="Erreur",
                                       message="Il n'y a pas de mot de passe à enregistrer. Voulez-vous en créer un?")
        if question is True:
            generate_password()
            with open("passwords.txt", "a") as file:
                file.write(password_entry.get())
            messagebox.showinfo(title="Enregistré",
                                message="Votre mot de passe a été enregistré dans le fichier passwords.txt qui est dans les même répertoire que cette application.")
        else:
            messagebox.showinfo("Annulation", "Le mot de passe n'a pas été enregistré.")


# créer une première fenêtre
window = Tk()
window.title("Générateur de mot de passe")
window.geometry("1080x720")
# window.iconbitmap("icon.ico") # this does not work anymore.
window.minsize(width="625", height="500")
window.config(background="#4065A4")

# créer la frame principale
frame = Frame(window, bg="#4065A4")

# création de l'image
width = 300
height = 330
image = PhotoImage(file="robot.png").zoom(3).subsample(3)
canvas = Canvas(frame, width=width, height=height, bg="#4065A4", bd=0, highlightthickness=0)
canvas.create_image(250, 260, image=image)
canvas.grid(row=0, column=0, sticky=W)

# creér une sous-boîte
right_frame = Frame(frame, bg="#4065A4")

# créer un titre
label_title = Label(right_frame, text="Mot de passe", font=("Helvetica", 20), bg="#4065A4", fg="white")
label_title.pack()

# créer un champ, une entrée, une input...
password_entry = Entry(right_frame, font=("Helvetica", 20), bg="#4065A4", fg="white")
password_entry.pack()

# créer un bouton
generate_password_button = Button(right_frame, text="Générer", font=("Helvetica", 20), bg="#4065A4", fg="white",
                                  command=generate_password)
generate_password_button.pack(fill=X)

# on place sous-boîte à droite de la frame principale
right_frame.grid(row=0, column=1, sticky=W)

# afficher la frame
frame.pack(expand=YES)

# création d'une barre de menu
menu_bar = Menu(window)
# créer un menu
password_menu = Menu(menu_bar, tearoff=0)
password_menu.add_command(label="Nouveau", command=generate_password)
password_menu.add_command(label="Copier dans le presse-papiers", command=copy_password)
password_menu.add_command(label="Enregistrer le mot de passe dans le fichier passwords.txt", command=save_password)
password_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=password_menu)
contact_menu = Menu(menu_bar, tearoff=0)
contact_menu.add_command(label="Me rendre sur le site internet", command=site)
menu_bar.add_cascade(label="Contact", menu=contact_menu)

# configurer notre fenêtre pour ajouter ce menu_bar
window.config(menu=menu_bar)

# afficher la fenêtre
window.mainloop()

