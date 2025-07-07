from pydantic import BaseModel
from typing import Dict, Any, List
from datetime import datetime

class WaterLossAnalysis(BaseModel):
    water_loss_percentage: float
    total_water_loss: float
    financial_loss: float

class EfficiencyIndicators(BaseModel):
    coverage_index: float
    average_consumption: float
    billed_consumed_ratio: float

class TimeSeriesData(BaseModel):
    dates: List[str]
    values: List[float]

class Analysis(BaseModel):
    water_loss: WaterLossAnalysis
    efficiency_indicators: EfficiencyIndicators
    time_series: TimeSeriesData

class AnalysisResult(BaseModel):
    analysis: Analysis
    insights: List[str]
    timestamp: str
    filename: str
