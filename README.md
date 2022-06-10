# DBFace

## Introduction

This is a HSE MCV week2 task 2 - Setup CI pipeline

## Installation

---Install virtualenv---
```
python -m pip install --user virtualenv
```

---Change to project directory---
```
cd paste/your/directory/here
```

---Create Python virtual enviroment under the directory---
```
python -m venv env
```

---Activate Python virtual environment---
```
.\env\Scripts\activate
```

---Install all the dependencies---
```
pip install -r requirements.txt
pip install -r requirements_dev.txt
```

---Install the package---
```
pip install .
```

## Run pytest
---Activate Python virtual environment if you havn't---
```
.\env\Scripts\activate
```

---Run Pytest---
```
pytest
```

![image](https://user-images.githubusercontent.com/59043071/171131131-d121e2f5-37be-4bde-bfa3-8e8fe733b0df.png)

## Set up CI pipeline

For auto build and test, set up testPush.yml .
For auto testing pull request, set up test_Pull_Request.yml .
to make it work, go to Settings -> Branches -> add rule.

![image](https://user-images.githubusercontent.com/59043071/171220219-472968a7-de15-4e9e-a01f-fab4eda682a3.png)

