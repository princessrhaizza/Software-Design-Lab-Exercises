def reverse(strs):

   if len(strs)==0:

       return ' '

   else:
       return reverse(strs[1:])+strs[0]

strs="hiraya at pahina"
print(reverse(strs))