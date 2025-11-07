import tkinter as tk

class ReverseGUI:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("reverse")
        tk.Label(self.win, text="Type a phrase and press Enter or Tab:").grid(row=0, column=0, columnspan=2, sticky="w", padx=10, pady=(10, 4)
                                                                              )
        self.entry = tk.Entry(self.win, width=40)
        self.entry.grid(row=1, column=0, columnspan=2, padx=10, pady=4, sticky="we")
        self.entry.focus()
        tk.Label(self.win, text="Reversed:").grid(row=2, column=0, sticky="w", padx=10)
        self.display = tk.Label(self.win, text="", anchor="w")
        self.display.grid(row=2, column=1, sticky="we", padx=10, pady=4)

        tk.Button(self.win, text="Reverse", command=lambda: self.entry_response(None)).grid(
            row=3, column=0, padx=10, pady=(6, 10), sticky="we"
        )
        tk.Button(self.win, text="Quit", command=self.win.destroy).grid(
            row=3, column=1, padx=10, pady=(6, 10), sticky="we"
        )

        self.entry.bind("<Return>", self.entry_response)
        self.entry.bind("<Tab>", self.entry_response)

    def entry_response(self, event):
        text = self.entry.get()
        reversed_text = text[::-1]
        self.display.config(text=reversed_text)

    def run(self):
        self.win.mainloop()
if __name__ == "__main__":
    ReverseGUI().run()