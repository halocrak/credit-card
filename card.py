import requests
import random

tok = input('tokin : ')
ID = input('id')
i =int('1000')
for i in range(i):
 user = '1234567890'
 us = str(''.join((random.choice(user) for i in range(16))))
 mrx ='🇺🇸🇫🇷🇩🇪🇨🇦🇪🇸🇷🇺🇮🇹🇬🇧🇮🇪🇳🇱🇳🇴🇫🇮🇭🇺🇨🇭🇩🇰🇦🇹🇨🇿🇮🇱🇮🇳🇹🇷🇰🇵'
 us4 = str(''.join((random.choice(mrx) for i in range(2))))
 tlg =(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=ᯓ\n
not hack sory❌
zhmaray cart:{user}
wlat:+{us4}
ᯓ CH :@python968''')
 i = requests.post(tlg)
 print(f'not hack sory❌')
print(f'zhmaray cart:{user}')
print(f'wlat:+{us4}')
print(f'ᯓ CH :@python968')