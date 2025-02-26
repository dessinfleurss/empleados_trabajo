from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.db import get_db

bp = Blueprint('departments', __name__, url_prefix='/departments')

@bp.route('/')
def index():
    db = get_db()
    departments = db.execute(
        """SELECT department_name AS nombre, city AS ciudad, state_province AS provincia, country_name AS pais, department_id AS id FROM departments depa
        JOIN locations loca ON depa.location_id = loca.location_id
        JOIN countries p ON loca.country_id = p.country_id
        ORDER BY nombre"""
    ).fetchall()
    return render_template('depas/index.html', departments=departments)

@bp.route('/<int:id>/detalle')
def detalle(id):
    db = get_db()
    d = db.execute(
        """SELECT department_name AS nombre, city AS ciudad, state_province AS provincia, country_name AS pais FROM departments depa
        JOIN locations loca ON depa.location_id = loca.location_id
        JOIN countries p ON loca.country_id = p.country_id
        WHERE department_id = ?""", (id,)
    ).fetchone()
    return render_template('depas/detalle.html', d=d)