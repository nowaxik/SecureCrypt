# -*- coding: utf-8 -*-
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import filedialog, messagebox


def szyfruj_plik(nazwa_pliku):
    """
    Funkcja szyfruje zawartość pliku za pomocą klucza wygenerowanego w funkcji.
    """
    klucz = Fernet.generate_key()
    with open('klucz.txt', 'wb') as plik:
        plik.write(klucz)

    fernet = Fernet(klucz)

    with open(nazwa_pliku, 'rb') as plik:
        zawartosc_pliku = plik.read()

    zaszyfrowana_zawartosc = fernet.encrypt(zawartosc_pliku)

    with open(nazwa_pliku, 'wb') as plik:
        plik.write(zaszyfrowana_zawartosc)


def deszyfruj_plik(nazwa_pliku):
    """
    Funkcja deszyfruje zawartość pliku za pomocą klucza znajdującego się w pliku klucz.txt
    i zapisuje odszyfrowaną zawartość do pliku o tej samej nazwie.
    """
    with open('klucz.txt', 'rb') as plik:
        klucz = plik.read()

    fernet = Fernet(klucz)

    with open(nazwa_pliku, 'rb') as plik:
        zaszyfrowana_zawartosc = plik.read()

    odszyfrowana_zawartosc = fernet.decrypt(zaszyfrowana_zawartosc)

    with open(nazwa_pliku, 'wb') as plik:
        plik.write(odszyfrowana_zawartosc)


def wybierz_plik():
    """
    Funkcja otwiera okno dialogowe wyboru pliku i zwraca ścieżkę wybranego pliku.
    """
    nazwa_pliku = filedialog.askopenfilename()
    return nazwa_pliku


def szyfrowanie():
    """
    Funkcja szyfruje wybrany plik za pomocą klucza wygenerowanego w funkcji.
    """
    nazwa_pliku = wybierz_plik()
    if nazwa_pliku:
        try:
            szyfruj_plik(nazwa_pliku)
            messagebox.showinfo("SecureCrypt", "Plik został zaszyfrowany.")
        except Exception as e:
            messagebox.showerror("Błąd", "Nie udało się zaszyfrować pliku: " + str(e))


def deszyfrowanie():
    """
    Funkcja deszyfruje wybrany plik za pomocą klucza znajdującego się w pliku klucz.txt.
    """
    nazwa_pliku = wybierz_plik()
    if nazwa_pliku:
        try:
            deszyfruj_plik(nazwa_pliku)
            messagebox.showinfo("SecureCrypt", "Plik został odszyfrowany.")
        except Exception as e:
            messagebox.showerror("Błąd", "Nie udało się odszyfrować pliku: " + str(e))


root = tk.Tk()
root.title("SecureCrypt")
root.geometry("500x200")
root.iconphoto(True, tk.PhotoImage(file="ikona.png"))

# Utwórz ramkę dla przycisków
button_frame = tk.Frame(root)
button_frame.pack(side=tk.LEFT, padx=20)

# Utwórz przyciski i umieść je w ramce
szyfruj_button = tk.Button(button_frame, text="Szyfruj plik", command=szyfrowanie, height=3, width=20)
szyfruj_button.pack(pady=20)

deszyfruj_button = tk.Button(button_frame, text="Deszyfruj plik", command=deszyfrowanie, height=3, width=20)
deszyfruj_button.pack(pady=20)

# Utwórz obiekt PhotoImage i zmniejsz jego rozmiar
image = tk.PhotoImage(file="czaszka.png")
image = image.subsample(25)

# Utwórz ramkę dla obrazka i nazwy programu
image_frame = tk.Frame(root)
image_frame.pack(side=tk.RIGHT, padx=20)

# Dodaj obrazek i nazwę programu do ramki
image_label = tk.Label(image_frame, image=image)
image_label.pack(padx=10)

program_name = tk.Label(image_frame, text="Program do szyfrowania plików", font=("Helvetica", 16))
program_name.pack(pady=20)

root.mainloop()
