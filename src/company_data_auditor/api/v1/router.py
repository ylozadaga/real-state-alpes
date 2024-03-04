from fastapi import APIRouter
from .audit.router import router as audit_router

router = APIRouter()
router.include_router(audit_router, prefix="/company/audit", tags=["audit-company"])
