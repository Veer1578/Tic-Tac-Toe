import random

character = [chr(i) for i in range(48, 58)] + [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
character2 = [chr(i)for i in range(48, 58)] + [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
random_char = ''.join(random.choices(character, k=3))
random_char2 = ''.join(random.choices(character2, k=3))
password = random_char + random_char2
print('The generated password is:',password)
