from tkinter import ttk, StringVar, constants
from services.note_service import UsernameAlreadyExistsError, note_service


class CreateUserLook:
    """Näkymä, kun luodaan uusi käyttäjä
    """
    def __init__(self, root, handle_creating, handle_showing_login):
        """Konstruktori, joka tekee näkymän rekisteröitymiselle

        Args:
            root: tkinter-rakenne, jossa näkymä luodaan
            handle_creating (arvo): kutsutaan, kun rekisteröidään käyttäjä. Argumentteina käyttäjänimi
            handle_showing_login (arvo): kutsutaan, kun siirrytään kirjautumaan sisään
        """
        self._root = root
        self._handle_creating = handle_creating
        self._handle_showing_login = handle_showing_login
        self._window = None
        self._username_entry = None
        self._error_variable = None
        self._error_label = None

        self._do_creating_window()

    def pack(self):
        """Näyttää ikkunan
        """
        self._window.pack(fill=constants.Y)

    def destroy(self):
        """Tuhoaa ikkunan
        """
        self._window.destroy()

    def _create_user_handler(self):
        username = self._username_entry.get()

        if len(username) == 0:
            self._show_error("Syötä käyttäjänimi")
            return

        try:
            note_service.create_new_user(username)
            self._handle_creating()

        except UsernameAlreadyExistsError:
            self._show_error(f"Käyttäjänimi {username} on jo olemassa")

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _do_name_field(self):
        username_label = ttk.Label(master=self._window, text="Käyttäjänimi:")

        self._username_entry = ttk.Entry(master=self._window)

        username_label.grid(row=0, padx=1, pady=10, sticky=constants.W)
        self._username_entry.grid(row=1, padx=4, pady=10, sticky=(constants.E, constants.W))

    def _do_creating_window(self):
        self._window = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._window)

        self._error_label = ttk.Label(
            master=self._window, textvariable=self._error_variable, foreground="red")

        self._error_label.grid(padx=4, pady=10)

        self._do_name_field()

        login_button = ttk.Button(master=self._window, text="Luo uusi ja kirjaudu", command=self._create_user_handler)

        self._window.grid_columnconfigure(0, weight=1, minsize=500)

        login_button.grid(row=2, padx=4, pady=10, sticky=(constants.E, constants.W))

        self._hide_error()
