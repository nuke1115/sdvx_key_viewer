import pygame as pg , os , configparser , random
konmai = random.randint(1,1000)
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