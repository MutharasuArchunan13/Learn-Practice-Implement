"""
   we have two  string  here we want to check both string
     have same letters position in not inportant
"""
class Anagram:
    def findAnagramOrNot(self,str1:str,str2:str)-> bool:
        if len(str1) != len(str2):
            return False
        str1 = ''.join(sorted(str1))
        str2 =''.join(sorted(str2))
        if str1 == str2:
            return True
        return False
name = "kumas"
name2 = "ramuk"
anagran_obj = Anagram()
anagran_value = anagran_obj.findAnagramOrNot(name,name2)
if anagran_value:
    print(f"this is the anagram.")

else:
    print(f"this is not anagram")