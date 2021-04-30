# PearlHacks  
Installation Guide:  
## **Flask Installation:**  
##### 1. Start Virtual Environment:  
- For Mac:   
  - $ python3 -m venv venv  
  - $ . venv/bin/activate  
- For Windows: 
  - use cmd terminal
  - $ py -3 -m venv venv
  - $ venv\Scripts\activate.bat
##### 2. Install Flask (should be in venv)  
- $ pip install Flask
- $ pip install -e .
- For Mac:
  - $ export FLASK_APP=flaskr  
  - $ export FLASK_ENV=development
- For Windows:  
  - $ set FLASK_APP=flaskr  
  - $ set FLASK_ENV=development  
##### 3. To Run:  
- $ py app.py
- open up http://127.0.0.1:5000