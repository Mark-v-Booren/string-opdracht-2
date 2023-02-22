# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
# Gullit 32'
# Van Basten 54'

scorer_1 = 'Ruud Gullit'
scorer_2 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54

scorers = scorer_1 + ' ' + str(32) + ', ' + scorer_2 + ' '+str(54)

report = f'{scorer_1} scored in the {goal_0}nd minute\n{scorer_2} scored in the {goal_1}th minute'

player = 'Hans van Breukelen'
splittedName = player.find(' ')
lastName = player[splittedName+1:]
first_name = player[0:splittedName]
name_short = first_name[0]+'. ' + lastName
last_name_len = len(lastName)
chantLen = len(first_name)
make_chant = f'{first_name}! ' * chantLen
chant = make_chant[0:-1]
good_chant = chant[-1] != ' '


print(scorers)
print(report)
print(lastName)
print(first_name, lastName, last_name_len, name_short, chant, good_chant)
