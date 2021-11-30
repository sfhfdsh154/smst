

ans="y"

print("초를 적으면 시간으로 계산해주는 프로그램 입니다.")

      
while ans=='y':

    second = int(input("계산이 필요한 초를 적어주세요. (ex: 173627 => 2 days 00h : 13m : 47s) : "))

    Day = second // (3600 * 24)

    second = second % (3600 * 24)

    h = second // (60 * 60)

    second = second % (60 * 60)

    m = second // 60

    s = second % 60

    print('%d days %02dh : %02dm : %02ds' %(Day,h,m,s))

    ans=input('다시할까요?(y/n)?')
