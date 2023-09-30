import sqlite3

def create_tables(cr):
    cr.execute('''
        CREATE TABLE IF NOT EXISTS patient (
            id INTEGER PRIMARY KEY NOT NULL,
            full_name VARCHAR(255),
            date_of_birth DATE,
            contacts VARCHAR(255),
            doctors TEXT,
            prescriptions TEXT
    )
    ''')
    cr.execute('''
        CREATE TABLE IF NOT EXISTS employee (
            id INTEGER PRIMARY KEY NOT NULL,
            full_name VARCHAR(255),
            position VARCHAR(255),
            date_of_birth DATE,
            contacts VARCHAR(255),
            patients TEXT,
            prescriptions TEXT
            )
        ''')
    


    cr.execute('''
        CREATE TABLE IF NOT EXISTS visit (
            id INTEGER PRIMARY KEY NOT NULL,
            appointment_id INTEGER REFERENCES appointment(id),
            patient_id INTEGER REFERENCES patient(id),
            doctor_id INTEGER REFERENCES employee(id),
            diagnosis TEXT,
            prescription_id INTEGER REFERENCES prescription(id)
    )
    ''')

    cr.execute('''
        CREATE TABLE IF NOT EXISTS prescription (
            id INTEGER PRIMARY KEY NOT NULL,
            patient_id INTEGER REFERENCES patient(id),
            doctor_id INTEGER REFERENCES employee(id),
            medicine TEXT,
            visit_id INTEGER REFERENCES visit(id)
        )
    ''')

    cr.execute('''
        CREATE TABLE IF NOT EXISTS appointment (
            id INTEGER PRIMARY KEY NOT NULL,
            patient_id INTEGER REFERENCES patient(id),
            doctor_id INTEGER REFERENCES employee(id),
            datetime DATETIME,
            reason TEXT
        )
    ''')

with sqlite3.connect("hospital.db") as db:
    cr = db.cursor()
    create_tables(cr)
