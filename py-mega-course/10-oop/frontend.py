from tkinter import *
from backend import Database

database = Database( "books.db" )

class GUI:
    BUTTON_WIDTH = 12

    def __init__( self ):

        self.window = Tk()
        self.window.title("Bookshop")

        #   LABELS
        self.label_title = Label( self.window, text="Title" )
        self.label_title.grid( row=0, column=0 )

        self.label_author = Label( self.window, text="Author" )
        self.label_author.grid( row=0, column=2 )

        self.label_year = Label( self.window, text="Year" )
        self.label_year.grid( row=1, column=0 )

        self.label_isbn = Label( self.window, text="ISBN" )
        self.label_isbn.grid( row=1, column=2 )

        #   ENTRIES
        self.entry_title_text = StringVar()
        self.entry_title = Entry(
            self.window,
            textvariable = self.entry_title_text )
        self.entry_title.grid( row = 0, column = 1 )

        self.entry_author_text = StringVar()
        self.entry_author = Entry(
            self.window,
            textvariable = self.entry_author_text )
        self.entry_author.grid( row = 0, column = 3 )

        self.entry_year_text = StringVar()
        self.entry_year = Entry(
            self.window,
            textvariable = self.entry_year_text )
        self.entry_year.grid( row = 1, column = 1 )

        self.entry_isbn_text = StringVar()
        self.entry_isbn = Entry(
            self.window,
            textvariable =  self.entry_isbn_text )
        self.entry_isbn.grid( row = 1, column = 3 )

        #   LISTBOX & SCROLLBAR
        self.listbox = Listbox(
            self.window,
            height=6, width=35 )
        self.listbox.grid(
            row=2, column=0,
            rowspan=6, columnspan=2)

        self.scrollbar = Scrollbar( self.window )
        self.scrollbar.grid(
            row=2, column=2,
            rowspan=6 )

        self.listbox.configure(
            yscrollcommand = self.scrollbar.set )
        self.scrollbar.configure(
            command = self.listbox.yview )

        self.listbox.bind(
            '<<ListboxSelect>>',
            self.get_selected_row )

        #   BUTTONS
        self.button_view = Button(
            self.window,
            text = "View all",
            width = self.BUTTON_WIDTH,
            command = self.command_view )
        self.button_view.grid( row=2, column=3 )

        self.button_search = Button(
            self.window,
            text = "Search entry",
            width = self.BUTTON_WIDTH,
            command =  self.command_search )
        self.button_search.grid( row=3, column=3 )

        self.button_add = Button(
            self.window,
            text = "Add entry",
            width = self.BUTTON_WIDTH,
            command = self.command_add )
        self.button_add.grid( row=4, column=3 )

        self.button_delete = Button(
            self.window,
            text = "Delete selected",
            width = self.BUTTON_WIDTH,
            command = self.command_delete )
        self.button_delete.grid( row=6, column=3 )

        self.button_update = Button(
            self.window,
            text = "Update",
            width = self.BUTTON_WIDTH,
            command= self.command_update )
        self.button_update.grid( row=5, column=3 )

        self.command_view()

    def run( self ):
        self.window.mainloop()

    def get_selected_row( self, event ):
        try:
            index = self.listbox.curselection()[0]

            self.selected_tuple = self.listbox.get( index )

            self.entry_title.delete( 0, END )
            self.entry_title.insert( END, self.selected_tuple[1] )

            self.entry_author.delete( 0, END )
            self.entry_author.insert( END, self.selected_tuple[2] )

            self.entry_year.delete( 0, END )
            self.entry_year.insert( END, self.selected_tuple[3] )

            self.entry_isbn.delete( 0, END )
            self.entry_isbn.insert( END, self.selected_tuple[4] )
        except IndexError:
            pass
        return None

    def command_view( self ):
        self.listbox.delete( 0, END )
        for row in database.view():
            self.listbox.insert( END, row )

    def command_search( self ):
        self.listbox.delete( 0, END )
        search_results = database.search(
            self.entry_title_text.get(),
            self.entry_author_text.get(),
            self.entry_year_text.get(),
            self.entry_isbn_text.get() )
        for row in search_results:
            self.listbox.insert( END, row )

    def command_add( self ):
        database.insert(
            self.entry_title_text.get(),
            self.entry_author_text.get(),
            self.entry_year_text.get(),
            self.entry_isbn_text.get()
        )
        self.command_view()

    def command_delete( self ):
        database.delete( self.selected_tuple[0] )
        self.command_view()

    def command_update( self ):
        database.update(
            self.selected_tuple[0],
            self.entry_title_text.get(),
            self.entry_author_text.get(),
            self.entry_year_text.get(),
            self.entry_isbn_text.get() )
        self.command_view()


GUI().run()
