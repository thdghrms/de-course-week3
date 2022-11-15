import psycopg


with psycopg.connect("host=localhost dbname=postgres user=postgres password=postgres") as conn:
    to_update = (32, "오선생")
    to_delete = ("구영호",)
    with conn.cursor() as cur:
        cur.execute(f"""
            UPDATE student set age=%s
            WHERE name=%s
        """, to_update)
        cur.execute(f"""
            DELETE FROM student
            WHERE name=%s
        """, to_delete)

    conn.commit()

if __name__ == "__main__":
    pass
