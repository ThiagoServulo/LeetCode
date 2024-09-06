def reverseWords(s):
    s_list = s.split(' ')
    s_list = [i[::-1] for i in s_list]
    return ' '.join(s_list)

print(reverseWords("Let's take LeetCode contest")) # "s'teL ekat edoCteeL tsetnoc"