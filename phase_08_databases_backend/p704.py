from fastapi import FastAPI, HTTPException, status

app = FastAPI()
users = {1: {"name": "Alice"}, 2: {"name": "Bob"}, 3: {"name": "Carol"}}

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    if user_id in users:
        return {"user_id": user_id, "name": users[user_id]["name"]}
    else:
        raise HTTPException(status_code=404, detail="User not found")
    
@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    if user_id in users:
        del users[user_id]
        return {"message": f"User {user_id} deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="User not found")
    
@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(name: str):
    new_id = max(users.keys()) + 1
    users[new_id] = {"name": name}
    return {"message": f"User '{name}' created successfully!", "user_id": new_id}


