from fastapi import BackgroundTasks
import time
from fastapi import FastAPI

app = FastAPI()

def send_email(email: str, message: str):
    time.sleep(2)
    print(f"Email sent to {email} with message: {message}")

def write_log(text: str):
    print(f"Log entry: {text}")

@app.post("/send-notification/")
def send_notification(email: str, message: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email, email, message)
    background_tasks.add_task(write_log, f"Notification sent to {email}")
    return {"message": "Notification is being sent in the background"}

