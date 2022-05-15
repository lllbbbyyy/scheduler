from fastapi import APIRouter

from ..page.index import router as index_router
from ..page.subject_upload import router as subject_upload_router
from ..page.teacher_info import router as teacher_info_router
from ..page.exam_list import router as exam_list_router
from ..page.statistics import router as statistics_router

router = APIRouter(prefix='/page', tags=['page'])

router.include_router(index_router)
router.include_router(subject_upload_router)
router.include_router(teacher_info_router)
router.include_router(exam_list_router)
router.include_router(statistics_router)
