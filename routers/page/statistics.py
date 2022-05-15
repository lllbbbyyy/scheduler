from fastapi.responses import HTMLResponse
from fastapi import Request, APIRouter
from .page_common import templates, config

router = APIRouter()


@router.get("/statistics_select", response_class=HTMLResponse)
async def render_page(request: Request):
    config['request'] = request
    return templates.TemplateResponse('statistics_select.html', config)


@router.get("/statistics", response_class=HTMLResponse)
async def render_page(grade: str, request: Request):
    config['request'] = request
    tmp_config = config.copy()
    tmp_config['grade'] = grade
    return templates.TemplateResponse('statistics.html', tmp_config)

@router.get("/statistics/duty", response_class=HTMLResponse)
async def render_page(request: Request):
    config['request'] = request
    return templates.TemplateResponse('statistics_duty.html', config)

@router.get("/statistics/charge", response_class=HTMLResponse)
async def render_page(request: Request):
    config['request'] = request
    return templates.TemplateResponse('statistics_charge.html', config)
