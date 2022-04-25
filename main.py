from flask import Blueprint, render_template
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('Index.html')

@main.route('/profile')
def profile():
    return render_template('Profile.html')