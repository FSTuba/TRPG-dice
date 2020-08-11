import re
import random

def mdn(n):
    tmp = re.split(r"d|D", n)
    summary = 0
    for i in range(int(tmp[0])):
        summary += random.randint(1, int(tmp[1]))

    return(summary)


def trpgdice(a):
    buffer = ""
    for i in a:		#處理輸入字串
        if i not in "0123456789dD+- ":
            return("Invalid input")
        if i != " ":
            buffer += i

    buffer = re.split(r'(\s|\+|\-)', buffer)
    b = ""
    for i in buffer:
        if (('d' in i) | ('D' in i)):
            i = str(mdn(i))

        b += i
    res = eval(b)
    return(res)


def make_coc_character():
    response = ("力量:" + str(mdn('3d6')) + "敏捷:" + str(mdn('3d6')) + "意志:" +
                str(mdn('3d6')) + "體質:" + str(mdn('3d6')) + "外貌:" + str(mdn('3d6')) + "\n")
    response += ("體型:" + str(mdn('2d6')+6) + "智慧:" + str(mdn('2d6')+6) + "\n")
    response += ("教育:" + str(mdn('3d6')+3) + "\n")
    response += ("財富:" + str(mdn('1d10')))
    return response


def main():
    print("+++++++++++TRPG DICE ROLLER!+++++++++++")
    print("(輸入範例:1d100,3d6 輸入ch創角  輸入 end 結束)")
    print("\n\n\n\n")
    print("偉大的骰子女神吶，請賜予我無上的力量!!!")
    print("=======================================")
    while(True):
        n = input("-->")
        if n == "end" or n == '':
            break
        elif n == 'ch':
            print(make_coc_character())
        elif ("d" in n or "D" in n):
            print(n, ">>>>>>", (trpgdice(n)))
        else:
            print("?")


if __name__ == '__main__':
    main()
