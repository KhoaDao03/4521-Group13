from flask import Flask, request, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='MedicalData'
    )

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/doctorhome')
def doctor_home():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM DoctorProfiles')
    doctors = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('doctorHome.html', doctors=doctors)

@app.route('/adddoctor', methods=('GET', 'POST'))
def add_doctor():
    if request.method == 'POST':
        fullname = request.form['fullname']
        specialty = request.form['specialty']
        contact_info = request.form['contactinfo']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO DoctorProfiles (FullName, Specialty, ContactInfo) VALUES (%s, %s, %s)',
                       (fullname, specialty, contact_info))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('doctor_home'))
    return render_template('addDoctor.html')

@app.route('/editdoctor/<int:id>', methods=('GET', 'POST'))
def edit_doctor(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    if request.method == 'POST':
        fullname = request.form['fullname']
        specialty = request.form['specialty']
        contact_info = request.form['contactinfo']
        cursor.execute('UPDATE DoctorProfiles SET FullName = %s, Specialty = %s, ContactInfo = %s WHERE DoctorID = %s',
                       (fullname, specialty, contact_info, id))
        conn.commit()
        return redirect(url_for('doctor_home'))

    cursor.execute('SELECT * FROM DoctorProfiles WHERE DoctorID = %s', (id,))
    doctor = cursor.fetchone()
    return render_template('editDoctor.html', doctor=doctor)

@app.route('/deletedoctor/<int:id>', methods=('POST',))
def delete_doctor(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM DoctorProfiles WHERE DoctorID = %s', (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('doctor_home'))

@app.route('/listdoctors')
def list_doctors():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM DoctorProfiles')
    doctors = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('listDoctors.html', doctors=doctors)

@app.route('/doctorprofile')
def doctorprofile():
    return render_template('doctorProfile.html')

@app.route('/patientspage')
def patientspage():
    return render_template('patientsPage.html')

@app.route('/doctorprescriptions')
def doctorprescriptions():
    return render_template('doctorPrescriptions.html')

@app.route('/doctormedicaldocs')
def doctormedicaldocs():
    return render_template('doctorMedicalDocs.html')

@app.route('/doctorappointments')
def doctorappointments():
    return render_template('doctorAppointments.html')

@app.route('/patienthome')
def patienthome():
    return render_template('patientHome.html')

@app.route('/patientprofile')
def patientprofile():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM PatientProfiles")
    profiles = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('patientProfile.html', patient_profiles=profiles)

@app.route('/patientmedicaldocs')
def patientmedicaldocs():
    return render_template('patientMedicalFocs.html')

@app.route('/patientprescriptions')
def patientprescriptions():
    return render_template('patientPrescriptions.html')

@app.route('/patientappointments')
def patientappointments():
    return render_template('patientAppointments.html')

@app.route('/billing')
def billing():
    return render_template('billing.html')

@app.route('/doctorsearch')
def doctorsearch():
    return render_template('doctorSearch.html')


@app.route('/addPatient', methods=['POST'])
def add_patient():
    if request.method == 'POST':
        fullname = request.form['FullName']
        dob = request.form['DOB']
        gender = request.form['Gender']
        address = request.form['Address']
        medicalhistoryid = request.form['MedicalHistoryID']
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)   
        cursor.execute("INSERT INTO PatientProfiles (FullName, DOB, Gender, Address, MedicalHistoryID) VALUES (%s, %s, %s, %s, %s)", (fullname, dob, gender, address, medicalhistoryid))
        conn.commit()
        #Flask('Patient Profile Added Successfully')
        return render_template('patientProfile.html')


@app.route('/delete/<int:patient_id>', methods=['POST'])
def delete_patient(patient_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM PatientProfiles WHERE PatientID = %s", (patient_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return patientprofile()


if __name__ == '__main__':
    app.run(debug=True)
