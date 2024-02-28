
from fastapi import FastAPI
from starlette.responses import RedirectResponse
import httpx

app = FastAPI()

#Add your ClientID and ClientSecret here. 
ClientID = ""
ClientSecret = ""



app = FastAPI()
#This method returns introductions to use FastAPI application. 
@app.get("/")
async def root():
    return {"Info": "Click on 'http://localhost:8080/login' to log in via GitHub, and after that, you will have access to all starred repositories."}


#This method redirects the user to the GitHub login page. 
@app.get("/login")
async def login():
    return RedirectResponse(f"https://github.com/login/oauth/authorize?client_id={ClientID}", status_code=302)


#This method waits for the authorization code and uses it along with the ClientID and ClientSecret to request an access token.
#After receiving the access token, it uses it to fetch users information in JSON format.
@app.get("/callback")
async def callback(code: str):
    
    params = {
        "client_id": ClientID,
        "client_secret": ClientSecret,
        "code": code
    }


    headers = {"Accept":"application/json"}

    #Here, it gets the access_token. 
    async with httpx.AsyncClient() as client:
            response = await client.post(url="https://github.com/login/oauth/access_token", params=params, headers=headers)
    json = response.json()   

    acc_token = json["access_token"]


    #Here, it fetches information such as starred repositories and their details.
    async with httpx.AsyncClient() as client:
         headers.update({"Authorization": f"Bearer {acc_token}"})
         response = await client.get("https://api.github.com/user/starred", headers=headers) 

    repositories = response.json()

    #Here, it presents information in neat JSON format. 
    amount = 0
    ParsedJson = {}   
    
    for i in repositories:
         amount += 1
         repository = {"repository:"+i["full_name"]:{"Repository name":i["full_name"], "Description":i["description"], "URL":i["html_url"], "License":i["license"], "Topics":i["topics"]}}
         ParsedJson.update(repository)
         
         
    ParsedJson.update({"Number of starred repositories":amount})                           
    return ParsedJson