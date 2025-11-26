from db import get_connection


failed_login_count = 0

def create_alert(severity, description, timestamp):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO alerts (timestamp, severity, description) VALUES (%s, %s, %s)",
        (timestamp, severity, description)
    )

    conn.commit()
    cur.close()
    conn.close()

def check_for_alert(message, timestamp):
    global failed_login_count

    if "Failed login attempt" in message:
        failed_login_count += 1

        if failed_login_count >= 3:
            create_alert(
                "High",
                "Multiple failed login attempts detected",
                timestamp
            )
            failed_login_count = 0

    if "Firewall rule change" in message:
        create_alert(
            "Medium",
            "Firewall configuration change detected",
            timestamp
        )

    if "Unusual traffic spike" in message:
        create_alert(
            "Medium",
            "Unusual network traffic detected",
            timestamp
        )
