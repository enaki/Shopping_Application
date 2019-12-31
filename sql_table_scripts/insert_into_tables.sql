/* locations */
INSERT INTO locations (street_address, city, country) VALUES ('Str. Mihai Eminescu', 'Ungheni', 'Republica Moldova');
INSERT INTO locations (street_address, city, country) VALUES ('Str. Nationala', 'Chisinau', 'Republica Moldova');
INSERT INTO locations (street_address, city, country) VALUES ('Str. Romana', 'Ungheni', 'Republica Moldova');
INSERT INTO locations (street_address, city, country) VALUES ('Str. Palas', 'Iasi', 'Romania');
INSERT INTO locations (street_address, city, country) VALUES ('Str. Tudor Vladimirescu', 'Iasi', 'Romania');
INSERT INTO locations (street_address, city, country) VALUES ('Bulevardul Timisoara', 'Bucuresti', 'Romania');
INSERT INTO locations (street_address, city, country) VALUES ('Str. Plopilor', 'Cluj-Napoca', 'Romania');
INSERT INTO locations (street_address, city, country) VALUES ('Str. Aurel David', 'Ungheni', 'Republica Moldova');
INSERT INTO locations (street_address, city, country) VALUES ('Str. Marinescu 18B', 'Ungheni', 'Republica Moldova');

/* shops */
INSERT INTO shops (shop_name, location_id) VALUES ('SA Covoare Ungheni', (select location_id from locations where street_address = 'Str. Mihai Eminescu' and city = 'Ungheni' and country='Republica Moldova'));
INSERT INTO shops (shop_name, location_id) VALUES ('BOMBA', (select location_id from locations where street_address = 'Str. Nationala' and city = 'Chisinau' and country='Republica Moldova'));
INSERT INTO shops (shop_name, location_id) VALUES ('MAXIMUM', (select location_id from locations where street_address = 'Str. Nationala' and city = 'Chisinau' and country='Republica Moldova'));

INSERT INTO shops (shop_name, location_id) VALUES ('Altex', (select location_id from locations where street_address = 'Str. Palas' and city = 'Iasi' and country='Romania'));
INSERT INTO shops (shop_name, location_id) VALUES ('Emag', (select location_id from locations where street_address = 'Bulevardul Timisoara' and city = 'Bucuresti' and country='Romania'));
INSERT INTO shops (shop_name, location_id) VALUES ('PC Garage', (select location_id from locations where street_address = 'Bulevardul Timisoara' and city = 'Bucuresti' and country='Romania'));
INSERT INTO shops (shop_name, location_id) VALUES ('Emag', (select location_id from locations where street_address = 'Str. Plopilor' and city = 'Cluj-Napoca' and country='Romania'));

/* products */
INSERT INTO products (product_name, price, shop_id) VALUES ('Covor Traditional', 20, 
    (SELECT shop_id FROM shops s, locations l WHERE s.location_id = l.location_id AND s.shop_name = 'SA Covoare Ungheni' AND l.street_address = 'Str. Mihai Eminescu' AND l.city = 'Ungheni' AND l.country='Republica Moldova'));
INSERT INTO products (product_name, price, shop_id) VALUES ('Covor Modern Vintage', 40, 
    (SELECT shop_id FROM shops s, locations l WHERE s.location_id = l.location_id AND s.shop_name = 'SA Covoare Ungheni' AND l.street_address = 'Str. Mihai Eminescu' and l.city = 'Ungheni' AND l.country='Republica Moldova'));
INSERT INTO products (product_name, price, shop_id) VALUES ('Cuptor cu microunde', 35.2, 
    (SELECT shop_id FROM shops s, locations l WHERE s.location_id = l.location_id AND s.shop_name = 'BOMBA' AND l.street_address = 'Str. Nationala' and l.city = 'Chisinau' AND l.country='Republica Moldova'));
INSERT INTO products (product_name, price, shop_id) VALUES ('Cuptor cu microunde', 40, 
    (SELECT shop_id FROM shops s, locations l WHERE s.location_id = l.location_id AND s.shop_name = 'MAXIMUM' AND l.street_address = 'Str. Nationala' and l.city = 'Chisinau' AND l.country='Republica Moldova'));
INSERT INTO products (product_name, price, shop_id) VALUES ('Masina de spalat', 65, 
    (SELECT shop_id FROM shops s, locations l WHERE s.location_id = l.location_id AND s.shop_name = 'MAXIMUM' AND l.street_address = 'Str. Nationala' and l.city = 'Chisinau' AND l.country='Republica Moldova'));

