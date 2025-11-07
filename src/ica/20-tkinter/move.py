import tkinter as tk
class Movecanvasapp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Canvas Move Demo")

        self.canvas = tk.Canvas(self.root, bg="#3b82f6", width=500, height=300)
        self.canvas.pack(fill="both", expand=True)

        self.text_id = self.canvas.create_text(
            80, 80,
            text="Han",
            fill="white",
            font=("Helvetica", 20, "bold"))

        for key in ("w", "a", "s", "d", "Up", "Down", "Left", "Right"):
            self.root.bind(f"<{key}>", self.move_callback)

    def move_callback(self, event):
        key = event.keysym
        dx = dy = 0
        if key in ("w", "Up"):
            dy = -10
        elif key in ("s", "Down"):
            dy = 10
        elif key in ("a", "Left"):
            dx = -10
        elif key in ("d", "Right"):
            dx = 10

        if dx or dy:
            self.canvas.move(self.text_id, dx, dy)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    Movecanvasapp().run()