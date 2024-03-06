from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.db import get_db

bp = Blueprint('jobs', __name__, url_prefix='/jobs')

@bp.route('/')
def index():
    db = get_db()
    jobs = db.execute(
        """SELECT job_title AS trabajo,min_salary AS salario_minimo, max_salary AS salario_maximo FROM jobs"""
    ).fetchall()
    return render_template('trabajos/index.html', jobs=jobs)