INSERT INTO products (product_name, price, shop_id) VALUES ('Geanta Dell', 30, 
    (SELECT shop_id FROM shops s, locations l WHERE s.location_id = l.location_id AND s.shop_name = 'Emag' AND l.street_address = 'Bulevardul Timisoara' and l.city = 'Bucuresti' AND l.country='Romania'));
INSERT INTO products (product_name, price, shop_id) VALUES ('Geanta Dell', 35, 
    (SELECT shop_id FROM shops s, locations l WHERE s.location_id = l.location_id AND s.shop_name = 'Emag' AND l.street_address = 'Str. Plopilor' and l.city = 'Cluj-Napoca' AND l.country='Romania'));
INSERT INTO products (product_name, price, shop_id) VALUES ('Boxa JBL2 GO', 45, 
    (SELECT shop_id FROM shops s, locations l WHERE s.location_id = l.location_id AND s.shop_name = 'Emag' AND l.street_address = 'Str. Plopilor' and l.city = 'Cluj-Napoca' AND l.country='Romania'));
INSERT INTO products (product_name, price, shop_id) VALUES ('Dell Inspiron 5567', 750, 
    (SELECT shop_id FROM shops s, locations l WHERE s.location_id = l.location_id AND s.shop_name = 'PC Garage' AND l.street_address = 'Bulevardul Timisoara' and l.city = 'Bucuresti' AND l.country='Romania'));
INSERT INTO products (product_name, price, shop_id) VALUES ('Lenovo Legion', 1000, 
    (SELECT shop_id FROM shops s, locations l WHERE s.location_id = l.location_id AND s.shop_name = 'PC Garage' AND l.street_address = 'Bulevardul Timisoara' and l.city = 'Bucuresti' AND l.country='Romania'));
INSERT INTO products (product_name, price, shop_id) VALUES ('Dell Inspiron 5567', 700, 
    (SELECT shop_id FROM shops s, locations l WHERE s.location_id = l.location_id AND s.shop_name = 'Altex' AND l.street_address = 'Str. Palas' and l.city = 'Iasi' AND l.country='Romania'));
INSERT INTO products (product_name, price, shop_id, description) VALUES ('Dell Inspiron 5567', 500, 
    (SELECT shop_id FROM shops s, locations l WHERE s.location_id = l.location_id AND s.shop_name = 'Altex' AND l.street_address = 'Str. Palas' and l.city = 'Iasi' AND l.country='Romania'), 'Resigilat');
INSERT INTO products (product_name, price, shop_id) VALUES ('Apple Stand', 1000, 
    (SELECT shop_id FROM shops s, locations l WHERE s.location_id = l.location_id AND s.shop_name = 'Emag' AND l.street_address = 'Str. Plopilor' and l.city = 'Cluj-Napoca' AND l.country='Romania'));


/* shipping methods */
INSERT INTO shipping_methods (provider, delivering_price) VALUES ('Fedex', 65);
INSERT INTO shipping_methods (provider, delivering_price) VALUES ('DHL', 25);
INSERT INTO shipping_methods (provider, delivering_price) VALUES ('Singapore Post', 5);

/* app users */
INSERT INTO app_users (first_name, last_name, location_id, email, phone) VALUES ('Marin','Moisii',
    (SELECT location_id FROM locations WHERE street_address='Str. Tudor Vladimirescu' AND city='Iasi' AND country='Romania'),
    'marin.moisii@yahoo.com', '0701234567');
    
INSERT INTO app_users (first_name, last_name, location_id, email, phone) VALUES ('Alex','Ilioi',
    (SELECT location_id FROM locations WHERE street_address='Str. Tudor Vladimirescu' AND city='Iasi' AND country='Romania'),
    'alex.ilioi@yahoo.com', '0701234568');
    
INSERT INTO app_users (first_name, last_name, location_id, email, phone) VALUES ('Maria','Mesina',
    (SELECT location_id FROM locations WHERE street_address='Str. Tudor Vladimirescu' AND city='Iasi' AND country='Romania'),
    'maria.mesina@yahoo.com', '0701234569');
    
INSERT INTO app_users (first_name, last_name, location_id, email, phone) VALUES ('Mihai','Heghea',
    (SELECT location_id FROM locations WHERE street_address='Str. Tudor Vladimirescu' AND city='Iasi' AND country='Romania'),
    'mihai.heghea@yahoo.com', '0701234570');
    
