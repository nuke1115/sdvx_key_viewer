import pygame as pg , os , configparser , random
konmai = random.randint(1,1000)
#konmai = int(573)#임시
config = configparser.ConfigParser()
config.read('assets/settings.ini')
key_value=[]
KeySettings = config.sections()
os.environ["SDL_JOYSTICK_ALLOW_BACKGROUND_EVENTS"] = "1"
pg.init()
pg.joystick.init()
width = 1311
height = 687
screen = pg.display.set_mode((width, height))
pg.display.set_caption('sdvx key viewer ver.1.0(yuancon)')
clock = pg.time.Clock()
joysticks = [pg.joystick.Joystick(x) for x in range(pg.joystick.get_count())]
running = bool(True)
start = bool(False)
font = pg.font.SysFont(None,42)
BLACK = (0,0,0)
WHITE = (255,255,255)
buttons = [int(0),int(0),int(0),int(0),int(0),int(0),int(0),int(0)]#0~3:bt 4~5:fx 6:start ,7:total_count , startcount=
gif_l = int(0)
gif_r = int(0)
class imgs:
    global bt0 ,bt1 ,fx0_r ,fx1_r ,fx0_l,fx1_l,start0 ,start1 ,bg ,vol_l, vol_r, vol_off , start , a , b , c , d , l , r , vol_l_img , vol_r_img, vol_konmai,al,ar,bb
    al = 142
    ar = 1068
    bb = 115
    bt0 = pg.image.load('assets/bt_off.jpg')
    bt1 = pg.image.load('assets/bt_on.jpg')
    fx0_l = pg.image.load('assets/fx_off.jpg')
    fx1_l = pg.image.load('assets/fx_on.jpg')
    fx0_r = pg.image.load('assets/fx_off.jpg')
    fx1_r = pg.image.load('assets/fx_on.jpg')
    vol_l = pg.image.load('assets/vol_l.png')
    vol_r = pg.image.load('assets/vol_r.png')
    vol_off = pg.image.load('assets/vol_off.png')
    start0 = pg.image.load('assets/start_off.jpg')
    start1 = pg.image.load('assets/start_on.jpg')
    bg = pg.image.load('assets/bg.png')
    vol_konmai = [pg.image.load('assets/vol_konmai_1.png'),pg.image.load('assets/vol_konmai_2.png'),pg.image.load('assets/vol_konmai_3.png'),pg.image.load('assets/vol_konmai_5.png'),pg.image.load('assets/vol_konmai_5.png'),pg.image.load('assets/vol_konmai_6.png'),pg.image.load('assets/vol_konmai_7.png'),pg.image.load('assets/vol_konmai_8.png'),pg.image.load('assets/vol_konmai_9.png'),pg.image.load('assets/vol_konmai_10.png')]
    if konmai == 573:
        bg = pg.image.load('assets/bg_konmai.png')
        bt1 = pg.image.load('assets/bt_konmai.png')
        fx0_r = pg.image.load('assets/fx_off_konmai_r.jpg')
        fx1_r = pg.image.load('assets/fx_on_konmai_r.jpg')
        fx0_l = pg.image.load('assets/fx_off_konmai_l.jpg')
        fx1_l = pg.image.load('assets/fx_on_konmai_l.jpg')
        start0 = pg.image.load('assets/start_off_konmai.png')
        start1 = pg.image.load('assets/start_on_konmai.jpg')
        vol_l = vol_konmai[0]
        vol_r = vol_konmai[0]
        vol_off = vol_konmai[0]
        al = 115
        ar = 1041
        bb = 90
    start = start0
    a = bt0
    b = bt0
    c = bt0
    d = bt0
    l = fx0_l
    r = fx0_r
    vol_l_img = vol_off
    vol_r_img = vol_off
class input_vars:
    global knob_l_stop, knob_r_stop , knob_r_run, knob_l_run, key_value
    knob_l_stop=bool(True)
    knob_l_run = bool(False)
    knob_r_stop=bool(True)
    knob_r_run = bool(False)
    key_value.append(int(config['KeySettings']['start']))
    key_value.append(int(config['KeySettings']['bt_a']))
    key_value.append(int(config['KeySettings']['bt_b']))
    key_value.append(int(config['KeySettings']['bt_c']))
    key_value.append(int(config['KeySettings']['bt_d']))
    key_value.append(int(config['KeySettings']['fx_l']))
    key_value.append(int(config['KeySettings']['fx_r']))
def keydown():
    global start, a, b, c, d, l, r, buttons
    if event.button != key_value[0]:
        buttons[7] += 1
    if event.button == key_value[0]:
        start = start1
        buttons[6] += 1
    if event.button == key_value[1]:
        a = bt1
        buttons[0] += 1
    if event.button == key_value[2]:
        b = bt1
        buttons[1] += 1
    if event.button == key_value[3]:
        c = bt1
        buttons[2] += 1
    if event.button == key_value[4]:
        d = bt1
        buttons[3] += 1
    if event.button == key_value[5]:
        l = fx1_l
        buttons[4] += 1
    if event.button == key_value[6]:
        r = fx1_r
        buttons[5] += 1
def keyup():
    global start, a, b, c, d, l, r
    if event.button == key_value[0]:
        start = start0
    if event.button == key_value[1]:
        a = bt0
    if event.button == key_value[2]:
        b = bt0
    if event.button == key_value[3]:
        c = bt0
    if event.button == key_value[4]:
        d = bt0
    if event.button == key_value[5]:
        l = fx0_l
    if event.button == key_value[6]:
        r = fx0_r
