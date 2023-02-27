import re
#1
text = 'abbb abb'
pattern = 'a{1}b*'
matching = re.findall(pattern, text)
print(matching)

#2
text = 'abbba hello abbusik'
pattern = 'ab{2,3}'

matching = re.findall(pattern, text)
print(matching)
#3
text = 'abc_abc_cde_hello'
pattern = '[a-z]+(?:_[a-z]+)+'

matching = re.findall(pattern, text)
print(matching)

#4
text = 'AbcDefQwertyLul'
pattern = '[A-Z]{1}[a-z]*'
matching = re.findall(pattern, text)
print(matching)
#5
text = 'acccabb aagresgf acdsebdfb dsaafdsa afrgsfhgb'
pattern = r'a{1}.+b' # если пробел не должен быть между а и б r'a{1}\w+b'
matching = re.findall(pattern, text)
print(matching)
#6
text = 'Hello, World.My name is Abylay'
pattern = '[., ]'
matching = re.sub(pattern, ':', text)
print(matching)
#7
text = 'hello_world_my_name_is_abylay'
text = text.split('_')
for index in range(1, len(text)):
    text[index] = re.sub(text[index][0], text[index][0].upper(),text[index])
ans = ''.join(text)
print(ans)
#8
text = 'HelloWorldHowAreYou'
split_string = re.findall('[A-Z][^A-Z]*', text)
print(split_string)
#9
text = 'HelloWorldHowAreYou'
text = ' '.join(re.findall('[A-Z][a-z]+', text))
print(text)
#10
text = 'HelloWorldMyNameIsAbylay'
pattern = r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))'
matching = re.findall(pattern, text)
ans = '_'.join(matching)
print(ans.lower())