import mysql.connector

# function to connect to MySQL database
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='MedicalData'
    )

# create new appointment records in Appointments table
def create_appointment(patient_id, doctor_id, appointment_date, purpose, notes):
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = '''INSERT INTO Appointments (PatientID, DoctorID, AppointmentDate, Purpose, Notes)
             VALUES (%s, %s, %s, %s, %s)'''
    cursor.execute(sql, (patient_id, doctor_id, appointment_date, purpose, notes))
    conn.commit()

    cursor.close()
    conn.close()

# retrieve all records from Appointments table
def read_appointments():
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = 'SELECT * FROM Appointments'
    cursor.execute(sql)
    return cursor.fetchall()


# retrieve specific appointment records by AppointmentID from Appointments table
def read_appointment(appointment_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = 'SELECT * FROM Appointments WHERE AppointmentID = %s'
    cursor.execute(sql, (appointment_id,))
    return cursor.fetchone()


# update specific appointment record in Appointments table
def update_appointment(appointment_id, patient_id, doctor_id, appointment_date, purpose, notes):
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = '''UPDATE Appointments
             SET PatientID = %s, DoctorID = %s, AppointmentDate = %s, Purpose = %s, Notes = %s
             WHERE AppointmentID = %s'''
    cursor.execute(sql, (patient_id, doctor_id, appointment_date, purpose, notes, appointment_id))
    conn.commit()

    cursor.close()
    conn.close()            

# delete a specific appointment record from Appointments table
def delete_appointment(appointment_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = 'DELETE FROM Appointments WHERE AppointmentID = %s'
    cursor.execute(sql, (appointment_id,))
    conn.commit()

    cursor.close()
    conn.close()

# create a new prescription record in Prescriptions table
def create_prescription(appointment_id, medication, dosage, duration, notes):
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = '''INSERT INTO Prescriptions (AppointmentID, Medication, Dosage, Duration, Notes)
             VALUES (%s, %s, %s, %s, %s)'''
    cursor.execute(sql, (appointment_id, medication, dosage, duration, notes))
    conn.commit()

    cursor.close()
    conn.close()

# retrieve all records from Prescriptions table
def read_prescriptions():
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = 'SELECT * FROM Prescriptions'
    cursor.execute(sql)
    return cursor.fetchall()

# retrieve a specific prescription record by PrescriptionID from Prescriptions table
def read_prescription(prescription_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = 'SELECT * FROM Prescriptions WHERE PrescriptionID = %s'
    cursor.execute(sql, (prescription_id,))
    return cursor.fetchone()

# update a specific prescription record in Prescriptions table
def update_prescription(prescription_id, appointment_id, medication, dosage, duration, notes):
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = '''UPDATE Prescriptions
             SET AppointmentID = %s, Medication = %s, Dosage = %s, Duration = %s, Notes = %s
             WHERE PrescriptionID = %s'''
    cursor.execute(sql, (appointment_id, medication, dosage, duration, notes, prescription_id))
    conn.commit()

    cursor.close()
    conn.close()

# delete a specific prescription record from Prescriptions table
def delete_prescription(prescription_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = 'DELETE FROM Prescriptions WHERE PrescriptionID = %s'
    cursor.execute(sql, (prescription_id,))
    conn.commit()

    cursor.close()
    conn.close()


