import abc
import tkinter as tk
from tkinter import font as tkfont

import logging as log
import sys

FORMAT = '[%(asctime)s] [%(levelname)s] : %(message)s'
log.basicConfig(stream=sys.stdout, level=log.DEBUG, format=FORMAT)


class TitlePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=parent['bg'])
        self.controller = controller
        self.parent = parent
        self.title_font = tkfont.Font(family='Helvetica', size=20, weight="bold")
        self.title_color = 'dark orange'
        self.init_title()

    def init_title(self):
        # ---------------Title------------------
        title_frame = tk.Frame(master=self, bg=self.parent['bg'])
        title_frame.pack(side=tk.TOP, fill=tk.X)
        for i in range(2):
            title_frame.grid_columnconfigure(i, weight=1)

        tk.Label(master=title_frame, text="BD", font=self.title_font, fg='red', bg=title_frame['bg']).grid(row=0,
                                                                                                           column=0,
                                                                                                           sticky='e')
        tk.Label(title_frame, text="Express", font=self.title_font, fg=self.title_color, bg=title_frame['bg']).grid(
            row=0, column=1, sticky='w')

    @staticmethod
    def is_word_letters_and_spaces(string):
        if all(x.isalpha() or x.isspace() for x in string):
            return True
        return False

    def is_user_in_db(self, user_id):
        query = "SELECT user_id from app_users where user_id={}".format(user_id)
        return bool(self.controller.run_query(query))

    def session_is_allright(self):
        if not self.controller.user_info or not self.is_user_in_db(self.controller.user_info['user_id']):
            from tkinter import messagebox
            messagebox.showinfo("Account Error", "User invalid. We are sorry! Bye")
            self.controller.show_frame('LoginPage')
            return False
        return True

    @staticmethod
    def is_number(number, min_range=0, max_range=1000_000, zero_permited=False):
        import re
        try:
            number_temp = float(number)
            if zero_permited and number_temp == 0:
                return True
            if number_temp <= min_range or number_temp >= max_range:
                return False
        except ValueError:
            return False
        return bool(re.match(r"[\d]+(.\d)?[\d]*", number))

    @staticmethod
    def string_length_is_okay(string, length=20, text='String'):
        if len(string) <= length:
            return True
        else:
            from tkinter import messagebox
            messagebox.showinfo("String Size Error", "{} length should be lower than {}".format(text, length))
            return False

    def get_countries(self):
        query = "SELECT unique(country) from locations"
        return [item for t in self.controller.run_query(query) for item in t]

    def get_cities(self, country):
        country = country.replace('\'', '\'\'')
        query = "SELECT unique(city) from locations where country='{}'".format(country)
        return [item for t in self.controller.run_query(query) for item in t]

    def get_streets(self, city, country):
        city = city.replace('\'', '\'\'')
        country = country.replace('\'', '\'\'')
        query = "SELECT unique(street_address) from locations where city='{}' and country='{}'".format(city, country)
        return [item for t in self.controller.run_query(query) for item in t]

    @staticmethod
    def is_email(number):
        import re
        return bool(re.match(r"[^@]+@[^@]+\.[^@]+", number))

    def insert_or_get_location(self, street, city, country):
        street = street.replace('\'', '\'\'')
        city = city.replace('\'', '\'\'')
        country = country.replace('\'', '\'\'')
        location_id_query = "SELECT location_id from locations where lower(street_address)='{}' and lower(city)='{}' and lower(country)='{}'".format(
            street.lower(), city.lower(), country.lower())
        query_select = self.controller.run_query(location_id_query)
        if not query_select:
            location_id_query = "INSERT INTO locations (street_address, city, country) VALUES ('{}', '{}', '{}')".format(
                street, city, country)
            self.controller.run_query(location_id_query)
            location_id_query = "SELECT location_id from locations where street_address='{}' and city='{}' and country='{}'".format(
                street, city, country)
            query_select = self.controller.run_query(location_id_query)
        return query_select[0][0]

class BasicPage(TitlePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.button_font = tkfont.Font(family='Helvetica', size=14)
        self.init_option_buttons()

    def init_option_buttons(self, button_bg='cadet blue', button_fg='white'):
        #---------------Options Frame Page----------------
        change_page_frame = tk.Frame(master=self, bg='gray87')
        change_page_frame.pack(side=tk.TOP, fill=tk.X)
        for i in range(4):
            change_page_frame.grid_columnconfigure(i, weight=1)

        self.button_home = tk.Button(change_page_frame, text="Home", bg=button_bg, fg=button_fg, font=self.button_font, command=self.on_home_button)
        self.button_home.grid(row=0, column=0, padx=5, pady=5, sticky='ew')

        self.button_shop = tk.Button(change_page_frame, text="Shops", bg=button_bg, fg=button_fg, font=self.button_font, command=self.on_shop_button)
        self.button_shop.grid(row=0, column=1, padx=5, pady=5, sticky='ew')

        self.button_product = tk.Button(change_page_frame, text="Products", bg=button_bg, fg=button_fg, font=self.button_font, command=self.on_product_button)
        self.button_product.grid(row=0, column=2, padx=5, pady=5, sticky='ew')

        self.button_shipping = tk.Button(change_page_frame, text="Shipping", bg=button_bg, fg=button_fg, font=self.button_font, command=self.on_shipping_button)
        self.button_shipping.grid(row=0, column=3, padx=5, pady=5, sticky='ew')

    @abc.abstractmethod
    def populate_the_table_with_all_values(self):
        pass

    def on_home_button(self):
        self.controller.show_frame('HomePage')

    def on_shop_button(self):
        self.controller.show_frame('ShopPage')

    def on_product_button(self):
        self.controller.show_frame('ProductPage')

    def on_shipping_button(self):
        self.controller.show_frame('ShippingPage')




