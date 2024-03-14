import sys
import pyautogui
import pytesseract
from PIL import Image, ImageEnhance, ImageDraw, ImageFont
import time
from googletrans import Translator
#import customtkinter
import tkinter as tk
import customtkinter
from tkinter import messagebox, PhotoImage, filedialog


pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
translator = Translator()

def on_closing():
    if messagebox.askokcancel("Chiusura", "Vuoi davvero chiudere l'applicazione?"):
        root.destroy()
        sys.exit()

def capture_and_translate():
    try:
        # Cattura lo schermo e ottieni il testo
        #screenshot = pyautogui.screenshot(region=(0, 0, 1920, 1080))  # Imposta le dimensioni dello schermo
        screenshot = pyautogui.screenshot(region=(400, 200, 1000, 950))
        text = pytesseract.image_to_string(screenshot)
        print(text)
        
        translation = translator.translate(text, dest='it')
        print(translation.text)
        
        
        # Stampa il testo tradotto
        # print("Testo originale:", text)
        # print("Testo tradotto:", translation.text)
        #label.config(text=translation.text)
        lbl.configure(text = translation.text)
            
    except KeyboardInterrupt:
        print("Programma terminato.")
        
        
        
# create root window
root = customtkinter.CTk()
 
# root window title and dimension
root.title("Traduzione")
root.protocol("WM_DELETE_WINDOW", on_closing)
# Set geometry(widthxheight)
root.geometry("300x600+{}+{}".format(root.winfo_screenwidth()-400, root.winfo_screenheight()-900)) # Posizione in basso a destra
 
lbl = tk.Label(root, text = "Vuoi tradurre?")
lbl.grid()

btn_screen = customtkinter.CTkButton(master = root, text = "Screen", command=capture_and_translate)
btn_screen.grid(column=0, row=1)


 
# Execute Tkinter
root.mainloop()
        

# if __name__ == "__main__":
#     capture_and_translate()
