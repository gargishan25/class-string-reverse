class reverse:
    def __init__(self, s):
        self.s = s
    def str_reverse(self):
        list_word = []
        for i in range((len(self.s)-1),-1,-1):
            list_word.append(self.s[i])
        self.s = "".join(list_word)
        return self.s
s_userinp = input("Enter a word. ")
a = reverse(s_userinp)
print(a.str_reverse())