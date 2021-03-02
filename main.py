import requests

headers = {
    'authority': 'www.reddit.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cookie': 'csv=1; edgebucket=PHFVz7X5f6u1GFe2WQ; __aaxsc=2; G_ENABLED_IDPS=google; reddit_session=509114073898%2C2021-02-20T19%3A44%3A28%2C8d2c0c9be05b6ec7d30e853fa6fb3631f5cfdf81; loid=00000000006hvtdhka.2.1589664844000.Z0FBQUFBQmdNV2FjVnRZZmcwVi1uUlNXOVZIWEdiVkFPNFZwTEhfVl9sc1pUWlpNeGJoUHJCNjBTUlAwbUQ4WDlXZUJ2ZzN2alJvWGVDS0FUMk9QMFhTUk9vdWppM2lmX0t2YW9xYjZnalVtZHNfc1Fnc2JKTW9vb3hfbGtEM01TUkdETlNHakFSVU0; token_v2=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MTM4NTM3NDgsInN1YiI6IjUwOTExNDA3Mzg5OC1MNENHcFB3bzFUNGpIM2hMMjhsTi1oa2V6N1EiLCJsb2dnZWRJbiI6dHJ1ZSwic2NvcGVzIjpbIioiLCJlbWFpbCJdfQ.FFC9y7eFdsryeuhH5JnjFEuWWfM8J4lU6wZr5h-3NY8; show_announcements=yes; session=77c829206251d2f19e9935ee3bc68b20783a209fgASVSQAAAAAAAABKn2YxYEdB2AxZls3N5X2UjAdfY3NyZnRflIwoMmFiNTQxMGY1OGZjZjBmMDdhNGY0NzlmNTliNDU5NTg0NjdkZDQ1MpRzh5Qu; aasd=2%7C1613850161488; __gads=ID=9d1b1dba1c7b3b77:T=1613850165:S=ALNI_MYVW1CrNBqtwK9rVSL_6iPh5wzcCQ; recent_srs=t5_2qjuv%2C; eu_cookie_v2=3; session_tracker=nhgemqhoeaikiejafi.0.1613850299649.Z0FBQUFBQmdNV2E3YWFVWkw3aEpXYlFxRmhOM0M5VWJSMlhDTmdWYzBzQXliMG5pWllfLTlFOXZmWDRHLXpHdHdvcThvRWdmcnJvaTlaY1ppNGtnTUcwbXM2RF81QVZfZHlzcEdIQkh0dTUxSWpraUNjNVhvTVkwOXNFU0VMdDEydmFjRkhmZy1sS2M',
}

response = requests.get('https://www.reddit.com/r/StockMarket/about/moderators.json', headers=headers)
#%%
# print(response.text)
json_response = response.json()
# json_response.keys()
# json_response['data']['children']
# for item in json_response['data']['children']:
#     print(item['name'])
moderators = [item['name'] for item in json_response['data']['children']]