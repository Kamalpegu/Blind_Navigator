# 🧭 Blind Navigator

### An accessibility-focused web application designed to assist visually impaired users through voice-based interaction.

**Blind Navigator** is a Python-based assistive technology project focused on making digital interaction and navigation more accessible for visually impaired users.

The current version focuses on building the core web application and voice-based interaction system, with **computer vision and advanced navigation capabilities planned for future development**.

---

## ✨ Current Features

* 🔊 **Voice-Based Interaction** — Designed around audio-based interaction rather than relying solely on visual interfaces.
* ♿ **Accessibility Focused** — Built with visually impaired users as the primary target audience.
* 🌐 **Web-Based Application** — Accessible through a standard web browser.
* 🐍 **Python Backend** — Lightweight Python-based application architecture.
* ⚡ **Responsive Interaction** — Designed for quick and simple user interaction.
* ☁️ **Cloud Deployment** — Can be deployed using PythonAnywhere.
* 🔧 **Extensible Architecture** — Structured to support additional assistive technologies in future versions.

---

## 🚧 Future Development

Blind Navigator is an ongoing project. The following capabilities are planned for future releases:

* 👁️ **Computer Vision** — Real-time understanding of the user's surroundings.
* 🚧 **Obstacle Detection** — Detect obstacles and provide audio warnings.
* 📦 **Object Recognition** — Identify important objects in the user's environment.
* 🚦 **Traffic Signal Recognition** — Assist users in understanding traffic signals.
* 🛣️ **Road & Sign Recognition** — Detect and interpret road signs and markings.
* 🗺️ **GPS Navigation** — Provide location-based navigation assistance.
* 🏢 **Indoor Navigation** — Assist users in navigating buildings and indoor environments.
* 🗣️ **Advanced Voice Assistant** — More natural conversational interaction.
* 📱 **Mobile Application** — Extend the platform to smartphones.
* 🌍 **Multi-Language Support** — Support multiple regional and international languages.

---

# 🏗️ Project Vision

The long-term goal of Blind Navigator is to create an **AI-powered assistive navigation platform** that can help visually impaired users better understand and navigate their surroundings.

The project is being developed incrementally, starting with the core application and gradually introducing advanced capabilities such as computer vision, object detection, navigation, and intelligent voice assistance.

```text
Current
   │
   ▼
Voice-Based Accessibility
   │
   ▼
Core Web Application
   │
   ▼
Computer Vision
   │
   ▼
Object & Obstacle Detection
   │
   ▼
Navigation Assistance
   │
   ▼
AI-Powered Assistive Navigator
```

---

# 🛠️ Technology Stack

| Technology                     | Purpose                       |
| ------------------------------ | ----------------------------- |
| 🐍 **Python**                  | Application logic and backend |
| 🌐 **HTML / CSS / JavaScript** | Web interface                 |
| 🔊 **Voice Technologies**      | Audio-based interaction       |
| ☁️ **PythonAnywhere**          | Cloud deployment              |
| 📦 **Git & GitHub**            | Version control               |

> Additional AI and computer-vision technologies will be introduced as the project evolves.

---

# 📂 Project Structure

```text
Blind_Navigator/
│
├── app.py
├── wsgi.py
├── requirements.txt
├── README.md
├── LICENSE
│
├── static/
│   └── ...
│
├── templates/
│   └── ...
│
└── ...
```

---

# 🚀 Getting Started

## Prerequisites

Make sure you have:

* Python 3.9+
* Git
* pip
* A modern web browser

---

## 1. Clone the Repository

```bash
git clone https://github.com/Kamalpegu/Blind_Navigator.git
cd Blind_Navigator
```

---

## 2. Create a Virtual Environment

### Windows

```powershell
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run the Application

```bash
python app.py
```

Open the application in your browser using the local URL provided by the application.

---

# ☁️ Deploy on PythonAnywhere

Blind Navigator can be deployed on **PythonAnywhere**.

### 1. Create a Web App

1. Log in to PythonAnywhere.
2. Open the **Web** tab.
3. Select **Add a new web app**.
4. Choose **Manual configuration**.
5. Select the Python version required by the project.

### 2. Clone the Repository

Open a Bash console:

```bash
git clone https://github.com/Kamalpegu/Blind_Navigator.git
cd Blind_Navigator
```

### 3. Create a Virtual Environment

```bash
mkvirtualenv --python=/usr/bin/python3.11 blind-navigator
```

Then:

```bash
workon blind-navigator
pip install -r requirements.txt
```

### 4. Configure the Virtual Environment

In the **Web** tab, set the virtual environment path to:

```text
/home/YOUR_USERNAME/.virtualenvs/blind-navigator
```

Replace `YOUR_USERNAME` with your PythonAnywhere username.

### 5. Configure WSGI

Open the WSGI configuration file and configure:

```python
import sys

project_path = '/home/YOUR_USERNAME/Blind_Navigator'

if project_path not in sys.path:
    sys.path.insert(0, project_path)

from wsgi import application
```

Replace `YOUR_USERNAME` with your PythonAnywhere username.

### 6. Reload

Go to the **Web** tab and click **Reload**.

Your application should now be available through your PythonAnywhere URL.

---

# 🔄 Updating the Application

After pushing new changes to GitHub:

```bash
cd ~/Blind_Navigator
git pull origin main
```

Then reload the application from the PythonAnywhere **Web** tab.

---

# 🔐 Security

Do not commit sensitive information such as:

* API keys
* Passwords
* Secret keys
* `.env` files
* Authentication credentials

Add sensitive files to `.gitignore`:

```text
.env
venv/
__pycache__/
*.pyc
```

---

# 🎯 Project Status

| Component                 | Status                                          |
| ------------------------- | ----------------------------------------------- |
| Core Web Application      | ✅ Available                                     |
| Voice-Based Interaction   | 🔄 In Development / Available where implemented |
| PythonAnywhere Deployment | ✅ Supported                                     |
| Computer Vision           | 🚧 Planned                                      |
| Object Detection          | 🚧 Planned                                      |
| Obstacle Detection        | 🚧 Planned                                      |
| GPS Navigation            | 🚧 Planned                                      |
| Indoor Navigation         | 🚧 Planned                                      |
| Mobile Application        | 🚧 Planned                                      |

---

# 🤝 Contributing

Contributions and ideas are welcome.

1. Fork the repository.
2. Create a new branch:

```bash
git checkout -b feature/new-feature
```

3. Make your changes.
4. Commit:

```bash
git commit -m "Add new feature"
```

5. Push your branch:

```bash
git push origin feature/new-feature
```

6. Open a Pull Request.

---

# 📜 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for details.

---

# 👨‍💻 Author

### Kamal Pegu

GitHub:
https://github.com/Kamalpegu

Repository:
https://github.com/Kamalpegu/Blind_Navigator

---

## ⭐ Support

If you like the idea behind **Blind Navigator**, consider giving the repository a ⭐ on GitHub.

---

> **Blind Navigator — Building technology for a more accessible future.** 🧭♿
