
class RectError(Exception):
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def __str__(self):
        if self.a <= 0 and self.b <= 0:
            return f"Error: Невалидное значение обеих сторон = {self.a}; {self.b}"
        else:
            if self.a <= 0:
                return f"Error: Невалидное значение стороны = {self.a} "
            else:
                return f"Error: Невалидное значение стороны = {self.b}"

class MatrError(Exception):
    def __init__(self, operation: str):
        self.operation = operation

    def __str__(self):
        if self.operation == '+':
            return f"Error: Нельзя складывать матрицы разных размеров"
        elif self.operation == '*':
            return f"Error: Размеры матриц не подходят для перемножения"
        else:
            return f"Error: Нельзя сравнивать матрицы разных размеров"