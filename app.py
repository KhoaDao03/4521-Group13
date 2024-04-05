from flask import Flask, render_template, flash, request, redirect, url_for
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "uploads/"
ALLOWED_EXTENSIONS = [".pdf"]

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 #16MB
app.secret_key = '_5#y2L"F4Q8z\n\xec]'

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
    return render_template('patientMedicalDocs.html')

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
        file.save(os.path.join(UPLOAD_FOLDER,secure_filename(file.filename)))
        return redirect('/')
    else:
        return redirect('/patientmedicaldocs')
        
    
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