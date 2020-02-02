import tweepy
import re

auth = tweepy.OAuthHandler()
auth.set_access_token()

api = tweepy.API(auth)
user = api.get_user(screen_name='@TTCAlerts1_2')
print("User id:" + str(user.id))


class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if re.search("^((?!@).)*$", status.text) and re.search("L|line 1", status.text):
            try:
                print(status.text)
                retweet(status.id_str)
            except tweepy.TweepError as e:
                print(e)

    def on_error(self, status_code):
        if status_code == 420:
            return False


def retweet(id_string):
    api.retweet(id_string)
    return


stream_listener = StreamListener()
print('running')
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
stream.filter(follow=["19025957"])
