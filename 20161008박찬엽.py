# This Python file uses the following encoding: utf-8
# -*- coding: utf-8 -*-

import random

def login(ID, PW):
    if (ID == "aaa" and PW == "1234"):
        return True
    return False

scenario = ["길을 가다가 퉁퉁이를 만났습니다.", "학교를 가다가 퉁퉁이를 만났습니다.",
            "마트에서 퉁퉁이를 만났습니다.", "버스 안에서 퉁퉁이를 만났습니다."]
action = ["퉁퉁이에게 이겼습니다.", "퉁퉁이에게 졌습니다.", "HP가 0입니다. 졌습니다.", "목표 달성입니다. 축하합니다."]
members = {"aaa": {"level":1,
                        "hp":100,
                        "items":["대나무헬리콥터", "빅라이트", "어디로든 문"],
                        "skill":["펀치", "핵펀치", "피하기"]}}

while (True):
    id = input("ID를 입력하시오: ")
    pw = input("PW를 입력하시오: ")
    if (login(id, pw)):
        if (id in members):
            print(id, "님 반갑습니다.", id, "HP", members[id]["hp"], "으로 게임을 시작 합니다.")
            break
        else:
            print(id, "님은 회원이 아닙니다. 재 입력하세요.")
            print()
    else:
        print("ID 또는 PW가 틀립니다. 재 입력하세요.")
        print()

while (True):
    print()
    print(random.choice(scenario))
    a = int(input("1. 싸운다 2. 도망간다? 0. 종료 "))
    print()

    if (a == 0):
        print("게임을 종료합니다.")
        break
    if (a == 1):
        item = input("사용할 아이템은? [" + str(members[id]["items"]) + "] ")
        print(item, "이(가) 사용되었습니다.")
    else:
        skill = input("사용할 기술은? [" + str(members[id]["skill"]) + "] ")
        print(skill, "이(가) 사용되었습니다.")

    print(random.choice(action))
