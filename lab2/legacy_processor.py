# legacy_processor.py
GLOBAL_DISCOUNT= 0.1
GLOBAL_TAX_RATE= 0.2
last_processed_status= None

def process(payload: dict)-> dict:
    global last_processed_status
    total= 0
    ptype= payload.get("type")
    amount= payload.get("amount", 0)
    user_status= payload.get("status", "new")
    
    if ptype== "A":
        if amount> 1000:
            total= amount * (1-GLOBAL_DISCOUNT)* (1+GLOBAL_TAX_RATE)
        elif amount> 500:
            total= amount * (1-0.05)*(1+GLOBAL_TAX_RATE)
        else:
            if amount< 0:
                raise ValueError("Amount cannot be negative")
            total= amount* (1 + GLOBAL_TAX_RATE)
    elif ptype== "B":
        if user_status== "vip":
            total= amount* 0.8
        elif user_status== "regular":
            if amount> 200:
                total= amount* 0.9
            else:
                total= amount
        else:
            if amount== 0:
                total= 0
            else:
                total= amount* 1.15
    elif ptype== "C":
        if amount< 0:
            raise ValueError("Negative amount for type C")
        i= 0
        while i< 3:
            amount+= i* 10
            i+= 1
        total= amount
    else:
        if ptype is None:
            total = 0
        else:
            total = amount * 1.2
            
    last_processed_status= user_status
    return{"type": ptype, "final_total": total, "status": user_status}