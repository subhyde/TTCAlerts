import tweepy
import re

auth = tweepy.OAuthHandler('', '')
auth.set_access_token('-',
                      '')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
print("running")


class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if re.search("^((?!@).)*$", status.text) and re.search("[lL]ine 1", status.text):
            try:
                retweet(status.id_str)
            except tweepy.TweepError as e:
                print(e)

    def on_error(self, status_code):
        if status_code == 420:
            return False

    def on_exception(self, exception):
        print(exception)
        return


def retweet(id_string):
    api.retweet(id_string)
    return


stream_listener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
stream.filter(follow=["19025957"])
