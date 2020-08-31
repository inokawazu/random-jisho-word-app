import tkinter as tk
import jisho_API
import random
import words as wds

# Add documentation later!

class Application(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master.title("Random Jisho Search Up")
        self.createWidgets()

    def createWidgets(self):
        self.grid()
        self.grid_rows = 0

        self.search_text_box = tk.Label(self, text = '''Search Box''')
        self.search_text_box.grid(column=0,rowspan=1)
        self.grid_rows =+ 1

        self.search_input = tk.Entry(self)
        self.search_input.grid(column=0,rowspan=1)
        self.grid_rows =+ 1
        self.search_input.bind('<Return>',func=self.search_word)

        self.rdm_wrd_btn = tk.Button(self,text="Random Word",fg="blue",
                              command=self.find_random_word)
        self.rdm_wrd_btn.grid(column=0,rowspan=1)
        self.grid_rows =+ 1

        self.search_amount_scale = tk.Scale(self,orient = "vertical", label = "Number of  Search Results \n to display", from_=1, to=5)
        self.search_amount_scale.grid(column=0,rowspan=2)
        self.grid_rows =+ 2

        self.text_box = tk.Label(self, text = '''Please enter a word to \n look up of from JISHO!\nor press the Random Word key!''',anchor="center")
        self.text_box.grid(column=1,row = 0,rowspan = self.grid_rows,sticky="NSEW")

    def search_word(self,event):
        search_response = jisho_API.search_JISHO(self.search_input.get())
        print_statement_list = jisho_API.display_definitions(self.search_amount_scale.get(),search_response)
        print_statement = '\n\n\n'.join(print_statement_list)
        self.text_box["text"] = print_statement

    def find_random_word(self):
        random_word = random.choice(wds.eng_words)
        self.search_input.delete(0,len(self.search_input.get())+1)
        self.search_input.insert(0,random_word)
        self.search_word(None)

    def start(self):
        self.mainloop()

Application(tk.Tk()).mainloop()
