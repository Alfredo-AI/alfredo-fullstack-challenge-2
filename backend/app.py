from fastapi import FastAPI


app = FastAPI(title = "Alfredo Fullstack Challenge")


@app.get("/complaints")
async def get_complaints():
    return []