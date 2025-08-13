# HOW TO RUN THE ADDRESS BOOK APPLICATION

## Create an virtual environment (VENV folder) to store external libraries

`python -m venv venv_name`

## Activate the venv through terminal

`venv_name/Scripts/Activate`

- Make sure the virtual environment is activated

- It is ussually indicated by: `(venv) PS C:\Users` in your terminal

## Install external libraries through requirements.txt file

`pip install -r requirements.txt`

## After installing the required libraries, Run the API on python_assesment.py locally

`uvicorn python_assesment:app` 

- Optional: `uvicorn python_assesment:app --reload` 

`--reload` -> automatically reloads the server when editing the source code



`INFO:     Started server process [17816]`<br>
`INFO:     Waiting for application startup.`<br>
`INFO:     Application startup complete.`<br>
`INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)`

- You can check the API through the given localhost server `http://127.0.0.1:8000`

## You can also test the api through Swagger Docs 

`http://127.0.0.1:8000/docs`



