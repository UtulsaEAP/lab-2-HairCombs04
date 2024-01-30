'''
Name: Bradyn Combs 
Lab Time: 2/1/24 2:00 PM
'''

def simple_stats():
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    num4 = float(input())
    ''' Type your code here. '''
    value = ((num1 * num2 * num3 * num4), (num1 + num2 + num3 + num4) /4)
    print(f'{value[0]:.0f} {value[1]:.0f}')
    print(f'{value[0]:.3f} {value[1]:.3f}')
if __name__ == "__main__":
    simple_stats()