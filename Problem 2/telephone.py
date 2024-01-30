'''
Name: Bradyn Combs 
Lab Time: 2/1/24 2:00 PM
'''

def telephone():
    phone_number = int(input())
    ''' Type your code here. '''
    # get the line number represnted by last four digits of the number
    line_num = phone_number % 10000 # get last 4-diguts using modulo 10000
    line_num = "-" + str(line_num)  # add an "-" using string concatenation 
    phone_number = phone_number // 10000

    prefix = phone_number % 1000 # get last 3-digits using modulo 1000 
    prefix = " " + str(prefix) # add an " " using string concatenation 
    phone_number = phone_number // 1000

    area_code = "(" + str(phone_number) + ")"

    # concatenate area code, prefix, and line number in order to get
    # the number in required format
    final_num = area_code + prefix + line_num
    print(final_num)   # print the number
if __name__ == "__main__":
    telephone()