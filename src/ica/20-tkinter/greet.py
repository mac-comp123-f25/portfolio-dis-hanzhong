import tkinter as tk

# ----- GUI class and methods -----
class BasicGui:
    def __init__(self):
        self.mainWin = tk.Tk()
        self.mainWin.title("Buttons & lables")
        quit_btn = tk.Button(self.mainWin, text="Quit", command=self.quit_callback)
        quit_btn.grid(row=0, column=0, padx=10, pady=6, sticky="ew")

        hello_btn = tk.Button(self.mainWin, text="Hello", command=self.hello_callback)
        hello_btn.grid(row=1, column=0, padx=10, pady=6, sticky="ew")

        goodbye_btn = tk.Button(self.mainWin, text="Goodbye", command=self.goodbye_callback)
        goodbye_btn.grid(row=2, column=0, padx=10, pady=6, sticky="ew")

        self.msg_label = tk.Label(self.mainWin, text="Welcome")
        self.msg_label.grid(row=1, column=1, padx=10, pady=6)

    def run(self):
        self.mainWin.mainloop()

    def quit_callback(self):
        self.mainWin.destroy()

    def hello_callback(self):
        self.msg_label.config(text="Hello")

    def goodbye_callback(self):
        self.msg_label.config(text="Goodbye")
# ----- Main program -----
myGui = BasicGui()
myGui.run()