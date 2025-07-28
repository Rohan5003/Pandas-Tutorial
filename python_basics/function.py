# def greatest(a,b,c):
#     if a>=b and a>=c:
#         return a 
#     elif b>=a and b>=c:
#         return b
#     else:
#         return c
    
# print("greatest of three numbers is : ", greatest(2,5,8))

def remove_word(word_list, word_to_remove):
    cleaned_list = []
    for word in word_list:
        if word.strip() != word_to_remove:
            cleaned_list.append(word.strip())
    return cleaned_list

# Example usage
words = [" apple ", "banana", " mango ", "banana"]
print(remove_word(words, "banana"))  # Output: ['apple', 'mango']



