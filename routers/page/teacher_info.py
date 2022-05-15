from fastapi.responses import HTMLResponse
from fastapi import Request, APIRouter
from .page_common import templates, config

router = APIRouter()


@router.get("/teacher_info", response_class=HTMLResponse)
async def render_page(request: Request):
    config['request'] = request
    return templates.TemplateResponse('teacher_info.html', config)
