from fastapi import APIRouter

from ..page.index import router as index_router
from ..page.subject_info import router as subject_info_router
from ..page.teacher_info import router as teacher_info_router
from ..page.exam_info import router as exam_info_router
from ..page.statistics import router as statistics_router

router = APIRouter(prefix='/page', tags=['page'])

router.include_router(index_router)
router.include_router(subject_info_router)
router.include_router(teacher_info_router)
router.include_router(exam_info_router)
router.include_router(statistics_router)
