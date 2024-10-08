from fastapi import APIRouter

from .demo.views import router as puzzle_demo_router

router = APIRouter()

# Include puzzle routes. Name entered into database should match the prefix.
router.include_router(puzzle_demo_router, prefix="/demo")


# Include a route to catch all invalid puzzle routes so we can throw a custom 404.
@router.get("/{path:path}/")
async def catch_all(path: str):
    pass
