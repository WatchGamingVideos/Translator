 pip install tkinter
 pip install googletrans
 
from tkinter import *
 from tkinter import ttk
 from googletrans import Translator, LANGUAGES
 
root = Tk()
 root.geometry('1080x400')

 root.resizable(0,0)
 root.config(bg = 'ghost white')
 
root.title("WatchGamingVideos--Language Translator")
Label(root, text = "LANGUAGE TRANSLATOR", font = "arial 20 bold", bg='white smoke').pack()
Label(root,text ="Project Gurukul", font = 'arial 15 bold', bg ='white smoke' , width = '20').pack(side = 'bottom')
 Label(root,text ="Enter Text", font = 'arial 13 bold', bg ='white smoke').place(x=200,y=60)
 Input_text = Text(root,font = 'arial 10', height = 11, wrap = WORD, padx=5, pady=5, width = 60)
 Input_text.place(x=30,y = 100)
 Label(root,text ="Output", font = 'arial 13 bold', bg ='white smoke').place(x=780,y=60)
 Output_text = Text(root,font = 'arial 10', height = 11, wrap = WORD, padx=5, pady= 5, width =60)
 Output_text.place(x = 600 , y = 100)
 language = list(LANGUAGES.values())
 src_lang = ttk.Combobox(root, values= language, width =22)
 src_lang.place(x=20,y=60)
 src_lang.set('choose input language')

 dest_lang = ttk.Combobox(root, values= language, width =22)
 dest_lang.place(x=890,y=60)
 dest_lang.set('choose output language')

language = list(LANGUAGES.values())
src_lang = ttk.Combobox(root, values= language, width =22)
src_lang.place(x=20,y=60)
src_lang.set('choose input language')
dest_lang = ttk.Combobox(root, values= language, width =22)
dest_lang.place(x=890,y=60)
dest_lang.set('choose output language')
trans_btn = Button(root, text = 'Translate',font = 'arial 12 bold',pady = 5,command = Translate , bg = 'royal blue1', activebackground = 'sky blue')
trans_btn.place(x = 490, y= 180 )
root.mainloop()