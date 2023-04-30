# def get_strings_methods():
#     i: int = 0
#     for method in dir(str):
#         if "_" not in method:
#             i += 1
#             print(i, method, sep=" : ")
#
#
# get_strings_methods()

# 1. capitalize
text = "hello EVERYONE"
print(text.capitalize())

# 2. case-fold
text1 = "heLLo"
text2 = "GUYs"
print(text1.casefold())
print(text2.casefold())

# 3. center
text3 = "DJ"
print(text3.center(26, "_"))

# 4. count
text4 = "abc_abc_abc_abc_abc"
print(text4.count("ab"))

# 5. encode
text5 = "Elon Musk"
print(text5.encode(encoding="UTF-8", errors="strict"))

# 6. endswith
text6 = "Apple"
print(text6.endswith("e"))

# 7. expend-tads
text7 = "Hello \tEveryone \tI'm DJ."
print(text7.expandtabs(20))
