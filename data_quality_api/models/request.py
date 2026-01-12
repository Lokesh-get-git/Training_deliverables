from pydantic import BaseModel
from typing import List, Dict, Any

class DataPayload(BaseModel):
    data: List[Dict[str, Any]]
