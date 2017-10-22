#!/usr/bin/env python
# coding=utf-8

import os
import sys
import time
import sqlite3
from optparse import OptionParser
from texttable import Texttable

class FavManager(object):
  """ Favorite manager """

  _db_location = os.getenv("HOME") + "/.favorite"
  _table_name = "fav"
  _db_conn = sqlite3.connect(_db_location)

  def __init__(self):
    """ init fav table """

    create_table_sql = """
      CREATE TABLE IF NOT EXISTS %s (
      id INTEGER PRIMARY KEY autoincrement,
      date TEXT,
      command TEXT,
      comment TEXT)
      """ % self._table_name

    self._db_conn.execute(create_table_sql)
    self._db_conn.commit()

  def __del__(self):
    """ close db conn """

    self._db_conn.close()

  def add(self, command, comment):
    """
    Add  `command` to favorite
    :param command:
    :param comment:
    :return:
    """

    now = time.strftime("%Y-%m-%d %H:%M:%S")

    insert_sql = """
      INSERT INTO %s VALUES(NULL, ?, ?, ?)
      """ % self._table_name

    self._db_conn.execute(insert_sql, (now, command, comment))
    self._db_conn.commit()

  def delete(self, fav_id):
    """
    Delete favorited command with id = `fav_id`
    :param fav_id:
    :return:
    """

    delete_sql = """
      DELETE FROM %s WHERE id = %d
      """ % (self._table_name, str(fav_id))

    self._db_conn.execute(delete_sql)
    self._db_conn.commit()

  def query(self, query_str):
    """
    Fetch from favorite by sql `query_str`
    :param query_str:
    :return:
    """

    query_result = []
    cursor = self._db_conn.execute(query_str)
    header = list(map(lambda x: x[0], cursor.description))
    query_result.append(header)
    for fav in cursor:
      query_result.append(fav)

    text_table = Texttable()
    text_table.add_rows(query_result)
    print text_table.draw()

  def list(self):
    """
    List all favorited commands
    :return:
    """

    select_sql = """
      SELECT * FROM %s
      """ % self._table_name

    table_header = ["Id", "Date", "Command", "Comment"]
    command_list = []
    command_list.append(table_header)
    for fav in self._db_conn.execute(select_sql):
      command_list.append(list(fav))

    text_table = Texttable()
    text_table.add_rows(command_list)
    print text_table.draw()

  def clean(self):
    """
    Clean up favorite
    :return:
    """

    drop_sql = """
      DROP TABLE %s
      """ % self._table_name

    self._db_conn.execute(drop_sql)
    self._db_conn.commit()

def print_err(str):
  """
  print str to sys.stderr
  :param str:
  :return:
  """
  sys.stderr.write(str)
  sys.stderr.write("\n")

def main():
  """ Entry point for the command-line tool """

  usage_str = """\n\t
    fav [-l] [-D] [-d FAV_ID] [-m COMMENT] COMMAND
  """
  parser = OptionParser(usage=usage_str, version="fav 0.1")
  parser.disable_interspersed_args()

  parser.add_option("-m", "--comment", dest="comment", type=str, default="",
                    help="Comment of this command")
  parser.add_option("-d", "--delete", dest="fav_id", type=int, default=None,
                    help="Remove favorited command")
  parser.add_option("-q", "--query", dest="query_str", type=str, default="",
                    help="Search favorited commands with filter")
  parser.add_option("-l", "--list", dest="list", action="store_true",
                    help="List all favorited commands")
  parser.add_option("-D", "--clean", dest="clean", action="store_true",
                    help="Clean up all favorited commands")

  parser.set_defaults(v=False, fmt="png", type="class", style="scruffy")

  (options, fav_commands) = parser.parse_args()

  fav_manager = FavManager()

  if options.list:
    fav_manager.list()

  elif options.clean:
    fav_manager.clean()
    print_err("Clean up favorite done.")

  elif fav_commands:
    print_err("Added command `%s` to favorite." % " ".join(fav_commands))
    fav_manager.add(" ".join(fav_commands), options.comment)

  elif options.fav_id:
    print_err("Deleted favorited command with id %d." % options.fav_id)
    fav_manager.delete(options.fav_id)

  elif options.query_str:
    fav_manager.query(options.query_str)

  else:
    parser.print_help()

if __name__ == "__main__":
  main()