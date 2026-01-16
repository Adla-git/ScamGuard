## ScamGuard AI

Objective - To detect the scam messages.

LLM Used: gemini-2.5-flash-lite

## Steps to use repository

- Clone this repo

- Create a virtual environment

    - python3 -m venv scamguard

- Activate virtual environment

    - source /Users/xxxxxx/xxxxxx/python/ScamGuard/scamguard/bin/activate

- Install dependencies

    - pip install -r requirements.txt


## Project Sttucture:

Scam_Guard_AI

- experments
    - ex1.py

- llm
    - prompts

- pipline
    - scam_detector

- streamlit
    - app.py

- main.py

- utils.py

- config.py

- requirements.txt

## Project Structure Description

- Scam_Guard_AI - Root folder for the Scam Detection AI project

- experiments >> Sandbox area for testing ideas and experiments

- workflow.ipynb - Notebook to experiment, test prompts, and run trial code

- llm - All Large Language Model–related code and assets

- prompts - Stores reusable LLM prompt templates and examples

- pipline - Core processing logic of the application

- scam_detector -Implements the scam detection workflow and decision logic

- streamlit -Frontend/UI layer for the application

- app.py - Streamlit app to take user input and display scam results

- main.py - Entry point to run scam detection without the UI

- utils.py - Common helper functions shared across modules

- config.py -Central place for configuration and environment settings

- requirements.txt - List of Python dependencies required to run the project