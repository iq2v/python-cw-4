#الجزء الاول
def my_name() :
    print('My name is jana')
my_name()

#الجزء الثاني
def my_meal(food , drink) :
    print(f'i like to eat {food } while drinking {drink}')

my_meal('popcorn','cola')

#الجزء الثالث
def cube(number) :
    return number **3
result = cube(4)
print(result)
 
def by_three(number) :
    if number %3 == 0 :
        return cube(number)
    else:
         False

example1 = by_three(9)
print(example1)

example2 = by_three(4)
print(example2)