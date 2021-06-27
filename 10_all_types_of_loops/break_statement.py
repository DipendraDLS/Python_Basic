# Break statement in While loop
index = -1
i = 1
while(i <= 20):
    print('Iteration', i)
    if i**2 >= 100:
        index = i
        print('Index :', index)
        break                               # break statement le jun sukai loop vaye pani loop ko iteration process lai nai terminate garaidincha & break statement doesn't care if the looping condition meets or not.
        print('statement below break statement does not executes')
    i += 1

print('Final value of i = ', i)
print('Final value of index =', index)




# Break statement in For Loop
languages = ["Python", "C++", "Java", "Perl", "C#"]

for language in languages:
    if language == "C++":
        print(language + " found inside if block")
        break
        print("This line never executes")
    print(language + ": is not the language what we are looking for.")


