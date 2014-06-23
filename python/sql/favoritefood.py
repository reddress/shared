from sqlsetup import connect, run, commit, tbl, close, sel

connect('learning')

run("""CREATE TABLE person
(person_id SMALLINT UNSIGNED,
fname VARCHAR(20),
lname VARCHAR(20),
gender ENUM('M','F'),
birth_date DATE,
street VARCHAR(30),
city VARCHAR(20),
state VARCHAR(20),
country VARCHAR(30),
postal_code VARCHAR(10),
CONSTRAINT pk_person PRIMARY KEY (person_id));""")

run("DROP TABLE person;")

run("DESC person;")

run("""CREATE TABLE favorite_food
(person_id SMALLINT UNSIGNED,
food VARCHAR(20),
CONSTRAINT pk_favorite_food PRIMARY KEY (person_id, food),
CONSTRAINT pk_fav_food_person_id FOREIGN KEY (person_id)
REFERENCES person (person_id));""")

run("DESC favorite_food")
tbl()

run("DROP TABLE favorite_food")
run("ALTER TABLE person MODIFY person_id SMALLINT UNSIGNED AUTO_INCREMENT")

run("DESC person")
tbl()

run('''INSERT INTO person
(person_id, fname, lname, gender, birth_date)
VALUES (null, "William", "Turner", "M", "1972-05-27");''')

run("SELECT * FROM person;")
tbl()

run("""INSERT INTO PERSON
(person_id, fname, lname, gender, birth_date)
VALUES (null, 'Tina', 'Peters', 'F', '1999-12-02');""")

run("""INSERT INTO person
(person_id, fname, lname, gender, birth_date)
VALUES (8, 'Lee', 'Starr', 'M', '1968-2-3');""")

run("""INSERT INTO person
(person_id, fname, lname, gender, birth_date)
VALUES (null, 'Sharon', 'Walker', 'F', '1973-9-12');""")

# IMPORTANT: COMMIT CHANGES
commit()

run("""SELECT person_id, fname, lname, birth_date
FROM person;""")
tbl()

sel("""SELECT person_id, fname, lname FROM person;""")

sel("""SELECT person_id, fname, lname FROM person
WHERE person_id = 8;""")

run("""INSERT INTO favorite_food (person_id, food)
VALUES(8, 'nachos');""")

commit()

sel("""SELECT * FROM favorite_food;""")

sel("""SELECT food FROM favorite_food
WHERE person_id = 8
ORDER BY food;""")

run("""UPDATE person
SET street = "124 Tremont St.",
city = "Boston"
WHERE person_id = 8;""")

sel("""SELECT * FROM person""")

run("""DELETE FROM person WHERE person_id = 20;""")
commit()

run("""INSERT INTO favorite_food (person_id, food)
VALUES (999, 'lasagna');""")

run("DESC person")
tbl()
