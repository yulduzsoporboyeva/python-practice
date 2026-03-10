# 2
savol = "Yoshingiz nechida? Yoshingizni kiriting, sizga chipta narxini chiqarib beramiz: "

while True:
    print("Agar siz 'exit' va 'quit' deb yozsangiz, dastur to'xtaydi")
    yosh= input(savol)
    if yosh == 'exit' or yosh == 'quit':
        print("dastur to'xtadi")
        break

    yosh = int(yosh)

    if yosh < 7:
        print("2000 so'm")
    elif yosh >= 7 and yosh < 18:
        print("3000 so'm")
    elif yosh >= 18 and yosh < 65:
        print("10000 so'm")
    else:
        print("Bepul")