INSERT INTO app_users (first_name, last_name, location_id, email, phone) VALUES ('Petru','Petrica',
    (SELECT location_id FROM locations WHERE street_address='Str. Tudor Vladimirescu' AND city='Iasi' AND country='Romania'),
    'petru.petrica@yahoo.com', '0701234571');

INSERT INTO app_users (first_name, last_name, location_id, email, phone) VALUES ('Andrei','Dorcu',
    (SELECT location_id FROM locations WHERE street_address='Str. Tudor Vladimirescu' AND city='Iasi' AND country='Romania'),
    'andrei.dorcu@yahoo.com', '0701234572');
INSERT INTO app_users (first_name, last_name, location_id, email, phone) VALUES ('Anisoara','Nanu',
    (SELECT location_id FROM locations WHERE street_address='Str. Aurel David' AND city='Ungheni' AND country='Republica Moldova'),
    'anisoara.nanu@yahoo.com', '0701234573');
INSERT INTO app_users (first_name, last_name, location_id, email, phone) VALUES ('Alina','Nanu',
    (SELECT location_id FROM locations WHERE street_address='Str. Aurel David' AND city='Ungheni' AND country='Republica Moldova'),
    'alina.nanu@yahoo.com', '0701234574');
INSERT INTO app_users (first_name, last_name, location_id, email, phone) VALUES ('Vasile','Enachi',
    (SELECT location_id FROM locations WHERE street_address='Str. Marinescu 18B' AND city='Ungheni' AND country='Republica Moldova'),
    'enaki.vasile@aol.com', '0746593368');

/* accounts */
INSERT INTO accounts (user_id, username, password, account_type) VALUES ((SELECT user_id from app_users where email='marin.moisii@yahoo.com'), 'marin', 'moisii', 'admin');
INSERT INTO accounts (user_id, username, password, account_type) VALUES ((SELECT user_id from app_users where email='alex.ilioi@yahoo.com'), 'alex', 'ilioi', 'admin_shop');
INSERT INTO accounts (user_id, username, password, account_type) VALUES ((SELECT user_id from app_users where email='maria.mesina@yahoo.com'), 'maria', 'mesina', 'admin_ship');
INSERT INTO accounts (user_id, username, password, account_type) VALUES ((SELECT user_id from app_users where email='mihai.heghea@yahoo.com'), 'mihai', 'heghea', 'client');
INSERT INTO accounts (user_id, username, password, account_type) VALUES ((SELECT user_id from app_users where email='petru.petrica@yahoo.com'), 'petru', 'petrica', 'client');
INSERT INTO accounts (user_id, username, password, account_type) VALUES ((SELECT user_id from app_users where email='andrei.dorcu@yahoo.com'), 'andrei', 'dorcu', 'client');
INSERT INTO accounts (user_id, username, password, account_type) VALUES ((SELECT user_id from app_users where email='anisoara.nanu@yahoo.com'), 'anisoara', 'nanu_e_mai_slab_ca_viorel', 'admin_shop');
INSERT INTO accounts (user_id, username, password, account_type) VALUES ((SELECT user_id from app_users where email='alina.nanu@yahoo.com'), 'alinutza', 'apple_is_my_life', 'admin_ship');
INSERT INTO accounts (user_id, username, password, account_type) VALUES ((SELECT user_id from app_users where email='enaki.vasile@aol.com'), 'enaki', 'vasile', 'client');
/* orders */

INSERT INTO orders (user_id, shipping_id, product_id, quantity, total_amount) VALUES
    ((SELECT user_id from app_users where email='petru.petrica@yahoo.com'),
    (SELECT shipping_id from shipping_methods where provider='Fedex' and delivering_price=65),
    (SELECT product_id from products where product_name='Covor Modern Vintage' and shop_id = 
        (select shop_id from shops s, locations l where s.shop_name = 'SA Covoare Ungheni' AND l.location_id = s.location_id AND l.street_address = 'Str. Mihai Eminescu' AND l.city = 'Ungheni' AND l.country='Republica Moldova')),
    2, 
    2 * (select price from products where product_name='Covor Modern Vintage' and shop_id = 
        (select shop_id from shops, locations l where shop_name = 'SA Covoare Ungheni' AND l.location_id = shops.location_id AND l.street_address = 'Str. Mihai Eminescu' AND l.city = 'Ungheni' AND l.country='Republica Moldova'))
        +(SELECT delivering_price from shipping_methods where provider='Fedex' and delivering_price=65));

