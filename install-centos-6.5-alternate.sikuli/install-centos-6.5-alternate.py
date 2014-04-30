vm_name = "centos-test"
# root password
password = "password"


def start_text_mode():
    '''Select non-gui (text mode) install mode'''
    wait("1398605856094.png", 30)
    App.focus(vm_name)        
    type(Key.TAB)    
    type(" text")
    type(Key.ENTER)

def skip_media_check():
    wait("1396998092666-1.png", 20)
    App.focus(vm_name)
    type(Key.RIGHT)
    type(Key.ENTER)

def splash_screen():
    wait("1398607150224.png", 30)
    App.focus(vm_name)        
    type(Key.ENTER)

def select_language():
    wait("1398607411659.png", 5)
    App.focus(vm_name)        
    type(Key.ENTER)        
    wait("1398606191410.png", 5)
    type(Key.ENTER)            

def reinitialise():
    try:
        wait("1398607491333.png", 5)
        App.focus(vm_name)        
        type(Key.TAB)        
        type(Key.TAB)        
        type(Key.TAB)        
        type(Key.ENTER)        
    except:
        pass

def time():
    wait("1398607655294.png", 5)
    App.focus(vm_name)        
    type(Key.TAB)
    for _ in range(32):
        type(Key.PAGE_DOWN)
    type(Key.UP)
    type(Key.UP)
    type(Key.UP)
    type(Key.UP)
    type(Key.TAB)
    type(Key.ENTER)        

def set_password():
    wait("1398607973622.png", 5)
    App.focus(vm_name)        
    type(password)
    type(Key.TAB)        
    type(password)
    type(Key.TAB)        
    type(Key.ENTER)        
    if exists("1398608123376.png"):
        type(Key.TAB)        
        type(Key.ENTER)        

def partitioning():
    wait("1398608259938.png", 10)
    App.focus(vm_name)        
    type(Key.UP)
    type(Key.TAB)
    type(Key.TAB)
    type(Key.ENTER)        
    # Confirmation window
    wait("1398608452100.png", 2)
    type(Key.TAB)
    type(Key.ENTER)        
    

start_text_mode()
skip_media_check()
splash_screen()
select_language()
reinitialise()
time()
set_password()
partitioning()
