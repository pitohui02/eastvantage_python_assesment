from pydantic import BaseModel, constr, confloat, conint
from typing import Annotated, Optional

# Models for Validation 

class AddAddress(BaseModel):
    label: Annotated[str, constr(min_length=1, max_length=50)]
    address: Annotated[str, constr(min_length=5, max_length=100)]
    latitude: Annotated[float, confloat(ge=-90, le=90)]
    longitude: Annotated[float, confloat(ge=-180, le=180)]
    
class UpdateAddress(BaseModel):
    label: Optional[Annotated[str, constr(min_length=1, max_length=100)]] = None
    address: Optional[Annotated[str, constr(min_length=5, max_length=100)]] = None
    latitude: Optional[Annotated[float, confloat(ge=-90, le=90)]] = None
    longitude: Optional[Annotated[float, confloat(ge=-180, le=180)]] = None
    
class GetCoordinates(BaseModel):
    radius: Annotated[int, conint(gt=1)]
    latitude: Annotated[float, confloat(ge=-90, le=90)]
    longitude: Annotated[float, confloat(ge=-180, le=180)]
    