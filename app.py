from fastapi.responses import FileResponse
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="html_pages")

my_app = FastAPI()

@my_app.get("/")
async def root():
    request: Request
    return templates.TemplateResponse("index.html",{"request" : request})
    # return FileResponse("html_pages/index.html")

@my_app.post("/calc")
async def calc_plus(

    request: Request,
    num1: str = Form(...),
    num2: str = Form(...),
    operation:  str = Form(...)):

    try:
        if operation == "+":
            result = float(num1) + float(num2)
        elif operation == "-":
            result = float(num1) - float(num2)
        elif operation == "*":
            result = float(num1) * float(num2)
        elif operation == "/":
            if  float(num2) == 0:
                return templates.TemplateResponse("division_by_zero.html", {"request" : request})
            result = float(num1) / float(num2)
        else:
            return templates.TemplateResponse("errorOperation.html", {"request": request})

        return templates.TemplateResponse(
                "result.html",
                {"request": request, "result": result}
            )
    except ValueError:
        return templates.TemplateResponse("operandError.html",{"request": request})

