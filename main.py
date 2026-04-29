from fastapi import FastAPI,Query,Path,Form,Body,status,HTTPException
from fastapi.responses import JSONResponse
import time



app=FastAPI()

costs=[
    {"ID":1,"descripsion":"car","amount":432},
    {"ID":2,"descripsion":"house","amount":890},
    {"ID":3,"descripsion":"computer","amount":100},
    {"ID":4,"descripsion":"loptop","amount":89},
    {"ID":5,"descripsion":"book","amount":43},
    {"ID":6,"descripsion":"table","amount":51},
    {"ID":7,"descripsion":"game","amount":30},
    {"ID":8,"descripsion":"glass","amount":11},
    {"ID":9,"descripsion":"fuset","amount":23},
    {"ID":10,"descripsion":"food","amount":97},
]

@app.post("/costs",status_code=status.HTTP_201_CREATED)
def creat_cost(id:int=Body(),name:str=Body(),amount:float=Body()):
    for cost in costs:
        if cost["ID"]==id:
            return {"message":"ID mavjod ast"}
        else:
            new_data={"ID":id,"descripsion":name,"amount":amount}
            costs.append(new_data)
            return {"message":"item is sppend"}


@app.get("/costs",status_code=status.HTTP_200_OK)
def print_list_costs():
    return costs



@app.get("/costs/{id}")
def creat_cost(id:int=Path):
    for cost in costs:
        if cost["ID"]==id:
            return cost
        
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND)



@app.put("/costs",status_code=status.HTTP_202_ACCEPTED)
def update_cost(id:int=Body(),name:str=Body(),amount:float=Body()):
    for cost in costs:
        if cost["ID"]==id:
            cost["descripsion"]=name
            cost["amount"]=amount
            return cost
            # raise HTTPException(status_code=status.HTTP_200_OK,detail="item is update")
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="opject not found")



@app.delete("/cost",status_code=status.HTTP_204_NO_CONTENT)
def delet_cost(id:int=Body(embed=True)):
    for cost in costs:
        if cost["ID"]==id:
            costs.remove(cost)
            return {"message":"item id delet"}
    
    HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="opject not found")