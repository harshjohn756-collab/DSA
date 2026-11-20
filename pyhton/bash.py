# from fastapi import  FastAPI

# from enum import Enum

# class UserName(str, Enum):
#     HarshithaBhat = "Harshitha Bhat"
#     HarshaA = "Harsha A"
#     Harshithps = "Harshith P S"
#     HarshaB = "Harsha B"

# app = FastAPI()

# @app.get("/Users/{input_name}")
# async def read_users(input_name : UserName):

#     if input_name.value == "Harshitha Bhat":
#         return {"Name":input_name,
#                 "Sill":"Web Developer"
#                 }
                
#     if input_name.value == "Harsha A":
#         return {"Name":input_name , 
#                 "Skill":"Backend Developer"
#                 }
    
#     if input_name.value == "Harshith P S":
#         return {
#             "Name":input_name,
#             "Skill":"FrontEnd Developer"
#         }


#     return {
#             "Name":input_name,
#             "Skill":"DSA enthusiasist "
#             }

from fastapi import FastAPI
from enum import Enum

class Name(str, Enum):
    Harsha = "Harsha A"
    harshitha_bhat = "Harshitha Bhat"

app = FastAPI()

@app.get("/Users/{Input_users}")
async def Informaton_users(Input_users: Name):
    if Input_users.value == "Harsha A":
        return {
            "name": Input_users,
            "about": "Backend Developer"
        }
    if Input_users.value == "Harshitha Bhat":
        return {
            "name": Input_users,
            "about": "Full Stack"
        }

    return {
        "name": Input_users,
        "about": "Unknown user"
    }