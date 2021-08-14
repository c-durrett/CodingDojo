INSERT INTO users (first_name, last_name, email) VALUES('Christian', 'Durrett', 'christiandurrett@codingdojo.com');
INSERT INTO users (first_name, last_name, email) VALUES('Jordan', 'Gilberg', 'jordangilberg@codingdojo.com');
INSERT INTO users (first_name, last_name, email) VALUES('Justin', 'Shin', 'justinshin@codingdojo.com');
SELECT * FROM users;
SELECT * FROM users WHERE email LIKE 'christiandurrett@codingdojo.com';
SELECT * FROM users WHERE id = 3; 
UPDATE users SET last_name = "Pankcakes" WHERE users.id = 3;
DELETE FROM users WHERE users.id = 2;
SELECT * FROM users ORDER BY first_name DESC;