import csv
import io
import uvicorn
from fastapi import FastAPI, File, HTTPException, UploadFile

app = FastAPI()

@app.post("/upload-csv")
def upload_csv(file: UploadFile = File(...)):
    if file.content_type != "text/csv":
        return{"error": "File must be a CSV"}

    content = file.file.read()

    try:
        decoded = content.decode("utf-8")
    except UnicodeDecodeError:
        raise HTTPException(status_code=400, detail="The file is not encoded correctly.")

    reader = csv.reader(io.StringIO(decoded))
    rows = [row for row in reader]

    return {
        "message": "CSV load",
        "rows_count": len(rows),
        "data": rows,
    }


     
        


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
