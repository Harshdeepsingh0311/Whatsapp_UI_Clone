from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from kivy.core.window import Window

Window.size = (350, 650)

KV = '''
Screen: 
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: 'WhatsApp'
            right_action_items: [['camera-outline', lambda x: print('Camera Clicked')],['magnify', lambda x: print('Magnify Clicked')],['dots-vertical', lambda x: print('Dots Clicked')]]
        MDTabs:
            id: tabs

<Tab>
    MDLabel:
        text: 'Tabs'
        halign: 'center'

            
<ChatTab>
    MDLabel:
        text: 'Chats'
        halign: 'center'        
'''

class ChatTab(MDFloatLayout, MDTabsBase):
    pass

class Tab(MDFloatLayout, MDTabsBase):
    pass


class WhatsApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Teal'
        self.theme_cls.primary_hue = '700'
        self.title = 'WhatsApp'
        screen = Builder.load_string(KV)

        return screen
    
    def on_start(self):
        self.root.ids.tabs.add_widget(Tab(icon='account-group'))
        self.root.ids.tabs.add_widget(ChatTab(title='Chats'))
        self.root.ids.tabs.add_widget(Tab(title='Status'))
        self.root.ids.tabs.add_widget(Tab(title='Calls'))

WhatsApp().run()