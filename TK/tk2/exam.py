"""Tunnikontroll 2"""

def middle_value(arv1 :int, arv2: int, arv3: int):
    if arv1 > arv2 > arv3 or arv3 > arv2 > arv1:
        return arv2
    elif arv2 > arv3 > arv1 or arv1 > arv3 > arv2:
        return arv3
    elif arv3 > arv1 > arv2 or arv2 > arv1 > arv3:
        return arv1
    else:
        return None
