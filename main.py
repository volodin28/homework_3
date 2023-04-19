import sqlite3

from flask import Flask, render_template

app = Flask(__name__)


def get_sec(time_str):
    """Get seconds from time."""
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


@app.route("/names")
def show_unique_names():
    con = sqlite3.connect("my_sqlite.db")
    cur = con.cursor()
    r = cur.execute("""SELECT COUNT(DISTINCT first_name) FROM customers""")
    count_names = f"Number of unique names {r.fetchone()[0]}"
    con.close()
    return render_template('index.html', content=count_names)


@app.route("/tracks")
def show_track_count():
    con = sqlite3.connect("my_sqlite.db")
    cur = con.cursor()
    r = cur.execute("""SELECT COUNT(track_name) FROM tracks""")
    count_names = f"Number of tracks {r.fetchone()[0]}"
    con.close()
    return render_template('index.html', content=count_names)


@app.route("/tracks-sec")
def show_track_duration():
    track_with_seconds = []
    con = sqlite3.connect("my_sqlite.db")
    cur = con.cursor()
    r = cur.execute("""SELECT * FROM tracks""")
    tracks = r.fetchall()
    for _ in tracks:
        track_with_seconds.append((_[0], get_sec(_[1])))
    con.close()
    return render_template('list.html', tracks=track_with_seconds)


if __name__ == '__main__':
    app.run(debug=True)
