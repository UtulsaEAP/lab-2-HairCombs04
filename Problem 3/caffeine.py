'''
Name: Bradyn Combs 
Lab Time: 2/1/24 2:00 PM
'''

def caffeine():
    caffeine_mg = float(input())
    ''' Type your code here. '''
    caffeine_after_6_hours = caffeine_mg / 2
    caffeine_after_12_hours = caffeine_after_6_hours / 2
    caffeine_after_24_hours = caffeine_after_12_hours / 4

    print("After 6 hours: %.2f mg" % caffeine_after_6_hours)
    print("After 12 hours: %.2f mg" % caffeine_after_12_hours)
    print("After 24 hours: %.2f mg" % caffeine_after_24_hours)
    
if __name__ == "__main__":
    caffeine()