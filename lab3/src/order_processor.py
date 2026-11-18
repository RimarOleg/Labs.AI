# src/order_processor.py


def calculate_order_total(
    base_price: float,
    quantity: int,
    coupon_code: str | None = None,
    is_member: bool = False,
) -> float:
    """
    Розраховує загальну вартість замовлення з урахуванням кількості,
    статусу учасника програми лояльності, купона та вартості доставки.
    """
    if base_price < 0:
        raise ValueError("Base price cannot be negative")
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero")

    subtotal = base_price * quantity

    if is_member:
        subtotal *= 0.90

    if coupon_code == "SUMMER20":
        subtotal *= 0.80
    elif coupon_code == "VIP50":
        subtotal -= 50.0
        if subtotal < 0:
            subtotal = 0.0
    elif coupon_code is not None and coupon_code != "":
        raise ValueError("Invalid coupon code")

    if 0 < subtotal < 100.0:
        subtotal += 15.0

    return round(subtotal, 2)
