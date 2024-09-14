is_Male = False
is_Tall = False
#if is_Male or is_Tall:
    #print("You are a male or tall or both")
#else:
    #print("You are neither a male nor tall")

if is_Male and is_Tall:
    print("You are a tall male")
elif is_Male and not (is_Tall):
    print("You are a short male")
elif not (is_Male) and is_Tall:
    print("You are not a male but you are tall")
else:
    print("You are not a male and not tall")