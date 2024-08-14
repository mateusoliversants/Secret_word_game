secret_word = 'life'
correct_letters = ''
attempts = 0

while True:
    typed_letter = input('Type a letter: ')
    attempts += 1
    if len(typed_letter) > 1:
        print('Type just one letter')
        continue

    if typed_letter in secret_word:
        correct_letters += typed_letter
    
    formed_word = ''
    for secret_letters in secret_word:
        if secret_letters in correct_letters:
            formed_word += secret_letters
        else:
            formed_word += '*'
    print(f'Secret word: {formed_word}')

    if formed_word == secret_word:
        break
print('===' * 9)

print('YOU WON, CONGRATULATIONS!!!')
print(f'The word was "{secret_word}"')
print(f'Number of attempts: {attempts}')
