# source: https://towardsdatascience.com/how-to-use-the-reddit-api-in-python-5e05ddfd1e5c
import requests
import pandas as pd

# def access(pus, token, user, pw, agent):
#     data = {'grant_type': 'password',
#             'username': user,
#             'password': pw}
#     headers = {'User-Agent': agent}
#     auth = requests.auth.HTTPBasicAuth(pus, token)
#
#     res = requests.post('https://www.reddit.com/api/v1/access_token',
#                              auth=auth, data=data, headers=headers)
#
#     TOKEN = res.json()['access_token']
#     headers = headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}
#     requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)
#
# test = access(pus='Z-NTXNH1_UPOhQ', token='xri9_3tON_fRlqv0i5befU2F615m4Q', user='smallchickbigtit',
#              pw='gyrqup-5pejgu-pacCom', agent='MA_test/0.0.2')

# note that CLIENT_ID refers to 'personal use script' and SECRET_TOKEN to 'token'
auth = requests.auth.HTTPBasicAuth('Z-NTXNH1_UPOhQ', 'xri9_3tON_fRlqv0i5befU2F615m4Q')
# here we pass our login method (password), username, and password
data = {'grant_type': 'password',
        'username': 'smallchickbigtit',
        'password': 'gyrqup-5pejgu-pacCom'}
# setup our header info, which gives reddit a brief description of our app
headers = {'User-Agent': 'MA_test/0.0.1'}
# send our request for an OAuth token
res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)
# convert response to JSON and pull access_token value
TOKEN = res.json()['access_token']
# add authorization to our headers dictionary
headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}
# while the token is valid (~2 hours) we just add headers=headers to our requests
a = requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)
print(a)

#%%
#####################################################
# get most popular posts (hot) from resp. subreddit #
#####################################################

res = requests.get("https://oauth.reddit.com/r/wallstreetbets/hot",
                   headers=headers)
df = pd.DataFrame()  # initialize dataframe

# loop through each post retrieved from GET request
for post in res.json()['data']['children']:
    # append relevant data to dataframe
    df = df.append({
        'subreddit': post['data']['subreddit'],
        'title': post['data']['title'],
        'selftext': post['data']['selftext'],
        'upvote_ratio': post['data']['upvote_ratio'],
        'ups': post['data']['ups'],
        'downs': post['data']['downs'],
        'score': post['data']['score']
    }, ignore_index=True)
