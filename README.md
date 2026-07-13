# Vitual Onscreen paint using OpenCV & Mediapipe in python

This project access your webcame and tracks you hand all over the reaching distance based on your webcame, the default selected colour is red.

Selection:
1. Use single pointed finger to draw
2. use doulbe pointed finger to select colour or eraser from top while hovering.

for now use `ctrl + c` in cmd to stop

---

#### Folder Structure
```
root/
│
├── assets/
│    └── ui/
│        ├── red_selected.jpg
│        ├── blue_selected.jpg
│        ├── purple_selected.jpg
│        └──eraser_selected.jpg   
│
├── docs/
│   ├── mini project.drawio
│   └── virtual_paint_handtracking_dark.html
│
├── src/
│   ├── hand-tracking-module.py
│   └── main.py
│
├── requirements.txt
├── .gitignore
└── README.md

```

---



! This project is for a webcame of size {video: {width: 1280, height: 720} }

100 1208 3

720h 1280w



python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python virtualpaint.py

