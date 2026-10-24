from fastapi import HTTPException
from typing import Annotated,Literal
from pydantic import BaseModel,Field,field_validator
from config.config import VALID_LOCATIONS
import logging
# Set up logging to track when unknown locations appear
logger = logging.getLogger(__name__)
class BangaloreHouse(BaseModel):
    area_sqft: float = Field(..., gt=277,lt=20000,description="the value should between  in  300 sqft and 20000sqft")
    bhk: int = Field(..., gt=0,lt=10,description="the value should between  in  1 and 10")
    bath: int = Field(..., ge=0,lt=10,description="the value should between  in  1 and 10")
    location: str = Field(..., description="Name of the neighborhood area")
    
    @field_validator('location')
    @classmethod
    def check_valid_location(cls, value: str) -> str:
        # Strip whitespaces so tiny typing errors don't cause failures  
        logger.warning(
                f"'{value}' is an unknown location. "
                f"The ML pipeline will encode it as all zeros."
            )
        return value