# Blind_Navigator

## Deploy on PythonAnywhere

1. Create a Python 3 web app in PythonAnywhere.
2. Clone this repository into your PythonAnywhere home directory:

	```bash
	git clone https://github.com/Kamalpegu/Blind_Navigator.git
	cd Blind_Navigator
	```

3. Create a virtual environment and install the web dependencies:

	```bash
	mkvirtualenv --python=/usr/bin/python3.11 blind-navigator
	pip install -r requirements.txt
	```

4. In the **Web** tab, set the virtualenv path to the environment you created.
5. Open the WSGI configuration file and replace its contents with:

	```python
	import sys

	project_path = '/home/YOUR_PYTHONANYWHERE_USERNAME/Blind_Navigator'
	if project_path not in sys.path:
		 sys.path.insert(0, project_path)

	from wsgi import application
	```

	Replace `YOUR_PYTHONANYWHERE_USERNAME` with your actual username.
6. Click **Reload** in the Web tab and open the site URL.