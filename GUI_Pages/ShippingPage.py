from tkinter import ttk

from GUI_Pages.BasicPage import BasicPage
from Utilities.TableFrame import TableFrame
import tkinter as tk

import logging as log
import sys

FORMAT = '[%(asctime)s] [%(levelname)s] : %(message)s'
log.basicConfig(stream=sys.stdout, level=log.DEBUG, format=FORMAT)


class ShippingPage(BasicPage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.init()

    def init(self):
        self.button_shipping['bg'] = 'dark orange'
        bg_color = 'gold'
        viewer_frame = tk.LabelFrame(self, bg=bg_color)
        viewer_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        viewer_frame.grid_columnconfigure(0, weight=1)
        viewer_frame.grid_columnconfigure(1, weight=1)
        viewer_frame.grid_columnconfigure(2, weight=1)
        viewer_frame.grid_columnconfigure(3, weight=1)
        viewer_frame.grid_rowconfigure(2, weight=1)

        # ------------search_bar------------------
        self.init_search_frame(viewer_frame)
        self.init_insert_frame(viewer_frame)
        self.init_update_frame(viewer_frame)
        self.init_delete_frame(viewer_frame)

        columns_names = list(map("".join, self.controller.get_columns_name('shipping_methods')))
        self.table = TableFrame(viewer_frame, columns_names)
        self.table.grid(row=2, column=0, columnspan=4, sticky="nesw", padx=5, pady=5)
        self.populate_the_table_with_all_values()
        self.table.tree.bind('<<TreeviewSelect>>', self.on_select)

    def OnDoubleClick(self, event):
        item = self.table.tree.identify('item', event.x, event.y)
        print("you clicked on", self.table.tree.item(item, "values"))

    def on_select(self, event):
        self.selected_item = event.widget.item(event.widget.selection()[0], "values")
        self.shipping_name_delete_var.set(self.selected_item[1])
        self.delivering_price_delete_var.set(self.selected_item[2])
        from bd_gui import BdGui
        BdGui.set_entry_text(self.shipping_provider_update, self.selected_item[1])
        BdGui.set_entry_text(self.price_update, self.selected_item[2])

    def init_search_frame(self, master, row=0, column=0):
        width_label = 13
        self.search_frame = tk.LabelFrame(master, bg='gray85', text='Search', fg='green')
        self.search_frame.grid(row=row, column=column, pady=10, padx=5)

        shipping_search_frame = tk.LabelFrame(self.search_frame, bg='gray94')
        shipping_search_frame.grid(row=0, column=0, pady=5, padx=5, sticky='w')
        tk.Label(shipping_search_frame, text='Shipping Provider', bg=shipping_search_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.shipping_name_search = tk.Entry(shipping_search_frame)
        self.shipping_name_search.grid(row=0, column=1, padx=5, pady=5)
        tk.Button(shipping_search_frame, text='Search', command=self.search_provider).grid(row=0, column=2)

        price_search_frame = tk.LabelFrame(self.search_frame, bg='gray94')
        price_search_frame.grid(row=1, column=0, pady=5, padx=5, sticky='w')
        tk.Label(price_search_frame, text='Delivering Price', bg=price_search_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.price_name_search = tk.Entry(price_search_frame)
        self.price_name_search.grid(row=0, column=1, padx=5, pady=5)
        tk.Button(price_search_frame, text='Search', command=self.search_price).grid(row=0, column=2)

        min_price_search_frame = tk.LabelFrame(self.search_frame, bg='gray94')
        min_price_search_frame.grid(row=2, column=0, pady=5, padx=5, sticky='w')
        tk.Label(min_price_search_frame, text='Min Price', bg=min_price_search_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.min_price_name_search = tk.Entry(min_price_search_frame)
        self.min_price_name_search.grid(row=0, column=1, padx=5, pady=5)

        max_price_search_frame = tk.LabelFrame(self.search_frame, bg='gray94')
        max_price_search_frame.grid(row=3, column=0, pady=5, padx=5, sticky='w')
        tk.Label(max_price_search_frame, text='Max Price', bg=max_price_search_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.max_price_name_search = tk.Entry(max_price_search_frame)
        self.max_price_name_search.grid(row=0, column=1, padx=5, pady=5)

        option_search_frame = tk.LabelFrame(self.search_frame, bg='gray94')
        option_search_frame.grid(row=4, column=0, pady=5, padx=5, sticky='ew')
        self.search_by_product_id = tk.IntVar()
        ttk.Checkbutton(option_search_frame, text="Shipping Id", variable=self.search_by_product_id,
                        command=self.on_check_product_id).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(option_search_frame, text='Search By Price Range', command=self.search_price_range, bg='light cyan',
                  fg='red').grid(row=0, column=1, padx=5, pady=5)

    def on_check_product_id(self):
        pass

    def search_for_provider_equal(self, provider):
        provider = provider.replace('\'', '\'\'')
        query = "SELECT shipping_id, provider, delivering_price from shipping_methods where lower(provider)='{}'".format(
            provider.lower())
        query_select = self.controller.run_query(query)
        return query_select

    def search_for_provider_like(self, provider):
        provider = self.controller.add_escape_characters(provider)
        query = "SELECT shipping_id, provider, delivering_price from shipping_methods where lower(provider) like '%{}%'".format(provider.lower())
        query_select = self.controller.run_query(query)
        return query_select

    def search_provider(self):
        log.info("Search_Provider Shipping Page")
        if self.search_by_product_id.get():
            name = self.shipping_name_search.get()
            if not name.isdigit():
                from tkinter import messagebox
                messagebox.showinfo("Search Error", "Shipping Id invalid")
                return
            else:
                query = "SELECT shipping_id, provider, delivering_price from shipping_methods where shipping_id={}".format(name)
                query_select = self.controller.run_query(query)
                self.table.clear_table()
                for row in query_select:
                    self.table.insert('', 'end', values=row)
        else:
            self.table.clear_table()
            name = self.shipping_name_search.get()
            if name == '':
                self.populate_the_table_with_all_values()
            else:
                for row in self.search_for_provider_like(name):
                    self.table.insert('', 'end', values=row)

    def search_price(self):
        log.info("Search_Price Shipping Page")
        self.table.clear_table()

        price = self.price_name_search.get()
        if price == '':
            self.populate_the_table_with_all_values()
        else:
            if not self.is_number(price):
                from tkinter import messagebox
                messagebox.showinfo("Insert Error", "Price is not number")
                return
            query = "SELECT shipping_id, provider, delivering_price from shipping_methods where delivering_price={}".format(price)
            query_select = self.controller.run_query(query)
            for row in query_select:
                self.table.insert('', 'end', values=row)

    def search_price_range(self):
        log.info("Search_Price Range Shipping Page")
        self.table.clear_table()

        price_min = self.min_price_name_search.get()
        price_max = self.max_price_name_search.get()
        if price_min == '' and price_max == '':
            self.populate_the_table_with_all_values()
        else:
            if not self.is_number(price_min):
                from tkinter import messagebox
                messagebox.showinfo("Insert Error", "Price MIN is not number")
                return
            if not self.is_number(price_max):
                from tkinter import messagebox
                messagebox.showinfo("Insert Error", "Price MAX is not number")
                return
            if price_min == '':
                price_min = '0'
            if price_max == '':
                price_max = '999999'
            query = "SELECT shipping_id, provider, delivering_price from shipping_methods where delivering_price between {} and {}".format(
                price_min, price_max)
            query_select = self.controller.run_query(query)
            for row in query_select:
                self.table.insert('', 'end', values=row)

    def init_insert_frame(self, master, row=0, column=1):
        width_label = 13
        self.insert_frame = tk.LabelFrame(master, bg='gray85', text='Insert', fg='green')
        self.insert_frame.grid(row=row, column=column, pady=10)

        shipping_insert_frame = tk.LabelFrame(self.insert_frame, bg='gray94')
        shipping_insert_frame.grid(row=0, column=0, pady=5, padx=5, sticky='w')
        tk.Label(shipping_insert_frame, text='Shipping Provider', bg=shipping_insert_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.shipping_name_insert = tk.Entry(shipping_insert_frame)
        self.shipping_name_insert.grid(row=0, column=1, padx=5, pady=5)

        price_insert_frame = tk.LabelFrame(self.insert_frame, bg='gray94')
        price_insert_frame.grid(row=1, column=0, pady=5, padx=5, sticky='w')
        tk.Label(price_insert_frame, text='Delivering Price', bg=price_insert_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.price_insert = tk.Entry(price_insert_frame)
        self.price_insert.grid(row=0, column=1, padx=5, pady=5)

        tk.Button(self.insert_frame, text='Insert', command=self.insert, bg='light cyan',
                  fg='red').grid(row=2, column=0, padx=5, pady=5)

    def init_update_frame(self, master, row=0, column=2):
        width_label = 13
        self.update_frame = tk.LabelFrame(master, bg='gray85', text='Update', fg='green')
        self.update_frame.grid(row=row, column=column, pady=10)

        shipping_update_frame = tk.LabelFrame(self.update_frame, bg='gray94')
        shipping_update_frame.grid(row=0, column=0, pady=5, padx=5, sticky='w')
        tk.Label(shipping_update_frame, text='Shipping Provider', bg=shipping_update_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.shipping_provider_update = tk.Entry(shipping_update_frame)
        self.shipping_provider_update.grid(row=0, column=1, padx=5, pady=5)

        street_update_frame = tk.LabelFrame(self.update_frame, bg='gray94')
        street_update_frame.grid(row=1, column=0, pady=5, padx=5, sticky='w')
        tk.Label(street_update_frame, text='Delivering Price', bg=street_update_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.price_update = tk.Entry(street_update_frame)
        self.price_update.grid(row=0, column=1, padx=5, pady=5)

        tk.Button(self.update_frame, text='Update', command=self.update, bg='light cyan',
                  fg='red').grid(row=2, column=0, padx=5, pady=5)

    def init_delete_frame(self, master, row=0, column=3):
        width_label = 13
        width_text_label = 20
        self.delete_frame = tk.LabelFrame(master, bg='gray85', text='Delete', fg='green')
        self.delete_frame.grid(row=row, column=column, pady=10)

        shipping_delete_frame = tk.LabelFrame(self.delete_frame, bg='gray94')
        shipping_delete_frame.grid(row=0, column=0, pady=5, padx=5, sticky='w')
        tk.Label(shipping_delete_frame, text='Shipping Provider', bg=shipping_delete_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.shipping_name_delete_var = tk.StringVar()
        tk.Label(shipping_delete_frame, textvariable=self.shipping_name_delete_var, width=width_text_label).grid(row=0, column=1, padx=5, pady=5)

        price_delete_frame = tk.LabelFrame(self.delete_frame, bg='gray94')
        price_delete_frame.grid(row=1, column=0, pady=5, padx=5, sticky='w')
        tk.Label(price_delete_frame, text='Delivering Price', bg=price_delete_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.delivering_price_delete_var = tk.StringVar()
        tk.Label(price_delete_frame, textvariable=self.delivering_price_delete_var, width=width_text_label).grid(row=0, column=1, padx=5, pady=5)

        tk.Button(self.delete_frame, text='Delete', command=self.delete, bg='light cyan',
                  fg='red').grid(row=2, column=0, padx=5, pady=5)

    def delete(self):
        log.info("Delete Shipping Page")
        if not self.table.is_item_selected():
            from tkinter import messagebox
            messagebox.showinfo("Delete Error", "Item not selected")
            return
        name = self.shipping_name_delete_var.get()

        name = name.replace('\'', '\'\'')
        delete_query = "DELETE FROM shipping_methods WHERE provider='{}'".format(name)
        import cx_Oracle
        try:
            self.controller.run_query(delete_query)
        except cx_Oracle.IntegrityError:
            from tkinter import messagebox
            messagebox.showinfo("Delete Error", "Can't delete shop because orders are present")
            return
        self.populate_the_table_with_all_values()
        self.controller.frames["HomePage"].update_buy()

    def is_empty(self, provider, price):
        from tkinter import messagebox
        if provider == '':
            messagebox.showinfo("Insert Error", "Provider Name required")
            return True
        if price == '':
            messagebox.showinfo("Insert Error", "Price Name required")
            return True

    def provider_exists(self, provider):
        from tkinter import messagebox
        if self.search_for_provider_equal(provider):
            messagebox.showinfo("Insert Error", "Shipping Method already exists")
            return True
        return False

    def insert(self):
        log.info("Insert Shipping Page")
        name = self.shipping_name_insert.get()
        if not self.string_length_is_okay(name, text='Shipping Provider', length=100):
            return
        name = name.strip()

        price = self.price_insert.get()

        if self.is_empty(name, price) or self.provider_exists(name):
            return

        if not self.is_number(price):
            from tkinter import messagebox
            messagebox.showinfo("Insert Error", "Price is not number")
            return

        name = name.replace('\'', '\'\'')
        insert_query = "INSERT INTO shipping_methods (provider, delivering_price) VALUES ('{}', {})".format(name, price)
        self.controller.run_query(insert_query)
        self.populate_the_table_with_all_values()
        self.controller.frames["HomePage"].update_buy()

    def update(self):
        log.info("Update Shipping Page")
        if not self.table.is_item_selected():
            from tkinter import messagebox
            messagebox.showinfo("Update Error", "Item not selected")
            return
        name = self.shipping_provider_update.get()
        if not self.string_length_is_okay(name, text='Shipping Provider', length=100):
            return
        name = name.strip()
        price = self.price_update.get()

        if self.is_empty(name, price):
            return

        log.info("Update provider {} to price {}".format(name, price))
        if not self.is_number(price):
            from tkinter import messagebox
            messagebox.showinfo("Insert Error", "Price is not number")
            return

        old_name = self.shipping_name_delete_var.get().replace('\'', '\'\'')

        name = name.replace('\'', '\'\'')
        insert_query = "UPDATE shipping_methods set provider = '{}', delivering_price = {} where provider='{}'".format(name, price, old_name)
        self.controller.run_query(insert_query)
        self.populate_the_table_with_all_values()
        self.controller.frames["HomePage"].update_buy()

    def populate_the_table_with_all_values(self):
        self.table.clear_table()
        query_select = self.controller.run_query("SELECT shipping_id, provider, delivering_price from shipping_methods")
        for row in query_select:
            self.table.insert('', 'end', values=row)
