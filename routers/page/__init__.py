from fastapi import APIRouter

from ..page.index import router as index_router
from ..page.upload import router as upload_router

router = APIRouter(prefix='/page', tags=['page'])

router.include_router(index_router)
router.include_router(upload_router)
