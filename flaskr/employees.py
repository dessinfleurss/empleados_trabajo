from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.db import get_db

bp = Blueprint('employees', __name__, url_prefix='/employees')

@bp.route('/')
def index():
    db = get_db()
    employees = db.execute(
        """SELECT first_name AS nombre, last_name AS apellido, department_name AS departamento
        FROM employees empleados
	    JOIN departments depa ON empleados.department_id = depa.department_id
	    ORDER BY nombre ASC"""
    ).fetchall()
    return render_template('employee/index.html', employees=employees)