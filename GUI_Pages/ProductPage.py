from GUI_Pages.BasicPage import BasicPage
import tkinter as tk

import logging as log
import sys

from GUI_utilities.TableFrame import TableFrame

FORMAT = '[%(asctime)s] [%(levelname)s] : %(message)s'
log.basicConfig(stream=sys.stdout, level=log.DEBUG, format=FORMAT)

class ProductPage(BasicPage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.init()

    def init(self):
        self.button_product['bg'] = 'dark orange'
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

        columns_names = ['PRODUCT ID', 'PRODUCT NAME', 'PRICE', 'SHOP ID', 'DESCRIPTION']
        print(columns_names)
        self.table = TableFrame(viewer_frame, columns_names)
        self.table.grid(row=2, column=0, columnspan=4, sticky="nesw", padx=5, pady=5)
        self.populate_the_table_with_all_values()
        self.table.tree.bind('<<TreeviewSelect>>', self.on_select)

    def OnDoubleClick(self, event):
        item = self.table.tree.identify('item', event.x, event.y)
        print("you clicked on", self.table.tree.item(item, "values"))

    def on_select(self, event):
        self.selected_item = event.widget.item(event.widget.selection()[0], "values")
        self.product_name_delete_var.set(self.selected_item[1])
        self.price_delete_var.set(self.selected_item[2])
        self.shop_id_delete_var.set(self.selected_item[3])
        self.description_delete_var.set(self.selected_item[4])
        from bd_gui import BdGui
        BdGui.set_entry_text(self.product_name_update, self.selected_item[1])
        BdGui.set_entry_text(self.price_update, self.selected_item[2])
        BdGui.set_entry_text(self.shop_id_update, self.selected_item[3])
        BdGui.set_entry_text(self.description_update, self.selected_item[4])

    def init_search_frame(self, master, row=0, column=0):
        width_label = 7
        self.search_frame = tk.LabelFrame(master, bg='gray85', text='Search', fg='green')
        self.search_frame.grid(row=row, column=column, pady=10, padx=5)

        product_search_frame = tk.LabelFrame(self.search_frame, bg='gray94')
        product_search_frame.grid(row=0, column=0, pady=5, padx=5, sticky='w')
        tk.Label(product_search_frame, text='Product/Id', bg=product_search_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.product_name_search = tk.Entry(product_search_frame)
        self.product_name_search.grid(row=0, column=1, padx=5, pady=5)
        tk.Button(product_search_frame, text='Search', command=self.search_product).grid(row=0, column=2)

        price_search_frame = tk.LabelFrame(self.search_frame, bg='gray94')
        price_search_frame.grid(row=1, column=0, pady=5, padx=5, sticky='w')
        tk.Label(price_search_frame, text='Price', bg=price_search_frame['bg'], fg='dark orange',
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
        from tkinter import ttk
        ttk.Checkbutton(option_search_frame, text="Product Id", variable=self.search_by_product_id,
                        command=self.on_check_product_id).grid(row=0, column=0, padx=5, pady=5)
        self.search_by_price_range_btn = tk.Button(option_search_frame, text='Search By Price Range', command=self.search_price_range, bg='light cyan',
                  fg='red')
        self.search_by_price_range_btn.grid(row=0, column=1, padx=5, pady=5)

    def on_check_product_id(self):
        pass

    def search_for_product_equal(self, product, price, shop_id, description):
        product = product.replace('\'', '\'\'')
        description = description.replace('\'', '\'\'')
        if description != 'None' and description != '':
            query = "SELECT product_id, product_name, price, shop_id, description from products where lower(product_name)='{}' and price={} and shop_id={} and lower(description)='{}'".format(
                product.lower(), price, shop_id, description.lower())
        else:
            query = "SELECT product_id, product_name, price, shop_id, description from products where lower(product_name)='{}' and price={} and shop_id={} and description is NULL".format(
                product.lower(), price, shop_id)
        query_select = self.controller.run_query(query)
        return query_select

    def search_for_product_like(self, product):
        product = self.controller.add_escape_characters(product)
        query = "SELECT product_id, product_name, price, shop_id, description from products where lower(product_name) like '%{}%'".format(
            product.lower())
        query_select = self.controller.run_query(query)
        return query_select

    def search_product(self):
        log.info("Search_Provider product Page")
        if self.search_by_product_id.get():
            name = self.product_name_search.get()
            if not name.isdigit():
                from tkinter import messagebox
                messagebox.showinfo("Search Error", "Product Id invalid")
                return
            else:
                query = "SELECT product_id, product_name, price, shop_id, description from products where product_id={}".format(name)
                query_select = self.controller.run_query(query)
                self.table.clear_table()
                for row in query_select:
                    self.table.insert('', 'end', values=row)
        else:
            self.table.clear_table()
            name = self.product_name_search.get()
            if name == '':
                self.populate_the_table_with_all_values()
            else:
                for row in self.search_for_product_like(name):
                    self.table.insert('', 'end', values=row)

    def exist_shop_id(self, shop_id):
        query = "SELECT shop_id from shops where shop_id={}".format(shop_id)
        query_select = self.controller.run_query(query)
        if query_select:
            return True
        else:
            return False

    def search_price(self):
        log.info("Search_Price product Page")
        self.table.clear_table()

        price = self.price_name_search.get()
        if price == '':
            self.populate_the_table_with_all_values()
        else:
            if not self.is_number(price):
                from tkinter import messagebox
                messagebox.showinfo("Insert Error", "Price is not number")
                return
            query = "SELECT product_id, product_name, price, shop_id, description from products where price={}".format(price)
            query_select = self.controller.run_query(query)
            for row in query_select:
                self.table.insert('', 'end', values=row)

    def search_price_range(self):
        log.info("Search_Price Range product Page")
        self.table.clear_table()

        price_min = self.min_price_name_search.get()
        price_max = self.max_price_name_search.get()
        if price_min == '' and price_max == '':
            self.populate_the_table_with_all_values()
        else:
            if not self.is_number(price_min, zero_permited=True):
                from tkinter import messagebox
                messagebox.showinfo("Insert Error", "Price MIN is not a valid number")
                return
            if not self.is_number(price_max, zero_permited=True):
                from tkinter import messagebox
                messagebox.showinfo("Insert Error", "Price MAX is not a valid number")
                return
            if price_min == '':
                price_min = '0'
            if price_max == '':
                price_max = '999999'
            query = "SELECT product_id, product_name, price, shop_id, description from products where price between {} and {}".format(
                price_min, price_max)
            query_select = self.controller.run_query(query)
            for row in query_select:
                self.table.insert('', 'end', values=row)

    def init_insert_frame(self, master, row=0, column=1):
        width_label = 13
        self.insert_frame = tk.LabelFrame(master, bg='gray85', text='Insert', fg='green')
        self.insert_frame.grid(row=row, column=column, pady=10)

        product_insert_frame = tk.LabelFrame(self.insert_frame, bg='gray94')
        product_insert_frame.grid(row=0, column=0, pady=5, padx=5, sticky='w')
        tk.Label(product_insert_frame, text='Product Name', bg=product_insert_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.product_name_insert = tk.Entry(product_insert_frame)
        self.product_name_insert.grid(row=0, column=1, padx=5, pady=5)

        price_insert_frame = tk.LabelFrame(self.insert_frame, bg='gray94')
        price_insert_frame.grid(row=1, column=0, pady=5, padx=5, sticky='w')
        tk.Label(price_insert_frame, text='Price', bg=price_insert_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.price_insert = tk.Entry(price_insert_frame)
        self.price_insert.grid(row=0, column=1, padx=5, pady=5)

        shop_id_insert_frame = tk.LabelFrame(self.insert_frame, bg='gray94')
        shop_id_insert_frame.grid(row=2, column=0, pady=5, padx=5, sticky='w')
        tk.Label(shop_id_insert_frame, text='Shop Id', bg=shop_id_insert_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.shop_id_insert = tk.Entry(shop_id_insert_frame)
        self.shop_id_insert.grid(row=0, column=1, padx=5, pady=5)

        description_insert_frame = tk.LabelFrame(self.insert_frame, bg='gray94')
        description_insert_frame.grid(row=3, column=0, pady=5, padx=5, sticky='w')
        tk.Label(description_insert_frame, text='Description', bg=description_insert_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.description_insert = tk.Entry(description_insert_frame)
        self.description_insert.grid(row=0, column=1, padx=5, pady=5)

        tk.Button(self.insert_frame, text='Insert', command=self.insert, bg='light cyan',
                  fg='red').grid(row=4, column=0, padx=5, pady=5)

    def init_update_frame(self, master, row=0, column=2):
        width_label = 13
        self.update_frame = tk.LabelFrame(master, bg='gray85', text='Update', fg='green')
        self.update_frame.grid(row=row, column=column, pady=10)

        product_update_frame = tk.LabelFrame(self.update_frame, bg='gray94')
        product_update_frame.grid(row=0, column=0, pady=5, padx=5, sticky='w')
        tk.Label(product_update_frame, text='Product Name', bg=product_update_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.product_name_update = tk.Entry(product_update_frame)
        self.product_name_update.grid(row=0, column=1, padx=5, pady=5)

        price_update_frame = tk.LabelFrame(self.update_frame, bg='gray94')
        price_update_frame.grid(row=1, column=0, pady=5, padx=5, sticky='w')
        tk.Label(price_update_frame, text='Price', bg=price_update_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.price_update = tk.Entry(price_update_frame)
        self.price_update.grid(row=0, column=1, padx=5, pady=5)

        shop_id_update_frame = tk.LabelFrame(self.update_frame, bg='gray94')
        shop_id_update_frame.grid(row=2, column=0, pady=5, padx=5, sticky='w')
        tk.Label(shop_id_update_frame, text='Shop Id', bg=shop_id_update_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.shop_id_update = tk.Entry(shop_id_update_frame)
        self.shop_id_update.grid(row=0, column=1, padx=5, pady=5)

        description_update_frame = tk.LabelFrame(self.update_frame, bg='gray94')
        description_update_frame.grid(row=3, column=0, pady=5, padx=5, sticky='w')
        tk.Label(description_update_frame, text='Description', bg=description_update_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.description_update = tk.Entry(description_update_frame)
        self.description_update.grid(row=0, column=1, padx=5, pady=5)

        tk.Button(self.update_frame, text='Update', command=self.update, bg='light cyan',
                  fg='red').grid(row=4, column=0, padx=5, pady=5)

    def init_delete_frame(self, master, row=0, column=3):
        width_label = 13
        width_text_label = 20
        self.delete_frame = tk.LabelFrame(master, bg='gray85', text='Delete', fg='green')
        self.delete_frame.grid(row=row, column=column, pady=10)

        product_delete_frame = tk.LabelFrame(self.delete_frame, bg='gray94')
        product_delete_frame.grid(row=0, column=0, pady=5, padx=5, sticky='w')
        tk.Label(product_delete_frame, text='Product', bg=product_delete_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.product_name_delete_var = tk.StringVar()
        tk.Label(product_delete_frame, textvariable=self.product_name_delete_var, width=width_text_label).grid(row=0, column=1, padx=5, pady=5)

        price_delete_frame = tk.LabelFrame(self.delete_frame, bg='gray94')
        price_delete_frame.grid(row=1, column=0, pady=5, padx=5, sticky='w')
        tk.Label(price_delete_frame, text='Price', bg=price_delete_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.price_delete_var = tk.StringVar()
        tk.Label(price_delete_frame, textvariable=self.price_delete_var, width=width_text_label).grid(row=0, column=1, padx=5, pady=5)

        shop_id_delete_frame = tk.LabelFrame(self.delete_frame, bg='gray94')
        shop_id_delete_frame.grid(row=2, column=0, pady=5, padx=5, sticky='w')
        tk.Label(shop_id_delete_frame, text='Shop Id', bg=shop_id_delete_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.shop_id_delete_var = tk.StringVar()
        tk.Label(shop_id_delete_frame, textvariable=self.shop_id_delete_var, width=width_text_label).grid(row=0, column=1, padx=5, pady=5)

        description_delete_frame = tk.LabelFrame(self.delete_frame, bg='gray94')
        description_delete_frame.grid(row=3, column=0, pady=5, padx=5, sticky='w')
        tk.Label(description_delete_frame, text='Description', bg=description_delete_frame['bg'], fg='dark orange',
                 width=width_label).grid(row=0, column=0)
        self.description_delete_var = tk.StringVar()
        tk.Label(description_delete_frame, textvariable=self.description_delete_var, width=width_text_label).grid(row=0, column=1, padx=5, pady=5)

        tk.Button(self.delete_frame, text='Delete', command=self.delete, bg='light cyan',
                  fg='red').grid(row=4, column=0, padx=5, pady=5)

    def delete(self):
        log.info("Delete product Page")
        if not self.table.is_item_selected():
            from tkinter import messagebox
            messagebox.showinfo("Delete Error", "Item not selected")
            return

        name = self.product_name_delete_var.get().replace('\'', '\'\'')
        if not name:
            return
        description = self.description_delete_var.get().replace('\'', '\'\'')
        price = self.price_delete_var.get()
        shop_id = self.shop_id_delete_var.get()

        if description!= 'None':
            delete_query = "DELETE FROM products where product_name='{}' and price={} and shop_id={} and description='{}'".format(name, price, shop_id, description)
        else:
            delete_query = "DELETE FROM products where product_name='{}' and price={} and shop_id={} and description is NULL".format(name, price, shop_id)

        import cx_Oracle
        try:
            self.controller.run_query(delete_query)
        except cx_Oracle.IntegrityError:
            from tkinter import messagebox
            messagebox.showinfo("Delete Error", "Can't delete shop because orders are present")
            return
        self.populate_the_table_with_all_values()
        self.controller.frames["HomePage"].update_buy()

    def fields_are_empty(self, name, price, shop_id):
        from tkinter import messagebox
        if name == '':
            messagebox.showinfo("Insert Error", "Product Name required")
            return True
        if price == '':
            messagebox.showinfo("Insert Error", "Price Name required")
            return True
        if shop_id == '':
            messagebox.showinfo("Insert Error", "Shop Id Name required")
            return True

    def product_exists(self, name, price, shop_id, description):
        from tkinter import messagebox
        if self.search_for_product_equal(name, price, shop_id, description):
            messagebox.showinfo("Insert Error", "Product already exists")
            return True
        return False

    def insert(self):
        log.info("Insert product Page")
        price = self.price_insert.get()
        shop_id = self.shop_id_insert.get()

        name = self.product_name_insert.get()
        if not self.string_length_is_okay(name, text='Product Name'):
            return
        name = name.strip()

        description = self.description_insert.get()
        if not self.string_length_is_okay(description, text='Description Name', length=100):
            return
        description = description.strip()

        if not self.is_number(price):
            from tkinter import messagebox
            messagebox.showinfo("Insert Error", "Price is not number")
            return
        if not shop_id.isdigit():
            from tkinter import messagebox
            messagebox.showinfo("Insert Error", "Shop Id is not number")
            return
        if not self.exist_shop_id(shop_id):
            from tkinter import messagebox
            messagebox.showinfo("Insert Error", "Shop Id does not exist")
            return

        if self.fields_are_empty(name, price, shop_id) or self.product_exists(name, price, shop_id, description):
            return

        name = name.replace('\'', '\'\'')
        description = description.replace('\'', '\'\'')

        insert_query = "INSERT INTO products (product_name, price, shop_id, description) VALUES ('{}', {}, {}, '{}')".format(name, price, shop_id, description)
        self.controller.run_query(insert_query)
        self.populate_the_table_with_all_values()
        self.controller.frames["HomePage"].update_buy()

    def update(self):
        log.info("Update product Page")
        if not self.table.is_item_selected():
            from tkinter import messagebox
            messagebox.showinfo("Update Error", "Item not selected")
            return

        price = self.price_update.get()
        shop_id = self.shop_id_update.get()

        name = self.product_name_update.get()
        if not self.string_length_is_okay(name, text='Product Name'):
            return
        name = name.strip()

        description = self.description_update.get()
        if not self.string_length_is_okay(description, text='Description Name', length=100):
            return
        description = description.strip()


        if self.fields_are_empty(name, price, shop_id) or self.product_exists(name, price, shop_id, description):
            return

        if not self.is_number(price):
            from tkinter import messagebox
            messagebox.showinfo("Insert Error", "Price is not number")
            return
        if not shop_id.isdigit():
            from tkinter import messagebox
            messagebox.showinfo("Insert Error", "Shop Id is not number")
            return
        if not self.exist_shop_id(shop_id):
            from tkinter import messagebox
            messagebox.showinfo("Insert Error", "Shop Id does not exist")
            return

        old_name = self.product_name_delete_var.get().replace('\'', '\'\'')
        old_price = self.price_delete_var.get()
        old_shop_id = self.shop_id_delete_var.get()
        old_description = self.description_delete_var.get().replace('\'', '\'\'')

        name = name.replace('\'', '\'\'')
        description = description.replace('\'', '\'\'')

        if description == 'None':
            description = ''
        if old_description != 'None':
            update_query = "UPDATE products set product_name = '{}', price = {}, shop_id={}, description='{}' where product_name='{}' and price = {} and shop_id={} and description='{}'".format(
                name, price, shop_id, description, old_name, old_price, old_shop_id, old_description)
        else:
            update_query = "UPDATE products set product_name = '{}', price = {}, shop_id={}, description='{}' where product_name='{}' and price = {} and shop_id={} and description is NULL".format(
                name, price, shop_id, description, old_name, old_price, old_shop_id)
        self.controller.run_query(update_query)
        self.populate_the_table_with_all_values()
        self.controller.frames["HomePage"].update_buy()

    def populate_the_table_with_all_values(self):
        self.table.clear_table()
        query_select = self.controller.run_query("SELECT product_id, product_name, price, shop_id, description from products")
        for row in query_select:
            self.table.insert('', 'end', values=row)

