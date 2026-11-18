from typing import Generic, Optional, TypeVar, Callable, List, Dict, Any

T = TypeVar("T")


class EquipmentManager(Generic[T]):
    """Менеджер для обліку обладнання та довільних елементів.

    Attributes:
        owner: Власник інвентарю.
        items: Список елементів у сховищі.
    """

    def __init__(self, owner: str) -> None:
        self.owner: str = owner
        self.items: List[Dict[str, Any]] = []

    def add_item(self, name: str, category: str, price: float) -> Dict[str, Any]:
        """Додає новий елемент до інвентарю.

        Args:
            name: Назва обладнання.
            category: Категорія обладнання.
            price: Вартість одиниці.

        Returns:
            Словник із доданим елементом.
        """
        item = {"name": name, "category": category, "price": price}
        self.items.append(item)
        return item

    def find_items(
        self, predicate: Callable[[Dict[str, Any]], bool]
    ) -> List[Dict[str, Any]]:
        """Шукає елементи за заданою умовою (предикатом).

        Args:
            predicate: Функція-умова для фільтрації елементів.

        Returns:
            Список знайдених елементів.
        """
        result: List[Dict[str, Any]] = []
        for item in self.items:
            if predicate(item):
                result.append(item)
        return result

    def get_total_value(self) -> float:
        """Обчислює загальну вартість усього обладнання.

        Returns:
            Сумарна вартість (float).
        """
        total = 0.0
        for item in self.items:
            total += float(item["price"])
        return total

    def get_newest_item(self) -> Optional[Dict[str, Any]]:
        """Повертає останній доданий елемент або None, якщо інвентар порожній.

        Returns:
            Останній словник-елемент або None.
        """
        if not self.items:
            return None
        return self.items[-1]
