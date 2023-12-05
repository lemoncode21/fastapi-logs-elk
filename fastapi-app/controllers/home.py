from fastapi import APIRouter
import logging

# Get logger for module
LOGGER = logging.getLogger(__name__)

router = APIRouter(
    prefix="/home",
    tags=['home']
)


@router.get("")
async def welcome_home():
    LOGGER.info("Welcome lemoncode21!")
    return "welcome lemoncode21"

@router.get("/test")
async def test_home():
    LOGGER.info("welcome page test!")
    return "welcome page test!"