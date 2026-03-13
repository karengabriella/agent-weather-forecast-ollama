
def rain_description(mm: float) -> str:
    
    if mm == 0:
        return " Sem previsão de chuva"
    
    elif mm < 2:
        return " Garoa leve"
    
    elif mm < 10:
        return " Chuva leve"
    
    elif mm < 25:
        return " Chuva moderada"
    
    elif mm < 50:
        return " Chuva forte"
    
    else:
        return " Chuva intensa"
    

def will_rain(mm: float) -> bool:
    return mm >= 0.1