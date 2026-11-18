# tests/test_order_processor.py (Версія 2: Розширена з Edge Cases та купонами)
import pytest
from src.order_processor import calculate_order_total


@pytest.mark.parametrize(
    "base_price, quantity, coupon_code, is_member, expected",
    [
        # Базові випадки без знижок і купонів (з доставкою, бо < 100)
        (50.0, 1, None, False, 65.0),  # 50.0 + 15 доставка = 65.0
        (120.0, 1, None, False, 120.0),  # Без доставки (> 100)
        # Перевірка кількості та знижки учасника (10%)
        (100.0, 2, None, True, 180.0),  # (200 * 0.9) = 180.0
        # Перевірка купона SUMMER20 (знижка 20%)
        (200.0, 1, "SUMMER20", False, 160.0),  # 200 * 0.8 = 160.0
        # Перевірка купона VIP50 (фіксоване мінус 50)
        (250.0, 1, "VIP50", False, 200.0),  # 250 - 50 = 200.0
        # Перевірка купона VIP50 з Edge Case (занулення суми та додавання доставки)
        (30.0, 1, "VIP50", False, 0.0),  # 30 - 50 = 0.0 + 15 доставка = 15.0
        # Порожній рядок купона (еквівалент відсутності)
        (100.0, 1, "", False, 100.0),
    ],
)
def test_calculate_order_total_valid(
    base_price: float,
    quantity: int,
    coupon_code: str | None,
    is_member: bool,
    expected: float,
) -> None:
    assert (
        calculate_order_total(base_price, quantity, coupon_code, is_member) == expected
    )


@pytest.mark.parametrize(
    "base_price, quantity, coupon_code, is_member",
    [
        (-10.0, 1, None, False),  # Негативна ціна -> ValueError
        (100.0, 0, None, False),  # Нульова кількість -> ValueError
        (100.0, -2, None, False),  # Негативна кількість -> ValueError
        (100.0, 1, "BADCOUPON", False),  # Невалідний купон -> ValueError
    ],
)
def test_calculate_order_total_exceptions(
    base_price: float, quantity: int, coupon_code: str | None, is_member: bool
) -> None:
    with pytest.raises(ValueError):
        calculate_order_total(base_price, quantity, coupon_code, is_member)
