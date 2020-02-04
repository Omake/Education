
-- Практическое задание по теме “Операторы, фильтрация, сортировка и ограничение”
-- 1 Задание


ALTER TABLE users ADD created_at VARCHAR(255);
ALTER TABLE users ADD updated_at VARCHAR(255);

UPDATE users SET created_at = NOW(), updated_at = NOW() WHERE created_at IS NULL AND updated_at IS NULL;



-- 2 Задание

	
ALTER TABLE users MODIFY COLUMN created_at DATETIME NULL;
ALTER TABLE users MODIFY COLUMN updated_at DATETIME NULL;



-- 3 Задание


INSERT INTO STOREHOUSES VALUES (1, "Первый склад", NOW(),NOW());
INSERT INTO STOREHOUSES_PRODUCTS VALUES (NULL, 1, 4, 10, NOW(),NOW());
INSERT INTO STOREHOUSES_PRODUCTS VALUES (NULL, 1, 3, 0, NOW(),NOW());
INSERT INTO STOREHOUSES_PRODUCTS VALUES (NULL, 1, 6, 111, NOW(),NOW());
INSERT INTO STOREHOUSES_PRODUCTS VALUES (NULL, 1, 5, 5, NOW(),NOW());
INSERT INTO STOREHOUSES_PRODUCTS VALUES (NULL, 1, 2, 0, NOW(),NOW());

SELECT value FROM STOREHOUSES_PRODUCTS ORDER BY value = 0, value;

-- Практическое задание теме “Агрегация данных”


-- 1 Задание


select AVG((YEAR(NOW()) - YEAR(birthday_at))) AS average_age FROM users;



-- 2 Задание


select COUNT(*) AS total, DAYOFWEEK(date_add(birthday_at, INTERVAL (YEAR(now()) - YEAR(birthday_at)) year)) as day_of_week from users GROUP BY day_of_week; -- Вот тут пришлось знатно повозиться


