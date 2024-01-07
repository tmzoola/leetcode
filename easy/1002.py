class Solution:
    def commonChars(self, words: str) -> str:
        
        while len(words)>1:
            word1 = words.pop()
            word2 = words.pop()
            string1 = ""
            for i in word1:
                if i in word2:
                    word2 = word2.replace(i,"",1)
                    string1+=i
            words.append(string1)
        return [i for i in words[0]]

obj = Solution()
print(obj.commonChars(["cool","lock","cook"]))