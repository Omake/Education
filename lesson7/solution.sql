-- Составьте список пользователей users, которые осуществили хотя бы один заказ orders в интернет магазине.


insert into orders (user_id, created_at, updated_at) values (
	1, now(),now()),(1, now(),now()),(1, now(),now()),(1, now(),now()),(2, now(),now()),(2, now(),now()),(3, now(),now()),(4, now(),now());


select distinct users.id,users.name from users,orders where users.id = orders.user_id;




-- Выведите список товаров products и разделов catalogs, который соответствует товару.

select PRODUCTS.ID,PRODUCTS.NAME as 'Наименование продукта',CATALOGS.NAME as 'Тип продукта' from products,catalogs where PRODUCTS.CATALOG_ID = CATALOGS.ID;


-- Пусть имеется таблица рейсов flights (id, from, to) и таблица городов cities (label, name). 
-- Поля from, to и label содержат английские названия городов, поле name — русское. Выведите список рейсов flights с русскими названиями городов.



DROP TABLE IF EXISTS cities;
CREATE TABLE cities (
  label varchar(255) PRIMARY KEY,
  name varchar(255)
);


DROP TABLE IF EXISTS flights;
CREATE TABLE flights (
  id SERIAL PRIMARY KEY,
  `from` varchar(255),
  `to` varchar(255),
  FOREIGN KEY (`from`)  REFERENCES cities (label),
  FOREIGN KEY (`to`)  REFERENCES cities (label)
);

insert into CITIES(label,name) values ('moscow','Москва'),
	('irkutsk','Иркутск'),
	('novgorod','Новгород'),
	('kazan','Казань'),
	('omsk','Омск');

insert into FLIGHTS(`from`,`to`) values ('moscow','omsk'),
	('novgorod','kazan'),
	('irkutsk','moscow'),
	('omsk','irkutsk'),
	('moscow','kazan');

select distinct FLIGHTS.id, (select cities.name from cities where FLIGHTS.`from` = CITIES.LABEL) as 'Из',(select cities.name from cities where FLIGHTS.`to` = CITIES.LABEL) as 'В' from flights, cities;
