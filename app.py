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
        self.grid(column=2)

        self.search_input = tk.Entry(self)
        self.search_input.grid(column=0,sticky="NSEW")
        self.search_input.bind('<Return>',func=self.search_word)
        # self.search_input.pack(fill="both")

        self.rdm_wrd_btn = tk.Button(self,text="Random Word",fg="blue",
                              command=self.find_random_word)
        self.rdm_wrd_btn.grid(column=0,sticky="NSEW")

        self.text_box = tk.Label(self, text = "Please enter a word to \n look up of from JISHO!",anchor="center")
        self.text_box.grid(column=1, rowspan = 2,sticky="NSEW")

    def search_word(self,event):
        search_response = jisho_API.search_JISHO(self.search_input.get())
        print(search_response['meta'])
        print_statement_list = jisho_API.display_definitions(4,search_response)
        print_statement = '\n'+'\n\n\n'.join(print_statement_list)
        self.text_box["text"] = print_statement

    def find_random_word(self):
        random_word = random.choice(wds.eng_words)
        self.search_input.delete(0,len(self.search_input.get())+1)
        self.search_input.insert(0,random_word)
        self.search_word(None)

    def start(self):
        self.mainloop()

Application(tk.Tk()).mainloop()
