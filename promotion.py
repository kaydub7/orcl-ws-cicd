"""
Simple Python application to show CI/CD capabilities.
"""


from bottle import Bottle, run

app = Bottle()
import cx_Oracle

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
    DBPASS = 'OraPTS#2020_' 
    DBHOST = '[DB System Public IP]'
    DBSERV = '[PDB_service_name]'
    conn_string = DBUSER + '/' + DBPASS + '@//' + DBHOST + '/' + DBSERV
    connection = cx_Oracle.connect(conn_string)
    run(app, host='0.0.0.0', port=8080)
    connection.close()
