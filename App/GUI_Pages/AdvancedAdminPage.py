from GUI_Pages.BasicPage import TitlePage
import tkinter as tk
from tkinter import font as tkfont, messagebox
from Utilities.TableFrame import TableFrame
import logging as log
import sys

FORMAT = '[%(asctime)s] [%(levelname)s] : %(message)s'
log.basicConfig(stream=sys.stdout, level=log.DEBUG, format=FORMAT)


class AdvancedAdminPage(TitlePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.init()

    def init(self):
        bg_color = 'black'
        btn_fg = 'white'

        self['bg'] = 'black'
        tk.Label(self, textvariable=self.controller.frames["HomePage"].home_page_welcome_label_var, font=self.title_font, bg='black', fg='white').pack(side=tk.TOP, fill=tk.X)

        home_frame = tk.Frame(master=self, bg=bg_color)
        home_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        home_frame.grid_rowconfigure(1, weight=1)
        home_frame.grid_columnconfigure(0, weight=1)
        home_frame.grid_columnconfigure(1, weight=1)

        viewer_frame = tk.LabelFrame(home_frame, bg=bg_color)
        viewer_frame.grid(row=0, column=0, columnspan=3, sticky='ew')
        viewer_frame.grid_columnconfigure(0, weight=1)
        viewer_frame.grid_rowconfigure(0, weight=1)
        #search menu
        self.init_search_frame(viewer_frame)

        #options row
        tk.Button(home_frame, text="Back", bg='red', fg=btn_fg, command=self.on_back, font=self.title_font).grid(row=2, column=0, padx=35, pady=15, sticky='w')
        tk.Label(home_frame, text="Advanced Option For Admins", fg='light green', bg=home_frame['bg'], font=self.title_font).grid(row=2, column=1, columnspan=2, padx=10, pady=10)

        #table
        columns_names = ['User Id', 'First Name', 'Last Name', 'Location Id', 'Email', 'Phone', 'Username', 'Password', 'Account Type']
        self.table = TableFrame(home_frame, columns_names)
        self.table.grid(row=1, column=0, columnspan=3, sticky="nesw", padx=5, pady=5)
        self.populate_the_table_with_all_values()
        self.table.tree.bind('<<TreeviewSelect>>', self.on_select)

    def on_select(self, event):
        pass

    def on_back(self):
        self.controller.show_frame('HomePage')

    def init_search_frame(self, master, row=0, column=0):
        width_label = 12
        self.search_frame = tk.LabelFrame(master, bg='gray85', text='Search', fg='green')
        self.search_frame.grid(row=row, column=column, pady=10)

        user_search_frame = tk.LabelFrame(self.search_frame, bg='gray94')
        user_search_frame.grid(row=0, column=0, pady=5, padx=5, sticky='w')
        tk.Label(user_search_frame, text='User Id', bg=user_search_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.user_id_entry = tk.Entry(user_search_frame)
        self.user_id_entry.grid(row=0, column=1, padx=5, pady=5)
        tk.Button(user_search_frame, text='Search', command=self.search_user).grid(row=0, column=2)

        first_name_search_frame = tk.LabelFrame(self.search_frame, bg='gray94')
        first_name_search_frame.grid(row=1, column=0, pady=5, padx=5, sticky='w')
        tk.Label(first_name_search_frame, text='First Name', bg=first_name_search_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.first_name_entry = tk.Entry(first_name_search_frame)
        self.first_name_entry.grid(row=0, column=1, padx=5, pady=5)
        tk.Button(first_name_search_frame, text='Search', command=self.search_first_name).grid(row=0, column=2)

        last_name_search_frame = tk.LabelFrame(self.search_frame, bg='gray94')
        last_name_search_frame.grid(row=2, column=0, pady=5, padx=5, sticky='w')
        tk.Label(last_name_search_frame, text='Last Name', bg=last_name_search_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.last_name_entry= tk.Entry(last_name_search_frame)
        self.last_name_entry.grid(row=0, column=1, padx=5, pady=5)
        tk.Button(last_name_search_frame, text='Search', command=self.search_last_name).grid(row=0, column=2)

        location_id_search_frame = tk.LabelFrame(self.search_frame, bg='gray94')
        location_id_search_frame.grid(row=3, column=0, pady=5, padx=5, sticky='w')
        tk.Label(location_id_search_frame, text='Location_id: ', bg=location_id_search_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.location_id_entry = tk.Entry(location_id_search_frame)
        self.location_id_entry.grid(row=0, column=1, padx=5, pady=5)
        tk.Button(location_id_search_frame, text='Search', command=self.search_location_id).grid(row=0, column=2)

        ###### second column
        email_search_frame = tk.LabelFrame(self.search_frame, bg='gray94')
        email_search_frame.grid(row=0, column=1, pady=5, padx=5, sticky='w')
        tk.Label(email_search_frame, text='Email', bg=email_search_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.email_entry = tk.Entry(email_search_frame)
        self.email_entry.grid(row=0, column=1, padx=5, pady=5)
        tk.Button(email_search_frame, text='Search', command=self.search_email).grid(row=0, column=2)

        phone_search_frame = tk.LabelFrame(self.search_frame, bg='gray94')
        phone_search_frame.grid(row=1, column=1, pady=5, padx=5, sticky='w')
        tk.Label(phone_search_frame, text='Phone', bg=phone_search_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.phone_entry = tk.Entry(phone_search_frame)
        self.phone_entry.grid(row=0, column=1, padx=5, pady=5)
        tk.Button(phone_search_frame, text='Search', command=self.search_phone).grid(row=0, column=2)

        username_search_frame = tk.LabelFrame(self.search_frame, bg='gray94')
        username_search_frame.grid(row=2, column=1, pady=5, padx=5, sticky='w')
        tk.Label(username_search_frame, text='Username', bg=username_search_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.username_entry = tk.Entry(username_search_frame)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)
        tk.Button(username_search_frame, text='Search', command=self.search_username).grid(row=0, column=2)

        account_search_frame = tk.LabelFrame(self.search_frame, bg='gray94')
        account_search_frame.grid(row=3, column=1, pady=5, padx=5, sticky='w')
        tk.Label(account_search_frame, text='Account Type: ', bg=account_search_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.account_entry = tk.Entry(account_search_frame)
        self.account_entry.grid(row=0, column=1, padx=5, pady=5)
        tk.Button(account_search_frame, text='Search', command=self.search_account).grid(row=0, column=2)

        option_search_frame = tk.LabelFrame(self.search_frame, bg='gray94')
        option_search_frame.grid(row=4, column=0, columnspan=2, pady=5, padx=5, sticky='ew')
        option_search_frame.grid_columnconfigure(0, weight=1)
        self.search_by_all_categories_button = tk.Button(option_search_frame, text='Search By All Categories (Without User Id)', command=self.global_search, bg='light cyan',
                  fg='red')
        self.search_by_all_categories_button.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    def populate_the_table_with_all_values(self):
        self.table.clear_table()
        query_select = self.controller.run_query("SELECT u.user_id, u.first_name, u.last_name, u.location_id, u.email, u.phone, a.username, decode(a.account_type, 'admin', lpad('*', length(a.password), '*'), a.password), a.account_type from app_users u, accounts a where "
                                                 "a.user_id=u.user_id")
        for row in query_select:
            self.table.insert('', 'end', values=row)

    def search_user(self):
        log.info("Search User Id")
        name = self.user_id_entry.get()
        if not name.isdigit() and name != '':
            messagebox.showinfo("Error Search", "User Id is not number")
            return
        name = self.controller.add_escape_characters(name)
        query = "SELECT u.user_id, u.first_name, u.last_name, u.location_id, u.email, u.phone, a.username, decode(a.account_type, 'admin', lpad('*', length(a.password), '*'), a.password), a.account_type from app_users u, accounts a " \
                "where a.user_id=u.user_id and u.user_id={}".format(name)
        self.search(name, query)

    def search(self, name, query):
        self.table.clear_table()
        if name == '':
            self.populate_the_table_with_all_values()
        else:
            query_select = self.controller.run_query(query)
            for row in query_select:
                self.table.insert('', 'end', values=row)

    def search_first_name(self):
        log.info("Search First Name")
        name = self.first_name_entry.get()

        name = self.controller.add_escape_characters(name)
        query = "SELECT u.user_id, u.first_name, u.last_name, u.location_id, u.email, u.phone, a.username, decode(a.account_type, 'admin', lpad('*', length(a.password), '*'), a.password), a.account_type from app_users u, accounts a " \
                "where a.user_id=u.user_id and lower(u.first_name) like '%{}%' escape '#'".format(name.lower())
        self.search(name, query)

    def search_last_name(self):
        log.info("Search Last Name")
        name = self.last_name_entry.get()

        name = self.controller.add_escape_characters(name)
        query = "SELECT u.user_id, u.first_name, u.last_name, u.location_id, u.email, u.phone, a.username, decode(a.account_type, 'admin', lpad('*', length(a.password), '*'), a.password), a.account_type from app_users u, accounts a " \
                "where a.user_id=u.user_id and lower(u.last_name) like '%{}%' escape '#'".format(name.lower())
        self.search(name, query)

    def search_location_id(self):
        log.info("Search Location Id")
        name = self.location_id_entry.get()
        if not name.isdigit() and name != '':
            messagebox.showinfo("Error Search", "Location Id is not number")
            return
        name = self.controller.add_escape_characters(name)
        query = "SELECT u.user_id, u.first_name, u.last_name, u.location_id, u.email, u.phone, a.username, decode(a.account_type, 'admin', lpad('*', length(a.password), '*'), a.password), a.account_type from app_users u, accounts a " \
                "where a.user_id=u.user_id and u.location_id={}".format(name)
        self.search(name, query)

    def search_email(self):
        log.info("Search Email")
        name = self.email_entry.get()

        name = self.controller.add_escape_characters(name)
        query = "SELECT u.user_id, u.first_name, u.last_name, u.location_id, u.email, u.phone, a.username, decode(a.account_type, 'admin', lpad('*', length(a.password), '*'), a.password), a.account_type from app_users u, accounts a " \
                "where a.user_id=u.user_id and lower(u.email) like '%{}%' escape '#'".format(name.lower())
        self.search(name, query)

    def search_phone(self):
        log.info("Search Phone")
        name = self.phone_entry.get()
        if not name.isdigit() and name != '':
            messagebox.showinfo("Error Search", "Phone Number is not number")
            return
        name = self.controller.add_escape_characters(name)
        query = "SELECT u.user_id, u.first_name, u.last_name, u.location_id, u.email, u.phone, a.username, decode(a.account_type, 'admin', lpad('*', length(a.password), '*'), a.password), a.account_type from app_users u, accounts a " \
                "where a.user_id=u.user_id and lower(u.phone) like '%{}%' escape '#'".format(name.lower())
        self.search(name, query)

    def search_username(self):
        log.info("Search Username")
        name = self.username_entry.get()

        name = self.controller.add_escape_characters(name)
        query = "SELECT u.user_id, u.first_name, u.last_name, u.location_id, u.email, u.phone, a.username, decode(a.account_type, 'admin', lpad('*', length(a.password), '*'), a.password), a.account_type from app_users u, accounts a " \
                "where a.user_id=u.user_id and lower(a.username) like '%{}%' escape '#'".format(name.lower())
        self.search(name, query)

    def search_account(self):
        log.info("Search Account")
        name = self.account_entry.get()

        name = self.controller.add_escape_characters(name)
        query = "SELECT u.user_id, u.first_name, u.last_name, u.location_id, u.email, u.phone, a.username, decode(a.account_type, 'admin', lpad('*', length(a.password), '*'), a.password), a.account_type from app_users u, accounts a " \
                "where a.user_id=u.user_id and lower(a.account_type) like '%{}%' escape '#'".format(name.lower())
        self.search(name, query)

    def global_search(self):
        log.info("Search Global")

        first_name = self.first_name_entry.get()
        first_name = self.controller.add_escape_characters(first_name)

        last_name = self.last_name_entry.get()
        last_name = self.controller.add_escape_characters(last_name)

        location_id = self.location_id_entry.get()
        if not location_id.isdigit() and location_id != '':
            messagebox.showinfo("Error Search", "Location Id is not number")
            return
        location_id = self.controller.add_escape_characters(location_id)

        email = self.email_entry.get()
        email = self.controller.add_escape_characters(email)

        phone = self.phone_entry.get()
        if not phone.isdigit() and phone != '':
            messagebox.showinfo("Error Search", "Phone Number is not number")
            return
        phone = self.controller.add_escape_characters(phone)

        username = self.username_entry.get()
        username = self.controller.add_escape_characters(username)

        account = self.account_entry.get()
        account = self.controller.add_escape_characters(account)
        if location_id != '':
            query = "SELECT u.user_id, u.first_name, u.last_name, u.location_id, u.email, u.phone, a.username, decode(a.account_type, 'admin', lpad('*', length(a.password), '*'), a.password), a.account_type from app_users u, accounts a " \
                    "where a.user_id=u.user_id and lower(u.first_name) like '%{}%' escape '#'" \
                    "and lower(u.last_name) like '%{}%' escape '#'" \
                    "and u.location_id={}" \
                    "and lower(u.email) like '%{}%' escape '#'" \
                    "and lower(u.phone) like '%{}%' escape '#'" \
                    "and lower(a.username) like '%{}%' escape '#'" \
                    "and lower(a.account_type) like '%{}%' escape '#'".format(first_name.lower(), last_name.lower(), location_id, email.lower(), phone, username.lower(),
                                                                              account.lower())
        else:
            query = "SELECT u.user_id, u.first_name, u.last_name, u.location_id, u.email, u.phone, a.username, decode(a.account_type, 'admin', lpad('*', length(a.password), '*'), a.password), a.account_type from app_users u, accounts a " \
                    "where a.user_id=u.user_id and lower(u.first_name) like '%{}%' escape '#'" \
                    "and lower(u.last_name) like '%{}%' escape '#'" \
                    "and lower(u.email) like '%{}%' escape '#'" \
                    "and lower(u.phone) like '%{}%' escape '#'" \
                    "and lower(a.username) like '%{}%' escape '#'" \
                    "and lower(a.account_type) like '%{}%' escape '#'".format(first_name.lower(), last_name.lower(),
                                                                              email.lower(), phone,
                                                                              username.lower(),
                                                                              account.lower())
        self.table.clear_table()
        query_select = self.controller.run_query(query)
        for row in query_select:
            self.table.insert('', 'end', values=row)
