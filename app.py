from flask import Flask, render_template, flash, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash
from PresAndAppo import read_appointments, read_prescriptions, create_appointment, create_prescription

import mysql.connector
import datetime

UPLOAD_FOLDER = "uploads/"
ALLOWED_EXTENSIONS = ["pdf"]
CURRENT_USERID = 1  ####This is to be removed when we get proper login and can hold the users ID that way

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 #16MB
app.secret_key = '_5#y2L"F4Q8z\n\xec]'

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

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']
        contact_info = ""  # Assuming you might want to add this later

        # Check if user already exists
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Users WHERE Username = %s", (username,))
        if cursor.fetchone():
            flash('Username already exists. Please choose another one.', 'error')
            return redirect(url_for('register'))
        
        # Hash the password for security
        hashed_password = generate_password_hash(password)
        
        # Insert the new user into the Users table
        cursor.execute("INSERT INTO Users (Username, Password, Role, ContactInfo) VALUES (%s, %s, %s, %s)",
                       (username, hashed_password, role, contact_info))
        conn.commit()
        cursor.close()
        conn.close()

        flash('Registration successful. Please login.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

# @app.route('/login', methods = ['GET','POST'])
# def login():
#     msg = ""
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         conn = get_db_connection()
#         cursor = conn.cursor(dictionary=True)
#         cursor.execute('SELECT * FROM users WHERE Username = %s AND Password =%s', (username, password))
#         record = cursor.fetchone()
#         if record:
#             return
#         return

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
        username = request.form['username']
        fullname = request.form['fullname']
        specialty = request.form['specialty']
        contact_info = request.form['contactinfo']
        conn = get_db_connection()
        cursor = conn.cursor()

        # Check if user exists and is a doctor
        cursor.execute("SELECT UserID FROM Users WHERE Username = %s AND Role = 'doctor'", (username,))
        user = cursor.fetchone()

        if user is None:
            cursor.close()
            conn.close()
            return redirect(url_for('register'))

        # Insert new doctor profile using the UserID from Users table
        user_id = user[0]
        cursor.execute('INSERT INTO DoctorProfiles (DoctorID, FullName, Specialty, ContactInfo) VALUES (%s, %s, %s, %s)',
                       (user_id, fullname, specialty, contact_info))
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
    prescriptions = read_prescriptions()
    return render_template('doctorPrescriptions.html', prescriptions=prescriptions)

@app.route('/doctormedicaldocs')
def doctormedicaldocs():
    return render_template('doctorMedicalDocs.html')

@app.route('/doctorappointments')
def doctorappointments():
    appointments = read_appointments()
    return render_template('doctorAppointments.html', appointments=appointments)

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
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM MedicalDocuments WHERE PatientID = %s', (CURRENT_USERID,))
    udocs = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('patientMedicalDocs.html', meddocs = udocs)

@app.route('/patientprescriptions')
def patientprescriptions():
    prescriptions = read_prescriptions()
    return render_template('patientPrescriptions.html', prescriptions=prescriptions)

@app.route('/patientappointments')
def patientappointments():
    appointments = read_appointments()
    return render_template('patientAppointments.html', appointments=appointments)

@app.route('/billing')
def billing():
    return render_template('billing.html')

@app.route('/doctorsearch', methods=['GET', 'POST'])
def doctorsearch():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    search_query = request.form.get('search_query', '')

    if request.method == 'POST' and search_query:
        cursor.execute("SELECT * FROM DoctorProfiles WHERE FullName LIKE %s", (f"%{search_query}%",))
    else:
        cursor.execute("SELECT * FROM DoctorProfiles")

    doctors = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('doctorSearch.html', doctors=doctors, search_query=search_query)




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


@app.route('/add_doctor_appointment', methods=['POST'])
def add_doctor_appointment():
    if request.method == 'POST':
        patient_id = request.form['patient_id']
        doctor_id = request.form['doctor_id']
        appointment_date = request.form['appointment_date']
        purpose = request.form['purpose']
        notes = request.form['notes']

        create_appointment(patient_id, doctor_id, appointment_date, purpose, notes)
        
        return redirect(url_for('doctorappointments'))
    
@app.route('/add_doctor_prescription', methods=['POST'])
def add_doctor_prescriptions():
    if request.method == 'POST':
        appointment_id = request.form['appointment_id']
        medication = request.form['medication']
        dosage = request.form['dosage']
        duration = request.form['duration']
        notes = request.form['notes']

        create_prescription(appointment_id, medication, dosage, duration, notes)

        return redirect(url_for('doctorprescriptions'))

@app.route('/uploadfile', methods = ['POST'])
def uploadfile():
    file = request.files['file']
    
    if file and allowed_file(file.filename):
        ##Get Patient Id Here
        userid = CURRENT_USERID
        docname = secure_filename(file.filename)
        doctype = "Medical Document"
        current_day = datetime.date
        uploaddate = (current_day.today())
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('INSERT INTO MedicalDocuments (PatientID, DocName, DocType, UploadDate) VALUES (%s,%s,%s,%s)',
                       (userid, docname, doctype, uploaddate))
        conn.commit()
        cursor.close()
        conn.close()
        file.save(os.path.join(UPLOAD_FOLDER,docname))
        return redirect('/')
    else:
        return redirect('/patientmedicaldocs')

@app.route('/list_docs', methods = ['POST'])  
def list_docs():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM MedicalDocuments')
    docs = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('doctorMedicalDocs.html', meddocs = docs)
    
# @app.route('/fileupload', methods = ['GET', 'POST'])
# def uploadfile():   
#     if request.method == 'POST':
#         if 'file' not in request.files:
#             flash('No file part')
#             return redirect(request.url)
#     file = request.files['file']
#     if file.filename == '':
#         flash("No file selected")
#         return redirect(request.url)
#     if file and allowed_file(file.filename):
#         filename = secure_filename(file.filename)
#         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#         return redirect(url_for('download_file'), name = filename)
#     return render_template('patientmedicaldocs.html')

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(debug=True)
