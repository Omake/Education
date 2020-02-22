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




/* 
	Создайте хранимую функцию hello(), которая будет возвращать приветствие, в зависимости от текущего времени суток.
С 6:00 до 12:00 функция должна возвращать фразу "Доброе утро", с 12:00 до 18:00 функция должна возвращать фразу "Добрый день", 
с 18:00 до 00:00 — "Добрый вечер", с 00:00 до 6:00 — "Доброй ночи". 
*/




delimiter //

drop FUNCTION if exists hello;
create function hello()
returns varchar(255) DETERMINISTIC
BEGIN
	declare morn varchar(255) default '06:00:00';
	declare noon varchar(255) default '12:00:00';
	declare evening varchar(255) default '18:00:00';
	declare midnight varchar(255) default '23:59:59';
	
	IF(CURRENT_TIME() > morn and CURRENT_TIME() < noon) THEN
		return 'Доброе утро';
	ELSEIF (CURRENT_TIME() > noon and current_time() < evening) then
		return 'Добрый день';
	elseif (current_time() > evening and current_time() < midnight) then 
		return 'Добрый вечер';
	else
		return 'Доброй ночи';
    END IF;
END//

delimiter ;

select hello();


/* 
В таблице products есть два текстовых поля: name с названием товара и description с его описанием.
Допустимо присутствие обоих полей или одно из них. Ситуация, когда оба поля принимают неопределенное значение NULL неприемлема. 
Используя триггеры, добейтесь того, чтобы одно из этих полей или оба поля были заполнены. 
При попытке присвоить полям NULL-значение необходимо отменить операцию.
*/

delimiter //

DROP TRIGGER IF EXISTS products_check //
CREATE TRIGGER products_check BEFORE INSERT ON products
FOR EACH ROW
BEGIN
	IF (new.name is null and new.description is null) THEN 
		SIGNAL SQLSTATE '45000' 
		SET MESSAGE_TEXT = "name and description can't be null at once";
	END IF;
END//

delimiter ;
