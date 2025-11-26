from fastapi import UploadFile
import csv
import io

def upload_csv(file: UploadFile):
    if file.content_type != "text/csv":
         return {"error": "File is NOT a CSV"}

    content = file.file.read().decode("utf-8")

    reader = csv.reader(io.StringIO(content))
    header = next(reader)
    rows = list(reader)

    for line in rows:
        print(line)

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "columns": header,
        "data": rows[0:5]
    }