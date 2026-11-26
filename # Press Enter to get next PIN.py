import random

used = set()

while True:
    otp = random.randint(1000, 9999)

    # digits should not repeat
    if len(set(str(otp))) == 4 and otp not in used:
        used.add(otp)

        input("Press Enter for next OTP...")
        print("OTP:", otp)