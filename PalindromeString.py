class Solution:
    def longestPalindrome():
        substringList = []
        bigSubstringList = []
        longest = ""
        s = "bb"

        for x in range(len(s)):
            if (x < len(s)-2) and(s[x] == s[x+2]):
                substringList.append((s[x:x+3], x))
            if (x < len(s)-1) and (s[x] == s[x+1]):
                substringList.append((s[x:x+2], x))
        
        if len(substringList) < 1:
            for i, e in enumerate(s):
                bigSubstringList.append(e)
                
        for i, e in enumerate(substringList):
            searching = True
            added = 0
            length = len(e[0])
            dummy = e[0]
            while searching:
                if (e[1] - added > 0) and (e[1] + length + added < len(s)):
                    dummy = s[e[1] - added : e[1] + length + added]
                    added += 1
                    if dummy != dummy[::-1]:
                        #bigSubstringList.append(dummy)
                        break
                else:
                    break
            bigSubstringList.append(dummy) 
                

        for i, e in enumerate(bigSubstringList):
            if len(e) > len(longest):
                longest = e
        print(longest)
        return(longest)

    longestPalindrome()