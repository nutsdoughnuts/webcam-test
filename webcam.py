print()
print()
print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
print('%%%%%% EJECUCIÒN EN CURSO %%%%%%')
print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')

import cv2

# Open the webcam (you can pass 0 for the default camera)
cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    ret2, frame2 = cap2.read()

    # Display the frame
    cv2.imshow('Webcam Feed', frame)
    cv2.imshow('Webcam Feed 2', frame2)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cap2.release()
cv2.destroyAllWindows()