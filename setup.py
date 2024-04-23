import mysql.connector
from werkzeug.security import generate_password_hash

def create_tables():
    try:
        # Connect to the MySQL database
        conn = mysql.connector.connect(
            host='localhost',  # or your host
            user='root',  # your MySQL username
            password='root',  # your MySQL password
            database='MedicalData'  # your database name
        )
        cursor = conn.cursor()
        print('Opened database successfully')
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return

    # Users Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
                      UserID INT AUTO_INCREMENT PRIMARY KEY,
                      Username VARCHAR(255) NOT NULL UNIQUE,
                      Password VARCHAR(255) NOT NULL,
                      Role VARCHAR(255) NOT NULL,
                      ContactInfo TEXT
                      )''')
    print('Users table created')

    # Patient Profiles Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS PatientProfiles (
                      PatientID INT AUTO_INCREMENT PRIMARY KEY,
                      FullName VARCHAR(255) NOT NULL,
                      DOB DATE,
                      Gender VARCHAR(50),
                      Address TEXT,
                      MedicalHistoryID INT,
                      FOREIGN KEY (MedicalHistoryID) REFERENCES Users(UserID)
                      )''')
    print('PatientProfiles table created')

    # Doctor Profiles Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS DoctorProfiles (
                      DoctorID INT AUTO_INCREMENT PRIMARY KEY,
                      FullName VARCHAR(255) NOT NULL,
                      Specialty VARCHAR(255),
                      ContactInfo TEXT,
                      FOREIGN KEY (DoctorID) REFERENCES Users(UserID)
                      )''')
    print('DoctorProfiles table created')

    # Medical Histories Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS MedicalHistories (
                      MedicalHistoryID INT AUTO_INCREMENT PRIMARY KEY,
                      PatientID INT,
                      `Condition` TEXT,
                      DiagnosisDate DATE,
                      Treatment TEXT,
                      FOREIGN KEY (PatientID) REFERENCES PatientProfiles(PatientID)
                      )''')
    print('MedicalHistories table created')

    #Medical Documents Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS MedicalDocuments (
                      MedDocID INT AUTO_INCREMENT PRIMARY KEY,
                      PatientID INT,
                      DocName VARCHAR(64),
                      DocType VARCHAR(64),
                      UploadDate DATE,
                      FOREIGN KEY (PatientID) REFERENCES Users(UserID)
                      )''')
    print('MedicalDocuments table created.')

    # Appointments Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Appointments (
                      AppointmentID INT AUTO_INCREMENT PRIMARY KEY,
                      PatientID INT,
                      DoctorID INT,
                      AppointmentDate DATETIME,
                      Purpose TEXT,
                      Notes TEXT,
                      FOREIGN KEY (PatientID) REFERENCES PatientProfiles(PatientID),
                      FOREIGN KEY (DoctorID) REFERENCES DoctorProfiles(DoctorID)
                      )''')
    print('Appointments table created')

    # Prescriptions Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Prescriptions (
                      PrescriptionID INT AUTO_INCREMENT PRIMARY KEY,
                      AppointmentID INT,
                      Medication TEXT,
                      Dosage TEXT,
                      Duration TEXT,
                      Notes TEXT,
                      FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID)
                      )''')
    print('Prescriptions table created')

    # Access Logs Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS AccessLogs (
                      LogID INT AUTO_INCREMENT PRIMARY KEY,
                      UserID INT,
                      PatientID INT,
                      AccessTime DATETIME,
                      ActionType TEXT,
                      FOREIGN KEY (UserID) REFERENCES Users(UserID),
                      FOREIGN KEY (PatientID) REFERENCES PatientProfiles(PatientID)
                      )''')
    print('AccessLogs table created')

    # Medical Tests Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS MedicalTests (
                      TestID INT AUTO_INCREMENT PRIMARY KEY,
                      PatientID INT,
                      TestType TEXT,
                      OrderDate DATE,
                      ResultDate DATE,
                      ResultSummary TEXT,
                      FOREIGN KEY (PatientID) REFERENCES PatientProfiles(PatientID)
                      )''')
    print('MedicalTests table created')

    # Billing Information Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS BillingInformation (
                      BillingID INT AUTO_INCREMENT PRIMARY KEY,
                      PatientID INT,
                      AppointmentID INT,
                      AmountDue DECIMAL(10,2),
                      PaymentStatus TEXT,
                      PaymentDate DATE,
                      FOREIGN KEY (PatientID) REFERENCES PatientProfiles(PatientID),
                      FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID)
                      )''')
    print('BillingInformation table created')

    # Insurance Information Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS InsuranceInformation (
                      InsuranceID INT AUTO_INCREMENT PRIMARY KEY,
                      PatientID INT,
                      ProviderName TEXT,
                      PolicyNumber TEXT,
                      CoverageDetails TEXT,
                      FOREIGN KEY (PatientID) REFERENCES PatientProfiles(PatientID)
                      )''')
    print('InsuranceInformation table created')


    # Check for an existing admin account
    cursor.execute("SELECT * FROM Users WHERE Username='admin'")
    result = cursor.fetchone()
    if not result:
        # No admin user found, let's create one
        hashed_password = generate_password_hash('adminpassword')
        cursor.execute(
            "INSERT INTO Users (Username, Password, Role) VALUES (%s, %s, %s)",
            ('admin', hashed_password, 'administrator')
        )
        print('Admin account created')
    else:
        print('Admin account already exists')
    
    conn.commit()
    cursor.close()
    conn.close()
    print('Database setup complete')

if __name__ == "__main__":
    create_tables()
