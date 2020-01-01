import tkinter as tk
import cx_Oracle

from GUI_Pages.SignUpPage import SignUpPage
from GUI_Pages.LoginPage import LoginPage
from GUI_Pages.HomePage import HomePage
from GUI_Pages.ShopPage import ShopPage
from GUI_Pages.ShippingPage import ShippingPage
from GUI_Pages.ProductPage import ProductPage
from GUI_Pages.AdvancedAdminPage import AdvancedAdminPage
import logging as log
import sys

FORMAT = '[%(asctime)s] [%(levelname)s] : %(message)s'
log.basicConfig(stream=sys.stdout, level=log.DEBUG, format=FORMAT)


class BdGui(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "BDExpress")

        self.container = tk.Frame(self, bg='gray97')
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.conn = cx_Oracle.connect("enaki", "dell5567", "localhost/xe")

        self.user_info = {}

        self.frames = {}
        for F in (HomePage, ShopPage, ProductPage, ShippingPage, LoginPage, SignUpPage, AdvancedAdminPage):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nesw")
        self.show_frame('LoginPage')

    def re_create_frames(self):
        for frame in self.frames.values():
            for widget in frame.winfo_children():
                widget.destroy()
        for F in (HomePage, ShopPage, ProductPage, ShippingPage, LoginPage, SignUpPage, AdvancedAdminPage):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nesw")
        self.show_frame('HomePage')
        log.info("Recreate Frames succesfully")

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()

    def run_query(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        try:
            query_results = [row for row in cursor]
            self.conn.commit()
            cursor.close()
        except cx_Oracle.InterfaceError:
            self.conn.commit()
            cursor.close()
            return None
        return query_results

    def get_columns_name(self, table_name):
        query = "SELECT column_name FROM USER_TAB_COLUMNS WHERE lower(table_name) = '{}'".format(table_name)
        return self.run_query(query)

    @staticmethod
    def add_escape_characters(name):
        special_characters = "#_%"
        for c in special_characters:
            name = name.replace(c, '#' + c)
        return name.replace('\'', "\'\'")

    @staticmethod
    def set_entry_text(widget, text):
        widget.delete(0, tk.END)
        widget.insert(0, text)

    def set_state(self, widget, state='disabled'):
        #log.info("Set state for {}".format(type(widget)))
        try:
            widget.configure(state=state)
        except tk.TclError:
            pass
        for child in widget.winfo_children():
            self.set_state(child, state=state)
