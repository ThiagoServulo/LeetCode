def countSeniors(details):
    return len(list(filter(lambda x: int(x[11:13]) > 60, details)))

print(countSeniors(["7868190130M7522","5303914400F9211","9273338290F4010"])) # s