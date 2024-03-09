## Part 1: Restaurant finder

###### The SQL code to create the ```restaurants``` table
``` sql
DROP TABLE IF EXISTS restaurants;
CREATE TABLE restaurants (
    id INTEGER PRIMARY KEY,
    restaurant_name TEXT,
    category TEXT,
    price TEXT,
    neighborhood TEXT,
    open_time TIME,
    close_time TIME,
    rating NUMERIC,
    good_for_kids BOOLEAN
);
```

###### The SQL code to create the ```reviews``` table
``` sql
DROP TABLE IF EXISTS reviews;
CREATE TABLE reviews (
    id INTEGER PRIMARY KEY,
    restaurant_id INTEGER,
    username TEXT,
    review_datetime DATETIME,
    review_content TEXT
);
```

###### A link to restaurants.csv in the data directory
Here is the [link](data/restaurants.csv).

###### The SQLite code to import restaurants.csv into the table
``` sql
.mode csv  
.import /Users/wulabama/Desktop/sql-crud-SisiDzy/data/restaurants.csv restaurants
```

###### The SQL queries that solve each of the tasks
1. Find all cheap restaurants in a particular neighborhood (pick any neighborhood as an example).
``` sql
SELECT restaurant_name,price,neighborhood FROM restaurants WHERE price = "Cheap" AND neighborhood = "SoHo";
```
2. Find all restaurants in a particular genre (pick any genre as an example) with 3 stars or more, ordered by the number of stars in descending order.
``` sql
SELECT restaurant_name,category,rating FROM restaurants WHERE category = "Mexican" AND rating >= 3.0 ORDER BY rating DESC;
```
3. Find all restaurants that are open now (see hint below).
``` sql
SELECT restaurant_name,open_time,close_time FROM restaurants WHERE strftime('%H:%M', 'now', 'localtime') BETWEEN open_time AND close_time;
```
4. Leave a review for a restaurant (pick any restaurant as an example).
``` sql
INSERT INTO reviews VALUES (1, 234, 'sisi', '2023-02-28 16:02:20', 'Pretty nice!');
```
5. Delete all restaurants that are not good for kids.
``` sql
DELETE FROM restaurants WHERE good_for_kids = "FALSE";
```
6. Find the number of restaurants in each NYC neighborhood.
``` sql
SELECT count(restaurant_name),neighborhood FROM restaurants GROUP BY neighborhood;
```

## Part 2: Social media app

###### The SQL code to create the ```users``` table
``` sql
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    usernames TEXT,
    emails TEXT,
    passwords TEXT
);
```

###### The SQL code to create the ```posts``` table
``` sql
DROP TABLE IF EXISTS posts;
CREATE TABLE posts (
    id INTEGER PRIMARY KEY,
    post_type TEXT,
    sender_id INTEGER,
    receiver_id INTEGER,
    post_datetime DATETIME,
    visible BOOLEAN,
    post_content TEXT
);
```

###### Links to users.csv and posts.csv in the data directory
Here is the [link](data/users.csv) to users.csv.  
Here is the [link](data/posts.csv) to posts.csv.

###### The SQLite code to import users.csv and posts.csv into the table
``` sql
.mode csv
.import /Users/wulabama/Desktop/sql-crud-SisiDzy/data/users.csv users
.import /Users/wulabama/Desktop/sql-crud-SisiDzy/data/posts.csv posts
```

###### The SQL queries that solve each of the tasks
1. Register a new User.
``` sql
INSERT INTO users VALUES (1001, 'pikachu', 'pika@gmail.com', 'PokeMon8890');
```
2. Create a new Message sent by a particular User to a particular User (pick any two Users for example).
``` sql
INSERT INTO posts VALUES (2001, 'message', 13, 14, '2023-02-14 17:20:00', 'TRUE', 'Love U babe.');
```
3. Create a new Story by a particular User (pick any User for example).
``` sql
INSERT INTO posts (id, post_type, sender_id, post_datetime, visible, post_content) VALUES (2002, 'story', 345, '2023-03-02 13:07:02', 'TRUE', 'Interesting dog.');
```
4. Show the 10 most recent visible Messages and Stories, in order of recency.
``` sql
SELECT * FROM posts WHERE visible = 'TRUE' ORDER BY post_datetime DESC LIMIT 10;
```
5. Show the 10 most recent visible Messages sent by a particular User to a particular User (pick any two Users for example), in order of recency.
``` sql
SELECT * FROM posts WHERE post_type = "message" AND visible = 'TRUE' AND sender_id = 100 AND receiver_id = 250 ORDER BY post_datetime DESC LIMIT 10;
```
6. Make all Stories that are more than 24 hours old invisible.
``` sql
UPDATE posts SET visible = 'FALSE' WHERE post_type = 'story' AND ROUND((JULIANDAY('now','localtime') - JULIANDAY(post_datetime)) * 24) > 24;
```
7. Show all invisible Messages and Stories, in order of recency.
``` sql
SELECT * FROM posts WHERE visible = "FALSE" ORDER BY post_datetime DESC;
```
8. Show the number of posts by each User.
``` sql
SELECT users.id, users.usernames, count(posts.sender_id) FROM users LEFT JOIN posts ON users.id = posts.sender_id GROUP BY users.id;
```
9. Show the post text and email address of all posts and the User who made them within the last 24 hours.
``` sql
SELECT users.usernames, users.emails, posts.post_datetime, posts.post_content FROM users INNER JOIN posts ON users.id = posts.sender_id WHERE ROUND((JULIANDAY('now','localtime') - JULIANDAY(post_datetime)) * 24) <=24;
```
10. Show the email addresses of all Users who have not posted anything yet.
``` sql
SELECT users.emails FROM users LEFT JOIN posts ON users.id = posts.sender_id WHERE posts.post_content IS NULL;
```

