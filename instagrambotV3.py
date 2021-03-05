from instapy import InstaPy
from instapy import smart_run
import random

insta_username = 'username'
insta_password = 'password'

# get a session!
session = InstaPy(username=insta_username,
                  password=insta_password,
                  multi_logs=True)

# let's go! :>
with smart_run(session):
    # general settings
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    max_followers=6000,
                                    max_following=3000,
                                    min_followers=30,
                                    min_following=30)



    # follow activity
    like_tags = ['MusicProducer', 'Songwriter', 'AudioEngineer', 'producertoiz', 'Lovinglife',
            'Blessed', 'Dreams', 'dreamsetups', 'SingerSongwriter', 'AudioRecording', 'HomeStudio',
            'RecordingStudio', 'ProTools', 'MusicBusiness', 'Entrepreneur', 'Dreams', 'Dancers', 'DallasMusic',
            'PostProduction', 'ableton', 'avidprotools']
    session.like_by_tags(like_tags, amount=2, randomize=True)
    session.set_do_comment(enabled=True, percentage=5)
    session.set_comments(
        ['Nice shot! @{}', 'I love your profile! @{}', '@{} Love it!',
         '@{} :heart::heart:',
         'Love your posts @{}',
         'Looks awesome @{}',
         'Getting inspired by you @{}',
         ':raised_hands: Yes!',
         '@{}:revolving_hearts::revolving_hearts:', '@{}:fire::fire::fire:'],
        media='Photo')
    session.do_follow(True, percentage=50)



    #unfollow activity
    """session.unfollow_users(amount=126, nonFollowers=True, style="RANDOM",
                               unfollow_after=42 * 60 * 60, sleep_delay=300)"""
