====
favorite
====

A tool for collect your favorite shell commands.

Have fun.

Options
-------

-m       Comment for ``command``.
-d       Delete from favorite with ``id``.
-q       Fetch command from favorite by ``sql``.
-l       List all of the favorited commands.
-D       Clean up favorite.

Example
-------

    $ fav -m "mem usage tool" free

    $ fav -d 1

    $ fav -q "select * from ``fav`` where ``command`` like '%free%'"

    $ fav -l

    $ fav -D

Table ``fav`` schema:
-------

+------------+------------+--------------------------+
| Column     | Type       | Desc                     |
+============+============+==========================+
| id         | Integer    | fav command id           |
+------------+------------+--------------------------+
| date       | Text       | date add to fav          |
+------------+------------+--------------------------+
| command    | Text       | command                  |
+------------+------------+--------------------------+
| comment    | Text       | desc of fav this command |
+------------+------------+--------------------------+

Installation
------------

To install ``favorite``, try:

    sudo pip install https://github.com/liyuance/favorite/zipball/master
