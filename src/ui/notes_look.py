from tkinter import ttk, constants
from services.note_service import note_service

class NoteListView:
    def __init__(self, root, notes):
        self._root = root
        self._notes = notes
        self._frame = None

        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        for note in self._notes:
            self._initialize_note_thing(note)

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_note_thing(self, note):
        thing_frame = ttk.Frame(master=self._frame)
        label = ttk.Label(master=thing_frame, text=note.note)

        label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

        thing_frame.grid_columnconfigure(0, weight=1)
        thing_frame.pack(fill=constants.X)

class NotesView:
    def __init__(self, root, handle_logout):
        self._root = root
        self._handle_logout = handle_logout
        self._user = note_service.see_current_user()
        self._frame = None
        self._create_note_entry = None
        self._note_list_frame = None
        self._note_list_look = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _logout_helper(self):
        note_service.logout()
        self._handle_logout()

    def _initialize_note_list(self):
        if self._note_list_look:
            self._note_list_look.destroy()

        notes = note_service.get_notes()

        self._note_list_look = NoteListView(self._note_list_frame, notes)

        self._note_list_look.pack()
        
    def _initialize_header(self):
        user_label = ttk.Label(master=self._frame, text=f"Kirjautuneena sisään käyttäjällä {self._user.name}")

        logout_button = ttk.Button(master=self._frame, text="Uloskirjautuminen", command=self._logout_helper)

        user_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

        logout_button.grid(row=0, column=1, padx=5, pady=5, sticky=constants.EW)

    def _handle_create_note(self):
        note_inside = self._create_note_entry.get()

        if note_inside:
            note_service.diary_note(note_inside)
            self._initialize_note_list()
            self._create_note_entry.delete(0, constants.END)

    def _initialize_footer(self):
        self._create_note_entry = ttk.Entry(master=self._frame)

        create_note_button = ttk.Button(master=self._frame, text="Kirjaa", command=self._handle_create_note)

        self._create_note_entry.grid(row=2, column=0, padx=5, pady=5, sticky=constants.EW)

        create_note_button.grid(row=2, column=1, padx=5, pady=5, sticky=constants.EW)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._note_list_frame = ttk.Frame(master=self._frame)

        self._initialize_header()
        self._initialize_note_list()
        self._initialize_footer()

        self._note_list_frame.grid(row=1, column=0, columnspan=2, sticky=constants.EW)

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._frame.grid_columnconfigure(1, weight=0)
