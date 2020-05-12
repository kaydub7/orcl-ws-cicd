"""
Unit tests for simple Python application
"""

import promotion
import pytest
from webtest import TestApp
import cx_Oracle


class TestPromotion:

    def test_addition(self):
        assert '1200' == promotion.addition(1150, 50)

    def test_increment(self):
        assert '1250.0' == promotion.increment(1000, 25)

    def test_decrease(self):
        assert '970' == promotion.decrease(1150, 180)


@pytest.fixture
def application():
    test_app = TestApp(promotion.app)
    return test_app


def test_response_shold_be_ok(application):
    response = application.get('/addition/1000/200')
    assert response.status == "200 OK"


def test_addition(application):
    response = application.get('/addition/1000/200')
    assert b'1200' == response.body


@pytest.fixture(scope='session')
def test_connection():
    DBUSER = 'hr'
    DBPASS = 'WWelcome##2018'
    DBHOST = '168.138.38.174:1521'
    DBSERV = 'pdb01.sub05080509280.mwvcn.oraclevcn.com'
    conn_string = DBUSER + '/' + DBPASS + '@//' + DBHOST + '/' + DBSERV
    connection = cx_Oracle.connect(conn_string)
    response = connection.version
    assert response == '19.6.0.0.0'
    connection.close()
