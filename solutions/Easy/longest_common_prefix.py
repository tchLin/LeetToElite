class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_word = min(strs, key=len)

        def find_common(word, the_other_word):
            comm=""
            for i in range(len(word)):
                if word[i] != the_other_word[i]:
                    return comm
                comm += word[i]
            return comm

        pref=shortest_word
        for word in strs:
            curr=find_common(shortest_word, word)
            pref = min(curr, pref, key=len)
            
        return pref
