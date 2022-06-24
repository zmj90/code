user_win = [['石头', '剪刀'],
            ['布', '石头'],
            ['剪刀', '布']]
while True:
    user = input('')
    if user == '':
        break
print(['石头', '剪刀'] in user_win)