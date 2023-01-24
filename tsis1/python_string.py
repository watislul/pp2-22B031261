print("Hello")
print('Hello')

a = "Hello"
print(a)

# You can assign a multiline string to a variable by using three quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

print('\n') # Or three single quotes:

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# Note: in the result, the line breaks are inserted at the same position as in the code.

a = "Hello, World!"
print(a[1])

print('\n')

for x in "banana":
  print(x)

print('\n')

a = "Hello, World!"
print(len(a))

print('\n')

txt = "The best things in life are free!"
print("free" in txt)

print('\n')

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

print('\n')

txt = "The best things in life are free!"
print("expensive" not in txt)

print('\n')

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")