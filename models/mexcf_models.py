from pydantic import BaseModel
from typing import List, Dict


class ContractInfo(BaseModel):
    symbol: str


class RespGetContractInfo(BaseModel):
    success: bool
    code: int
    data: List[ContractInfo]
