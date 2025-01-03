# **Drowsiness and Distraction Alertness System**

## **Overview** 

### The Drowsiness and Distraction Alertness System is a real-time monitoring application designed to enhance road safety by detecting signs of driver drowsiness or distraction. Leveraging computer vision, machine learning, and speech processing techniques, the system ensures the safety of the driver and passengers, reducing the likelihood of accidents.

## **Features**

### Drowsiness Detection: 
Monitors eye closure and blinking patterns using image processing techniques.

### Distraction Detection: 
Identifies distractions such as mobile phone use or handling objects while driving.

### Alert System: 
Voice-enabled alerts to snap the driver out of drowsy or distracted states.

### Interactive Chatbot: 
Provides basic assistance, plays music, and responds to voice commands.

## Technology Stack
**Programmig Language:** Python

## Libraries Used:

OpenCV: Image processing and computer vision.

SciPy, NumPy: Scientific computing.

Dlib: Facial landmark detection.

gTTS: Text-to-speech processing.

Selenium: Web automation for extended functionality.


## System Requirements
### Hardware
GPU: Nvidia/AMD

Processor: Intel Core i3/i5 or equivalent

RAM: 8GB (recommended)

Peripheral Devices: Dash Camera, Speaker, Microphone


### Software
Python 3.x

Libraries: Install dependencies listed in requirements.txt.

## Installation
### 1)Clone the repository
git clone https://github.com/prawalika-t/DROWSINESS-AND-DISTRACTION-ALERTING-SYSTEM

### 2)Navigate to the project directory:
cd drowsiness-detection

### 3)Install dependencies
pip install -r requirements.txt

### 4)Run the application:
python main.py


## Usage
Position the camera to capture the driver’s face.

Ensure good lighting conditions inside the vehicle for optimal performance.

Start the application and let it run in the background during driving.

## Results
Drowsiness Detection: Alerts when eye aspect ratio (EAR) drops below the threshold.

Distraction Detection: Identifies objects like mobile phones or cups in the driver’s hands.

Chatbot: Responds to voice commands and provides assistance.

Future Enhancements

Integration with advanced hardware for better accuracy.

Expansion to support multiple vehicle types.

Incorporation of adaptive auto-driving capabilities.

## Authors

### Akansha Jain

### Kartik Nesari

### Pratik Shankar

### Prawalika Tewari
