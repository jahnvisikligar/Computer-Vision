# Avaatar assignment
This repo is a reflection of my work for the assignment by Avaatar

## Execution of code
This guide provides step-by-step instructions on how to execute the code for the floor planner application. Ensure that Python 3.7+ is installed and all required dependencies are installed as mentioned in requirements.txt. You can install them using pip by running:
    
    pip install -r requirements.txt

### Depth Estimation

Run the depth_estimation.py script to generate the depth map:

    python depth_estimation.py

This script reads the scene.png image, computes the depth map using the MiDaS model, and saves it as depth_map.png.

### Interactive Viewer

Execute the interactive_viewer.py script to launch the interactive viewer:
    
    python interactive_viewer.py

This script opens a window displaying the scene image (scene.png) and allows you to interactively place and resize objects within the scene.

## Usage Examples
Moving Objects: Click and drag the object within the scene window to move it around. The object resizes automatically as it is moved.

Depth Awareness: Observe how the object adjusts its size and positioning based on the depth map generated in the previous step, providing realistic occlusion and depth perception.

Additional Notes
- Ensure that the input images (scene.png, chair.png) are present in the same directory as the Python scripts.
- You can replace chair.png with any other object image you wish to place in the scene. Just ensure that it has an alpha channel for transparency if needed.
- Experiment with different scene and object images to explore the capabilities of the interactive viewer.

## Task Breakdown:
To accomplish the assignment objectives, the project was broken down into several tasks, each requiring specific functionalities and considerations:

Depth Estimation: Generate a depth map from the scene image. Utilize the MiDaS model for depth estimation, ensuring accurate depth perception in the scene.

Interactive Viewer Setup: Create an interactive viewer with a scene image and movable object. Develop a Python script using OpenCV to display the scene image and allow user interaction for object placement and movement.

Object Rescaling: Ensure the object resizes automatically while being moved around the scene. Implement logic to dynamically adjust the object's size relative to its position within the scene, providing a realistic viewing experience.

Occlusion Awareness: Implement occlusion awareness to ensure correct object placement behind or in front of scene elements. Utilize the depth map generated in Task 1 to determine occlusion dynamically, adjusting object visibility based on depth information.

Floor Traversal: Prevent the object from intersecting with other objects in the scene, ensuring it traverses the visible floor. Enhance the interactive logic to account for visible floor space, restricting object movement to maintain realism and prevent clipping.

## Challenges Faced:
Depth Estimation Accuracy: Ensuring accurate depth estimation proved challenging due to variations in scene complexity and lighting conditions. Fine-tuning model parameters and preprocessing techniques were employed to improve accuracy.

Realistic Object Placement: Achieving realistic object placement and occlusion awareness required careful consideration of depth information and dynamic adjustment of object visibility based on depth values.

Performance Optimization: Balancing computational efficiency with accuracy and realism was crucial, especially when handling large scene images and complex object interactions.
