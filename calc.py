from logging import raiseExceptions


class Calc:
    def get_divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("분모가 0일 수 없습니다.")
        return a / b

