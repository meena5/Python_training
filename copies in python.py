#shallow copy and deep copy in lists
import copy
print("-----------shallow copy in lists--------")
l=[16,8,29,650,287,3876,367]
print("beore copy")
print(l)
l2=l
l2[0]=43
l2.append(26)
print("after copy")
print(l)

l1=copy.copy(l)#creates a deep copy over shallow copy so original list will not effect
print("beore copy")
print(l)
l1[0]=43
print("after copy does not show any effect in lists with copy.copy(l)")
print(l)

print("--------------deep copy in lits-----------")
l=[16,8,29,650,287,3876,367]
l1=copy.deepcopy(l)# whatever changes made to l1(copied list) will not  affect the l(original list)
print("beore deep copy")
print(l)
l1.append(12)
l1.append(17)
print("after deep copy")
print(l)
print(l1)

l4=[2,7,3,7,9,5]
l5=l4[:]
l5[0]=43
print(l4)



#coping in nested lists

li1=[[1,2,3],[4,5,6],[7,8,9]]
li2=copy.deepcopy(li1)
li1[2][2]='meena'
print(li1)#does not show affect to new list 
print(li2)

#copying in strings (strings in python are immutable)
print("-------------------------------------------------copy in strings--------------------------------------------")
s1="heello"
s2=s1
s2="hiiii"
print(s1)#so it will give the heello as output


s2=copy.copy(s1)
s2="hiiiiiii"
print("shallow copy:{} {}".format(s1,s2))#in python strings are immutable while copying so there is no difference between shallow copy and deepn copy in strings

s2=copy.deepcopy(s1)
s2="hiiiiiii"
print("deep copy:{} {}".format(s1,s2))  


