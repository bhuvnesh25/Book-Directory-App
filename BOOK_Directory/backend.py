
import sqlite3


def database():
    """Set up a connection with the database."""
    con = sqlite3.connect("Library.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Library (id integer PRIMARY KEY, title text, author text, year integer, isbn integer,language text,placed text)")
    con.commit()
    con.close()

def account():
    """Set up a connection with the database."""
    con = sqlite3.connect("Account.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Account (id integer PRIMARY KEY, name text, department text, roll_no integer, mobile integer,books text,isbn integer,date text,email text)")
    con.commit()
    con.close()

def login():
    """Set up a connection with the database."""
    con = sqlite3.connect("Login.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS member (id integer PRIMARY KEY, Username text, Password text)")
    con.commit()
    con.close()


def add(title, author, year, isbn,lang,placed):
    """Insert entry into database."""
    con = sqlite3.connect("Library.db")
    cur = con.cursor()
    cur.execute("INSERT INTO Library VALUES (NULL, ?, ?, ?, ?, ?, ?)", (title, author, year, isbn,lang,placed))
    con.commit()
    con.close()







def stu(name, department, roll_no, mobile,books,isbn,date,email):
    """Insert entry into database."""
    con = sqlite3.connect("Account.db")
    cur = con.cursor()
    cur.execute("INSERT INTO Account VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)", (name, department, roll_no, mobile,books,isbn,date,email))
    con.commit()
    con.close()

def view_all():
    """View all database entries."""
    con = sqlite3.connect("Library.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Library")
    rows = cur.fetchall()
    con.close()
    return rows





def view():
    """View all database entries."""
    con = sqlite3.connect("Account.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Account")
    rows = cur.fetchall()
    con.close()
    return rows


def update(id, title, author, year, isbn,lang,placed):
    """Update a database entry."""
    con = sqlite3.connect("Library.db")
    cur = con.cursor()
    cur.execute("UPDATE Library SET title = ?,author = ?,year = ?, isbn = ? ,language = ? ,placed = ? WHERE id = ?",(title, author, year, isbn, lang, placed, id))
    con.commit()
    con.close()


def delete(id):
    """Delete a database entry."""
    con = sqlite3.connect("Library.db")
    cur = con.cursor()
    cur.execute("DELETE FROM Library WHERE id = ?",(id,))
    con.commit()
    con.close()

def dele(isbn):
    """Delete a database entry."""
    con = sqlite3.connect("Library.db")
    cur = con.cursor()
    cur.execute("DELETE FROM Library WHERE isbn = ?",(isbn,))
    con.commit()
    con.close()

def de(id):
    """Delete a database entry."""
    con = sqlite3.connect("Account.db")
    cur = con.cursor()
    cur.execute("DELETE FROM Account WHERE id =? ",(id,))
    con.commit()
    con.close()

def search(title="", lang=""):
    """Search for a database entry."""
    con = sqlite3.connect("Library.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Library WHERE title = ?  OR  language = ? ", (title, lang))
    rows = cur.fetchall()
    con.close()
    return rows

def check(user_name,password):


        con = sqlite3.connect("Login.db")
        cur = con.cursor()

        cur.execute("SELECT * FROM member WHERE Username = ? AND Password = ? ",(user_name,password))
        if cur.fetchone() is None:

            con.commit()
            return 1


database()
account()
