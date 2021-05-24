from add_one import add_one
from library.multiply_by_two import multiply_by_two

def double_plus_one():
  try:
    number = input('please enter a number in digits: ')
    number = int(number)
    print(add_one(multiply_by_two(number)))
  except Exception as e:
    print(f'the numbers must be digits, {e}')
  



if __name__ == '__main__':
  double_plus_one()