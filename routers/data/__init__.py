from fastapi import APIRouter

from ..data.subject_info import router as subject_router
from ..data.teacher_info import router as teacher_router
from ..data.teacher_coursetable_info import router as teacher_coursetable_router
from ..data.exam_info import router as exam_router
from ..data.statistics import router as statistics_router

router = APIRouter(prefix='/data', tags=['data'])

router.include_router(subject_router)
router.include_router(teacher_router)
router.include_router(teacher_coursetable_router)
router.include_router(exam_router)
router.include_router(statistics_router)