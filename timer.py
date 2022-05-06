import time

timer_time = int(input('타이머를 설정할 시간 입력... '))
timer_min = int(input('타이머를 설정할 분 입력...'))
timer_sec = int(input('타이머를 설정할 초 입력...'))
print('--------------------------------------------------------')
print('타이머를 시작합니다.')
print('--------------------------------------------------------')

time.sleep(timer_time * 3600)
time.sleep(timer_min * 60)
time.sleep(timer_sec)

print('타이머가 종료되었습니다.')