# CSC_exercise

I used a (.venv) virtual environment and uvicorn to run my application on port 8080.

Before running the application you need to add your own ClientID and ClientSecret in to the main.py  

When creating OAuth app in github, you need to set homepage URL as (http://localhost:8080) and Authorization callback URL as (http://localhost:8080/callback).

When running the application, you need to open your browser and navigate to "http://localhost:8080".

To log in via GitHub, you should visit "http://localhost:8080/login".

After logging in, the application fetches the desired data from GitHub and presents it in a neat JSON format.

I have also added additional specifications to the source code.

