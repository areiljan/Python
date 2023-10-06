"""Tunnikontroll 2"""


def middle_value(arv1 :int, arv2: int, arv3: int):
    """Leiab keskmise väärtuse"""
    if min(arv1, arv2, arv3) == arv1 and max(arv1, arv2, arv3) == arv3:
        return arv2
    elif min(arv1, arv2, arv3) == arv2 and max(arv1, arv2, arv3) == arv1:
        return arv3
    elif min(arv1, arv2, arv3) == arv3 and max(arv1, arv2, arv3) == arv2:
        return arv1
    elif max(arv1, arv2, arv3) == arv1 and min(arv1, arv2, arv3) == arv3:
        return arv2
    elif max(arv1, arv2, arv3) == arv2 and min(arv1, arv2, arv3) == arv1:
        return arv3
    elif max(arv1, arv2, arv3) == arv3 and min(arv1, arv2, arv3) == arv2:
        return arv1
    else:
        return None
