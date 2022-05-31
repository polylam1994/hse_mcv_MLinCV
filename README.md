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
pip install -r requirements_dev.txt


## Running the checks
---Activate Python virtual environment if you havn't---
.\env\Scripts\activate

---Run checks---
pre-commit run --all-files
