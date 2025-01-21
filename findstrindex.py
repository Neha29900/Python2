str = "hello world"
fstr= "world"
index = str.find(fstr)

if index != -1:
    print(f"The first occurrence of '{fstr}' is at index {index}.")
else:
    print(f"'{fstr}' is not found in the string.")
