from tkinter import ttk, StringVar, constants
from services.note_service import UsernameAlreadyExistsError  # ja joku toinen


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

    def _initialize_name_field(self):
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

        self._initialize_name_field()

        create_user_button = ttk.Button(
            master=self._frame, text="Luo uusi ja kirjaudu", command=self._create_user_handler)

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        create_user_button.grid(padx=5, pady=5, sticky=constants.EW)

        self._hide_error()
