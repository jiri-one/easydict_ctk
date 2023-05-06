import sqlite3
from pathlib import Path

db_file = Path(__file__).parent.parent / "data/easydict.db"
raw_file = Path(__file__).parent.parent / "data/en-cs.txt"
print(db_file)
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# cursor.execute("""CREATE TABLE eng_cze
#                   (eng TEXT, cze TEXT, notes TEXT,
#                    special TEXT, author TEXT)
#                """)

def data_from_line(line):
    line_list = line.split("\t")
    return (line_list[0], line_list[0], line_list[0], line_list[0], str(line_list[4]).replace("\n", ""))

data = [] 
with open(raw_file) as file:
    for line in file:
        data.append(data_from_line(line))

cursor.executemany('INSERT INTO eng_cze VALUES (?,?,?,?,?)', data)
# save data
conn.commit()
