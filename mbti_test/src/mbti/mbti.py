with open('./src/mbti/question.txt', 'r', encoding='utf-8') as file:
    questions = file.readlines()
tmp = []
for v in questions:
    tmp.append([v[:-6],v[-6:]])

class MBTI():
    def __init__(self):
        self.questions = tmp
        self.score = {'E' : 1, 'I' : 1, 'N' : 1, 'S' : 1, 'F' : 1, 'T' : 1, 'J' : 1, 'P' : 1}
        self.res = ''        
        print('MBTI 테스트를 시작하겠습니다.')
        self.test()

    def result(self):
        if self.score['E'] >= self.score['I']:
            self.res = self.res + 'E'
        else:
            self.res = self.res + 'I'
        if self.score['S'] >= self.score['N']:
            self.res = self.res + 'S'
        else:
            self.res = self.res + 'N'
        if self.score['T'] >= self.score['F']:
            self.res = self.res + 'T'
        else:
            self.res = self.res + 'F'
        if self.score['J'] >= self.score['P']:
            self.res = self.res + 'J'
        else:
            self.res = self.res + 'P'

        print(f'당신의 MBTI는 {self.res}입니다.')
        if self.res[0] == 'E':
            print('외향형(E) ' + '*'*round(20 * self.score['E'] / (self.score['E'] + self.score['I'])) + '.'*round(20 * self.score['I'] / (self.score['E'] + self.score['I'])) + ' 내향형(I)')
        else:
            print('외향형(E) ' + '*'*round(20 * self.score['I'] / (self.score['E'] + self.score['I'])) + '.'*round(20 * self.score['E'] / (self.score['E'] + self.score['I'])) + ' 내향형(I)')

        if self.res[1] == 'S':
            print('감각형(S) ' + '*'*round(20 * self.score['S'] / (self.score['S'] + self.score['N'])) + '.'*round(20 * self.score['N'] / (self.score['S'] + self.score['N'])) + ' 직관형(N)')
        else:
            print('감각형(S) ' + '*'*round(20 * self.score['N'] / (self.score['S'] + self.score['N'])) + '.'*round(20 * self.score['S'] / (self.score['S'] + self.score['N'])) + ' 직관형(N)')
        
        if self.res[2] == 'T':
            print('사고형(T) ' + '*'*round(20 * self.score['T'] / (self.score['T'] + self.score['F'])) + '.'*round(20 * self.score['F'] / (self.score['T'] + self.score['F'])) + ' 감정형(F)')
        else:
            print('사고형(T) ' + '*'*round(20 * self.score['F'] / (self.score['T'] + self.score['F'])) + '.'*round(20 * self.score['T'] / (self.score['T'] + self.score['F'])) + ' 감정형(F)')
        
        if self.res[3] == 'J':
            print('판단형(J) ' + '*'*round(20 * self.score['J'] / (self.score['J'] + self.score['F'])) + '.'*round(20 * self.score['F'] / (self.score['J'] + self.score['F'])) + ' 인식형(F)')
        else:
            print('판단형(J) ' + '*'*round(20 * self.score['F'] / (self.score['J'] + self.score['F'])) + '.'*round(20 * self.score['J'] / (self.score['J'] + self.score['F'])) + ' 인식형(F)')


        

    def test(self):
        print('질문 내용에 해당되면 o, 해당되지 않으면 x를 입력하세요.')
        for idx, v in enumerate(self.questions):
            inp = input(f'\n{len(self.questions)} 중 {idx+1}번째 질문\n{v[0]}\n')
            if v[1] == '(E/I)':
                if inp == 'o':
                    self.score['E'] += 1
                else:
                    self.score['I'] += 1
            if v[1] == '(S/N)':
                if inp == 'o':
                    self.score['S'] += 1
                else:
                    self.score['N'] += 1
            if v[1] == '(T/F)':
                if inp == 'o':
                    self.score['T'] += 1
                else:
                    self.score['F'] += 1
            if v[1] == '(J/P)':
                if inp == 'o':
                    self.score['J'] += 1
                else:
                    self.score['P'] += 1
        self.result()


