def create_tag(tag_name):
    click("1398695755110.png")
    click("1398695791349.png")
    click("1398695819476.png")
    type(tag_name)
    type(Key.TAB)
    type(Key.TAB)
    type(Key.TAB)
    type(Key.TAB)
    type(Key.TAB)
    type(Key.TAB)
    type(Key.TAB)
    type(Key.ENTER)
    if exists(Pattern("1398695893759.png").targetOffset(13,1)):
        click(Pattern("1398695893759.png").targetOffset(13,1))
    click("1398696192611.png")

def add_contact(name, email):
    click(Pattern("1398695755110.png").targetOffset(-71,-1))
    click("1398696317827.png")
    click("1398696340339.png")
    type(name)
    click("1398696361775.png")
    type(email)
    click("1398696375911.png")
    click(Pattern("1398696441057.png").targetOffset(119,35))
    click("1398696192611.png")

def send_email(to, subject, body):
    click(Pattern("1398695755110.png").targetOffset(-137,-2))
    click("1398696673057.png")
    type(to)
    type(Key.ENTER)
    click("1398696685413.png")
    type(subject)
    click("1398696703076.png")
    type(body)
    click("1398696715933.png")
    if exists(Pattern("1398695893759.png").targetOffset(13,1)):
        click(Pattern("1398695893759.png").targetOffset(13,1))
    click("1398696192611.png")
    

create_tag('foo')
add_contact("Bob Rock", "bobrock@metallica.net")
send_email(
    'Joker <thejoker@marvel.com>', 
    'Come and face justice, Joker',
    'Your time is up, evil-doer'
    )