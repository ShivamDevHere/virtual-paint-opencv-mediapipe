# Virtual On-screen Paint Using OpenCV And MediaPipe

<table>
<tr>
<td width="60%">

### How It Works

This project uses your webcam to detect and track your hand using **MediaPipe** and **OpenCV**, allowing you to draw on a virtual canvas using hand gestures.

**Controls:**
- ☝️ Raise only your index finger to draw.
- ✌️ Raise your index and middle fingers to enter selection mode.
- Hover over a tool in the top toolbar to select a color or the eraser.
- Press `Ctrl + C` in the terminal to stop the application.

</td>

<td width="40%" align="center">

<img src="assets/demo.gif" width="300"/>

</td>
</tr>
</table>












---
### Table of Contents

- [Description](#virtual-on-screen-paint-using-opencv-and-mediapipe)
- [How to run this project](#installation)
- [Folder Structure](#folder-structure)
- [Notes](#notes)
- [Additional Information](#additional-information)
	1. Recommended Screen Size
	2. Features
	3. Technology

---
# Installation
- Run these all code in terminal depending on Operating System.
#### 1. Clone Repository
	git clone `https://github.com/ShivamDevHere/virtual-paint-opencv-mediapipe` 
	`cd virtual-onscreen-paint-using-opencv-and-mediapipe-in-python`
#### 2. Create a virtual environment

- **Windows**

```

	python -m venv venv
	venv\Scripts\activate
```

- **Linux/macOS**

```

	python3 -m venv venv
	source venv/bin/activate
```

#### 3. Install dependencies: 
`pip install -r requirements.txt`
#### 4. Run the application
`python src\main.py`

---
### Folder Structure

```
virtual-onscreen-paint-using-opencv-and-mediapipe-in-python/
├── assets/
│    └── ui/
│        ├── red_selected.jpg
│        ├── blue_selected.jpg
│        ├── purple_selected.jpg
│        └──eraser_selected.jpg   
├── docs/
│   ├── mini project.drawio
│   └── virtual_paint_handtracking_dark.html
├── src/
│   ├── HandTrackingModule.py
│   └── main.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---
### Notes

To deep dive in this project please see the `docs/` directory.

---
## Additional Information

#### Recommended Screen Size
- Recommended webcam resolution: **1280 × 720**
- Toolbar image size: **1280 × 100**
#### Features

- Real-time hand tracking
- Virtual drawing canvas
- Multiple brush colors
- Eraser tool
- Finger gesture controls
- Built with OpenCV and MediaPipe
#### Technologies

- Python
- OpenCV
- MediaPipe
- NumPy

---

[⬆ Back to Top](#virtual-on-screen-paint-using-opencv-and-mediapipe)
