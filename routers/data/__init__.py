from fastapi import APIRouter

from ..data.subject_info import router as subject_router

router = APIRouter(prefix='/data', tags=['data'])

router.include_router(subject_router)