# AI Virtual Zoom Using Gesture

This project creates a virtual zoom system using hand gestures. It uses **OpenCV** and **cvzone** to track hand movements and zoom in or out based on the distance between hands. The system detects hands in real-time and changes the image size based on gestures.

## Installation
### 1. Clone the Repository
```
git clone 
cd AI-Virtual-Zoom-Gesture
```

### 2. Install Dependencies
Ensure you have Python installed, then run:
```
pip install -r requirements.txt
```

## Usage
Run the script:
```
python app.py
```

### How It Works
1. **Run the script** → Your webcam will turn on.
2. **Raise both hands with your index and middle fingers extended** → The zoom function will activate.
3. **Bring your hands closer together** → The image will zoom in.
4. **Move your hands farther apart** → The image will zoom out.
5. **Lower your hands or stop the gesture** → The zoom resets to normal.

## Code Explanation
- **Hand tracking**: Detects hands using `cvzone.HandTrackingModule`.
- **Distance measurement**: Calculates distance between hand centers.
- **Dynamic image resizing**: Resizes the image based on hand distance.

## Troubleshooting
- **Webcam not detected** -> `cv2.VideoCapture(0)`, try `1` if using an external webcam. 
- **Image not appearing** -> Ensure `Image` is in the correct directory
