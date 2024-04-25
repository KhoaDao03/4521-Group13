# Healthcare Information Management System 4521-Group13
Group members: James Hugglestone, Trent Guillen, Nathan Wallen, Khoa Dao, Chris Canty.

## Description: 
The Healthcare Information Management System is a web application designed to make handling patient healthcare information simpler and more secure. It serves three main user roles: doctors, patients, and a database manager. Each user has their own profile, which can be accessed by both doctors and the patients themselves to manage health data effectively. The system focuses on security and uses techniques like Secure Computing along with Distributed Computing for other site operations. This ensures that patient records are both safe and easy to access, meeting the crucial need for privacy and efficiency in managing healthcare information.

## Instructions for the user interface that is beyond the obvious
To login as an admin:
username: admin
password: adminpassword
which allows the users to have admin privileges by granting access admin portal


## Website application overview structure
![image](https://github.com/KhoaDao03/4521-Group13/assets/129322478/695ff1e6-b95a-471a-a3c9-178a568fc805)

## Libraries Used:
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
James Hugglestone: Responsible for doctors page (CRUD), admin page, login and register page, ensure user data protection(secure programming) 
Trent Guillen: Responsilbe for appointments, prescription pages (CRUD), distribution plan (distributed programming)
Nathan Wallen: Responsible for file management functionality of the website (CRUD), website application structure
Khoa Dao: Responsible for doctors page (CRUD operations), distribution plan (distributed programming)
Chris Canty: Responsible for website application structure, distribution plan (distributed programming)
