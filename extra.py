# # import mysql.connector
import pymysql
import pymysql

import cv2

# Correct configuration
# connection = mysql.connector.connect(host="localhost",user="root",password="Rohit@123",database="face_recognizer", auth_plugin='mysql_native_password')
connection = pymysql.connect(host="localhost",user="root",password="Rohit@123",database="face_recognizer")

# Do something with the connection, like querying
cursor = connection.cursor()
rows = cursor.execute("SELECT * FROM student")


cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open camera.")
else:
    print("Camera opened successfully.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    cv2.imshow("Camera Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


