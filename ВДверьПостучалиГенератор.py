print("knoks = ?")
knoks=str(input())
print("thoughts = ?")
thoughts=str(input())
print("who?")
character=str(input())
sex = 0
while not (sex=="m" or sex=="f"):
    print("sex = ? (m/f)")
    sex=str(input())
print("final = ?")
final=str(input())
print("В дверь постучали", knoks)
if sex == "m":
    print(" << ", thoughts,">> - подумал",character)
elif sex == "f":
    print(" << ", thoughts,">> - подумала",character)
print(final)
