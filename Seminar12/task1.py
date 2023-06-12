import json
from typing import Any

class Factorial:

    def __init__(self, amount: int = 2) -> None:
        self.results = []
        self.amount = amount

    def __call__(self, limit: int = 10) -> list[int]:
        if limit < 0:
            raise ValueError("Incomtible value")
        if limit in (0, 1):
            self.results.append(1)
        else:
            result = 1
            for i in range(1, limit + 1):
                result *= i
                self.results.append(result)
                if len(self.results)>self.amount:
                    self.results.pop(0)
        return self
    
    def __repr__(self):
        return f'{self.results}'
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        with open('result.json', 'w', encoding = "UTF - 8") as file:
            json.dump(self.results, file)

def main():
    with Factorial(5)(5) as fact:
        print(fact)

if __name__ == '__main__':
    main()