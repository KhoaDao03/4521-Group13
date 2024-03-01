import sqlite3

def create_tables():
    conn = sqlite3.connect('MedicalData.db')
    print('Opened database successfully')

    # Users Table
    conn.execute('''CREATE TABLE IF NOT EXISTS Users (
                    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Username TEXT NOT NULL UNIQUE,
                    Password TEXT NOT NULL,
                    Role TEXT NOT NULL,
                    ContactInfo TEXT
                    )''')
    print('Users table created')

    # Patient Profiles Table
    conn.execute('''CREATE TABLE IF NOT EXISTS PatientProfiles (
                    PatientID INTEGER PRIMARY KEY,
                    FullName TEXT NOT NULL,
                    DOB DATE,
                    Gender TEXT,
                    Address TEXT,
                    MedicalHistoryID INTEGER,
                    FOREIGN KEY (PatientID) REFERENCES Users(UserID)
                    )''')
    print('PatientProfiles table created')

    # Doctor Profiles Table
    conn.execute('''CREATE TABLE IF NOT EXISTS DoctorProfiles (
                    DoctorID INTEGER PRIMARY KEY,
                    FullName TEXT NOT NULL,
                    Specialty TEXT,
                    ContactInfo TEXT,
                    FOREIGN KEY (DoctorID) REFERENCES Users(UserID)
                    )''')
    print('DoctorProfiles table created')

    # Medical Histories Table
    conn.execute('''CREATE TABLE IF NOT EXISTS MedicalHistories (
                    MedicalHistoryID INTEGER PRIMARY KEY AUTOINCREMENT,
                    PatientID INTEGER,
                    Condition TEXT,
                    DiagnosisDate DATE,
                    Treatment TEXT,
                    FOREIGN KEY (PatientID) REFERENCES PatientProfiles(PatientID)
                    )''')
    print('MedicalHistories table created')

    # Appointments Table
    conn.execute('''CREATE TABLE IF NOT EXISTS Appointments (
                    AppointmentID INTEGER PRIMARY KEY AUTOINCREMENT,
                    PatientID INTEGER,
                    DoctorID INTEGER,
                    AppointmentDate DATETIME,
                    Purpose TEXT,
                    Notes TEXT,
                    FOREIGN KEY (PatientID) REFERENCES PatientProfiles(PatientID),
                    FOREIGN KEY (DoctorID) REFERENCES DoctorProfiles(DoctorID)
                    )''')
    print('Appointments table created')

    # Prescriptions Table
    conn.execute('''CREATE TABLE IF NOT EXISTS Prescriptions (
                    PrescriptionID INTEGER PRIMARY KEY AUTOINCREMENT,
                    AppointmentID INTEGER,
                    Medication TEXT,
                    Dosage TEXT,
                    Duration TEXT,
                    Notes TEXT,
                    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID)
                    )''')
    print('Prescriptions table created')

    # Access Logs Table
    conn.execute('''CREATE TABLE IF NOT EXISTS AccessLogs (
                    LogID INTEGER PRIMARY KEY AUTOINCREMENT,
                    UserID INTEGER,
                    PatientID INTEGER,
                    AccessTime DATETIME,
                    ActionType TEXT,
                    FOREIGN KEY (UserID) REFERENCES Users(UserID),
                    FOREIGN KEY (PatientID) REFERENCES PatientProfiles(PatientID)
                    )''')
    print('AccessLogs table created')

    # Medical Tests Table
    conn.execute('''CREATE TABLE IF NOT EXISTS MedicalTests (
                    TestID INTEGER PRIMARY KEY AUTOINCREMENT,
                    PatientID INTEGER,
                    TestType TEXT,
                    OrderDate DATE,
                    ResultDate DATE,
                    ResultSummary TEXT,
                    FOREIGN KEY (PatientID) REFERENCES PatientProfiles(PatientID)
                    )''')
    print('MedicalTests table created')

    # Billing Information Table
    conn.execute('''CREATE TABLE IF NOT EXISTS BillingInformation (
                    BillingID INTEGER PRIMARY KEY AUTOINCREMENT,
                    PatientID INTEGER,
                    AppointmentID INTEGER,
                    AmountDue REAL,
                    PaymentStatus TEXT,
                    PaymentDate DATE,
                    FOREIGN KEY (PatientID) REFERENCES PatientProfiles(PatientID),
                    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID)
                    )''')
    print('BillingInformation table created')

    # Insurance Information Table
    conn.execute('''CREATE TABLE IF NOT EXISTS InsuranceInformation (
                    InsuranceID INTEGER PRIMARY KEY AUTOINCREMENT,
                    PatientID INTEGER,
                    ProviderName TEXT,
                    PolicyNumber TEXT,
                    CoverageDetails TEXT,
                    FOREIGN KEY (PatientID) REFERENCES PatientProfiles(PatientID)
                    )''')
    print('InsuranceInformation table created')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
