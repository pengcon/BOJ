vowels=['a','e','i','o','u']

while True :
    string=input()
    if string=='end':
        break
    have_vowels=False
    not_three_strick=True
    not_equal=True
    for i in vowels:
        if i in string:
            have_vowels=True
    vowel_count=0
    consonants_count=0
    for i in string:
        if i in vowels:
            vowel_count+=1
            consonants_count=0
        else:
            vowel_count=0
            consonants_count+=1
        if vowel_count>=3 or consonants_count>=3:
            not_three_strick=False

    for j in range(len(string)-1):
        if string[j]=='e' or string[j]=='o':
            continue
        elif string[j]==string[j+1]:
            not_equal=False
    if have_vowels and not_three_strick and not_equal:
        print(f"<{string}> is acceptable.")
    else:
        print(f"<{string}> is not acceptable.")
