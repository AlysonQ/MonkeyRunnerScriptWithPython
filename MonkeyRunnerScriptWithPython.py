#coding=utf-8
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage

#等待手機與電腦連接
device = MonkeyRunner.waitForConnection()
MonkeyRunner.sleep(1)
print("Device OK!!")

#執行動作的次數
count = 0

while True:
  count += 1
  #只是個log
  print("count = " + str(count))
  device.touch ( 963, 1716, "DOWN_AND_UP")
  MonkeyRunner.sleep(1)
  print("[回主頁面]")
  device.touch ( 200, 1194, "DOWN_AND_UP")
  MonkeyRunner.sleep(1)
  device.touch ( 200, 1194, "DOWN_AND_UP")
  MonkeyRunner.sleep(1)
  device.touch ( 200, 1194, "DOWN_AND_UP")
  MonkeyRunner.sleep(1)
  print("[點選第一張]")
  device.touch ( 982, 275,  "DOWN_AND_UP")
  MonkeyRunner.sleep(1)
  print("[點選選項]")
  device.touch ( 500, 490, "DOWN_AND_UP")
  MonkeyRunner.sleep(1)
  print("[點選典藏]")
  device.touch ( 963, 1716, "DOWN_AND_UP")
  MonkeyRunner.sleep(2)
  print("[回主頁面_end]")