import tkinter as tk
from tkinter import font as tkfont, ttk

import logging as log
import sys

from GUI_Pages.BasicPage import TitlePage

FORMAT = '[%(asctime)s] [%(levelname)s] : %(message)s'
log.basicConfig(stream=sys.stdout, level=log.DEBUG, format=FORMAT)


class LoginPage(TitlePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.init()

    def init(self):
        width_label = 10
        width_entry = 25

        text_font = tkfont.Font(family='Helvetica', size=13)
        button_font = tkfont.Font(family='Helvetica', size=10)

        login_frame = tk.Frame(master=self, bg='gold')
        login_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        login_frame.grid_rowconfigure(0, weight=1)
        login_frame.grid_columnconfigure(0, weight=1)

        login_label_frame = tk.LabelFrame(login_frame, bg='gray80')
        login_label_frame.grid(row=0, column=0)

        tk.Label(login_label_frame, text='username', font=text_font, bg=login_label_frame['bg'], fg='red',
                 width=width_label).grid(row=0, column=0, padx=5, pady=10)
        self.username_entry = tk.Entry(login_label_frame, width=width_entry)
        self.username_entry.grid(row=0, column=1,)

        tk.Label(login_label_frame, text='password', font=text_font, bg=login_label_frame['bg'], fg='red',
                 width=width_label).grid(row=1, column=0, padx=5, pady=10)
        self.password_entry = tk.Entry(login_label_frame, show="*", width=width_entry)
        self.password_entry.grid(row=1, column=1, padx=5, pady=10)

        self.login_button = tk.Button(login_label_frame, text='Login', font=button_font, command=self.on_login, bg='gray', fg='white')
        self.login_button.grid(row=2, column=1, padx=5, pady=5)

        self.sign_up_button = tk.Button(login_label_frame, text='Sign Up', font=button_font, command=self.on_sign_up, bg='gray', fg='white')
        self.sign_up_button.grid(row=2, column=0, padx=5, pady=5)

    def set_states(self, user_level):
        if user_level == 'admin':
            return
        else:
            self.controller.set_state(self.controller.frames['HomePage'].advanced_options_button)
            self.controller.set_state(self.controller.frames['ShopPage'].insert_frame)
            self.controller.set_state(self.controller.frames['ShopPage'].update_frame)
            self.controller.set_state(self.controller.frames['ShopPage'].delete_frame)
            self.controller.set_state(self.controller.frames['ProductPage'].insert_frame)
            self.controller.set_state(self.controller.frames['ProductPage'].update_frame)
            self.controller.set_state(self.controller.frames['ProductPage'].delete_frame)
            self.controller.set_state(self.controller.frames['ShippingPage'].insert_frame)
            self.controller.set_state(self.controller.frames['ShippingPage'].update_frame)
            self.controller.set_state(self.controller.frames['ShippingPage'].delete_frame)
            if user_level == 'admin_shop':
                self.controller.set_state(self.controller.frames['ShopPage'].insert_frame, 'normal')
                self.controller.set_state(self.controller.frames['ShopPage'].update_frame, 'normal')
                self.controller.set_state(self.controller.frames['ShopPage'].delete_frame, 'normal')
                self.controller.set_state(self.controller.frames['ProductPage'].insert_frame, 'normal')
                self.controller.set_state(self.controller.frames['ProductPage'].update_frame, 'normal')
                self.controller.set_state(self.controller.frames['ProductPage'].delete_frame, 'normal')
            if user_level == 'admin_ship':
                self.controller.set_state(self.controller.frames['ShippingPage'].insert_frame, 'normal')
                self.controller.set_state(self.controller.frames['ShippingPage'].update_frame, 'normal')
                self.controller.set_state(self.controller.frames['ShippingPage'].delete_frame, 'normal')

    def on_login(self):
        username = self.username_entry.get().replace('\'', '\'\'')
        password = self.password_entry.get().replace('\'', '\'\'')

        query = "SELECT u.user_id, u.first_name, u.last_name, u.location_id, u.email, u.phone, a.account_type from app_users u, accounts a where u.user_id = a.user_id and a.username='{}' and a.password='{}'".format(username, password)
        user_info = [item for t in self.controller.run_query(query) for item in t]
        if user_info:
            self.controller.user_info['user_id'] = user_info[0]
            self.controller.user_info['first_name'] = user_info[1]
            self.controller.user_info['last_name'] = user_info[2]
            self.controller.user_info['location_id'] = user_info[3]
            self.controller.user_info['email'] = user_info[4]
            self.controller.user_info['phone'] = user_info[5]
            self.controller.user_info['user_level'] = user_info[6]

            self.controller.re_create_frames()
            self.set_states(user_info[6])

            self.controller.frames["HomePage"].home_page_welcome_label_var.set("Welcome {}".format(user_info[1]))
            self.controller.frames["HomePage"].populate_the_table_with_all_values()
            self.controller.show_frame("HomePage")
        else:
            log.info("Login Failed Incorect username as password")
            from tkinter import messagebox
            messagebox.showinfo("Login Failed", "Wrong username or password")


    def on_sign_up(self):
        self.controller.show_frame("SignUpPage")