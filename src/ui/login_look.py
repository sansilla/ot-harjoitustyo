from tkinter import ttk, StringVar, constants
from services.note_service import note_service, InvalidCredentialsError


class LoginLook:
    """Näkymä, joka hoitaa sisäänkirjautumisen
    """
    def __init__(self, root, handle_login, handle_create_user_look):
        """Konstruktori, joka luo kirjautumisikkunan

        Args:
            root: tkinter-rakenne, jossa näkymä luodaan
            handle_login (arvo): kutsutaan, kun kirjaudutaan sisään
            handle_create_user_look (arvo): kutsutaan, kun siirrytään luomaan uutta käyttäjää
        """
        self._root = root
        self._handle_login = handle_login
        self._handle_create_user_look = handle_create_user_look
        self._window = None
        self._username_entry = None
        self._error_variable = None
        self._error_label = None

        self._do_login_window()

    def pack(self):
        """Näyttää ikkunan
        """
        self._window.pack(fill=constants.Y)

    def destroy(self):
        """Tuhoaa ikkunan
        """
        self._window.destroy()

    def _do_login(self):
        username = self._username_entry.get()

        try:
            note_service.login(username)
            self._handle_login()
        except InvalidCredentialsError:
            self._show_error("Virheellinen käyttäjänimi")

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _do_username_field(self):
        username_label = ttk.Label(master=self._window, text="Käyttäjänimi:")

        self._username_entry = ttk.Entry(master=self._window)

        username_label.grid(row=0, padx=1, pady=10, sticky=constants.W)
        self._username_entry.grid(row=1, padx=4, pady=10, sticky=(constants.E, constants.W))

    def _do_login_window(self):
        self._window = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._window)

        self._error_label = ttk.Label(
            master=self._window, textvariable=self._error_variable, foreground="red")

        self._error_label.grid(padx=4, pady=10)

        self._do_username_field()

        login_button = ttk.Button(
            master=self._window, text="Kirjaudu sisään", command=self._do_login)

        user_creating_button = ttk.Button(
            master=self._window, text="Luo uusi käyttäjä", command=self._handle_create_user_look)

        self._window.grid_columnconfigure(0, weight=1, minsize=500)

        login_button.grid(row=2, padx=4, pady=10, sticky=(constants.E, constants.W))
        user_creating_button.grid(row=3, padx=4, pady=10, sticky=(constants.E, constants.W))

        self._hide_error()
