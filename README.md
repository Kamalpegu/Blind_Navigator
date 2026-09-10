# 🧭 Blind Navigator

### An AI-powered assistive navigation system designed to help visually impaired users understand and navigate their surroundings.

**Blind Navigator** is a Python-based accessibility project that uses computer vision, audio feedback, and intelligent processing to help visually impaired users identify objects, understand their environment, and navigate more independently.

The application is designed with simplicity and accessibility in mind, providing information through **voice-based interaction** rather than relying primarily on visual interfaces.

---

## ✨ Features

* 🧭 **Assistive Navigation** — Helps users understand their surrounding environment.
* 👁️ **Object Detection** — Identifies objects and obstacles using computer vision.
* 🔊 **Voice Feedback** — Converts detected information into audio guidance.
* 🎙️ **Voice Interaction** — Enables hands-free interaction.
* ⚡ **Real-Time Processing** — Processes visual information and provides feedback with minimal delay.
* ♿ **Accessibility Focused** — Designed specifically around the needs of visually impaired users.
* 🌐 **Web-Based Interface** — Can be deployed and accessed through a web browser.
* ☁️ **PythonAnywhere Deployment** — Supports easy cloud deployment.

---

## 🏗️ How It Works

```text
                ┌──────────────────┐
                │      User        │
                │  Voice / Camera  │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │ Blind Navigator  │
                │     Backend      │
                └────────┬─────────┘
                         │
              ┌──────────┴──────────┐
              │                     │
              ▼                     ▼
       ┌──────────────┐      ┌──────────────┐
       │ Computer     │      │ Voice        │
       │ Vision       │      │ Processing   │
       └──────┬───────┘      └──────┬───────┘
              │                     │
              └──────────┬──────────┘
                         ▼
                ┌──────────────────┐
                │ Intelligent      │
                │ Processing       │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │ Audio Guidance   │
                │ & User Feedback  │
                └──────────────────┘
```

---

## 🛠️ Tech Stack

| Technology                     | Purpose                         |
| ------------------------------ | ------------------------------- |
| 🐍 **Python**                  | Core application logic          |
| 👁️ **Computer Vision**        | Environment and object analysis |
| 🔊 **Speech / Audio**          | Voice-based feedback            |
| 🌐 **HTML / CSS / JavaScript** | Web interface                   |
| ⚡ **Python Web Framework**     | Backend/API                     |
| ☁️ **PythonAnywhere**          | Cloud deployment                |
| 📦 **Git & GitHub**            | Version control                 |

---

## 📂 Project Structure

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
│   ├── css/
│   ├── js/
│   └── ...
│
├── templates/
│   ├── index.html
│   └── ...
│
└── ...
```

---

# 🚀 Getting Started

## Prerequisites

Make sure you have the following installed:

* Python 3.9+
* Git
* pip
* A supported web browser

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

Start the application using the appropriate command for the project's backend.

For a Flask application, for example:

```bash
python app.py
```

The application will normally be available at:

```text
http://127.0.0.1:5000
```

Open the address in your browser.

---

# ☁️ Deploy on PythonAnywhere

Blind Navigator can be deployed using **PythonAnywhere**.

### 1. Create a Web App

1. Log in to PythonAnywhere.
2. Open the **Web** tab.
3. Select **Add a new web app**.
4. Choose **Manual configuration**.
5. Select the Python version required by the project.

---

### 2. Clone the Repository

Open a Bash console:

```bash
git clone https://github.com/Kamalpegu/Blind_Navigator.git
cd Blind_Navigator
```

---

### 3. Create a Virtual Environment

```bash
mkvirtualenv --python=/usr/bin/python3.11 blind-navigator
```

Activate it:

```bash
workon blind-navigator
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

### 4. Configure the Virtual Environment

In the **Web** tab, set the virtual environment path to:

```text
/home/YOUR_USERNAME/.virtualenvs/blind-navigator
```

Replace `YOUR_USERNAME` with your PythonAnywhere username.

---

### 5. Configure WSGI

Open the WSGI configuration file from the **Web** tab.

Use:

```python
import sys

project_path = '/home/YOUR_USERNAME/Blind_Navigator'

if project_path not in sys.path:
    sys.path.insert(0, project_path)

from wsgi import application
```

Replace `YOUR_USERNAME` with your actual PythonAnywhere username.

---

### 6. Reload

Go back to the **Web** tab and click:

**Reload**

Your application should now be accessible through your PythonAnywhere URL.

---

# 🔄 Updating the Deployment

After pushing new changes to GitHub:

```bash
cd ~/Blind_Navigator
git pull origin main
```

Then go to the **Web** tab and click **Reload**.

---

# 🔐 Environment Variables

If the project uses API keys or other credentials, keep them outside the repository.

For example:

```text
API_KEY=your_api_key
SECRET_KEY=your_secret_key
```

**Never commit sensitive credentials to GitHub.**

Add sensitive files such as `.env` to `.gitignore`:

```text
.env
venv/
__pycache__/
*.pyc
```

---

# 🖥️ Screenshots

Add screenshots of the application here to showcase the project.

```text
screenshots/
├── home.png
├── navigation.png
└── detection.png
```

Example:

```markdown
![Blind Navigator](screenshots/home.png)
```

---

# 🎯 Project Goals

Blind Navigator aims to explore how modern software and AI technologies can be used to improve accessibility.

### Main goals

* Improve environmental awareness for visually impaired users.
* Provide useful information through audio instead of visual output.
* Reduce the complexity of assistive interfaces.
* Explore real-time computer vision and voice technologies.
* Build an accessible and practical assistive technology solution.

---

# 🔮 Future Improvements

Potential improvements include:

* 🗺️ GPS-based navigation
* 🚦 Traffic-light and road-sign recognition
* 🚧 Advanced obstacle detection
* 🧑‍🤝‍🧑 Person recognition
* 🏢 Indoor navigation
* 📍 Location-aware assistance
* 📱 Mobile application
* 🗣️ More natural conversational voice interaction
* ⚡ Improved real-time processing
* 🌐 Multi-language support

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new branch:

```bash
git checkout -b feature/new-feature
```

3. Make your changes.
4. Commit your changes:

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

See the [`LICENSE`](LICENSE) file for details.

---

# 👨‍💻 Author

### Kamal Pegu

GitHub:
https://github.com/Kamalpegu

Project:
https://github.com/Kamalpegu/Blind_Navigator

---

## ⭐ Show Your Support

If you find **Blind Navigator** interesting or useful, consider giving the repository a ⭐ on GitHub.

---

### 🧭 Blind Navigator

> **Technology should make the world more accessible — not less.**
