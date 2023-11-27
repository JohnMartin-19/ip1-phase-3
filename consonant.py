def get_highest_value(s):
    highest_value = 0
    for i in range(len(s)):
        if s[i] in 'bcdfghjklmnpqrstvwxyz':
            value = ord(s[i]) - ord('a') + 1
            highest_value = max(highest_value, value)
    return highest_value 
print(get_highest_value('gggggg'))