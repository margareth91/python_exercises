def build_profile(first, last, **user_info):
    """Budowa slownika zawierajacego wszelkie informacje o uzytkowniku"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('fiosus', 'miodus', location='mlaskusie', hobbys='paczenie na ptaszki za oknem')
print(user_profile)
user_profile2 = build_profile('pycka', 'lobuziara', hobbys='tupanie')
print(user_profile2)

user_profile3 = build_profile('dziosia', 'brzosia', hobbys='lego', favorite_pet='kitki',
                              husband='dziusio')
print(user_profile3
      )