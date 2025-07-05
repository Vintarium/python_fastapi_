import mimetypes
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="html_pages")


my_app = FastAPI()


@my_app.get("/")
async def root():
    return FileResponse("html_pages/index.html")

@my_app.post("/calc")
async def calc_plus(

    request: Request,
    num1: str = Form(...),
    num2: str = Form(...),
    operation:  str = Form(...)):

    if num1.isdigit() and num2.isdigit():
        
        if operation == "+":
            result = int(num1) + int(num2)
        elif operation == "-":
            result = int(num1) - int(num2)
        elif operation == "*":
            result = int(num1) * int(num2)
        elif operation == "/":
            result = int(num1) / int(num2)
        else:
            return FileResponse("html_pages/errorOperation.html")

        return templates.TemplateResponse(
                "result.html",
                {"request": request, "result": result}
            )
    else:
        return FileResponse("html_pages/operandError.html")





# localhost:8000/calc_divide?num1=10&num2=2


# @my_app.get("/")
# async def root():
#     return FileResponse("index.html")
