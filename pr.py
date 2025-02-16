#list=[4,3,22,65]
#str="hello"
#int=38
#print(type(list))
#print(type(str))
#print(type(int))
#list.clear()
#print(list)
#str=str.capitalize()
#print(str)
#a='a'
#b='b'
#print(a+b)
#print("x"+"y")

#function
l=[2,4,5,66,6]
s=len(l)
print(s)

#method
from oops_proj import chatbook
user=chatbook()
print(user.user_id)
#chatbook.set_id(10)
user2=chatbook()
print(user2.id)


#user.sendmsg()
print(user._chatbook__username)
#print(user.__init__())
print(user.get_name())
user.set_name("Agent") 
print(user.get_name())