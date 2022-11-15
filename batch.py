import psycopg
import datetime


def batch_insert_test(conn, cur):
    data = [(i, f"{i} 번째", f"안녕 {i}", f"잘가 {i}") for i in range(0, 3000)]

    current = datetime.datetime.now()
    for d in data:
        cur.execute("INSERT INTO perf_test values(%s, %s, %s, %s)", d)
    conn.commit()
    elapsed = datetime.datetime.now() - current
    print(f"One by one approach took {elapsed}")

    # Table clean up
    cur.execute("TRUNCATE perf_test")
    conn.commit()

    current = datetime.datetime.now()
    cur.executemany("INSERT INTO perf_test values(%s, %s, %s, %s)", data)
    conn.commit()
    elapsed = datetime.datetime.now() - current
    print(f"Batch approach took {elapsed}")


with psycopg.connect("host=localhost dbname=postgres user=postgres password=postgres") as conn:
    with conn.cursor() as cur:
        batch_insert_test(conn, cur)

    conn.commit()

if __name__ == "__main__":
    pass