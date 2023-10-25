import requests
import json

### 토큰만료시 실행
#https://kauth.kakao.com/oauth/authorize?client_id=ea52238db25c250497088162256e68d1&redirect_uri=https://example.com/oauth&response_type=code

def create_tk():
    url = "https://kauth.kakao.com/oauth/token"
    data = {
        "grant_type" : "authorization_code",
        "client_id" : "ea52238db25c250497088162256e68d1",
        "redirect_url" : "https://google.com",
        "code" : 'BhScug-SBgpvlpP368OjG0WJEpUFg4C8LT-LflfpL9qbmMmly_1HTT_KxDwKPXVcAAABi2S7aIWm1x-HnlkNwQ'
    }   
    response = requests.post(url, data=data)
    tokens = response.json()
    if 'access_token' in tokens:
        with open('./src/kakaopipeline/kakao_token.json', 'w') as fp:
            json.dump(tokens, fp)
            print('token saved')
    else:
        print('error happened')
        print(tokens)

def refresh_tk():
    with open('./src/kakaopipeline/kakao_token.json', 'r') as fp:
        tokens = json.load(fp)
    url = 'https://kauth.kakao.com/oauth/token'
    data = {
        'grant_type' : 'refresh_token',
        'client_id' : 'ea52238db25c250497088162256e68d1',
        'refresh_token' : tokens['refresh_token']
    }

    response = requests.post(url, data = data)
    result = response.json()

    # 갱신 된 내용으로 파일 업데이트
    if 'access_token' in result:
        tokens['access_token'] = result['access_token']

    if 'refresh_token' in result:
        tokens['refresh_token'] = result['refresh_token']
    else:
        pass

    with open("./src/kakaopipeline/kakao_token.json", "w") as fp:
        json.dump(tokens, fp)

