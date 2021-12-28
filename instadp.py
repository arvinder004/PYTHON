#program to download instagram profile picture of any account only by typing its username


import instaloader

ig = instaloader.Instaloader()
dp = input("ENTER INSTAGRAM USERNAME::")
ig.download_profile(dp.profile_pic_only == True)
