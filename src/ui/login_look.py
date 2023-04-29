from tkinter import ttk, StringVar, constants
from services.note_service import note_service, InvalidCredentialsError


class LoginLook:
    def __init__(self, root, handle_login, handle_create_user_look):
        self._root = root
        self._handle_login = handle_login
        self._handle_create_user_look = handle_create_user_look
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

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
        username_label = ttk.Label(master=self._frame, text="Käyttäjänimi:")

        self._username_entry = ttk.Entry(master=self._frame)

        username_label.grid(padx=5, pady=5, sticky=constants.W)
        self._username_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame, textvariable=self._error_variable, foreground="red")

        self._error_label.grid(padx=5, pady=5)

        self._do_username_field()

        login_button = ttk.Button(
            master=self._frame, text="Kirjaudu sisään", command=self._do_login)

        create_user_button = ttk.Button(
            master=self._frame, text="Luo uusi käyttäjä", command=self._handle_create_user_look)

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        login_button.grid(padx=5, pady=5, sticky=constants.EW)
        create_user_button.grid(padx=5, pady=5, sticky=constants.EW)

        self._hide_error()
