from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import pandas as pd
import io
from datetime import datetime
from app.analysis import analyze_water_data, generate_insights
from app.schemas import AnalysisResult

app = FastAPI(title="Saneamento Analytics API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze", response_model=AnalysisResult)
async def analyze_file(file: UploadFile = File(...)):
    if not file.filename.endswith(('.xlsx', '.csv')):
        raise HTTPException(status_code=400, detail="Formato de arquivo inválido. Apenas .xlsx ou .csv são aceitos.")

    try:
        content = await file.read()

        if file.filename.endswith('.xlsx'):
            df = pd.read_excel(io.BytesIO(content))
        else:
            df = pd.read_csv(io.BytesIO(content), encoding='utf-8', sep=';')

        analysis = analyze_water_data(df)
        insights = generate_insights(analysis)

        return {
            "analysis": analysis,
            "insights": insights,
            "timestamp": datetime.now().isoformat(),
            "filename": file.filename
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar arquivo: {str(e)}")

@app.get("/")
def read_root():
    return {"message": "Saneamento Analytics API - Envie um arquivo para /analyze"}
