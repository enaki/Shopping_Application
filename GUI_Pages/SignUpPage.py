import tkinter as tk
from tkinter import font as tkfont, ttk

import logging as log
import sys

from GUI_Pages.BasicPage import TitlePage
from Utilities.Cipher import Cipher

FORMAT = '[%(asctime)s] [%(levelname)s] : %(message)s'
log.basicConfig(stream=sys.stdout, level=log.DEBUG, format=FORMAT)


class SignUpPage(TitlePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.init()

    def init(self):
        width_label = 20
        width_entry = 25
        width_combo = 22

        self.text_font = tkfont.Font(family='Helvetica', size=13)
        self.button_font = tkfont.Font(family='Helvetica', size=10)

        sign_up_frame = tk.Frame(master=self, bg='gold')
        sign_up_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        sign_up_frame.grid_rowconfigure(1, weight=1)
        sign_up_frame.grid_columnconfigure(0, weight=1)

        tk.Label(sign_up_frame, text='Authentification', font=self.title_font, bg=sign_up_frame['bg'], fg='black').grid(row=0, column=0, padx=5, pady=5)

        ##---------------------Autentificaton-------------------
        sign_up_label_frame = tk.LabelFrame(sign_up_frame, bg='gray80')
        sign_up_label_frame.grid(row=1, column=0)

        tk.Label(sign_up_label_frame, text='First Name', font=self.text_font, bg=sign_up_label_frame['bg'], fg='red',
                 width=width_label).grid(row=0, column=0, padx=5, pady=10)
        self.first_name_entry = tk.Entry(sign_up_label_frame, width=width_entry)
        self.first_name_entry.grid(row=0, column=1,)

        tk.Label(sign_up_label_frame, text='Last Name', font=self.text_font, bg=sign_up_label_frame['bg'], fg='red',
                 width=width_label).grid(row=1, column=0, padx=5, pady=10)
        self.last_name_entry = tk.Entry(sign_up_label_frame, width=width_entry)
        self.last_name_entry.grid(row=1, column=1, padx=5, pady=10)

        tk.Label(sign_up_label_frame, text='Phone', font=self.text_font, bg=sign_up_label_frame['bg'], fg='red',
                 width=width_label).grid(row=2, column=0, padx=5, pady=10)
        self.phone_entry = tk.Entry(sign_up_label_frame, width=width_entry)
        self.phone_entry.grid(row=2, column=1, padx=5, pady=10)

        tk.Label(sign_up_label_frame, text='Email', font=self.text_font, bg=sign_up_label_frame['bg'], fg='red',
                 width=width_label).grid(row=3, column=0, padx=5, pady=10)
        self.email_entry = tk.Entry(sign_up_label_frame, width=width_entry)
        self.email_entry.grid(row=3, column=1, padx=5, pady=10)

        tk.Label(sign_up_label_frame, text='Country', font=self.text_font, bg=sign_up_label_frame['bg'], fg='red',
                 width=width_label).grid(row=4, column=0, padx=5, pady=10)
        self.country_combobox = ttk.Combobox(sign_up_label_frame, width=width_combo, values=self.get_countries())
        self.country_combobox.grid(row=4, column=1, padx=5, pady=10)
        self.country_combobox.bind("<<ComboboxSelected>>", self.country_combo_update)

        tk.Label(sign_up_label_frame, text='City', font=self.text_font, bg=sign_up_label_frame['bg'], fg='red',
                 width=width_label).grid(row=5, column=0, padx=5, pady=10)
        self.city_combobox = ttk.Combobox(sign_up_label_frame, width=width_combo)
        self.city_combobox.grid(row=5, column=1, padx=5, pady=10)
        self.city_combobox.bind("<<ComboboxSelected>>", self.city_combo_update)


        tk.Label(sign_up_label_frame, text='Street Address', font=self.text_font, bg=sign_up_label_frame['bg'], fg='red',
                 width=width_label).grid(row=6, column=0, padx=5, pady=10)
        self.street_combobox = ttk.Combobox(sign_up_label_frame, width=width_combo)
        self.street_combobox.grid(row=6, column=1, padx=5, pady=10)

        tk.Label(sign_up_label_frame, text='Username', font=self.text_font, bg=sign_up_label_frame['bg'], fg='red',
                 width=width_label).grid(row=7, column=0, padx=5, pady=10)
        self.username_entry = tk.Entry(sign_up_label_frame, width=width_entry)
        self.username_entry.grid(row=7, column=1, padx=5, pady=10)

        tk.Label(sign_up_label_frame, text='Password', font=self.text_font, bg=sign_up_label_frame['bg'], fg='red',
                 width=width_label).grid(row=8, column=0, padx=5, pady=10)
        self.password_entry = tk.Entry(sign_up_label_frame, show="*", width=width_entry)
        self.password_entry.grid(row=8, column=1, padx=5, pady=10)

        tk.Label(sign_up_label_frame, text='Retype Password', font=self.text_font, bg=sign_up_label_frame['bg'], fg='red',
                 width=width_label).grid(row=9, column=0, padx=5, pady=10)
        self.re_password_entry = tk.Entry(sign_up_label_frame, show="*", width=width_entry)
        self.re_password_entry.grid(row=9, column=1, padx=5, pady=10)

        tk.Label(sign_up_label_frame, text='User Level', font=self.text_font, bg=sign_up_label_frame['bg'],
                 fg='red',
                 width=width_label).grid(row=10, column=0, padx=5, pady=10)
        self.user_level = ttk.Combobox(sign_up_label_frame, state="readonly",
                  values=("client", "admin_shop", "admin_ship", "admin"))
        self.user_level.current(0)
        self.user_level.grid(row=10, column=1, padx=5, pady=10)

        self.sign_up_button = tk.Button(sign_up_label_frame, text='Submit', font=self.button_font, command=self.on_sign_up, bg='green', fg='white')
        self.sign_up_button.grid(row=11, column=1, padx=5, pady=5)

        self.back_button = tk.Button(sign_up_frame, text='Back', font=self.title_font, command=self.on_back, bg='red', fg='white')
        self.back_button.grid(row=2, column=0, padx=15, pady=15, sticky='w')

    def country_combo_update(self, event):
        self.city_combobox['values'] = self.get_cities(event.widget.get())

    def city_combo_update(self, event):
        self.street_combobox['values'] = self.get_streets(event.widget.get(), self.country_combobox.get())

    @staticmethod
    def fields_are_empty(first_name, last_name, phone, email, country, city, street_address, username, password, re_password):
        from tkinter import messagebox
        if first_name == '':
            messagebox.showinfo("Sign Up Error", "First Name required")
            return True
        if last_name == '':
            messagebox.showinfo("Sign Up Error", "Last Name required")
            return True
        if phone == '':
            messagebox.showinfo("Sign Up Error", "Phone required")
            return True
        if email == '':
            messagebox.showinfo("Sign Up Error", "Email required")
            return True
        if country == '':
            messagebox.showinfo("Sign Up Error", "Country required")
            return True
        if city == '':
            messagebox.showinfo("Sign Up Error", "City required")
            return True
        if street_address == '':
            messagebox.showinfo("Sign Up Error", "Street Address required")
            return True
        if username == '':
            messagebox.showinfo("Sign Up Error", "Username required")
            return True
        if password == '':
            messagebox.showinfo("Sign Up Error", "Password required")
            return True
        if re_password == '':
            messagebox.showinfo("Sign Up Error", "Re Password required")
            return True
        return False

    def validate_fields(self, phone, email, username, password, re_password):
        from tkinter import messagebox
        if not phone.isdigit():
            messagebox.showinfo("Sign Up Error", "Phone number invalid")
            return False
        if not self.is_email(email):
            messagebox.showinfo("Sign Up Error", "Email invalid")
            return False
        if self.get_user_id_by_username(username):
            messagebox.showinfo("Sign Up Error", "Username already taken")
            return False
        if self.get_user_id_by_email(email):
            messagebox.showinfo("Sign Up Error", "Email already taken")
            return False
        if self.get_user_id_by_phone(phone):
            messagebox.showinfo("Sign Up Error", "Phone already taken")
            return False
        if len(password) < 6:
            messagebox.showinfo("Sign Up Error", "Password too short")
            return False
        if password != re_password:
            messagebox.showinfo("Sign Up Error", "Passwords don't fetch")
            return False
        return True

    def get_user_id_by_username(self, username):
        username = username.replace('\'', '\'\'')
        query = "SELECT user_id from accounts where username='{}'".format(username)
        return [item for t in self.controller.run_query(query) for item in t]

    def get_user_id_by_email(self, email):
        email = email.replace('\'', '\'\'')
        query = "SELECT u.user_id from app_users u where email='{}'".format(email)
        return [item for t in self.controller.run_query(query) for item in t]

    def get_user_id_by_phone(self, phone):
        phone = phone.replace('\'', '\'\'')
        query = "SELECT u.user_id from app_users u where phone='{}'".format(phone)
        return [item for t in self.controller.run_query(query) for item in t]

    def on_sign_up(self):
        last_name = self.last_name_entry.get()
        first_name = self.first_name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        country = self.country_combobox.get()
        city = self.city_combobox.get()
        street_address = self.street_combobox.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        re_password = self.re_password_entry.get()
        user_level = self.user_level.get()

        if not self.string_length_is_okay(last_name, text='Last Name'):
            return
        last_name = last_name.strip()
        if not self.string_length_is_okay(first_name, text='First Name'):
            return
        first_name = first_name.strip()
        if not self.string_length_is_okay(phone, text='Phone'):
            return
        phone = phone.strip()
        if not self.string_length_is_okay(email, text='Email', length=30):
            return
        email = email.strip()
        if not self.string_length_is_okay(country, text='Country Name', length=30):
            return
        country = country.strip()
        if not self.string_length_is_okay(city, text='City Name', length=30):
            return
        city = city.strip()
        if not self.string_length_is_okay(street_address, text='Street Address', length=50):
            return
        street_address = street_address.strip()
        if not self.string_length_is_okay(username, text='Username', length=30):
            return
        username = username.strip()

        if not self.string_length_is_okay(password, text='Password', length=100):
            return
        if not self.string_length_is_okay(user_level, text='User Level', length=10):
            return

        if self.fields_are_empty(first_name, last_name, phone, email, country, city, street_address, username, password, re_password):
            return
        if not self.validate_fields(phone, email, username, password, re_password):
            return
        if not self.is_word_letters_and_spaces(country):
            from tkinter import messagebox
            messagebox.showinfo("Country Name Error", "Country Name should contains only letters and spaces")
            return
        if not self.is_word_letters_and_spaces(city):
            from tkinter import messagebox
            messagebox.showinfo("City Name Error", "City Name should contains only letters and spaces")
            return
        if not self.is_word_letters_and_spaces(first_name):
            from tkinter import messagebox
            messagebox.showinfo("First Name Error", "First Name should contains only letters and spaces")
            return
        if not self.is_word_letters_and_spaces(last_name):
            from tkinter import messagebox
            messagebox.showinfo("Last Name Error", "Last Name should contains only letters and spaces")
            return
        location_id = self.insert_or_get_location(street_address, city, country)
        last_name = last_name.replace('\'', '\'\'')
        first_name = first_name.replace('\'', '\'\'')
        email = email.replace('\'', '\'\'')
        username = username.replace('\'', '\'\'')
        password = password.replace('\'', '\'\'')
        user_level = user_level.replace('\'', '\'\'')

        query = "INSERT INTO app_users (first_name, last_name, location_id, email, phone) VALUES ('{}', '{}', {}, '{}', '{}')".format(first_name, last_name, location_id, email, phone)
        self.controller.run_query(query)
        user_id = self.get_user_id_by_email(self.email_entry.get())
        log.info("User Id Created : {}".format(user_id))

        # -------Use encryption when sending data across internet
        pass_encrypted = Cipher.encrypt(password)
        log.info("Password encrypted: {}".format(pass_encrypted.decode()))
        password = Cipher.decrypt(pass_encrypted)
        # log.info("Password decrypted: {}".format(password))
        # end encryption and decryption part

        query = "INSERT INTO accounts (user_id, username, password, account_type) VALUES ({}, '{}', '{}', '{}')".format(user_id[0], username, password, user_level)
        self.controller.run_query(query)
        from tkinter import messagebox
        messagebox.showinfo("Sign Up", "Account Created Succesfully")

    def on_back(self):
        self.controller.show_frame("LoginPage")

