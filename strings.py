def get_strings_methods():
    i: int = 0
    for method in dir(str):
        if "_" not in method:
            i += 1
            print(i, method, sep=" : ")


get_strings_methods()

# 1. capitalize
text = "hello EVERYONE"
print(text.capitalize())

# 2. case-fold
text1 = "heLLo"
text2 = "HELlo"
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

# 8. find
text8 = "My name is DJ."
print(text8.find("DJ"))

# 9. format
text9 = "{0}, My mane is {1}".format("Hello everyone!", "DJ")
print(text9)

# 10. index
text10 = "Hello"
index_num = text10.index("l")
print(index_num)

# 11. is_al_num
text11 = "10"
text12 = "Dj-03"
print(text11.isalnum())
print(text12.isalnum())

# 12. is_a_pha
text13 = "Helo"
text14 = "10"
print(text13.isalpha())
print(text14.isalpha())
