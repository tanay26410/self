#making anagram
def makingAnagrams(s1,s2):
    for i in s1:
        if i in s2:
            s1=s1.replace(i,'',1)
            s2=s2.replace(i,'',1)
    return (len(s1)+len(s2)) 
s1='absdjkvuahdakejfnfauhdsaavasdlkj'
s2='djfladfhiawasdkjvalskufhafablsdkashlahdfa'
print(makingAnagrams(s1,s2))