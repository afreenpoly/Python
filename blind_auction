import art
print(art.logo)
print("welcome to the secret auction program")
auctioning=True
dict={}
while auctioning:
  name=input("What is your name: ")
  bid=int(input("Whats your bid: "))
  dict1={name:bid}
  dict.update(dict1)
  check=int(input("Are there any bidders left? \nPress 1 to continue , 2 to stop: "))
  if check==2:
    auctioning=False

max=dict[name]
for x in dict:
  if dict[x]>max:
    max=dict[x]
key_list=list(dict.keys())
val_list=list(dict.values())
pos=val_list.index(max)

print(f"The Winner is {key_list[pos]} with a bid of {max}")
