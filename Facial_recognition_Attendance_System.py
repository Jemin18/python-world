import cv2
import face_recognition
import cmake
import numpy as np
import csv
from datetime import datetime

video_capture = cv2.VideoCapture(0)
person_1_image = face_recognition.load_image_file("images/new_jemin_image.png")
person_1_encodings = face_recognition.face_encodings(person_1_image)[0]

known_faces_encodings = [person_1_encodings]
known_face_names = ["Jemin"]

persons = known_face_names.copy()

face_locations = []
face_encodings = []

date_time = datetime.now()
current_date_time = date_time.strftime("%d-%m-%y")

f = open(f"{current_date_time}.csv", "w+", newline="")

l = csv.writer(f)

while True:
    _, frame = video_capture.read()
    resize_frame = cv2.resize(frame, (0,0), fx = 0.25, fy = 0.25)
    rgb_small_frame = cv2.cvtColor(resize_frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for encodings in face_encodings:
        face_match = face_recognition.compare_faces(known_faces_encodings, encodings)
        face_distance = face_recognition.face_distance(known_faces_encodings,  encodings)
        best_match_index = np.argmin(face_distance)
        if face_match[best_match_index]:
            name = known_face_names[best_match_index]

        if name in known_face_names:
            font = cv2.FONT_HERSHEY_SIMPLEX
            bottom_left_corner_of_text = (10,100)
            font_scale = 1
            font_color = (260,0,0)
            thickness = 2
            line_type = 2
            cv2.putText(frame, name + " present", bottom_left_corner_of_text, font, font_scale, font_color, thickness, line_type)

            if name in persons:
                persons.remove(name)
                current_time = date_time.strftime("%H-%M-%S")
                l.writerow([name , current_time])

    cv2.imshow("a", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()
f.close()