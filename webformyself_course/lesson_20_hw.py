words = ['мадам', 'топот', 'test', 'madam', 'word']
my_str = ['Око за око', 'А роза упала на лапу Азора', 'Около Миши молоко']

words_res = [word for word in words if word == word[::-1]]
print(words_res)

my_str_res = [str_orig for str_orig in my_str if "".join(str_orig.split()).lower() == "".join(str_orig.split()).lower()[::-1]]
print(my_str_res)