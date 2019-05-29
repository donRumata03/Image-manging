def copy_ammunition(amm):
    if type(amm) == type(dict()):
        amm_copy = dict()
    elif type(amm) == type([]):
        amm_copy = []
    for i in amm:
        if type(amm[i]) == type(dict()) or type(amm) == type([]):
            amm_copy[i] = copy_ammunition(amm[i])
        else:
            amm_copy[i] = amm[i]
    return amm_copy


a = {"things": {"sdgdsg" : 123, "wrfaeft" : 14, "thingss" : [123, 1345]}}

b = copy_ammunition(a)

b["thingss"] = [13, 15235]

b["things"][0] = "asdfghjkl"

print(a)
