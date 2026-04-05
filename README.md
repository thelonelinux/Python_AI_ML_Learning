# LEARNING AND EXPLORING PYTHON, ML AND AI
* For very basic starting with all these at once, watch this below 1 hour video
  * https://www.youtube.com/watch?v=JoPWFaS5l-A
* Python is the language used to build these tools
* AI is the main final product which do some manly task, ML is used in backend to create final AI.
* some important packages used in python for ML is
  * numpy : do mathematical tasks
  * pandas : do table arrangements of data
  * sklearn : do linear regression, like making relationship between numbers and stuffs, linear regression, y equals mx plus c things

-------------------------

## A. SOME BASIC KEYWORDS, POINTS TO REMEMBER
* Model : It is the brain model which can predict something. We can create model for like linear regression, log regression
  * there can be large models also, It is just like a simple AI agent doing simple task on its own to predict something.

-------------------------

## B. Tell me about setting up the env in python project
* For a Python project, "setting up the env" usually means creating an isolated virtual environment and installing the project's dependencies into it.
* Basic workflow on Windows PowerShell from your project folder:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

* What each step does:
  * `python -m venv .venv` creates a local virtual environment in `.venv`
  * `Activate.ps1` switches your shell to use that environment's Python
  * upgrading `pip` helps avoid old installer issues
  * `pip install -r requirements.txt` installs the packages your project needs

* Useful checks:

```powershell
python --version
where python
pip list
```

* If your project does not have a `requirements.txt`, install packages manually:

```powershell
pip install numpy pandas scikit-learn
```

* Then save them:

```powershell
pip freeze > requirements.txt
```

* A few practical rules:
  * keep the env inside the project as `.venv`
  * do not install project packages globally
  * add `.venv/` to `.gitignore`


-------------------------

## C. MCP in PYTHON, AI, ML
* https://chatgpt.com/share/69d1fb33-ca58-8323-8dd3-29246efff5a5
* What is MCP (Model Context Protocol)?
* Model Context Protocol (MCP) is a standardized way for AI models (like LLMs) to interact with external tools, data sources, and services in a structured and controlled manner.
* Think of it as:
  * A bridge/interface layer that allows AI models to safely access external capabilities (APIs, databases, files, tools) with clear rules.
* Why MCP is Important in AI/ML
  * Traditional LLMs:
    * Work only with the data they were trained on
    * Cannot directly access live systems or tools
  * With MCP:
    * Models can query databases
    * Call external APIs
    * Execute code/tools
    * Maintain context across interactions

