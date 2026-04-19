import cv2
import numpy as np


def start_pushup_counter():

    cap = cv2.VideoCapture(0)

    pushups = 0
    direction = 0
    prev_y = None

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        frame = cv2.flip(frame, 1)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # detect body movement using frame difference
        if prev_y is None:
            prev_y = np.mean(gray)

        current_y = np.mean(gray)

        diff = prev_y - current_y

        # DOWN movement
        if diff > 2 and direction == 0:
            direction = 1

        # UP movement
        if diff < -2 and direction == 1:
            pushups += 1
            direction = 0

        prev_y = current_y

        cv2.putText(
            frame,
            f"Pushups: {pushups}",
            (30, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            3
        )

        cv2.putText(
            frame,
            "Press Q to stop",
            (30, 100),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2
        )

        cv2.imshow("AI Fitness Trainer - Pushup Counter", frame)

        key = cv2.waitKey(1)

        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    return pushups