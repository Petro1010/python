from instabot import Bot 

my_bot = Bot()

# login into account

my_bot.login(username="", password="")

# Follow a user
my_bot.follow("username of account")

#Follow multiple people
my_bot.follow_users(["user1", "user2", "user3"])

#Also methods to follow all people someone is following or all their followers

#Unfollow the non followers
my_bot.unfollow_non_followers()

#uploading an image
my_bot.upload_photo("image path here", caption="This is a photo")

#Sending a message
my_bot.send_message("type message here", "username of user to send to")

#like a post
my_bot.like_user("user name of person", amount=2, filtration=False)

#comment on a post
user_id = my_bot.get_user_id_from_username("user name of person")
media_id = my_bot.get_last_user_medias(user_id, 1) # get the last post
my_bot.comment(media_id[0], "This is very nice")

#Get list of followers of anyone (will return a list of user Ids)
followers_list = my_bot.get_user_followers(" Username ")
following_list = my_bot.get_user_following(" User name")

for follower in followers_list:
    print(my_bot.get_username_from_user_id(follower))


#can put delays using the sleep function to be more human like