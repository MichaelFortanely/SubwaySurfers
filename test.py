import requests

BASE = "http://127.0.0.1:5000/"

# response = requests.put(BASE + "video/20", json={'likes': 10000, 
#     'name': "Michael", 'views': 24})
# print(response.json())
# # name = str(input('Enter the name of the movie: '))
# # likes = int(input('How many likes does this movie have: '))
# # views = int(input('How many views does the movie have: '))
# # response = requests.put(BASE + 'video/2', json={
# #     'likes': likes, 'name': name, 'views': views
# # })

stringer = '1'


response = requests.put(BASE + "text/" + stringer, json={'text': 'Michael Fortanely is cool'})
print(response.json())


# response = requests.get(BASE + 'text/' + stringer)
# try:
#     print('response: ' + str(response.json()))
# except Exception as e:
#     print('An exception happended')