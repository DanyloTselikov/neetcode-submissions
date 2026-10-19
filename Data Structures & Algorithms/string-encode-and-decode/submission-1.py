class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string =""
        for i in range(len(strs)):
            
            encoded_string = encoded_string + str(len(strs[i]))+'#'+strs[i]
        return encoded_string 

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        
        while i < len(s):
            j = i 
            while s[j] != '#':
                j += 1
            lenh = int(s[i:j])
            word = s[j + 1 : j + 1 + lenh]
            decoded.append(word)
            i = j + 1 + lenh
            j+=1
        return decoded 