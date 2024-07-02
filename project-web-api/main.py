from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI() # เริ่มต้นกำหนด api ในการตั้งค่าต่างๆ

# เชื่อมต่อไฟล์ templates ด้วยการเข้าถึง html หรือ ใช้ในการเชื่อมต่อ ไฟล์ main.html นั้นเอง
templates = Jinja2Templates(directory="templates") 

# ดึง directory ไฟล์ css 
app.mount("/CSS_file", StaticFiles(directory="CSS_file"), name="CSS_file")

# ดึง directory ไฟล์ icon
app.mount("/imagess", StaticFiles(directory="imagess"), name="imagess")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})