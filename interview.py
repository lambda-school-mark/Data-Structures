# Print out each element of the following array on a separate line, but this time the input array can contain arrays nested to an arbitrarily deep level:

# ['Bob', 'Slack', ['reddit', '89', 101, ['alacritty', '(brackets)', 5, 375]], 0, ['{slice, owned}'], 22]

# For the above input, the expected output is:

# Bob
# Slack
# reddit
# 89
# 101
# alacritty
# (brackets)
# 5
# 375
# 0
# {slice, owned}
# 22

list = ['Bob', 'Slack', ['reddit', '89', 101, [
    'alacritty', '(brackets)', 5, 375]], 0, ['{slice, owned}'], 22]

print(list[0])
print(list[1])
print(list[2][0])
print(list[2][1])
print(list[2][2])
print(list[2][3][0])
print(list[2][3][1])
print(list[2][3][2])
print(list[2][3][3])
print(list[3])
print(list[4][0])
print(list[5])
