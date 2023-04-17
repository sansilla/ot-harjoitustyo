from tkinter import ttk, StringVar, constants
from services import UsernameAlreadyExistsError #ja joku toinen


class CreateUserLook:
    def __init__(self, root, handle_creating, handle_showing_login):
        self._root = root
        self._handle_creating = handle_creating
        self._handle_showing_login = handle_showing_login
        self._frame = None
        self._username_entry = None
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _create_user_handler(self):
        username = self._username_entry.get()

        if len(username) == 0:
            self._show_error("Syötä käyttäjänimi")
            return

        try:
            # services -kansiosta asiaa
            self._handle_creating()
        except UsernameAlreadyExistsError:
            self._show_error(f"Käyttäjänimi {username} on jo olemassa")

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()
