# DBFace

## Introduction

This is a HSE MCV week2 task 1 - Setup project for team work (style tools, static analysis)

## Installation

---Install virtualenv---
python -m pip install --user virtualenv

---Change to project directory---
cd paste/your/directory/here

---Create Python virtual enviroment under the directory---
python -m venv env

---Activate Python virtual environment---
.\env\Scripts\activate

---Install all the dependencies for development---
pip install -r requirements.txt
pip install -r requirements_dev.txt


## Running the checks
---Activate Python virtual environment if you havn't---
.\env\Scripts\activate

---Install the git hook scripts---
git init
pre-commit install

---Run checks---
pre-commit run --all-files

![Screenshot_2](https://user-images.githubusercontent.com/59043071/171103906-8c6aa086-4522-4f34-b1c4-f98b802577b7.jpg)
