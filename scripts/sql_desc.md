DESC ask_tags;
+-------------+------------------+------+-----+---------+----------------+
| Field       | Type             | Null | Key | Default | 描述          |
+-------------+------------------+------+-----+---------+----------------+
| id          | int(10) unsigned | NO   | PRI | NULL    |     表 id     |
| name        | varchar(128)     | NO   | UNI | NULL    |  标签的名称   |
| main_id     | int(11)          | NO   | MUL | NULL    |  主标签的 Id   |
| category_id | int(11)          | NO   | MUL | 0       |                |
| logo        | varchar(128)     | YES  |     | NULL    |                |
| summary     | varchar(255)     | YES  |     | NULL    |                |
| description | text             | YES  |     | NULL    |                |
| parent_id   | int(10) unsigned | NO   | MUL | 0       |   父标签的 Id  |
| followers   | int(10) unsigned | NO   | MUL | 0       |                |
| created_at  | timestamp        | YES  |     | NULL    |                |
| updated_at  | timestamp        | YES  |     | NULL    |                |
+-------------+------------------+------+-----+---------+----------------+


desc ask_taggables;
+---------------+---------------------+------+-----+---------+----------------+
| Field         | Type                | Null | Key | Default | Extra          |
+---------------+---------------------+------+-----+---------+----------------+
| id            | int(10) unsigned    | NO   | PRI | NULL    | auto_increment |
| tag_id        | int(10) unsigned    | NO   | MUL | NULL    |                |
| taggable_type | varchar(255)        | NO   | MUL | NULL    |                |
| taggable_id   | bigint(20) unsigned | NO   |     | NULL    |                |
+---------------+---------------------+------+-----+---------+----------------+



