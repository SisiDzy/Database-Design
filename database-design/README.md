# Data Normalization and Entity-Relationship Diagramming

## Original Table

| assignment_id | student_id | due_date | professor | assignment_topic                | classroom | grade | relevant_reading    | professor_email   |
| :------------ | :--------- | :------- | :-------- | :------------------------------ | :-------- | :---- | :------------------ | :---------------- |
| 1             | 1          | 23.02.21 | Melvin    | Data normalization              | WWH 101   | 80    | Deumlich Chapter 3  | l.melvin@foo.edu  |
| 2             | 7          | 18.11.21 | Logston   | Single table queries            | 60FA 314  | 25    | Dümmlers Chapter 11 | e.logston@foo.edu |
| 1             | 4          | 23.02.21 | Melvin    | Data normalization              | WWH 101   | 75    | Deumlich Chapter 3  | l.melvin@foo.edu  |
| 5             | 2          | 05.05.21 | Logston   | Python and pandas               | 60FA 314  | 92    | Dümmlers Chapter 14 | e.logston@foo.edu |
| 4             | 2          | 04.07.21 | Nevarez   | Spreadsheet aggregate functions | WWH 201   | 65    | Zehnder Page 87     | i.nevarez@foo.edu |
| ...           | ...        | ...      | ...       | ...                             | ...       | ...   | ...                 | ...               |

## Problems

1. Lack of data: There are serveral fields that are important for the table but not shown on it, such as `student_name` and `course_name`.
2. Redundancy: Data in the table is duplicated across multiple fields, such as `due_date` (23.02.21), `professor` (Melvin), and `assignment_topic`  (Data normalization).
3. Anomalies: The table does not allow us to insert or delete certain attributes without doing the same change to other attributes, and to update certain attributes at once to keep data integrity.
4. 2NF: Based on the data set, we can use `assignment_id` and `student_id` as a composite primary key. With this composite key, fields such as `due_date` and `assignment_topic` are only about a part of that entity.
5. 3NF: Non-key fields of the table are facts about other non-key fields instead of key fields. For example, `professor_email` is the fact about `professor`.   
6. 4NF: The table contains more than one independent multi-valued facts about an entity. For instance, `due_date` and `relevant_reading` are about `assignment_id`, but they are independent. And an assignment may have multiple readings relevant to it and multiple due dates if different professors give the same assignment, so `due_date` and `relevant_reading` are both multi-valued facts.

## New Tables

1. Professor:

| professor_id* | professor_name | professor_email |
| :------------ | :--------- | :------- |
| 1             | Melvin          | l.melvin@foo.edu    |
| 2             | Logston         | e.logston@foo.edu    |
| 3             | Nevarez         | i.nevarez@foo.edu    |

2. Student:

| student_id* | student_name | student_email |
| :------------ | :--------- | :------- |
| 1             | Sisi          | zd773@nyu.edu    |
| 2             | Jasmine       | jasmine4343@nyu.edu    |
| 3             | Luna         | luna211@nyu.edu    |

3. Course:

| course_id* | course_name |
| :------------ | :---------------- |
| 1             | Database Design |
| 2             | Intro to Python |
| 3             | Social Media |

4. Section:

| section_id* | course_id | section_number |
| :------------ | :--------- | :------- |
| 1             | 1          | 001    |
| 2             | 1          | 002    |
| 3             | 2          | 001    |

5. Classroom:

| classroom_id* | classroom |
| :------------ | :-------- |
| 1              | WWH 101 |
| 2              | 60FA 314 |
| 3              | WWH 201 |

6. Assignment:

| assignment_id* | assignment_topic |
| :------------ | :---------------- |
| 1             | Data normalization |
| 2             | Single table queries |
| 3             | Data munging |

7. Assignment Due Date:

| assignment_id* | professor_id* | section_id* | due.date |
| :------------  | :-------  | :-------  | :-------  |
| 1             | 1    | 1 | 23.02.21 |
| 1             | 1    | 7 | 25.02.21 |
| 2             | 1    | 1 | 04.05.21 |

8. Reading:

| assignment_id* | professor_id* | relevant_reading* |
| :------------ | :------------ | :----------------- |
| 1             | 1 | Deumlich Chapter 3    |
| 1             | 1 | Zehnder Page 27    |
| 1             | 2 | Dümmlers Chapter 11    |

9. Grade:

| assignment_id* | student_id* | grade |
| :------------ | :--------- | :------- |
| 1             | 1          | 80    |
| 1             | 2          | 25    |
| 1             | 3          | 75    |

10. Section and Student:

| section_id* | student_id* |
| :------------  | :------- |
| 1              | 1 |
| 1              | 8 |
| 1              | 15 |

11. Section, Professor, and Classroom:

| section_id* | professor_id* | classroom_id* |
| :------------ | :-------  | :-------  |
| 1             | 1 | 1 |
| 2             | 2 | 8 |
| 3             | 2 | 5 |

## ER Diagram

![ER Diagram](ERD.drawio.svg)

## Changes

1. Found important but missing fields so that the data set was complete
2. Reorganized fields into different tables to eliminate data redundancy and anomalies
3. Assigned the primary key to each table to make sure that they were unique
4. Adjusted the improper relationship between the key field and the non-key field in each table to ensure the normalization of the data set.
