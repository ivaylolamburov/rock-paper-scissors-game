from random import shuffle

file_name = 'rating.txt'
rating_file = open(file_name, 'a')
rating_file.close()
rating_file = open(file_name, 'r')
options = ['paper', 'rock', 'scissors']
wining_options = {
    'rock': ['paper'],
    'paper': ['scissors'],
    'scissors': ['rock']
}
player_name = input('Enter your name: ')
player_score = 0
has_account = False
print('Hello, ' + player_name)
for x in rating_file.readlines():
    if player_name in x:
        x = x.replace('\n', '')
        player_name, player_score = x.split()
        player_score = int(player_score)
        old_score = player_score
        has_account = True
rating_file.close()
new_options = input()
if new_options == '':
    pass
elif new_options == 'rock,gun,lightning,devil,dragon,water,air,paper,sponge,wolf,tree,human,snake,scissors,fire':
    new_options = list(new_options.replace(',', ' ').split())
    new_options = new_options + ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air']
    for omp in range(16):
        wining_options[new_options[omp]] = [i for i in new_options[omp:omp + 8]]
    options = options + new_options
else:
    new_options = list(new_options.replace(',', ' ').split())
    for option in range(len(new_options)):
        try:
            wining_options[new_options[option]] = new_options[option + 1]
        except:
            shuffle(options)
            wining_options[new_options[option]] = options[0]
    options = options + new_options
print('Okay, let\'s start')
while True:
    shuffle(options)
    computer_option = options[0]
    player_input = input()
    if player_input not in options and player_input != '!exit' and player_input != '!rating' and player_input not in new_options:
        print('Invalid input')
        continue
    if player_input == '!rating':
        print(f'Your rating: {player_score}')
        continue
    if player_input == '!exit':
        print('Bye!')
        if not has_account:
            rating_file = open(file_name, 'a')
            print(f'{player_name} {player_score}', file=rating_file)
            rating_file.close()
        else:
            rating_file = open(file_name, 'r')
            file_data = rating_file.readlines()
            for data in file_data:
                if player_name in data:
                    file_data.remove(data)
                    file_data.append(f'{player_name} {player_score}')
                    rating_file.close()
            rating_file = open(file_name, 'w')
            print(*file_data, file=rating_file)
            rating_file.close()
        break
    elif player_input == computer_option:
        print(f'There is a draw ({computer_option})')
        player_score += 50
    elif player_input in wining_options[computer_option]:
        print(f'Well done. The computer chose {computer_option} and failed')
        player_score += 100
    elif computer_option in wining_options[player_input]:
        print(f'Sorry, but the computer chose {computer_option}')
