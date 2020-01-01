@ delete_tables.sql

CREATE TABLE locations(
    location_id NUMBER(4) NOT NULL,
    street_address VARCHAR2(50) NOT NULL,
    city VARCHAR2(30) NOT NULL,
    country VARCHAR2(30) NOT NULL,
    CONSTRAINT location_id_pk PRIMARY KEY (location_id),
    CONSTRAINT location_id_uk UNIQUE (street_address, city, country));

CREATE TABLE shops(
    shop_id NUMBER(4) NOT NULL,
    shop_name VARCHAR2(20) NOT NULL,
    location_id NUMBER(4) NOT NULL,
    CONSTRAINT shop_id_pk PRIMARY KEY(shop_id),
    CONSTRAINT shop_location_id_fk FOREIGN KEY (location_id) REFERENCES locations,
    CONSTRAINT shop_uk UNIQUE (shop_name, location_id));
    
CREATE TABLE products(
    product_id NUMBER(4) NOT NULL,
    product_name VARCHAR2(20) NOT NULL,
    price NUMBER(6, 2) NOT NULL,
    shop_id NUMBER(4) NOT NULL,
    description VARCHAR2(100),
    CONSTRAINT product_id_pk PRIMARY KEY(product_id),
    CONSTRAINT product_shop_id_fk FOREIGN KEY(shop_id) REFERENCES shops,
    CONSTRAINT price_range_ch CHECK (price > 0 and price < 1000000),
    CONSTRAINT product_uk UNIQUE (product_name, price, shop_id, description));
    
CREATE TABLE shipping_methods(
    shipping_id NUMBER(4) NOT NULL,
    provider VARCHAR2(100) NOT NULL,
    delivering_price NUMBER(6,2) NOT NULL,
    CONSTRAINT shipping_id_pk PRIMARY KEY(shipping_id),
    CONSTRAINT delivering_price_range_ch CHECK (delivering_price > 0 and delivering_price < 1000000),
    CONSTRAINT shipping_uk UNIQUE (provider));
    
CREATE TABLE app_users(
    user_id NUMBER(4) NOT NULL ,
    first_name VARCHAR2(20) NOT NULL,
    last_name VARCHAR2(20) NOT NULL,
    location_id NUMBER(4) NOT NULL,
    email VARCHAR2(30) NOT NULL UNIQUE,
    phone VARCHAR2(20) NOT NULL UNIQUE,
    CONSTRAINT user_id_pk PRIMARY KEY(user_id),
    CONSTRAINT user_location_id_fk FOREIGN KEY(location_id) REFERENCES locations);

CREATE TABLE accounts(
    user_id NUMBER(4) NOT NULL,
    username VARCHAR2(30) NOT NULL UNIQUE,
    password VARCHAR2(100) NOT NULL,
    account_type VARCHAR2(10) NOT NULL,
    CONSTRAINT account_id_pk PRIMARY KEY(user_id),
    CONSTRAINT account_user_id_fk FOREIGN KEY(user_id) REFERENCES app_users,
    CONSTRAINT account_user_pass_ch CHECK (length(password) >= 6)
);
    
CREATE TABLE orders(
    order_id NUMBER(4) NOT NULL,
    user_id NUMBER(4) NOT NULL,
    shipping_id NUMBER(4) NOT NULL,
    product_id NUMBER(4) NOT NULL,
    quantity NUMBER(4) NOT NULL,
    total_amount NUMBER(10, 2) NOT NULL,
    date_ordered DATE DEFAULT sysdate NOT NULL,
    CONSTRAINT order_id_pk PRIMARY KEY(order_id), 
    CONSTRAINT order_user_id_fk FOREIGN KEY(user_id) REFERENCES app_users,
    CONSTRAINT order_shipping_id_fk FOREIGN KEY(shipping_id) REFERENCES shipping_methods,
    CONSTRAINT order_product_id_fk FOREIGN KEY(product_id) REFERENCES products,
    CONSTRAINT quantity_range_ch CHECK (quantity > 0 and quantity < 10000),
    CONSTRAINT amount_range_ch CHECK (total_amount > 0 and total_amount < 10000000000)
);
    
CREATE SEQUENCE location_sequence_incrementer START WITH 1 INCREMENT BY 1;   
CREATE SEQUENCE shop_sequence_incrementer START WITH 1 INCREMENT BY 1;   
CREATE SEQUENCE product_sequence_incrementer START WITH 1 INCREMENT BY 1;   
CREATE SEQUENCE shipping_method_sequence_incrementer START WITH 1 INCREMENT BY 1;   
CREATE SEQUENCE user_sequence_incrementer START WITH 1 INCREMENT BY 1;   
CREATE SEQUENCE order_sequence_incrementer START WITH 1 INCREMENT BY 1;

CREATE OR REPLACE TRIGGER location_inc_on_insert_trigger
BEFORE INSERT
    ON locations
    FOR EACH ROW
BEGIN
    :NEW.location_id := location_sequence_incrementer.nextval;
END;
/

CREATE OR REPLACE TRIGGER shop_inc_on_insert_trigger
BEFORE INSERT
    ON shops
    FOR EACH ROW
BEGIN
    :NEW.shop_id := shop_sequence_incrementer.nextval;
END;
/

CREATE OR REPLACE TRIGGER product_inc_on_insert_trigger
BEFORE INSERT
    ON products
    FOR EACH ROW
BEGIN
    :NEW.product_id := product_sequence_incrementer.nextval;
END;
/

CREATE OR REPLACE TRIGGER shipping_inc_on_insert_trigger
BEFORE INSERT
    ON shipping_methods
    FOR EACH ROW
BEGIN
    :NEW.shipping_id := shipping_method_sequence_incrementer.nextval;
END;
/

CREATE OR REPLACE TRIGGER user_inc_on_insert_trigger
BEFORE INSERT
    ON app_users
    FOR EACH ROW
BEGIN
    :NEW.user_id := user_sequence_incrementer.nextval;
END;
/

CREATE OR REPLACE TRIGGER order_inc_on_insert_trigger
BEFORE INSERT
    ON orders
    FOR EACH ROW
BEGIN
    :NEW.order_id := order_sequence_incrementer.nextval;
END;
/

CREATE OR REPLACE TRIGGER order_date_trigger
BEFORE INSERT
    ON orders
    FOR EACH ROW
BEGIN
    :NEW.date_ordered := SYSDATE;
END;
/

