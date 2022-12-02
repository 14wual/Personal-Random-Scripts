# Write a function that receives a string and returns True if it is a palindrome
# (that is, whether it reads the same from left to right or from right to left),
# False otherwise. Use this function in a program that allows the
# user enter words until you enter the word “fin” (assume all
# words are either lowercase or all uppercase, consistently). To the
# finish, display the number of palindromes entered.

def api():  

    string = ""
    count = 0
    while string != "fin" and string != "FIN":

        string = input("Write your sentence: ")

        val = validator(string)
        if val == True:
            count += 1
    
    print(f"You have made {count} polyndomas")


def validator(string):
    
    string = string.upper()
    list_string = list(string)
    list.reverse(list_string)
    
    reverse_string = ""
    for x in list_string:
        reverse_string += x
    
    if reverse_string == string:
        return True

if __name__ == '__main__':
    api()
