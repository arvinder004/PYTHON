#program to download instagram profile picture of any account only by typing its username


import instaloader          #library

ig = instaloader.Instaloader()
dp = input("ENTER INSTAGRAM USERNAME::")          #username
ig.download_profile(dp.profile_pic_only == True)
