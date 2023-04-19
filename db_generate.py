import sqlite3

from faker import Faker

fake = Faker()


def create_fake_tracks(num):
    fake_track = []
    for _ in range(num):
        track.append((fake.paragraph(nb_sentences=1), fake.time()))
    return fake_track


def create_fake_names(num):
    name = []
    for _ in range(num):
        name.append(fake.first_name())
    return name


con = sqlite3.connect("my_sqlite.db")
cur = con.cursor()
cur.execute("""CREATE TABLE if not exists customers(first_name)""")

for first_name in create_fake_names(10):
    cur.execute("INSERT INTO customers(first_name) VALUES(?)", (first_name,))
    con.commit()


# cur.execute("SELECT * FROM customers")
# rows = cur.fetchall()
# for row in rows:
#     print(row)


cur.execute("""CREATE TABLE if not exists tracks(track_name, duration)""")

for track in create_fake_tracks(10):
    cur.execute("INSERT INTO tracks(track_name, duration) VALUES(?,?)", (track[0], track[1]))
    con.commit()

# cur.execute("SELECT * FROM tracks")
# rows = cur.fetchall()
# for row in rows:
#     print(row)

con.close()