INSERT INTO orders (user_id, shipping_id, product_id, quantity, total_amount) VALUES
    ((SELECT user_id from app_users where email='andrei.dorcu@yahoo.com'),
    (SELECT shipping_id from shipping_methods where provider='Fedex' and delivering_price=65),
    (SELECT product_id from products where product_name='Covor Traditional' and shop_id = 
        (select shop_id from shops s, locations l where s.shop_name = 'SA Covoare Ungheni' AND l.location_id = s.location_id AND l.street_address = 'Str. Mihai Eminescu' AND l.city = 'Ungheni' AND l.country='Republica Moldova')),
    1, 
    1 * (select price from products where product_name='Covor Traditional' and shop_id = 
        (select shop_id from shops s, locations l where shop_name = 'SA Covoare Ungheni' AND l.location_id = s.location_id AND l.street_address = 'Str. Mihai Eminescu' AND l.city = 'Ungheni' AND l.country='Republica Moldova'))
        + (SELECT delivering_price from shipping_methods where provider='Fedex' and delivering_price=65));

INSERT INTO orders (user_id, shipping_id, product_id, quantity, total_amount) VALUES
    ((SELECT user_id from app_users where email='andrei.dorcu@yahoo.com'),
    (SELECT shipping_id from shipping_methods where provider='Singapore Post' and delivering_price=5),
    (SELECT product_id from products where product_name='Geanta Dell' and shop_id = 
        (select shop_id from shops s, locations l where l.location_id = s.location_id AND s.shop_name = 'Emag' AND l.street_address = 'Str. Plopilor' and l.city = 'Cluj-Napoca' AND l.country='Romania')),
    3, 
    3 * (select price from products where product_name='Geanta Dell' and shop_id =
        (select shop_id from shops s, locations l where l.location_id = s.location_id AND s.shop_name = 'Emag' AND l.street_address = 'Str. Plopilor' and l.city = 'Cluj-Napoca' AND l.country='Romania'))
        + (SELECT delivering_price from shipping_methods where provider='Singapore Post' and delivering_price=5));

INSERT INTO orders (user_id, shipping_id, product_id, quantity, total_amount) VALUES
    ((SELECT user_id from app_users where email='alina.nanu@yahoo.com'),
    (SELECT shipping_id from shipping_methods where provider='Fedex' and delivering_price=65),
    (SELECT product_id from products where product_name='Apple Stand' and shop_id = 
        (select shop_id from shops s, locations l where l.location_id = s.location_id AND s.shop_name = 'Emag' AND l.street_address = 'Str. Plopilor' and l.city = 'Cluj-Napoca' AND l.country='Romania')),
    3, 
    3 * (select price from products where product_name='Apple Stand' and shop_id =
        (select shop_id from shops s, locations l where l.location_id = s.location_id AND s.shop_name = 'Emag' AND l.street_address = 'Str. Plopilor' and l.city = 'Cluj-Napoca' AND l.country='Romania'))
        + (SELECT delivering_price from shipping_methods where provider='Fedex' and delivering_price=65));


INSERT INTO orders (user_id, shipping_id, product_id, quantity, total_amount) VALUES
    ((SELECT user_id from app_users where email='maria.mesina@yahoo.com'),
    (SELECT shipping_id from shipping_methods where provider='DHL' and delivering_price=25),
    (SELECT product_id from products where product_name='Boxa JBL2 GO' and shop_id = 
        (select shop_id from shops s, locations l where l.location_id = s.location_id AND  shop_name = 'Emag' AND s.location_id = l.location_id AND l.street_address = 'Str. Plopilor' and l.city = 'Cluj-Napoca' AND l.country='Romania')),
    1, 
    1 * (SELECT product_id from products where product_name='Boxa JBL2 GO' and shop_id =
    (select shop_id from shops s, locations l where l.location_id = s.location_id AND  shop_name = 'Emag' AND s.location_id = l.location_id AND l.street_address = 'Str. Plopilor' and l.city = 'Cluj-Napoca' AND l.country='Romania'))
    +(SELECT delivering_price from shipping_methods where provider='DHL' and delivering_price=25));
   
SELECT * FROM locations;
SELECT * FROM shops;
SELECT * FROM products;
SELECT * FROM app_users;
SELECT * FROM accounts;
SELECT * FROM orders;

COMMIT;

