def get_active_users(users: dict[str, dict[str, bool | str]]) -> list[str]:
    active_users = []
    for i, j in users.items():
        if j == True or j == 'active':
            active_users.append(i)
    
    return active_users

users = {
    'ali':True,
    'sami':'active',
    'bek':False,
    'said':'passive',
    'vali':True
}
print(get_active_users(users))