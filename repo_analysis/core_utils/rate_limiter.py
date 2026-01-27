from core_utils.config import MAX_DIGITS, MAX_ABS_VALUE

class MemoryLimiter:
    def is_safe_input(self, value_str: str) -> bool:
        digits = value_str.replace(".", "").replace("-", "")
        return len(digits) <= MAX_DIGITS

    def is_safe_value(self, value: float) -> bool:
        return abs(value) <= MAX_ABS_VALUE
