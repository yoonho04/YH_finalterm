import pyotp
import time

# 1. 서버와 사용자가 공유할 비밀키를 생성합니다. (Base32 형식)
# 실제 서비스에서는 이 키를 데이터베이스에 안전하게 저장하고 사용자에게는 QR코드로 보여줍니다.
shared_secret = pyotp.random_base32()
print(f"공유된 비밀키: {shared_secret}")

# 2. TOTP 객체를 생성합니다. (기본값: 30초 간격, 6자리 숫자)
totp = pyotp.TOTP(shared_secret)

# 3. 현재 시점의 OTP 번호를 생성해봅니다.
current_otp = totp.now()
print(f"현재 생성된 OTP 번호: {current_otp}")

# 4. 검증 시뮬레이션
user_input = input("스마트폰 앱에 표시된 6자리 번호를 입력하세요: ")

if totp.verify(user_input):
    print("인증 성공! 환영합니다.")
else:
    print("인증 실패. 번호가 잘못되었거나 시간이 만료되었습니다.")

# 5. 시간 동기화 방식 확인 (30초 대기 후 변화 관찰)
print("\n30초 후 번호가 어떻게 변하는지 확인해볼까요?")
# time.sleep(30) # 실제로 기다려보려면 주석을 해제하세요.
