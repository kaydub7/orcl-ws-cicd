"""
Simple Python application to show CI/CD capabilities.
"""

import cx_Oracle
from bottle import Bottle, run

app = Bottle()


@app.route('/conn')
def conn():
    return str(connection.version)


@app.route('/addition/<salary>/<amount>')
def addition(salary, amount):
    return str(int(salary) + int(amount))


@app.route('/increment/<salary>/<percentage>')
def increment(salary, percentage):
    return str(int(salary) * (1 + int(percentage)/100))


@app.route('/decrease/<salary>/<amount>')
def decrease(salary, amount):
    return str(int(salary) - int(amount))


if __name__ == '__main__':
    DBUSER = 'hr'
    DBPASS = 'WWelcome##2018'
    DBHOST = 'DBCS_sjc1nw.sub02250147130.docvcn.oraclevcn.com'
    DBSERV = 'pdb01.sub02250147130.docvcn.oraclevcn.com'
    conn_string = DBUSER + '/' + DBPASS + '@//' + DBHOST + '/' + DBSERV
    connection = cx_Oracle.connect(conn_string)
    run(app, host='0.0.0.0', port=8080)
    connection.close()
