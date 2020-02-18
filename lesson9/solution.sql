-- В базе данных shop и sample присутствуют одни и те же таблицы, учебной базы данных. Переместите запись id = 1 из таблицы shop.users в таблицу sample.users. Используйте транзакции.

START TRANSACTION;

select * from shop.users where id=1;

insert into sample.users select * from shop.users where id=1;

delete from shop.users where id=1;

commit;




-- Создайте представление, которое выводит название name товарной позиции из таблицы products и соответствующее название каталога name из таблицы catalogs.

create view prod_list as 
select 
	p.name 'Наименование',
	c.name 'Категория'

from products p
join catalogs c
on p.catalog_id = c.id;


-- Проверяем
select * from prod_list;
