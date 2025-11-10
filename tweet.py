tweet=input("Enter your tweet:")
max_ch=140
char_len=len(tweet)
max_long=char_len-max_ch
if len(tweet)<140:
    print(f"That {char_len} char tweet will work!")
else:
    print("Your  char tweet is 5 chars too long")