from GUI_Pages.BasicPage import BasicPage
from Utilities.TableFrame import TableFrame
import tkinter as tk

import logging as log
import sys

FORMAT = '[%(asctime)s] [%(levelname)s] : %(message)s'
log.basicConfig(stream=sys.stdout, level=log.DEBUG, format=FORMAT)


class ShopPage(BasicPage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.init()

    def init(self):
        self.button_shop['bg'] = 'dark orange'

        bg_color = 'gold'
        viewer_frame = tk.LabelFrame(self, bg=bg_color)
        viewer_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        viewer_frame.grid_columnconfigure(0, weight=1)
        viewer_frame.grid_columnconfigure(1, weight=1)
        viewer_frame.grid_columnconfigure(2, weight=1)
        viewer_frame.grid_columnconfigure(3, weight=1)
        viewer_frame.grid_rowconfigure(2, weight=1)

        #------------search_bar------------------
        self.init_search_frame(viewer_frame)
        self.init_insert_frame(viewer_frame)
        self.init_update_frame(viewer_frame)
        self.init_delete_frame(viewer_frame)

        query = list(map("".join, self.controller.get_columns_name('shops')))[:2]
        query.extend(list(map("".join, self.controller.get_columns_name('locations')))[1:])
        self.table = TableFrame(viewer_frame, query)
        self.table.grid(row=2, column=0, columnspan=4, sticky="nesw", padx=5, pady=5)
        self.populate_the_table_with_all_values()
        self.table.tree.bind('<<TreeviewSelect>>', self.on_select)

    def OnDoubleClick(self, event):
        item = self.table.tree.identify('item', event.x, event.y)
        print("you clicked on", self.table.tree.item(item, "values"))

    def on_select(self, event):
        self.selected_item = event.widget.item(event.widget.selection()[0], "values")
        self.shop_name_var.set(self.selected_item[1])
        self.street_name_var.set(self.selected_item[2])
        self.city_name_var.set(self.selected_item[3])
        self.country_name_var.set(self.selected_item[4])
        from bd_gui import BdGui
        BdGui.set_entry_text(self.shop_name_update_entry, self.selected_item[1])
        BdGui.set_entry_text(self.street_name_update_entry, self.selected_item[2])
        BdGui.set_entry_text(self.city_name_update_entry, self.selected_item[3])
        BdGui.set_entry_text(self.country_name_update_entry, self.selected_item[4])

    def init_search_frame(self, master, row=0, column=0):
        width_label = 7
        self.search_frame = tk.LabelFrame(master, bg='gray85', text='Search', fg='green')
        self.search_frame.grid(row=row, column=column, pady=10)

        shop_search_frame = tk.LabelFrame(self.search_frame, bg='gray94')
        shop_search_frame.grid(row=0, column=0, pady=5, padx=5, sticky='w')
        tk.Label(shop_search_frame, text='Shop/Id', bg=shop_search_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.shop_name_search = tk.Entry(shop_search_frame)
        self.shop_name_search.grid(row=0, column=1, padx=5, pady=5)
        tk.Button(shop_search_frame, text='Search', command=self.search_shop).grid(row=0, column=2)

        street_search_frame = tk.LabelFrame(self.search_frame, bg='gray94')
        street_search_frame.grid(row=1, column=0, pady=5, padx=5, sticky='w')
        tk.Label(street_search_frame, text='Street', bg=street_search_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.street_name_search = tk.Entry(street_search_frame)
        self.street_name_search.grid(row=0, column=1, padx=5, pady=5)
        tk.Button(street_search_frame, text='Search', command=self.search_street).grid(row=0, column=2)

        city_search_frame = tk.LabelFrame(self.search_frame, bg='gray94')
        city_search_frame.grid(row=2, column=0, pady=5, padx=5, sticky='w')
        tk.Label(city_search_frame, text='City', bg=city_search_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.city_name_search= tk.Entry(city_search_frame)
        self.city_name_search.grid(row=0, column=1, padx=5, pady=5)
        tk.Button(city_search_frame, text='Search', command=self.search_city).grid(row=0, column=2)

        country_search_frame = tk.LabelFrame(self.search_frame, bg='gray94')
        country_search_frame.grid(row=3, column=0, pady=5, padx=5, sticky='w')
        tk.Label(country_search_frame, text='Country: ', bg=country_search_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.country_name_search = tk.Entry(country_search_frame)
        self.country_name_search.grid(row=0, column=1, padx=5, pady=5)
        tk.Button(country_search_frame, text='Search', command=self.search_country).grid(row=0, column=2)

        option_search_frame = tk.LabelFrame(self.search_frame, bg='gray94')
        option_search_frame.grid(row=4, column=0, pady=5, padx=5, sticky='ew')
        self.search_by_shop_id = tk.IntVar()
        from tkinter import ttk
        ttk.Checkbutton(option_search_frame, text="Shop Id", variable=self.search_by_shop_id, command=self.on_check_shop_id).grid(row=0, column=0, padx=5, pady=5)
        self.search_by_all_categories_button = tk.Button(option_search_frame, text='Search By All Categories', command=self.global_search, bg='light cyan',
                  fg='red')
        self.search_by_all_categories_button.grid(row=0, column=1, padx=5, pady=5)

    def on_check_shop_id(self):
        if self.search_by_shop_id.get():
            self.search_by_all_categories_button['state'] = tk.DISABLED
        else:
            self.search_by_all_categories_button['state'] = tk.NORMAL

    def init_insert_frame(self, master, row=0, column=1):
        width_label = 7
        self.insert_frame = tk.LabelFrame(master, bg='gray85', text='Insert', fg='green')
        self.insert_frame.grid(row=row, column=column, pady=10)

        shop_insert_frame = tk.LabelFrame(self.insert_frame, bg='gray94')
        shop_insert_frame.grid(row=0, column=0, pady=5, padx=5, sticky='w')
        tk.Label(shop_insert_frame, text='Shop: ', bg=shop_insert_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.shop_name_insert = tk.Entry(shop_insert_frame)
        self.shop_name_insert.grid(row=0, column=1, padx=5, pady=5)

        street_insert_frame = tk.LabelFrame(self.insert_frame, bg='gray94')
        street_insert_frame.grid(row=1, column=0, pady=5, padx=5, sticky='w')
        tk.Label(street_insert_frame, text='Street: ', bg=street_insert_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.street_name_insert = tk.Entry(street_insert_frame)
        self.street_name_insert.grid(row=0, column=1, padx=5, pady=5)

        city_insert_frame = tk.LabelFrame(self.insert_frame, bg='gray94')
        city_insert_frame.grid(row=2, column=0, pady=5, padx=5, sticky='w')
        tk.Label(city_insert_frame, text='City: ', bg=city_insert_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.city_name_insert = tk.Entry(city_insert_frame)
        self.city_name_insert.grid(row=0, column=1, padx=5, pady=5)

        country_insert_frame = tk.LabelFrame(self.insert_frame, bg='gray94')
        country_insert_frame.grid(row=3, column=0, pady=5, padx=5, sticky='w')
        tk.Label(country_insert_frame, text='Country: ', bg=country_insert_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.country_name_insert = tk.Entry(country_insert_frame)
        self.country_name_insert.grid(row=0, column=1, padx=5, pady=5)

        tk.Button(self.insert_frame, text='Insert', command=self.insert, bg='light cyan',
                  fg='red').grid(row=4, column=0, padx=5, pady=5)

    def init_update_frame(self, master, row=0, column=2):
        width_label = 7
        self.update_frame = tk.LabelFrame(master, bg='gray85', text='Update', fg='green')
        self.update_frame.grid(row=row, column=column, pady=10)

        shop_update_frame = tk.LabelFrame(self.update_frame, bg='gray94')
        shop_update_frame.grid(row=0, column=0, pady=5, padx=5, sticky='w')
        tk.Label(shop_update_frame, text='Shop: ', bg=shop_update_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.shop_name_update_entry = tk.Entry(shop_update_frame)
        self.shop_name_update_entry.grid(row=0, column=1, padx=5, pady=5)

        street_update_frame = tk.LabelFrame(self.update_frame, bg='gray94')
        street_update_frame.grid(row=1, column=0, pady=5, padx=5, sticky='w')
        tk.Label(street_update_frame, text='Street: ', bg=street_update_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.street_name_update_entry = tk.Entry(street_update_frame)
        self.street_name_update_entry.grid(row=0, column=1, padx=5, pady=5)

        city_update_frame = tk.LabelFrame(self.update_frame, bg='gray94')
        city_update_frame.grid(row=2, column=0, pady=5, padx=5, sticky='w')
        tk.Label(city_update_frame, text='City: ', bg=city_update_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.city_name_update_entry = tk.Entry(city_update_frame)
        self.city_name_update_entry.grid(row=0, column=1, padx=5, pady=5)

        country_update_frame = tk.LabelFrame(self.update_frame, bg='gray94')
        country_update_frame.grid(row=3, column=0, pady=5, padx=5, sticky='w')
        tk.Label(country_update_frame, text='Country: ', bg=country_update_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.country_name_update_entry = tk.Entry(country_update_frame)
        self.country_name_update_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Button(self.update_frame, text='Update', command=self.update, bg='light cyan',
                  fg='red').grid(row=4, column=0, padx=5, pady=5)

    def init_delete_frame(self, master, row=0, column=3):
        width_label = 7
        width_text_label = 17
        self.delete_frame = tk.LabelFrame(master, bg='gray85', text='Delete', fg='green')
        self.delete_frame.grid(row=row, column=column, pady=10)

        shop_delete_frame = tk.LabelFrame(self.delete_frame, bg='gray94')
        shop_delete_frame.grid(row=0, column=0, pady=5, padx=5, sticky='w')
        tk.Label(shop_delete_frame, text='Shop: ', bg=shop_delete_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.shop_name_var = tk.StringVar()
        tk.Label(shop_delete_frame, textvariable=self.shop_name_var, width=width_text_label).grid(row=0, column=1, padx=5, pady=5)

        street_delete_frame = tk.LabelFrame(self.delete_frame, bg='gray94')
        street_delete_frame.grid(row=1, column=0, pady=5, padx=5, sticky='w')
        tk.Label(street_delete_frame, text='Street: ', bg=street_delete_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.street_name_var = tk.StringVar()
        tk.Label(street_delete_frame, textvariable=self.street_name_var, width=width_text_label).grid(row=0, column=1, padx=5, pady=5)

        city_delete_frame = tk.LabelFrame(self.delete_frame, bg='gray94')
        city_delete_frame.grid(row=2, column=0, pady=5, padx=5, sticky='w')
        tk.Label(city_delete_frame, text='City: ', bg=city_delete_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.city_name_var = tk.StringVar()
        tk.Label(city_delete_frame, textvariable=self.city_name_var, width=width_text_label).grid(row=0, column=1,
                                                                                                    padx=5, pady=5)

        country_delete_frame = tk.LabelFrame(self.delete_frame, bg='gray94')
        country_delete_frame.grid(row=3, column=0, pady=5, padx=5, sticky='w')
        tk.Label(country_delete_frame, text='Country: ', bg=country_delete_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.country_name_var = tk.StringVar()
        tk.Label(country_delete_frame, textvariable=self.country_name_var, width=width_text_label).grid(row=0, column=1,
                                                                                                  padx=5, pady=5)

        tk.Button(self.delete_frame, text='Delete', command=self.delete, bg='light cyan',
                  fg='red').grid(row=4, column=0, padx=5, pady=5)

    def delete(self):
        log.info("Delete Shop Page")
        if not self.table.is_item_selected():
            from tkinter import messagebox
            messagebox.showinfo("Delete Error", "Item not selected")
            return

        shop_name = self.shop_name_var.get().replace('\'', '\'\'')
        street = self.street_name_var.get().replace('\'', '\'\'')
        city = self.city_name_var.get().replace('\'', '\'\'')
        country = self.country_name_var.get().replace('\'', '\'\'')

        shop_id_query = "SELECT shop_id from shops s, locations l where s.location_id = l.location_id and s.shop_name = '{}' and l.street_address='{}' and l.city='{}' and l.country='{}'".format(shop_name, street, city, country)
        try:
            shop_id = self.controller.run_query(shop_id_query)[0][0]
        except IndexError:
            from tkinter import messagebox
            messagebox.showinfo("Delete Error", "Shop inexistent")
            return
        import cx_Oracle
        try:
            products_query = "DELETE FROM products WHERE shop_id = '{}'".format(shop_id)
            self.controller.run_query(products_query)
        except cx_Oracle.IntegrityError:
            from tkinter import messagebox
            messagebox.showinfo("Delete Error", "Can't delete shop because orders are present")
            return

        location_id_query = "SELECT location_id from locations where street_address='{}' and city='{}' and country='{}'".format(
            street, city, country)
        location_id = self.controller.run_query(location_id_query)[0][0]

        delete_query = "DELETE FROM shops WHERE shop_name='{}' and location_id = '{}'".format(shop_name, location_id)
        self.controller.run_query(delete_query)
        self.populate_the_table_with_all_values()

    def search_for_shop(self, shop_name, street_name, city_name, country_name):
        shop_name_temp = shop_name.replace('\'', '\'\'')
        street_name_temp = street_name.replace('\'', '\'\'')
        city_name_temp = city_name.replace('\'', '\'\'')
        country_name_temp = country_name.replace('\'', '\'\'')
        query = "SELECT shop_id, shop_name, street_address, city, country from shops s, locations l where s.location_id = l.location_id and " \
                "lower(s.shop_name)='{}'and lower(l.street_address) = '{}' and lower(l.city) = '{}' and lower(l.country) = '{}'".format(shop_name_temp.lower(), street_name_temp.lower(), city_name_temp.lower(), country_name_temp.lower())
        query_select = self.controller.run_query(query)
        return query_select

    def global_search(self):
        shop_name = self.shop_name_search.get()
        street_name = self.street_name_search.get()
        country_name = self.country_name_search.get()
        city_name = self.city_name_search.get()
        self.table.clear_table()

        if shop_name + street_name + country_name + city_name == "":
            self.populate_the_table_with_all_values()
        else:
            shop_name = self.controller.add_escape_characters(shop_name)
            street_name = self.controller.add_escape_characters(street_name)
            country_name = self.controller.add_escape_characters(country_name)
            city_name = self.controller.add_escape_characters(city_name)
            query = "SELECT shop_id, shop_name, street_address, city, country from {} s, {} l where s.location_id = l.location_id and " \
                    "lower(shop_name) like '%{}%' escape '#' and lower(street_address) like '%{}%' escape '#' " \
                    "and lower(city) like '%{}%' escape '#' and lower(country) like '%{}%' escape '#'".format(
                'shops', 'locations', shop_name.lower(), street_name.lower(), city_name.lower(), country_name.lower())
            query_select = self.controller.run_query(query)
            for row in self.search_for_shop(shop_name, street_name, country_name, city_name):
                self.table.insert('', 'end', values=row)

    def is_empty(self, shop_name, street, city, country):
        from tkinter import messagebox
        if shop_name == '':
            messagebox.showinfo("Insert Error", "Shop Name required")
            return True
        if street == '':
            messagebox.showinfo("Insert Error", "Street Name required")
            return True
        if city == '':
            messagebox.showinfo("Insert Error", "City Name required")
            return True
        if country == '':
            messagebox.showinfo("Insert Error", "Country Name required")
            return True
        shops = self.search_for_shop(shop_name, street, city, country)
        if shops:
            messagebox.showinfo("Insert Error", "Shop already exists")
            return True
        return False

    def insert(self):
        log.info("Insert Shop Page")

        shop_name = self.shop_name_insert.get()
        if not self.string_length_is_okay(shop_name, text='Shop Name'):
            return
        shop_name = shop_name.strip()

        street = self.street_name_insert.get()
        if not self.string_length_is_okay(street, text='Street Address', length=50):
            return
        street = street.strip()

        city = self.city_name_insert.get()
        if not self.string_length_is_okay(city, text='City Name', length=30):
            return
        city = city.strip()

        country = self.country_name_insert.get()
        if not self.string_length_is_okay(country, text='Country Name', length=30):
            return
        country = country.strip()

        if self.is_empty(shop_name, street, city, country):
            return

        if not self.is_word_letters_and_spaces(country):
            from tkinter import messagebox
            messagebox.showinfo("Country Name Error", "Country Name should contains only letters and spaces")
            return
        if not self.is_word_letters_and_spaces(city):
            from tkinter import messagebox
            messagebox.showinfo("City Name Error", "City Name should contains only letters and spaces")
            return

        shop_name = shop_name.replace('\'', '\'\'')

        location_id = self.insert_or_get_location(street, city, country)
        if self.shop_exists(shop_name, location_id):
            from tkinter import messagebox
            messagebox.showinfo("Insert Error", "Shop Already Exists")
            return

        insert_query = "INSERT INTO shops (shop_name, location_id) VALUES ('{}', '{}')".format(shop_name, location_id)
        self.controller.run_query(insert_query)
        self.populate_the_table_with_all_values()

    def update(self):
        log.info("Update Shop Page")

        if not self.table.is_item_selected():
            from tkinter import messagebox
            messagebox.showinfo("Update Error", "Item not selected")
            return

        shop_name = self.shop_name_update_entry.get()
        if not self.string_length_is_okay(shop_name, text='Shop Name'):
            return
        shop_name = shop_name.strip()

        street = self.street_name_update_entry.get()
        if not self.string_length_is_okay(street, text='Street Address', length=50):
            return
        street = street.strip()

        city = self.city_name_update_entry.get()
        if not self.string_length_is_okay(city, text='City Name', length=30):
            return
        city = city.strip()

        country = self.country_name_update_entry.get()
        if not self.string_length_is_okay(country, text='Country Name', length=30):
            return
        country = country.strip()

        if shop_name == self.shop_name_var.get() and street == self.street_name_var.get() and city == self.city_name_var.get() and country == self.country_name_var.get():
            return
        if self.is_empty(shop_name, street, city, country):
            return

        if not self.is_word_letters_and_spaces(country):
            from tkinter import messagebox
            messagebox.showinfo("Country Name Error", "Country Name should contains only letters and spaces")
            return
        if not self.is_word_letters_and_spaces(city):
            from tkinter import messagebox
            messagebox.showinfo("City Name Error", "City Name should contains only letters and spaces")
            return

        location_id = self.insert_or_get_location(street, city, country)

        shop_name = shop_name.replace('\'', '\'\'')

        if self.shop_exists(shop_name, location_id):
            from tkinter import messagebox
            messagebox.showinfo("Insert Error", "Shop Already Exists")
            return

        shop_name_to_delete = self.shop_name_var.get().replace('\'', '\'\'')
        street_to_delete = self.street_name_var.get().replace('\'', '\'\'')
        city_to_delete = self.city_name_var.get().replace('\'', '\'\'')
        country_to_delete = self.country_name_var.get().replace('\'', '\'\'')

        location_id_query = "SELECT location_id from locations where street_address='{}' and city='{}' and country='{}'".format(
            street_to_delete, city_to_delete, country_to_delete)
        location_id_to_delete = self.controller.run_query(location_id_query)[0][0]

        insert_query = "UPDATE shops SET shop_name = '{}', location_id={} WHERE shop_name='{}' AND location_id={}".format(shop_name, location_id, shop_name_to_delete, location_id_to_delete)
        self.controller.run_query(insert_query)
        self.populate_the_table_with_all_values()

    def search_shop(self):
        log.info("Search_Shop Shop Page")
        if self.search_by_shop_id.get():
            name = self.shop_name_search.get()
            if not name.isdigit():
                from tkinter import messagebox
                messagebox.showinfo("Search Error", "Shop Id invalid")
                return
            else:
                query = "SELECT shop_id, shop_name, street_address, city, country from {} s, {} l where s.location_id = l.location_id and s.shop_id={}".format(
                    'shops', 'locations', name)
                query_select = self.controller.run_query(query)
                self.table.clear_table()
                for row in query_select:
                    self.table.insert('', 'end', values=row)
        else:
            name = self.shop_name_search.get()
            name = self.controller.add_escape_characters(name)
            query = "SELECT shop_id, shop_name, street_address, city, country from {} s, {} l where s.location_id = l.location_id and lower(shop_name) like '%{}%' escape '#'".format(
                    'shops', 'locations', name.lower())
            self.search(name, query)

    def search_street(self):
        log.info("Search_Street Shop Page")

        name = self.street_name_search.get()
        name = self.controller.add_escape_characters(name)
        query = "SELECT shop_id, shop_name, street_address, city, country from {} s, {} l where s.location_id = l.location_id and lower(street_address) like '%{}%' escape '#'".format(
            'shops', 'locations', name.lower())
        self.search(name, query)

    def search_country(self):
        log.info("Search_Country Shop Page")

        name = self.country_name_search.get()
        name = self.controller.add_escape_characters(name)
        query = "SELECT shop_id, shop_name, street_address, city, country from {} s, {} l where s.location_id = l.location_id and lower(country) like '%{}%' escape '#'".format(
            'shops', 'locations', name.lower())
        self.search(name, query)

    def search_city(self):
        log.info("Search_City Shop Page")

        name = self.city_name_search.get()
        name = self.controller.add_escape_characters(name)
        query = "SELECT shop_id, shop_name, street_address, city, country from {} s, {} l where s.location_id = l.location_id and lower(city) like '%{}%' escape '#'".format(
            'shops', 'locations', name.lower())
        self.search(name, query)

    def search(self, name, query):
        self.table.clear_table()
        if name == '':
            self.populate_the_table_with_all_values()
        else:
            query_select = self.controller.run_query(query)
            for row in query_select:
                self.table.insert('', 'end', values=row)

    def populate_the_table_with_all_values(self):
        self.table.clear_table()
        query_select = self.controller.run_query(
            "SELECT shop_id, shop_name, street_address, city, country from {} s, {} l where s.location_id = l.location_id".format('shops', 'locations'))
        for row in query_select:
            self.table.insert('', 'end', values=row)

    def shop_exists(self, shop_name, location_id):
        query_select = self.controller.run_query(
            "SELECT shop_id from shops s where lower(s.shop_name) = '{}' and s.location_id = {}".format(
                shop_name.lower(), location_id))
        return bool(query_select)
