# 주의사항 1. 각 파일 간의 함수, 혹은 로직을 공유하지 마세요
# 주의사항 2. test_로 시작하는 함수는 절대 변경하지 마세요
# 위를 위반하면 채점이 제대로 되지 않아 0점 처리됩니다.

# DB Connection 정보는 수강할 때 썼던 정보와 정확히 같습니다.
# dbname: postgres
# host: localhost
# user: postgres
# password: postgres

# 아래에서 pass를 지우고 로직을 작성하세요
# 아래 함수를 실행하면, Tuple list값을 반환해야합니다.
# 리턴 타입의 예는 아래와 같습니다.
# [("name1", 3, "A00107"), ("name2", 1, "B10730")]
def get_visitor_in_2022_07_11_09_00() -> list:
    pass




# 여기서부터는 절대 건들지 마세요
from tests.score.criteria import Q9Score
from tests.util.fixtures import *
from tests.homework.q4_insert_visitlog_table import create_visit_log_fixture
from tests.homework.q2_insert_employee_table import create_employee_table_fixture


def test_get_visitor_in_2022_07_11_09_00(drop_schema_if_exist, create_schema_if_not_exist,
                                         create_employee_table_fixture, create_visit_log_fixture,
                                         prepare_employees, prepare_visit_logs):
    actual = get_visitor_in_2022_07_11_09_00()
    Q9Score(actual).score()










def verify():
    pass