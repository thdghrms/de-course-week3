import psycopg
import sys

# ID: troll
# Password: troll'); drop table users; --
def input():
    print("가입 ID: ")
    uid = sys.stdin.readline().strip()
    print("사용할 비밀번호: ")
    password = sys.stdin.readline().strip()
    return uid, password


# SQL injection
with psycopg.connect("host=localhost dbname=postgres user=postgres password=postgres") as conn:
    new_joiner = input()
    with conn.cursor() as cur:
        # Password: troll'); drop table users; --
        # INSERT INTO users values('troll', 'troll'); drop table users; --'
        # query = f"INSERT INTO users values('{new_joiner[0]}', '{new_joiner[1]}')"
        # cur.execute(query)
        query = f"INSERT INTO users values(%s, %s)"
        cur.execute(query, new_joiner)

    conn.commit()

if __name__ == "__main__":
    pass