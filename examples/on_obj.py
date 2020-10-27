from insta_profile import Profile
from pprint        import pprint

profile = Profile("francistaylor.py").on_obj()

pprint(profile.name)
pprint(profile.username)
pprint(profile.followers)
pprint(profile.following)
pprint(profile.picture)

"""
'Francis Taylor'
'@francistaylor.py'
'431'
'558'
'https://instagram.fssz7-1.fna.fbcdn.net/v/t51.2885-19/s150x150/118779313_800640644085014_1604849649686799309_n.jpg?_nc_ht=instagram.fssz7-1.fna.fbcdn.net&_nc_ohc=ZmyJ4Dl_iW4AX9DMvXy&oh=bdc735ba9d906d52fcf0a4094565ef5b&oe=5FBFCBAB'
"""
