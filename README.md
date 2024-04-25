# Healthcare Information Management System 4521-Group13
Group members: James Hugglestone, Trent Guillen, Nathan Wallen, Khoa Dao, Chris Canty.

## Description: 
The Healthcare Information Management System is a web application designed to make handling patient healthcare information simpler and more secure. It serves three main user roles: doctors, patients, and a database manager. Each user has their own profile, which can be accessed by both doctors and the patients themselves to manage health data effectively. The system focuses on security and uses techniques like Secure Computing along with Distributed Computing for other site operations. This ensures that patient records are both safe and easy to access, meeting the crucial need for privacy and efficiency in managing healthcare information.

## Instructions for the user interface that is beyond the obvious
This web application needs a local MySQL server running with:
username: root
password: root
database: medicaldata
If there is a local MySQL server running already/exists, go to ./.vscode/settings.json and change
database, username, password to match with the local MySQL.

These are preset users for admin, doctor, patient credentials

- To login as an admin:
username: admin
password: adminpassword
which allows the users to have admin privileges by granting access admin portal
from the admin portal, user can grant doctor privileges to other users

- To login as an doctor:
username: doctor
password: doctorpassword
which allow the doctors to access to doctor's dashboard with doctor's functionalities

- To login as an patient:
username: patient
password: patientpassword
which allow the doctors to access to doctor's dashboard with patient's functionalities


## Web application overview structure
![image](https://github.com/KhoaDao03/4521-Group13/assets/129322478/695ff1e6-b95a-471a-a3c9-178a568fc805)

## Websites overview
- addDoctor.html: A form for adding a new doctor to the database.
- adminHome.html: The dashboard for an admin user.
- billing.html: A page for handling billing information and transactions.
- doctorAppointments.html: An interface for view and managing doctor's appointments.
- doctorHome.html: The dashboard for a doctor user.
- doctorMedicalDocs.html: A repository or interface for accessing medical documents by doctors.
- doctorPrescriptions.html: A page for managing and issuing patient prescriptions.
- doctorProfile.html: A profile page for doctors.
- doctorSearch.html: A search function for finding doctors within the database.
- editDoctor.html: An interface for editing doctor's details.
- listDoctors.html: A list view of all doctors in the database.
- login.html: The login page for user authentication.
- patientAppointments.html: A page for patients to view their appointments.
- patientHome.html: The homepage or dashboard for a patient user.
- patientMedicalDocs.html: A page where patients can access their medical documents.
- patientPrescriptions.html: An interface where patients can view their prescriptions.
- patientProfile.html: A personal profile page for a patient.
- patientsPage.html: A listing and dashboard for patients.
- register.html: A registration page for new users to sign up.



## Libraries Used:
- MySQL: For database management.
- Flask: A micro web framework for Python, used to construct and manage the web application's server-side. It handles URL routing, HTTP requests, and the rendering of HTML templates.
    + render_template: Utilized to render HTML templates.
    + flash: Used to display flash messages to the user.
    + request: Handles requests data from clients (e.g., form data).
    + redirect, url_for: Assist in redirecting users to different endpoints within the application.
    + session: Manages user sessions throughout the web application.
- os: A standard Python library that provides functions to interact with the operating system. Used in this project for file path manipulation and environment variable access.
- werkzeug: A comprehensive WSGI web application library.
    + secure_filename: Ensures a secure filename for file uploads.
    + generate_password_hash, check_password_hash: Used for hashing passwords before storing them in the database, and checking hashed passwords during login, respectively.
- mysql.connector: A library that allows Python to connect to MySQL databases, enabling database operations such as queries, updates, and data manipulation.
- datetime: Provides classes for manipulating dates and times in both simple and complex ways. Used to manage date/time data, crucial for features like appointments and prescriptions.



## Work Separation
- James Hugglestone: Responsible for doctors page (CRUD), login and register page, ensure user data protection(secure programming) 
- Trent Guillen: Responsilbe for appointments, prescription pages (CRUD), distribution plan (distributed programming)
- Nathan Wallen: Responsible for file management functionality of the website (CRUD), web application structure
- Khoa Dao: Responsible for doctors page (CRUD operations), distribution plan (distributed programming)
- Chris Canty: Responsible for web application structure, distribution plan (distributed programming)