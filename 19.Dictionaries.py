# dictionary = A changeable, unordered collection of unique key: value pairs fast because they use hashing, allow us to access a value quick

capitals =  {'USA':'Washington DC',
             'India':'New Delhi',
             'China':'Beijing',
             'Russia':'Moscow'}

capitals.update({'Germany':'Berlin'}) # add to new items to the dictionary
capitals.update({'USA':'Las Vegas'}) # change a USA capital
capitals.pop('China') # remove China from dictionary
capitals.clear() # clear the dictionary
print(capitals['Russia'])  # and print Moscow
print("---------------------------")
print(capitals.get('Germany')) #print "none" bcs doesn't exist
print("---------------------------")
print(capitals.keys()) #print dict_keys(['USA', 'India', 'China', 'Russia'])
print("---------------------------")
print(capitals.values()) #print dict_values(['Washington DC', 'New Delhi', 'Beijing', 'Moscow'])
print("---------------------------")
print(capitals.items()) # print a list items
print("---------------------------")
for key,value in capitals.items():
    print(key,value) # print country and capital for every country on a new line
