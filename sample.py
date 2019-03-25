import re
def test(str):
    string_no_numbers = re.sub("\d+", " ", str)
    print(string_no_numbers)
test('abc123') #prints abc

