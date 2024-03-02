from fastapi import APIRouter
from .audit.router import router as auth_router

router = APIRouter()
router.include_router(auth_router, prefix="/company/audit", tags=["audit-company"])
