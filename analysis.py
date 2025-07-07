def analyze_water_data(df):
    return {
        "water_loss": {
            "water_loss_percentage": 35.2,
            "total_water_loss": 12000,
            "financial_loss": 48000
        },
        "efficiency_indicators": {
            "coverage_index": 91.5,
            "average_consumption": 128.4,
            "billed_consumed_ratio": 0.87
        },
        "time_series": {
            "dates": ["2023-01", "2023-02"],
            "values": [120, 130]
        }
    }

def generate_insights(analysis):
    return [
        "Alta perda de água identificada: 35.2%",
        "Índice de cobertura está dentro do esperado",
        "Consumo médio por ligação elevado"
    ]
