# SETUP STEPS AND ALL
* (.venv) PS C:\Users\HP\Desktop\Python_AI_ML_Learning> .\.venv\Scripts\python -m pip install -r requirements.txt
* (.venv) PS C:\Users\HP\Desktop\Python_AI_ML_Learning> .\.venv\Scripts\python -m pip install -r requirements.txt


## A. HOW TO SETUP ENV AND RUN THE PROJECT
### ADD PYTHON
* (.venv) PS C:\Users\HP\Desktop\Python_AI_ML_Learning> python --version
* Python 3.14.3
### CREATE ENVIRONMENT BY COPILOT ACTIVATE ENVIRONMENT
* PS C:\Users\HP\Desktop\Python_AI_ML_Learning> Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force
* PS C:\Users\HP\Desktop\Python_AI_ML_Learning> .\.venv\Scripts\Activate.ps1
(.venv) PS C:\Users\HP\Desktop\Python_AI_ML_Learning> 

### TO DOWNLOAD FROM REQUIREMENTES.TXT
* py -m pip install -r requirements.txt

### TO RUN THE FILE
* py model.py
* http://127.0.0.1:8000

### IF U WANT TO RUN IN DEBUG MODE
* py model.py --debug





## B. USE OF .VENV IN THIS PROJECT
* `.venv` is the local virtual environment folder for this project.
* It keeps the Python interpreter and installed packages isolated from the system-wide Python.
* This means packages installed with `pip install -r requirements.txt` are stored only for this project.
* Using `.venv` avoids package version conflicts with other projects and makes the setup reproducible.
* Activate `.venv` before installing dependencies or running the code:
  * `.\.venv\Scripts\Activate.ps1` on PowerShell
  * `.\.venv\Scripts\activate.bat` on CMD
* After activation, install dependencies with:
  * `py -m pip install -r requirements.txt`
* Then run project files from the same activated environment.
