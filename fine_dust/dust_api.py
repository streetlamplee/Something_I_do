import requests
import json

def leveling(data):
    if data < 33:
        return '좋음'
    elif data < 66:
        return '보통'
    else:
        return '나쁨'

def get_dust_data():
    inp = input('지역 입력 : ')
    url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty'


    params ={'serviceKey' : '3xJixLktNjSGwaAq+sKzOhz4jOZSswacVcPdJmMZp6oWE/Fk+WYkYaUHbph3U2UaApumtTrzPA+3eycLFHuXLA==',
            'returnType' : 'json', 
            'numOfRows' : '1', 
            'pageNo' : '1', 
            'stationName' : inp, 
            'dataTerm' : 'DAILY', 
            'ver' : '1.0' }


    response = requests.get(url, params=params)

    if response.status_code == 200:
        print('success')
        res = json.loads(response.text)

        item = res['response']['body']['items'][0]
        print('측정 시간 : {}'.format(item['dataTime']))
        print('미세먼지 : {}'.format(leveling(int(item['pm10Value'])))) 
        print('초미세먼지 : {}'.format(leveling(int(item['pm25Value'])))) 
    else:
        print('Requests failed error {}'.format(response.status_code))

get_dust_data()