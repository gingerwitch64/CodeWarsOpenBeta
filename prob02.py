import sys
flash_failed = False
for line in sys.stdin:
    if int(line) % 2 != 0:
        flash_failed = True
        print(f"{int(line)} is odd")
if flash_failed:
    print("FLASH FAILED")
else:
    print("FLASH FORWARD")