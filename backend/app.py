from db import get_connection
from datetime import datetime
import detector




def insert_log(timestamp, source, message):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO logs (timestamp, source, message) VALUES (%s, %s, %s)",
        (timestamp, source, message)
    )

    conn.commit()
    cur.close()
    conn.close()

def process_logs():
    with open("sample_logs.txt", "r") as file:
        for line in file:
            parts = line.strip().split(" ", 3)
            timestamp_str = parts[0] + " " + parts[1]
            source = parts[2]
            message = parts[3]

            timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")

            insert_log(timestamp, source, message)
            detector.check_for_alert(message, timestamp)

if __name__ == "__main__":
    process_logs()
    print("Logs processed and alerts generated.")
