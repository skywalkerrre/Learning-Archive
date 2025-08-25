import sqlite3

# Connect to the SQLite database
def connect_db(db_name):
    try:
        conn = sqlite3.connect(db_name)
        print(f"Connected to database: {db_name}")
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

# Create the 'ports' table if it doesn't exist
def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ports (
                port INTEGER PRIMARY KEY,
                application TEXT
            )
        ''')
        conn.commit()
        print("Table 'ports' created or already exists.")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

# Add a new row to the 'ports' table
def add_port_application(conn, port, application):
    try:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO ports (port, application) VALUES (?, ?)', (port, application))
        conn.commit()
        return (f"Port {port} with application '{application}' added to the database.")
    except sqlite3.Error as e:
        return None

# Retrieve the application given a port number
def get_application_by_port(conn, port):
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT application FROM ports WHERE port = ?', (port,))
        row = cursor.fetchone()
        if row:
            return row[0]
        else:
            return None
    except sqlite3.Error as e:
        print(f"Error retrieving application: {e}")
        return None

if __name__ == '__main__':
    # Provide the name of the SQLite database
    database_name = 'portmap.db'

    # Connect to the database
    connection = connect_db(database_name)

    if connection:
        
        port_applications = {
    21: 'FTP (File Transfer Protocol)',
    22: 'SSH (Secure Shell)',
    23: 'Telnet',
    25: 'SMTP (Simple Mail Transfer Protocol)',
    53: 'DNS (Domain Name System)',
    67: 'DHCP (Dynamic Host Configuration Protocol)',
    68: 'DHCP (Dynamic Host Configuration Protocol)',
    80: 'HTTP (Hypertext Transfer Protocol)',
    110: 'POP3 (Post Office Protocol version 3)',
    115: 'SFTP (Simple File Transfer Protocol)',
    123: 'NTP (Network Time Protocol)',
    143: 'IMAP (Internet Message Access Protocol)',
    161: 'SNMP (Simple Network Management Protocol)',
    443: 'HTTPS (HTTP Secure)',
    465: 'SMTPS (SMTP Secure)',
    587: 'SMTP Submission (Email message submission)',
    587: 'SMTP Submission (Email message submission)',
    5900: 'VNC (Virtual Network Computing)',
    8080: 'HTTP Alternative (commonly used for web proxies)',
    8081: 'Alternative HTTP (commonly used for web proxies)',
    8088: 'Alternative HTTP (commonly used for web proxies)',
    8443: 'HTTPS Alternative (commonly used for secure web proxies)',
    27017: 'MongoDB',
    3306: 'MySQL',
    3389: 'RDP (Remote Desktop Protocol)',
    1433: 'Microsoft SQL Server'
}
        # Create the 'ports' table
        create_table(connection)

        # Add a new row (port and application)
        for port, app in port_applications.items():
            add_port_application(connection, port, app)

        # Retrieve the application given a port number
        app = get_application_by_port(connection, 80)
        if app:
            print(f"Application running on port 80: {app}")
        else:
            print("No application found for port 80.")
        
        # Close the connection to the database
        connection.close()
