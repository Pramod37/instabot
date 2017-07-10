import requests,urllib

MY_ACCESS_TOKEN = '5687932517.0496933.05f78e1fbb5d4bb29b1eaf153a049f25'
BASE_URL = 'https://api.instagram.com/v1/'


def own_info():
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (MY_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username: %s' % (user_info['data']['username'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
            print 'User does not exist!'
    else:
        print 'Status code other than 200 received!'


def get_user_id(insta_username):
    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, MY_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            return user_info['data'][0]['id']
        else:
            return None
    else:
        print 'Status code other than 200 received!'
        exit()


def get_user_info(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id, MY_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username: %s' % (user_info['data']['username'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
            print 'There is no data for this user!'
    else:
        print 'Status code other than 200 received!'


def get_own_post():
    request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (MY_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    own_media = requests.get(request_url).json()
    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            image_name = own_media['data'][0]['id'] + '.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Your image has been downloaded!'
        else:
            print 'Post does not exist!'
    else:
        print 'Status code other than 200 received!'


def get_user_post(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, MY_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            image_name = user_media['data'][0]['id'] + '.jpeg'
            image_url = user_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Your image has been downloaded!'
        else:
            print 'Post does not exist!'
    else:
        print 'Status code other than 200 received!'


def get_post_id(insta_username):
    user_id = get_user_id(insta_username)
    if user_id is None:
        print "User does not exist"
        exit()
    request_url = (BASE_URL + "users/%s/media/recent/?access_token=%s") % (user_id, MY_ACCESS_TOKEN)
    print "GET request url : %s" % (request_url)
    user_media = requests.get(request_url).json()

    if user_media["meta"]["code"] == 200:
        if len(user_media["data"]):
            return user_media["data"][0]["id"]
        else:
            print "There is no recent post of the user"
            exit()
    else:
        print "Status code other than 200 received"
        exit()


def get_list_of_like(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + "media/%s/likes?access_token=%s") % (media_id ,MY_ACCESS_TOKEN)
    print "Get request url : %s" % (request_url)
    likes_list = requests.get(request_url).json()
    print likes_list
    if len(likes_list['data']):
       for x in likes_list['data']:
           print x['usernamae']
    else:
       print "Unsuccessful"


def like_a_post(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/likes') % (media_id)
    payload = {"access_token": MY_ACCESS_TOKEN}
    print 'POST request url : %s' % (request_url)
    post_a_like = requests.post(request_url, payload).json()
    if post_a_like['meta']['code'] == 200:
        print 'Like was successful!'
    else:
        print 'Your like was unsuccessful. Try again!'


def post_a_comment(insta_username):
    media_id = get_post_id(insta_username)
    comment_text = raw_input("Your comment: ")
    payload = {"access_token": MY_ACCESS_TOKEN, "text": comment_text}
    request_url = (BASE_URL + 'media/%s/comments') % (media_id)
    print 'POST request url : %s' % (request_url)

    make_comment = requests.post(request_url, payload).json()

    if make_comment['meta']['code'] == 200:
        print "Successfully added a new comment!"
    else:
        print "Unable to add comment. Try again!"


def list_of_comment(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/comments?access_token = %s') % (media_id,MY_ACCESS_TOKEN)
    print "Get request url : %s" % (request_url)
    comment_list = requests.get(request_url).json()
    print comment_list
    print comment_list
    if len(comment_list['data']['from']):
        for x in comment_list['data']['from']:
            print x['usernamae']
    else:
        print "Unsuccessful"


def start_bot():
    while True:

        print '\n'
        print 'Hey! Welcome to instaBot!'
        print 'Here are your menu options:'
        print "a.Get your own details"
        print "b.Get details of a user by username"
        print "c.Get own Recent Post"
        print "d.Get another user Post"
        print "e.check the list liked by friends: "
        print "f.likes a post of a user: "
        print "g.comment on a post of a user: "
        print "h. list of comment on a post of user"

        print "j.Exit"

        choice = raw_input("Enter you choice: ")
        if choice == "a":
            own_info()
        elif choice == "b":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_info(insta_username)
        elif choice == "c":
            get_own_post()
        elif choice == "d":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_post(insta_username)
        elif choice == "e":
            insta_username = raw_input("Enter the username: ")
            print "your post is like by:\n"
            get_list_of_like(insta_username)
        elif choice == "f":
            insta_username = raw_input("Enter the username of the user: ")
            print like_a_post(insta_username)
        elif choice == "g":
            insta_username = raw_input("Enter the username of the user: ")
            print post_a_comment(insta_username)
        elif choice == "h":
            insta_username =raw_input("Enter username of the user:")
            print list_of_comment(insta_username)

        elif choice == "j":
            exit()
        else:
            print "wrong choice"

start_bot()


