class Solution:

    def encode(self, strs: List[str]) -> str:
        bigString = ""

        for string in strs: 
            bigString += string + "~"

        return bigString


    def decode(self, s: str) -> List[str]:

        stringList = []
        currWord = ""

        for l in s: 
            if l == "~":
                stringList.append(currWord)
                currWord = ""
            else: 
                currWord += l
        
        return stringList

            

