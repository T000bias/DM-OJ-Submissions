# Solution 1: Doesn't work, correct process
# def find_word_count(str):
#     count = 1
#     for word in range(len(str)):
#         if str[word] == " ":
#             count += 1
#             print(count)
#     return count
# print(find_word_count("problem one is really long"))

# Solution 2: Works
user = input()
count = 1
for word in range(len(user)):
    if user[word] == ' ':
        count += 1
print(count)