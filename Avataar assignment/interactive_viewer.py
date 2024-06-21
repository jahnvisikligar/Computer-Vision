import cv2
import numpy as np

# Load images
scene_img = cv2.imread('scene.png')
object_img = cv2.imread('chair.png', cv2.IMREAD_UNCHANGED)
depth_map = cv2.imread('depth_estimation.png', cv2.IMREAD_GRAYSCALE)

# Get image dimensions
scene_height, scene_width, _ = scene_img.shape
object_height, object_width, _ = object_img.shape

# Create a window with the same aspect ratio as the scene image
WINDOW_WIDTH = 800
WINDOW_HEIGHT = int(scene_height * WINDOW_WIDTH / scene_width)

# Resize images to fit the window while preserving aspect ratio
scene_img = cv2.resize(scene_img, (WINDOW_WIDTH, WINDOW_HEIGHT))
object_img = cv2.resize(object_img, (0, 0), fx=WINDOW_WIDTH / scene_width, fy=WINDOW_HEIGHT / scene_height)
depth_map = cv2.resize(depth_map, (WINDOW_WIDTH, WINDOW_HEIGHT))

# Function to handle mouse events
def on_mouse(event, x, y, flags, param):
    global scene_img, object_img, depth_map
    if event == cv2.EVENT_MOUSEMOVE:
        temp_scene = scene_img.copy()
        ox, oy = x, y
        ow, oh = object_img.shape[1], object_img.shape[0]

        # Ensure the object fits within the scene boundaries
        if ox + ow > temp_scene.shape[1] or oy + oh > temp_scene.shape[0]:
            return

        # Get depth value at the mouse position
        depth_value = depth_map[oy, ox]

        # Adjust placement based on depth (this example simply prints depth, you can adjust logic as needed)
        #uncomment to read the depth as and when the object moves
        #print(f"Depth at ({ox}, {oy}): {depth_value}")

        alpha_s = object_img[:, :, 3] / 255.0  # Extract the alpha channel and normalize it
        alpha_l = 1.0 - alpha_s               # Compute the inverse alpha for the background
        for c in range(0, 3):  # Loop over the color channels
            temp_scene[oy:oy + oh, ox:ox + ow, c] = (alpha_s * object_img[:, :, c] +
                                                     alpha_l * temp_scene[oy:oy + oh, ox:ox + ow, c])
        cv2.imshow('Scene', temp_scene)

# Display window
cv2.namedWindow('Scene', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Scene', WINDOW_WIDTH, WINDOW_HEIGHT)
cv2.imshow('Scene', scene_img)
cv2.setMouseCallback('Scene', on_mouse)

# Wait for the window to be closed properly
while cv2.getWindowProperty('Scene', cv2.WND_PROP_VISIBLE) >= 1:
    key = cv2.waitKey(50)
    if key == 27:  # Press Esc to exit
        break
cv2.destroyAllWindows()
