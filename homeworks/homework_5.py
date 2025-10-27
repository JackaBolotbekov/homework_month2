# ДЗ + с ДОП заданиями!

class Distance:
    measurement = {
        "mm": 0.001, "миллиметр": 0.001, "миллиметры": 0.001, "мм": 0.001,
        "cm": 0.01, "сантиметр": 0.01, "сантиметры": 0.01, "см": 0.01,
        "m": 1.0, "meter": 1.0, "meters": 1.0, "метр": 1.0, "метры": 1.0, "м": 1.0,
        "km": 1000.0, "kilometer": 1000.0, "kilometers": 1000.0,
        "километр": 1000.0, "километры": 1000.0, "км": 1000.0,
    }
    # Нормализуем в базовые ключи (для вывода)
    normal_form = {
        "мм": "mm", "миллиметр": "mm", "миллиметры": "mm",
        "см": "cm", "сантиметр": "cm", "сантиметры": "cm",
        "м": "m", "метр": "m", "метры": "m", "meter": "m", "meters": "m",
        "км": "km", "километр": "km", "километры": "km",
    }

    def __init__(self, value, unit):
        self.value = float(value)
        self.unit = self._normalize_unit(unit)

    # ---------- ошибочные ----------
    @classmethod
    def _normalize_unit(cls, unit: str) -> str:
        u = str(unit).strip().lower()
        if u in cls.normal_form:
            u = cls.normal_form[u]
        if u not in cls.measurement:
            raise ValueError(f"Неподдерживаемая единица измерения: {unit}")
        return u

    def _to_meters(self) -> float:
        return self.value * self.measurement[self.unit]

    @classmethod
    def _from_meters(cls, meters: float, unit: str) -> float:
        return meters / cls.measurement[unit]

    @staticmethod
    def _fmt(x: float) -> str:
        s = f"{x:.6f}".rstrip("0").rstrip(".")
        return s if s else "0"

    # ---------- магические методы ----------
    def __str__(self) -> str:
        return f"{self._fmt(self.value)} {self.unit}"

    def __add__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        total_m = self._to_meters() + other._to_meters()
        return Distance(self._from_meters(total_m, self.unit), self.unit)  # результат в единицах левого операнда

    def __sub__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        diff_m = self._to_meters() - other._to_meters()
        if diff_m < 0:
            raise ValueError("Результат вычитания расстояний не может быть отрицательным.")
        return Distance(self._from_meters(diff_m, self.unit), self.unit)

    # сравнения (учитываем единицы)
    def __eq__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        return abs(self._to_meters() - other._to_meters()) < 1e-9

    def __lt__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        return self._to_meters() < other._to_meters() - 1e-9

    def __le__(self, other):
        return self == other or self < other

    def __gt__(self, other):
        return not (self <= other)

    def __ge__(self, other):
        return not (self < other)

    # ---------- конвертация ----------
    def convert(self, target_unit: str):
        target_unit = self._normalize_unit(target_unit)
        meters = self._to_meters()
        return Distance(self._from_meters(meters, target_unit), target_unit)


d1 = Distance(10, "m")
d2 = Distance(2, "km")
d3 = Distance(150, "cm")
d4 = Distance(5000, "мм")  # русские обозначения тоже работают

print("Инициализация и вывод:")
print(d1)  # 10 m
print(d2)  # 2 km
print(d3)  # 150 cm
print(d4)  # 5000 mm

print("\nСложение (+):")
print(d1 + d2)  # в метрах левого операнда: 10 m + 2 km = 2010 m
print(d3 + d4)  # 150 cm + 5000 mm = 150 cm + 500 cm = 650 cm

print("\nВычитание (-):")
print(
    d2 - d1)
try:
    print(d1 - d2)  # должно бросить ошибку (нельзя отрицательно)
except ValueError as e:
    print("Ошибка:", e)

print("\nСравнения:")
print(Distance(1000, "m") == Distance(1, "km"))  # True
print(Distance(100, "cm") < Distance(2, "m"))  # True
print(Distance(500, "mm") >= Distance(0.4, "m"))  # True

print("\nКонвертация единиц:")
print(d2.convert("m"))  # 2000 m
print(d1.convert("cm"))  # 1000 cm
