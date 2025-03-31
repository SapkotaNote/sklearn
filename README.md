# sklearn
# Project Overview: Real-Time Traffic Monitoring & News Filtering System

This project aims to create a real-time system that:
1. Filters Facebook Messenger posts/news based on preferences.
2. Monitors traffic data via Google Maps.
3. Detects speed limits while riding a bike using camera input and overlays speed notifications.

| **Feature**                              | **Description**                                                                 | **Tools/Technologies**                                                       | **Approach**                                                                 |
|------------------------------------------|---------------------------------------------------------------------------------|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| **Facebook Messenger Post Filtering**    | Filters and categorizes posts/news from Facebook Messenger.                    | Python, spaCy, transformers, Facebook Graph API                               | Use NLP models to filter and categorize messages based on preferences.       |
| **Google Maps Traffic Monitoring**       | Monitors real-time traffic data and predicts traffic patterns.                  | Google Maps API, Python                                                       | Fetch real-time traffic data, analyze patterns, and visualize traffic info.  |
| **Speed Limit Detection (Bike)**         | Detects speed limits based on GPS location and camera feed while riding.       | OpenCV, TensorFlow, Google Maps API, Python                                   | Use camera feed to detect speed limits, overlay on screen, and alert rider.  |
| **Real-time Camera Feed Access**         | Provides access to camera input for real-time video processing and analysis.   | OpenCV, Python                                                              | Access camera feed using OpenCV, process video in real-time for detection.   |

## Workflow

1. **Data Collection**:  
   - Access Facebook Messenger data using the Facebook Graph API.  
   - Access Google Maps API for traffic data and speed limit information.  
   - Use the camera feed for real-time processing.

2. **Model Development**:  
   - Train NLP models to filter and categorize Messenger posts.  
   - Build a computer vision model for detecting road signs and speed limits.  
   - Integrate real-time data processing for traffic and speed monitoring.

3. **System Integration**:  
   - Combine all features into a seamless real-time system.  
   - Implement user interface for displaying alerts and traffic info.

4. **Real-Time Processing**:  
   - Handle real-time camera input and model predictions without lag.

## Tools & Libraries

- **Programming Language**: Python
- **Machine Learning Framework**: TensorFlow, PyTorch
- **Computer Vision**: OpenCV
- **Natural Language Processing**: spaCy, transformers
- **APIs**: Google Maps API, Facebook Graph API
- **Web Framework**: Flask/Django (optional for UI)

