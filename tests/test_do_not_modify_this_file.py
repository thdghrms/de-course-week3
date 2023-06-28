from tests.score.criteria import *
from tests.util.fixtures import *
from tests.homework.q1_create_employee_table import create_employee_table
from tests.homework.q2_insert_employee_table import insert_employee_table
from tests.homework.q3_create_visit_log import create_visit_log_table
from tests.homework.q4_insert_visitlog_table import insert_visit_log_table
from tests.homework.q5_employee_female import find_employee_female_table
from tests.homework.q6_employee_male import find_employee_male_table
from tests.homework.q7_visit_log_cnt import get_total_visit_in_2022_07_12
from tests.homework.q8_visit_log_group_by_purpose_cnt import get_total_visit_by_purpose
from tests.homework.q9_find_visit_employee import get_visitor_in_2022_07_11_09_00
from tests.homework.q10_update_peach_position import update_peach_position
from tests.homework.q11_delete_null_visit import delete_null_visit


"""
이 파일은 채점을 위한 파일입니다. 수정하지 마세요.
"""
@pytest.fixture
def create_employee_table_fixture():
    create_employee_table()


@pytest.fixture
def create_visit_log_fixture():
    create_visit_log_table()


def test_create_employee_table(drop_schema_if_exist, create_schema_if_not_exist):
    create_employee_table()
    Q1Score().score()


def test_create_employees(drop_schema_if_exist, create_schema_if_not_exist, create_employee_table_fixture):
    insert_employee_table()
    Q2Score().score()


def test_create_visit_log_table(drop_schema_if_exist, create_schema_if_not_exist):
    create_visit_log_table()
    Q3Score().score()


def test_create_visit_logs(drop_schema_if_exist, create_schema_if_not_exist, create_visit_log_fixture):
    insert_visit_log_table()
    Q4Score().score()


def test_female_employee(drop_schema_if_exist, create_schema_if_not_exist, create_employee_table_fixture,
                                    prepare_employees):
    actual = find_employee_female_table()
    Q5Score(actual).score()


def test_male_employee(drop_schema_if_exist, create_schema_if_not_exist, create_employee_table_fixture,
                                  prepare_employees):
    actual = find_employee_male_table()
    Q6Score(actual).score()


def test_cnt_visit_log(drop_schema_if_exist, create_schema_if_not_exist, create_visit_log_fixture,
                                    prepare_visit_logs):
    actual = get_total_visit_in_2022_07_12()
    Q7Score(actual).score()


def test_group_by_visit_log_purpose(drop_schema_if_exist, create_schema_if_not_exist, create_visit_log_fixture,
                                    prepare_visit_logs):
    actual = get_total_visit_by_purpose()
    Q8Score(actual).score()


def test_find_visit_employee(drop_schema_if_exist, create_schema_if_not_exist,
                                         create_employee_table_fixture, create_visit_log_fixture,
                                         prepare_employees, prepare_visit_logs):
    actual = get_visitor_in_2022_07_11_09_00()
    Q9Score(actual).score()


def test_update_peach_position(drop_schema_if_exist, create_schema_if_not_exist, create_employee_table_fixture,
                                    prepare_employees):
    update_peach_position()
    Q10Score().score()


def test_delete_null_visit(drop_schema_if_exist, create_schema_if_not_exist, create_visit_log_fixture,
                           prepare_visit_logs):
    delete_null_visit()
    Q11Score().score()