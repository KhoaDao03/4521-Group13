from flask import Flask, render_template, flash, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
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

@app.route('/register')
def register():
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
    return render_template('patientProfile.html')

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
