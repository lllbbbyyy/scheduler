from fastapi.responses import HTMLResponse
from fastapi import Request, APIRouter
from .templates import templates

router = APIRouter()


@router.get("/subject_upload", response_class=HTMLResponse)
async def render_page(request: Request):
    return templates.TemplateResponse('subject_upload.html', {"request": request})


