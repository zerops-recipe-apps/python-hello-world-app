import os
import psycopg2

conn = psycopg2.connect(
    host=os.environ["DB_HOST"],
    port=int(os.environ["DB_PORT"]),
    user=os.environ["DB_USER"],
    password=os.environ["DB_PASS"],
    dbname=os.environ["DB_NAME"],
)

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS greetings (
        id      INTEGER PRIMARY KEY,
        message TEXT    NOT NULL
    )
""")

cur.execute("""
    INSERT INTO greetings (id, message)
    VALUES (1, 'Hello from Zerops!')
    ON CONFLICT (id) DO NOTHING
""")

conn.commit()
cur.close()
conn.close()

print("Migration complete.")
