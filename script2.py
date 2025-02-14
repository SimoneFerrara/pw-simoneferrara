import sqlite3
import pandas as pd

dati = pd.read_excel("utenti.xlsx")

conn = sqlite3.connect("database_utenti.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS utenti (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome TEXT,
        Cognome TEXT,
        Email TEXT,
        Telefono TEXT
    )
""")

for _, row in dati.iterrows():
    cursor.execute("""
        INSERT INTO utenti (Nome, Cognome, Email, Telefono)
        VALUES (?, ?, ?, ?)
    """, (row['Nome'], row['Cognome'], row['Email'], row['Telefono']))

conn.commit()
conn.close()
print("Tabella SQL creata e popolata.")
