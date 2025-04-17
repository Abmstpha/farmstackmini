from enum import Enum
from pydantic import BaseModel
class MLModels(Enum):
    LINEAR_REGRESSION = "linear_regression"
    LOGISTIC_REGRESSION = "logistic_regression"


class User(BaseModel):
    id: int
    name: str
    age: int
    salary: int
    has_car: bool
    has_house: bool
    has_job: bool
    has_education: bool
    has_children: bool
    has_pet: bool
    has_insurance: bool