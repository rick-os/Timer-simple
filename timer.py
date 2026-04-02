import time

seconds = int(input("Digite o tempo em segundos: "))

def countdonw_timer(seconds):
  while seconds > 0: 
    mins = int(seconds / 60)
    sec = int(seconds % 60)

    timer = f'{mins}:{sec}'
    print(timer)
    time.sleep(1)
    seconds -= 1
  print("Tempo esgotado")
countdonw_timer(int(seconds))