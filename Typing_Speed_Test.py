import tkinter as tk #This library is used to work with gui applications with python
import time
import threading
import random
class TypeSpeedGui:
    def __init__(self):
        self.root=tk.Tk()#it helps us to display window and manges the components in tkinter application
        self.root.title('Typing Speed Test')
        self.root.geometry("750x250")
        self.text=open("texts.txt","r").read().split('\n')
        self.frame=tk.Frame(self.root)
        
        self.label=tk.Label(self.frame,text=random.choice(self.text),font= ('Courier 20'),bg='green')
        self.label.grid(row=0,column=0,columnspan=2,padx=5,pady=10)
        
        self.input_entry=tk.Entry(self.frame,width=40,font= ('Courier 30'))
        self.input_entry.grid(row=1,column=0,columnspan=2,padx=5,pady=10)
        self.input_entry.bind("<KeyPress>",self.start)
        
        self.speed=tk.Label(self.frame,text="Speed: \n0.00CPS\n0.00CPM",font= ('Courier 20'))
        self.speed.grid(row=2,column=0,columnspan=2,padx=5,pady=10)
        
        self.reset=tk.Button(self.frame,text="RESET",command=self.reset)
        self.reset.grid(row=3,column=0,columnspan=2,padx=5,pady=10)
        self.frame.pack(expand=True)

        self.counter=0
        self.started=False
        self.root.mainloop()
        
    def start(self,event):
            if not self.started:
                if not event.keycode in [16,17,18]:
                    self.started=True
                    t=threading.Thread(target=self.time_thread)
                    t.start()
            if not self.label.cget('text').startswith(self.input_entry.get()):
                self.input_entry.config(fg="red")
            else:
                self.input_entry.config(fg="black")
            if self.label.cget('text')==self.input_entry.get():
                self.started=False
                self.input_entry.config(fg="green")
    def time_thread(self):
            while self.started:
                time.sleep(0.1)
                self.counter+=0.1
                cps=len(self.input_entry.get())/self.counter
                cpm=cps*60
                self.speed.config(text=f"Speed: \n{cps:.2f} CPS\n{cpm:.2f} CPM")
    def reset(self):
            self.started=False
            self.counter=0
            self.speed.config(text="Speed: \n0.00CPS\n0.00CPM")
            self.label.config(text=random.choice(self.text))
            self.input_entry.delete(0,tk.END)
TypeSpeedGui()
