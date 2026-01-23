def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

profile_1 = build_profile('alucard','hellsing', location='hellsing organization', job="hellsing's guard dog", age=568)

print(profile_1)