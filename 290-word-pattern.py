class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        既要判断key是否存在，又要判断value是否存在，使用双map
        """
        word2ch = {}
        ch2word = {}
        str_list = s.split(" ")
        if len(pattern) != len(str_list):
            return False
        for i in range(len(pattern)):
            one_p = pattern[i]
            if one_p not in word2ch:
                word2ch[one_p] = str_list[i]
                if str_list[i] in ch2word:
                    if ch2word[str_list[i]] != one_p:
                        return False
            else:
                if word2ch[one_p] != str_list[i]:
                    return False
            ch2word[str_list[i]] = one_p
        return True