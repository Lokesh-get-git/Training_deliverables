from fastapi import APIRouter, HTTPException
from analyzers.missing import analyze_missing
from analyzers.outliers import analyze_outliers
from analyzers.feature_inference import analyze_feature_inference

from models.request import DataPayload

router = APIRouter(prefix="/v1/data-quality")

@router.post("/missing")
def missing_analysis(payload: DataPayload):
    try:
        return analyze_missing(payload.data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.post("/outliers")
def outlier_analysis(payload: DataPayload):
    try:
        return analyze_outliers(payload.data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.post("/feature-inference")
def feature_inference(payload: DataPayload):
    try:
        return analyze_feature_inference(payload.data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))