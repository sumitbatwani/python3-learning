def voting_age_check(age):
    if age > 21:
        return "eligible to vote"
    elif age == 21:
        return "right on border"
    else:
        return "see you later"

print(voting_age_check(21))
print(voting_age_check(25))
print(voting_age_check(16))
