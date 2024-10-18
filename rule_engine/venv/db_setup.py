# db_setup.py
import sqlite3


def init_db():
    conn = sqlite3.connect('rules.db')
    c = conn.cursor()

    # Create table for storing rules
    c.execute('''
    CREATE TABLE IF NOT EXISTS rules (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        rule_string TEXT NOT NULL,
        ast TEXT
    )
    ''')

    conn.commit()
    conn.close()


def insert_rule(rule_string):
    conn = sqlite3.connect('rules.db')
    c = conn.cursor()
    c.execute("INSERT INTO rules (rule_string) VALUES (?)", (rule_string,))
    conn.commit()
    conn.close()
