import psycopg

with psycopg.connect("host=localhost dbname=postgres user=postgres password=postgres") as conn:
    with conn.cursor() as cur:
        cur.execute("""
                    select * from student
                """)
        fetch_size = 3
        need_fetch = True
        while need_fetch:
            partial_students = cur.fetchmany(fetch_size)
            if len(partial_students) < fetch_size:
                need_fetch = False
            print(partial_students)

    conn.commit()
if __name__ == "__main__":
    pass




