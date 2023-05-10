from task2 import puzzle_solver, show_results
import random

if __name__ == '__main__':
    puzzle_solver('Зимой и летом одним цветом:', random.randint(3, 6))
    puzzle_solver('Висит груша - нельзя скушать', random.randint(3, 6))
    show_results()