#! /usr/bin/env bash

source sql_app/venv/bin/activate
uvicorn sql_app.main:app --reload
