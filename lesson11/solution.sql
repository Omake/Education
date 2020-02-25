-- Создайте таблицу logs типа Archive. Пусть при каждом создании записи в таблицах users,
-- catalogs и products в таблицу logs помещается время и дата создания записи, название 
-- таблицы, идентификатор первичного ключа и содержимое поля name.


drop table if exists `logs`;
create table `logs` (
	id bigint unsigned auto_increment primary key,
	created_at datetime default now(),
	table_name VARCHAR(255),
	element_id BIGINT,
	source_name VARCHAR(255)
) ENGINE =  Archive;

delimiter //

DROP TRIGGER IF EXISTS users_log //
CREATE TRIGGER users_log AFTER INSERT ON users
FOR EACH ROW
BEGIN
	insert into `logs`(table_name, element_id, source_name) values ('users', new.id, new.name);
END//




DROP TRIGGER IF EXISTS catalogs_log //
CREATE TRIGGER catalogs_log AFTER INSERT ON catalogs
FOR EACH ROW
BEGIN
	insert into `logs`(table_name, element_id, source_name) values ('catalogs', new.id, new.name);
END//

DROP TRIGGER IF EXISTS products_log //
CREATE TRIGGER products_log AFTER INSERT ON products
FOR EACH ROW
BEGIN
	insert into `logs`(table_name, element_id, source_name) values ('products', new.id, new.name);
END//


delimiter ;




insert into users (name, BIRTHDAY_AT) values ('Test','1991-05-18');
insert into products (name, DESCRIPTION, PRICE, CATALOG_ID) values ('Test','Another test',123,1);
insert into catalogs (name) values ('Test');

select * from logs;
