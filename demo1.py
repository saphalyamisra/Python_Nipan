age = int(input("Enter your age to check your muscularity! -->"))

if age > 32:
    name = input("Wow! you are a holy man, please enter your name -->")
    print(f"{name} the great Alexander! get married soon! Other wise you can't find a girl")
elif age == 32:
    exicited_name = input("Excited to know your name, please enter your name -->")
    print(f"{exicited_name} our chocopie! What you are waiting for? Do you think you are a kid! Go search a girl soon to get married this year only")
else:
    print("Chill! There is time, we will find one for you!")


def new_function_test(s):
    d = {}
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i]+=1
    new_op = [i for i,j in d.items() if j > 1]
    return d, new_op
input = "Saphalya Misra"
occurence = new_function_test(input)[0]
duplicates = new_function_test(input)[1]

print(occurence)
print(duplicates)