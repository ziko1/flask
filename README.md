---
title: Flask
description: A popular minimal server framework for Python
tags:
  - python
  - flask
---

# Python Flask Example

This is a [Flask](https://flask.palletsprojects.com/en/1.1.x/) app that serves a simple JSON response.

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/zUcpux)

## ✨ Features

- Python
- Flask

## 💁‍♀️ How to use

- Install Python requirements `pip install -r requirements.txt`
- Start the server for development `python3 main.py` (localhost only; debug disabled).
- Production: `gunicorn main:app --bind 0.0.0.0:${PORT:-5000}`.
- Health: `GET /health`; tests: `python -m unittest -v`.
- Dependencies are pinned and verified in Python 3.12. This repository remains a minimal service template; no business application is claimed.
