import sqlite3
import sys
import csv
import os


delimiter = ","
path_to_db = os.getcwd()+'\db'
db_name = 'Storage.sqlite'
name_of_table = 'black_hole'


def create_directory_db(path):
    if not os.path.exists(path):
        os.makedirs(path)


def get_records_for_table(file_name):
    rows_list = []
    file = open(file_name, "r")
    reader = csv.reader(file)
    for row in reader:
        rows_list.append(('{}'.format(os.path.basename(file.name)), '{}'.format(" ".join(row))))
    file.close()
    return rows_list


def create_table_and_get_cursor(path, name_table):
    create_directory_db(path)
    connect = sqlite3.connect(path+'\{}'.format(db_name))
    curs = connect.cursor()
    curs.execute("""CREATE TABLE IF NOT EXISTS """+name_table+""" (file_name text, row text)""")
    return curs, connect


def insert_and_commit(rows_list, name_table, curs, connect):
    curs.executemany("""INSERT INTO """+name_table+""" VALUES(?, ?)""", rows_list)
    connect.commit()


def print_summary(curs, name_table, connect):
    print("{} records inserted".format(curs.rowcount))
    curs.execute("select count(*) from "+name_table)
    record = curs.fetchone()
    print("Total records are {}".format(record[0]))
    connect.close()


def check_file(args):
    return len(args) == 2 and os.path.exists(args[1])


if check_file(sys.argv):
    cursor, conn = create_table_and_get_cursor(path_to_db, name_of_table)
    rowsList = get_records_for_table(sys.argv[1])
    insert_and_commit(rowsList, name_of_table, cursor, conn)
    print_summary(cursor, name_of_table, conn)
else:
    print("Wrong command")