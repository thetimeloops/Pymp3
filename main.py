



print(r'''


  ^    ^    ^    ^    ^
 /P\  /y\  /M\  /p\  /3\
<___><___><___><___><___>

''')


print("Enter a digit from 1 to 2: ")
print(" ")
print("1. Download by name")
print("")
print("2. Download by Youtube Link")
print("")
user_choice = input(">")
if user_choice=="1":
    import name_downloader
    name_downloader.main()
elif user_choice=="2":
    import youtube_downloader
    youtube_downloader.main()
else:
    print("Wrong Input")
