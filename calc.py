from logging import raiseExceptions


class Calc:


    def get_divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("분모가 0일 수 없습니다.")
        return a / b

    def get_nzegop(self, a:int, n:int):
        return a**n

    def get_sum(self, a, b):
        return  a + b

