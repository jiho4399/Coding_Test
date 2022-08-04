# 백준 5575번 : 타임 카드

for _ in range(3):
  sh, sm, ss, fh, fm, fs = map(int, input().split())
  time_s = sh * (60**2) + sm * 60 + ss
  time_f = fh * (60**2) + fm * 60 + fs
  time = time_f - time_s
  print(time//(60**2) % 24, time//60 % 60, time%60)