import psycopg2
import os


def connect_to_database(func):

    def wrapper(*args, **kwargs):
        try:
            global cursor
            connect_str = "dbname='sm_andris' user='sm_andris' host='localhost' password='busmann77'"
            conn = psycopg2.connect(connect_str)
            conn.autocommit = True
            cursor = conn.cursor()
            result = func(*args, **kwargs)
            cursor.close()
            conn.close()
            return result

        except Exception as exc:
            error_message = "Cannot connect to the database. Incorrect username or password. \n" + str(exc)
            return error_message

    return wrapper


@connect_to_database
def mentors_and_schools():
    cursor.execute(""" SELECT CONCAT_WS(' ', mentors.last_name, mentors.first_name) AS full_name,
                       schools.name, schools.country
                       FROM mentors
                       INNER JOIN schools ON mentors.city = schools.city
                       ORDER BY mentors.id; """)
    results = cursor.fetchall()
    return results 


@connect_to_database
def all_school():
    cursor.execute("""SELECT CONCAT_WS(' ', mentors.last_name, mentors.first_name) AS full_name,
                       schools.name, schools.country
                       FROM mentors INNER JOIN schools
                       ON mentors.city = schools.city
                       ORDER BY mentors.id; """)
    results = cursor.fetchall()
    return results


@connect_to_database
def mentors_by_contry():
    cursor.execute(""" SELECT COUNT(mentors.id) AS count, schools.country
                       FROM mentors
                       RIGHT JOIN schools ON mentors.id=schools.contact_person
                       GROUP BY schools.country ORDER BY schools.country; """)
    results = cursor.fetchall()
    return results


@connect_to_database
def contacts():
    cursor.execute(""" SELECT schools.name, CONCAT_WS(' ', mentors.first_name, mentors.last_name)
                       AS full_name
                       FROM schools
                       INNER JOIN mentors ON mentors.id=schools.contact_person
                       ORDER BY schools.name; """)
    results = cursor.fetchall()
    return results


@connect_to_database
def applicants():
    cursor.execute(""" SELECT applicants.first_name, applicants.application_code,
                       applicants_mentors.creation_date
                       FROM applicants INNER JOIN applicants_mentors
                       ON applicants.id = applicants_mentors.applicant_id
                       WHERE applicants_mentors.creation_date > '2016-01-01'
                       ORDER BY applicants_mentors.creation_date ASC; """)
    results = cursor.fetchall()
    return results


@connect_to_database
def mentors_and_applicants():
    cursor.execute(""" SELECT applicants.first_name, applicants.application_code,
                       CONCAT_WS(' ', mentors_last_name, mentors_first_name)
                       AS full_name
                       FROM applicants
                       LEFT JOIN applicants_mentors
                       ON applicants.id = applicants_mentors.applicant_id
                       LEFT JOIN mentors
                       ON applicants_mentors.mentor_id = mentors.id
                       ORDER BY applicants.id; """)
    results = cursor.fetchall()
    return results
