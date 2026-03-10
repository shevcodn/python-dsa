from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    return {"filename": file.filename, "content_type": file.content_type, "size": len(content)}

@app.post("/upload-multiple/")
async def upload_multiple_files(files: list[UploadFile] = File(...)):
    results = []
    for file in files:
        content = await file.read()
        results.append({"filename": file.filename, "content_type": file.content_type, "size": len(content)})
    return results
    
