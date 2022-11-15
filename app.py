import psycopg

with psycopg.connect("host=localhost dbname=postgres user=postgres password=postgres") as conn:

    with conn.cursor() as cur:

        cur.execute("""
            CREATE TABLE test (
                id serial PRIMARY KEY,
                num integer,
                data text)
            """)

        conn.commit()

if __name__ == "__main__":
    pass