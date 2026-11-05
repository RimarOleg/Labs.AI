from dataclasses import dataclass
from enum import Enum

class ItemType(Enum):
    A= "A"
    B= "B"
    C= "C"

@dataclass
class ProcessorInput:
    type: str | None
    amount: float
    status: str

GLOBAL_DISCOUNT= 0.1
GLOBAL_TAX_RATE= 0.2

def _calculate_type_a(amount: float) -> float:
    if amount< 0:
        raise ValueError("Amount cannot be negative")
    if amount> 1000:
        return amount * (1-GLOBAL_DISCOUNT) * (1+GLOBAL_TAX_RATE)
    if amount> 500:
        return amount * (1- 0.05)* (1+GLOBAL_TAX_RATE)
    return amount * (1+GLOBAL_TAX_RATE)

def _calculate_type_b(amount: float, status: str)-> float:
    match status:
        case "vip":
            return amount*0.8
        case "regular":
            return amount*0.9 if amount > 200 else amount
        case _:
            return 0 if amount== 0 else amount* 1.15

def _calculate_type_c(amount: float) -> float:
    if amount< 0:
        raise ValueError("Negative amount for type C")
    total= amount
    for i in range(3):
        total += i*10
    return total

def process(payload: dict) -> dict:
    data = ProcessorInput(
        type=payload.get("type"),
        amount=payload.get("amount", 0),
        status=payload.get("status", "new")
    )
    
    match data.type:
        case "A":
            total= _calculate_type_a(data.amount)
        case "B":
            total= _calculate_type_b(data.amount, data.status)
        case "C":
            total= _calculate_type_c(data.amount)
        case None:
            total= 0
        case _:
            total= data.amount* 1.2
            
    return{"type": data.type, "final_total": total, "status": data.status}