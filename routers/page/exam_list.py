from fastapi.responses import HTMLResponse
from fastapi import Request, APIRouter
from .page_common import templates, config

router = APIRouter()


@router.get("/exam_list", response_class=HTMLResponse)
async def render_page(request: Request):
    config['request'] = request
    return templates.TemplateResponse('exam_list.html', config)
