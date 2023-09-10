"""
# 주의사항 1. 각 파일 간의 함수, 혹은 로직을 공유하지 마세요
# 주의사항 2. 아래의 함수명을 바꾸지 마세요
# 위를 위반하면 채점이 제대로 되지 않아 0점 처리됩니다.

# 아래에서 pass를 지우고 로직을 작성하세요

아래 함수를 실행하면, employee 테이블에 과제에 제시된 레코드가 존재해야합니다.

Q2. 아래의 데이터를 넣는 쿼리를 작성해주세요.
첫 줄은 테이블의 컬럼명입니다.
두 번째 줄부터는 테이블의 데이터입니다.
테이블의 컬럼명과 데이터는 탭으로 구분되어 있습니다.


emp_id	gender	name	address	                    department	manager	age	position
A00001	Male	Moon	10-199, Gang-nam, Seoul	    1	        C00001	30	Senior engineer
B00100	Female	Sun	    587/8, Gwan-ak, Seoul	    2	        B00102	25	Associate marketer
A08771	Others	Peach	203-3, Guro, Seoul	        1	        C00001	26	Junior engineer
C00129	Male	Alex	20-331, Bundang, Gyonggi	3	        C00002	40	Director
C00001	Male	Lion	53-3, Namyang-ju, Gyonghi	1	        C00000	55	CTO
C00002	Others	Cindy	100, Jong-ro, Seoul	        3	        C00000	52	Director
B00102	Female	Ran	    290-10, Gwanghwamun, Seoul	2	        C00000	45	Director
C00000	Male	K	    1010, Sung-soo, Seoul		                    51	CEO

K의 department와 manager의 값은 빈 문자열('')이 아닌 null입니다, 빈 문자열을 넣을 경우 오답처리됩니다.

# DB Connection 정보는 수강할 때 썼던 정보와 정확히 같습니다.
# dbname: postgres
# host: localhost
# user: postgres
# password: postgres
"""


import psycopg2
# Connect to your postgres DB
conn = psycopg2.connect("host=localhost, dbname=postgres user=postgres password=postgres")
# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
def insert_employee_table(a, b, c, d, e, f, g, h):
    if f == 'null':
        cur.execute("insert into employee values ('%s','%s','%s','%s',%s,%s,%s,'%s'); " % (a, b, c, d, e, f, g, h))
    else:
        cur.execute("insert into employee values ('%s','%s','%s','%s',%s,'%s',%s,'%s'); " % (a, b, c, d, e, f, g, h))
    conn.commit()
    return

insert_employee_table('A00001', 'Male','Moon','10-199, Gang-nam, Seoul',1,'C00001',30,'Senior engineer')
insert_employee_table('B00100', 'Female','Sun','587/8, Gwan-ak, Seoul',2,'B00102',25,'Associate marketer')    
insert_employee_table('A08771', 'Others','Peach','203-3, Guro, Seoul',1,'C00001',26,'Junior engineer')
insert_employee_table('C00129', 'Male','Alex','20-331, Bundang, Gyonggi',3,'C00002',40,'Director')
insert_employee_table('C00001', 'Male','Lion','53-3, Namyang-ju, Gyonghi',1,'C00000',55,'CTO')
insert_employee_table('C00002', 'Others','Cindy','100, Jong-ro, Seoul',3,'C00000',52,'Director')
insert_employee_table('B00102', 'Female','Ran','290-10, Gwanghwamun, Seoul',2,'C00000',45,'Director')
insert_employee_table('C00000', 'Male','K','1010, Sung-soo, Seoul','null','null',51,'CEO')
