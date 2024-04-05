from flask import Flask, render_template, redirect, url_for, request
from PresAndAppo import read_appointments, read_prescriptions, create_appointment, create_prescription

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/doctorhome')
def doctorhome():
    return render_template('doctorHome.html')

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
    return render_template('patientProfile.html')

@app.route('/patientmedicaldocs')
def patientmedicaldocs():
    return render_template('patientMedicalFocs.html')

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

@app.route('/doctorsearch')
def doctorsearch():
    return render_template('doctorSearch.html')

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

if __name__ == '__main__':
    app.run(debug=True)