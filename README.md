# DBFace

## Introduction

This is a DBFace (a real-time, single-stage detector for face detection) demo for HSE MCV week1 task 2 - Make a package for your project


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

---install gitpython---
```
pip install gitpython
```

---Install the package---
```
pip install git+https://github.com/polylam1994/hse_mcv_MLinCV@task-1.2
```

---Install all the dependencies---
```
pip install -r requirements.txt
```


## Running the demo
---Activate Python virtual environment if you havn't---
```
.\env\Scripts\activate
```

---Run demo in Python IDE---
```
from hse_mcv_dbface import demo
demo.image_demo()
```

![image](https://user-images.githubusercontent.com/59043071/171104175-17a8d9df-eba3-4886-b36f-d368b7f67576.png)
