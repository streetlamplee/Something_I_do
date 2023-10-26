import json
import random

class Game():
    def __init__(self):
        with open('./src/dictionary.json') as file:
            self.dictionary = json.load(file)
        self.dictionary = dict(self.dictionary)
        x = int(input('          선공/후공을 정해주세요\n            선공 : 0 , 후공 : 1\n잘못된 값이 입력되면 자동으로 선공으로 시작합니다.\n'))
        print('\n게임을 시작합니다.\n(규칙 : 2글자 이상 4글자 이하)\n\n')
        self.start(first = x)


    def start(self, first : int):
        if first != 1:
            self.playerturn()
        else:
            self.computerturn()


    def playerturn(self, last = '0'):
        if last == '0':
            wrd_p = input('단어를 적어주세요\n\n')
            self.computerturn(last = wrd_p[-1])
        else:
            if last not in self.dictionary.keys():
                print(f'{last} (으)로 시작하는 단어가 없습니다.\n  졌습니다 :(')
                return
            else:
                wrd_p = input(f'"{last}" (으)로 시작하는 단어를 적어주세요\n\n')
                checking = False
                for v in self.dictionary.values():
                    if wrd_p in v:
                        checking = True
                    else:
                        continue
                if checking:
                    self.computerturn(last = wrd_p[-1])
                else:
                    print(f'{wrd_p} (은)는 사전에 없는 단어입니다.\n  졌습니다 :(')

                    
    def computerturn(self, last = '0'):
        if last == '0':
            cpt_p = random.choice(self.dictionary[random.choice(list(self.dictionary.keys()))])
            print(f'\n{cpt_p}\n\n')
            self.playerturn(last = cpt_p[-1])
        else:
            if last not in self.dictionary.keys():
                print(f'\n{last} (으)로 시작하는 단어가 없습니다.\n  이겼습니다 :)')
                return
            else:
                cpt_p = random.choice(self.dictionary[last])
                print(f'\n{cpt_p}\n\n')
                self.playerturn(last = cpt_p[-1])
