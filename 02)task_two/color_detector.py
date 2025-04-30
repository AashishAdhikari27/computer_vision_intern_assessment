import cv2
from util import display_color_info

# Initialize the  webcam
cap = cv2.VideoCapture(0) # if we have only one web cam in our setup then the default value would be 0

cv2.namedWindow("Color Detector") ## naming the webcam window 


# Global variables
last_click = None  # Stores the last clicked point on the frame
last_color_info = None  # Stores the color information for the last clicked point


# Mouse callback function
def mouse_callback(event, x, y, flags, param):
    global last_click, last_color_info, frame

    if event == cv2.EVENT_LBUTTONDOWN:  # Detects left mouse button click
        b, g, r, color_name = display_color_info(frame, x, y)  # Get the color info at the clicked point
        b, g, r = int(b), int(g), int(r)  # Ensure BGR values are integers
        last_click = (x, y)  # Store the clicked coordinates
        last_color_info = (b, g, r, color_name)  # Store the color info for the clicked pixel

# Set mouse callback
cv2.setMouseCallback("Color Detector", mouse_callback)

# Main loop
while True:
    ret, frame = cap.read()
    if not ret:
        break

    if last_click and last_color_info:  # If there's valid click and color info
        x, y = last_click  # Get the last clicked coordinates
        b, g, r, color_name = last_color_info  # Get the BGR and color name of the clicked pixel

        # Ensure rectangle and text don't go off frame
        rect_w, rect_h = 300, 40  # Define rectangle width and height
        rect_x1 = x if x + rect_w < frame.shape[1] else frame.shape[1] - rect_w  # Adjust the rectangle position to stay within the frame width
        rect_y1 = y if y + rect_h < frame.shape[0] else frame.shape[0] - rect_h  # Adjust the rectangle position to stay within the frame height
        rect_x2, rect_y2 = rect_x1 + rect_w, rect_y1 + rect_h  # Calculate the opposite corner of the rectangle

        # Draw the filled rectangle with the detected color
        cv2.rectangle(frame, (rect_x1, rect_y1), (rect_x2, rect_y2), (b, g, r), -1)

        # Draw a border around the clicked area (green square)
        cv2.rectangle(frame, (x - 5, y - 5), (x + 5, y + 5), (0, 255, 0), 2)

        # Overlay the color name and BGR values on the frame
        text = f'{color_name} BGR=({b},{g},{r})'  # Text to display with the color name and BGR values
        
        cv2.putText(frame, text, (rect_x1 + 10, rect_y1 + 25), cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                    (255 - b, 255 - g, 255 - r), 2, cv2.LINE_AA)  # Put the text on the frame, inverted color for better visibility

    # Show the frame in the window
    cv2.imshow("Color Detector", frame)

    # Exit the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()  # Release the webcam
cv2.destroyAllWindows()  # Close the OpenCV windows
