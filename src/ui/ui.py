from ui.login_look import LoginLook
from ui.notes_look import NotesView
from ui.create_user_look import CreateUserLook


class UI:
    """Luokka, joka hoitaa käyttöliittymää
    """
    def __init__(self, root):
        """Konstruktori, joka vastaa käyttöliittymän luokasta

        Args:
            root: tkinter-rakenne, jossa näkymä luodaan
        """
        self._root = root
        self._current_look = None

    def start(self):
        """Käynnistää käyttöliittymän
        """
        self._show_login_look()

    def _show_login_look(self):
        self._hide_current_look()
        self._current_look = LoginLook(
            self._root, self._show_notes_look, self._show_create_user_look)

        self._current_look.pack()

    def _hide_current_look(self):
        if self._current_look:
            self._current_look.destroy()

    def _show_notes_look(self):
        self._hide_current_look()

        self._current_look = NotesView(self._root, self._show_login_look)

        self._current_look.pack()

    def _show_create_user_look(self):
        self._hide_current_look()

        self._current_look = CreateUserLook(
            self._root, self._show_notes_look, self._show_login_look)

        self._current_look.pack()
