def LongestRepeatingSubstringWithReplacement(s,k):
    l=0  #left pointer of the window
    count = {} # Dictionary To keep Track of character frequency
    max_freq =0 # Max Occurance in current window
    max_length = 0
    for r in range(len(s)):

        count[s[r]] = count.get(s[r], 0) + 1
        max_freq = max(max_freq,count[s[r]])

        window_size = r - l + 1

        if(window_size - max_freq >k):
           count[s[l]] -= 1
           l += 1

        max_length = max(max_length,r - l + 1)

        print(f"Current window: s[{l}:{r + 1}] = {s[l:r + 1]}, max_freq = {max_freq}, count = {count}")
        
    





s = "AABABBA" 
k = 2
longestLength = LongestRepeatingSubstringWithReplacement(s,k)

