from tkinter import Tk
from ui.ui import UI


def main():
    window = Tk()
    window.title("Sääpäiväkirja")

    ui_look = UI(window)
    ui_look.start()

    window.mainloop()


if __name__ == "__main__":
    main()