def knob():
    global knob_l_stop, knob_l_run, vol_l_img, knob_r_stop, knob_r_run, vol_r_img, gif_l, gif_r
    if event.axis == 0:
        knob_l_stop = bool(False)
        knob_l_run = bool(True)
        if konmai != 573:
            vol_l_img = vol_l
        if konmai == 573:
            gif_l += 1
            vol_l_img = vol_konmai[gif_l]
            if gif_l == 8:
                gif_l = int(0)
    if event.axis == 1:
        knob_r_stop = bool(False)
        knob_r_run = bool(True)
        if konmai != 573:
            vol_r_img = vol_r
        if konmai == 573:
            gif_r += 1
            vol_r_img = vol_konmai[gif_r]
            if gif_r == 8:
                gif_r = int(0)
def screenblit():
    screen.blit(bg, (0,0))
    screen.blit(start, (619,105))
    screen.blit(a, (299,271))
    screen.blit(b, (493,271))
    screen.blit(c, (694,271))
    screen.blit(d, (888,271))
    screen.blit(l, (409,481))
    screen.blit(r, (803,481))
    screen.blit(vol_l_img,(al,bb))
    screen.blit(vol_r_img,(ar,bb))
    screen.blit(button_sum_txt[0],(345,320))
    screen.blit(button_sum_txt[1],(543,320))
    screen.blit(button_sum_txt[2],(744,320))
    screen.blit(button_sum_txt[3],(938,320))
    screen.blit(button_sum_txt[4],(440,495))
    screen.blit(button_sum_txt[5],(839,495))
    screen.blit(button_sum_txt[6],(650,600))
    pg.display.update()
def debug():
    if start == True:
        print("start")
    if a == True:
        print("a")
    if b == True:
        print("b")
    if c == True:
        print("c")
    if d == True:
        print("d")
    if l == True:
        print("e")
    if r == True:
        print("f")
    if knob_l_stop == False:
        print("L")
    if knob_r_stop == False:
        print("R")
while running:
    knob_l_run = bool(False)
    knob_r_run = bool(False)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = bool(False)
        if event.type == pg.JOYBUTTONDOWN:
            keydown()
        if event.type == pg.JOYBUTTONUP:
            keyup()
        if event.type == pg.JOYAXISMOTION:
            knob()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_DELETE:
                buttons = [int(0),int(0),int(0),int(0),int(0),int(0),int(0),int(0)]
    if knob_l_run == False:
        vol_l_img = vol_off
        knob_l_stop = bool(True)
        knob_l_run = bool(False)
    if knob_r_run == False:
        vol_r_img = vol_off
        knob_r_stop = bool(True)
        knob_r_run = bool(False)
    clock.tick(240)
    button_sum_txt = [font.render(str(buttons[0]),True,BLACK),font.render(str(buttons[1]),True,BLACK),font.render(str(buttons[2]),True,BLACK),font.render(str(buttons[3]),True,BLACK),font.render(str(buttons[4]),True,WHITE),font.render(str(buttons[5]),True,WHITE),font.render(str(buttons[7]),True,WHITE)]
    screenblit()
pg.joystick.quit()
pg.quit()
'''
https://www.youtube.com/watch?v=Hp0M8iExfDc&t=181s
https://www.youtube.com/watch?v=ax3E0pjXVKs&t=691s
knob_l_now = round(pg.joystick.Joystick(0).get_axis(0),10)
knob_r_now = round(pg.joystick.Joystick(0).get_axis(1),10)
todo:
노브 돌리는대로 화면에 출력하기
    방법:
    1(실패):
    노브의 현제값과 과거값을 저장하고 비교해가면서 현제>과거면 노브를 안쪽으로 돌린거, 현제<과거면 밖으로 돌린거
        ㄴ이 방법을 무슨 이유에선지 작동이 똑바로 안된다(노브를 일정 속도 이하로 돌리면 감지가 안됨.)
    2(실패):
    노브의값과 고정되있는 노브의 값과 비교해서 현재 노브의 값과 일치하는 곳의 변수를 이미지의 각도에 고정해서 노브가 돌아가면 이미지가 같이 돌아가게 하기
        ㄴ이미지의 각도를 임의로 고정을 할 방법을 못찾음(아마도 코드 자체가 없을것으로 보임)
        문제점2:
        코드가 너무나도 길어진다(찾은 위치값만 255게인데 조건문같은걸 쓰면 저기에 2배가 된다. 그러면 코드는 저거 하나만을 위해 대략 1천줄이 들어가게 된다)
또다른 방법:
    그냥 노브 방향을 보여주지 말고, 노브가 입력이 됐다는것만 보여준다.
    문제점:
        ㄴ노브 방향이 어디로 들어갔는지 안보여주면 나중에 영상을 돌려볼때
        내가 틀린이유를 못찾을수도 있음
    장점:
        ㄴ코드가 상당히 간편해진다
또 다른거:
    최대, 최소를 구한다.
    처음 코드가 실행됬을때 노브의 현재 값과 최대, 최소의 값 차이를 구하고 그 차이를 변수 2개에 기록한다
    노브가 돌아가면, 노브의 현재 값과 최대, 최소의 값 차이를 구하고 또다른 변수 2개에 기록한다
    그 차이를 보고 노브가 최대와는 멀어지고 최소와 가까워지면 왼쪽, 그 반대면 오른쪽으로 돌아간거다
ㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗ
'''