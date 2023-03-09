# Validate Credit Card Number
 
# get the count of the credit cards
count = int(input())
# create a list of 0-9 in str format
str_num_range = [str(num) for num in range(10)] 
# create a list of 4 consecutive digits for each number in 0-9 range
consec_list = [str(num)*4 for num in range(10)]
 
def validatecreditcard(creditcard):
    '''
    Takes a string and validates if it meets some creditcard conditions
    input: string
    output: return "Valid" or "Invalid"
    '''
    
    #create a dashfree version of the cc for later
    dashfree_cc = creditcard.replace('-','')
    #create a list of consecutive digits from the cc using the dashfree version
    consec_cc_list = [str(dashfree_cc[i:i+4]) for i in range(0, 13)]
    # create a list where we only keep 0-9 digits
    zerotonine_list = [num in str_num_range for num in creditcard]
    # create a bool var to check if there is a dash in the creditcard
    dash_in_cc = "-" in creditcard
    # initiate the dashes condition
    c5 = False
    
    # check if first digit is 4, 5, or 6
    c1 = int(creditcard[0]) in [4, 5, 6]
    # check if length of cc is 16 (after removing dashes)
    c2 = len(dashfree_cc) == 16
    # check if length of cc is 16 (after removing dashes)
    c3 = len(zerotonine_list) == 16 or len(zerotonine_list) == 19
    # count if any at least 4 consec digits are the same
    c4 = sum([consec_cc in consec_list for consec_cc in consec_cc_list]) == 0
    
    # check if there is a dash in the cc/string
    if dash_in_cc:
        # for each group split by "-" has 4 digits
        c5 = sum([len(group) == 4 and group.isdigit() for group in creditcard.split('-')]) == 4
    
    # bring it all together
    dash_total_condition = c1 and c2 and c3 and c4 and c5 and dash_in_cc 
    no_dash_total_condition = c1 and c2 and c3 and c4 and not dash_in_cc
    
    # if the cc meets either condition, it is valid, otherwise, it's invalid
    if dash_total_condition or no_dash_total_condition:
        return "Valid"
    else:
        return "Invalid"
    
    
# loop through the credit card numbers
for cc in range(count):
    # get the cc
    cc = input() 
    # call the validatecreditcard function and store output
    output = validatecreditcard(cc)
    print(output)