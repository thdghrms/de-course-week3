import pytest
import logging
from tests.util.dbutil import *
from tests.data.all_data import *
import base64


@pytest.fixture
def drop_schema_if_exist():
    logging.info("DROP schema public")
    execute_sql(f"drop schema if exists public CASCADE")


@pytest.fixture
def create_schema_if_not_exist():
    logging.info("Create schema")
    execute_sql(f"create schema if not exists public")

@pytest.fixture
def prepare_employees():
    for e in ALL_EMPLOYEE:
        execute_sql(base64.b64decode("SU5TRVJUIElOVE8gZW1wbG95ZWUgdmFsdWVzKCVzLCAlcywgJXMsICVzLCAlcywgJXMsICVz"
                                        + "LCAlcyk="), e)
@pytest.fixture
def prepare_visit_logs():
    for v in ALL_VISIT_LOG:
        execute_sql(base64.b64decode("SU5TRVJUIElOVE8gdmlzaXRfbG9nIHZhbHVlcyglcywgJXMsICVzLCAlcyk="), v)
