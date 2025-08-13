# HOW TO RUN THE ADDRESS BOOK APPLICATION

## Create a virtual environment (VENV folder) to store external libraries

```bash
python -m venv venv_name
```

## Activate the venv through terminal

```bash
venv_name/Scripts/Activate
```

* Make sure the virtual environment is activated
* It is usually indicated by: `(venv) PS C:\Users` in your terminal

## Install external libraries through requirements.txt file

```bash
pip install -r requirements.txt
```

## After installing the required libraries, run the API locally

```bash
uvicorn python_assesment:app
```

* Optional:

```bash
uvicorn python_assesment:app --reload
```

`--reload` → automatically reloads the server when editing the source code

```text
INFO:     Started server process [17816]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

* You can check the API through the given localhost server:
  `http://127.0.0.1:8000`

## You can also test the API through Swagger Docs or POSTMAN

`http://127.0.0.1:8000/docs`

---

## ✅ Conclusion

* You have successfully set up and run the **Address Book API** locally.

* You can now interact with the API through:

  * **Browser**: `http://127.0.0.1:8000/docs` (Swagger UI)
  * **Postman** or other API testing tools
  * Direct **GET/POST requests** via localhost

* Make sure to **keep your virtual environment activated** whenever you work with this project.

* If you want to make changes to the API code, use the `--reload` flag to automatically apply updates.

---

