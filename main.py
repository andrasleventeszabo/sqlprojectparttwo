from flask import Flask, request, redirect, render_template
import sql_queries
from headers import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main_page():
    return render_template('mainpage.html')


@app.route('/mentors')
def mentors_page():
    results = sql_queries.mentors_and_schools()
    return render_template('results.html', results=results, 
                           table_headers=MENTORS_PAGE)


@app.route('/all-school')
def allschool():
    results = sql_queries.all_school()
    return render_template('results.html', results=results,
                           table_headers=MENTORS_PAGE)


@app.route('/mentors-by-country')
def mentors_country():
    results = sql_queries.mentors_by_contry()
    return render_template('results.html', results=results,
                           table_headers=MENTORS_BY_COUNTRY)


@app.route('/contacts')
def mentors_contacts():
    results = sql_queries.contacts()
    return render_template('results.html', results=results,
                           table_headers=MENTORS_CONTACTS)


@app.route('/applicants')
def applicants_contacts():
    results = sql_queries.applicants()
    return render_template('results.html', results=results,
                           table_headers=APPLICANTS_CONTACTS)


@app.route('/applicants-and-mentors')
def applicants_mentors():
    results = sql_queries.mentors_and_applicants()
    return render_template('results.html', results=results,
                           table_headers=APPLICANTS_AND_MENTORS)


if __name__ == '__main__':
    app.run(debug=True)