from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/doctorhome')
def doctorhome():
    return render_template('doctorhome.html')

@app.route('/doctorprofile')
def doctorprofile():
    return render_template('doctorprofile.html')

@app.route('/patientspage')
def patientspage():
    return render_template('patientspage.html')

@app.route('/doctorprescriptions')
def doctorprescriptions():
    return render_template('doctorprescriptions.html')

@app.route('/doctormedicaldocs')
def doctormedicaldocs():
    return render_template('doctormedicaldocs.html')

@app.route('/doctorappointments')
def doctorappointments():
    return render_template('doctorappointments.html')

@app.route('/patienthome')
def patienthome():
    return render_template('patienthome.html')

@app.route('/patientprofile')
def patientprofile():
    return render_template('patientprofile.html')

@app.route('/patientmedicaldocs')
def patientmedicaldocs():
    return render_template('patientmedicaldocs.html')

@app.route('/patientprescriptions')
def patientprescriptions():
    return render_template('patientprescriptions.html')

@app.route('/patientappointments')
def patientappointments():
    return render_template('patientappointments.html')

@app.route('/billing')
def billing():
    return render_template('billing.html')

@app.route('/doctorsearch')
def doctorsearch():
    return render_template('doctorsearch.html')

if __name__ == '__main__':
    app.run(debug=True)