from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from kivy.core.window import Window

Window.size = (375, 650)

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
    ScrollView:
        MDList:
            TwoLineAvatarListItem:
                text: 'Jaggi Bhai'
                secondary_text: 'Hello'
                ImageLeftWidget:
                    source: 'static/jaggi.jpeg' 

            TwoLineAvatarListItem:
                text: 'Hemnag'
                secondary_text: 'Ok Bhai!'
                ImageLeftWidget:
                    source: 'static/hemnag.jpeg' 

            TwoLineAvatarListItem:
                text: 'Piyus'
                secondary_text: 'Khaane peene ka plan banao bhai!!'
                ImageLeftWidget:
                    source: 'static/piyus.jpeg'      

            TwoLineAvatarListItem:
                text: 'Pamreet'
                secondary_text: 'Bhai Straight lines kr rha hu'
                ImageLeftWidget:
                    source: 'static/pamreet.jpeg'

            TwoLineAvatarListItem:
                text: 'Anuz Bhai'
                secondary_text: 'Aaj kal kuchh hara hara nahi dikh rha sab orange hi h!'
                ImageLeftWidget:
                    source: 'static/anuz.jpeg'

<StatusTab>
    MDLabel:
        text: 'Status'
        halign: 'center'

<CallsTab>
    MDLabel:
        text: 'Calls'
        halign: 'center'

<CommunityTab>
    Image:
        source: 'static/community.png'
        size_hint: 0.5, 0.5 
        pos_hint: {'center_x': 0.5,'center_y': 0.8}
        halign: 'center'
    MDLabel:
        text: 'Introducing communities'
        pos_hint: {'center_x': 0.5,'center_y': 0.6}
        halign: 'center'
        font_style: 'H5'
        theme_text_color: 'Primary'
    MDLabel:
        text: 'Easily organize your related grups and send announcements. Now, your communities, like neighbourhoods or schools, can have their own space.'
        pos_hint: {'center_x': 0.5,'center_y': 0.5}
        halign: 'center'
        theme_text_color: 'Secondary'
    MDFillRoundFlatButton:
        text: "Start your community"
        text_color: "white"
        pos_hint: {'center_x': 0.5,'center_y': 0.35}
        halign: 'center'

'''

class ChatTab(MDFloatLayout, MDTabsBase):
    pass

class StatusTab(MDFloatLayout, MDTabsBase):
    pass

class CallsTab(MDFloatLayout, MDTabsBase):
    pass

class CommunityTab(MDFloatLayout, MDTabsBase):
    pass

class WhatsApp(MDApp):
    def build(self):
        # self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Teal'
        self.theme_cls.primary_hue = '700'
        self.title = 'WhatsApp'
        screen = Builder.load_string(KV)

        return screen
    
    def on_start(self):
        self.root.ids.tabs.add_widget(CommunityTab(icon='account-group'))
        self.root.ids.tabs.add_widget(ChatTab(title='Chats'))
        self.root.ids.tabs.add_widget(StatusTab(title='Status'))
        self.root.ids.tabs.add_widget(CallsTab(title='Calls'))

WhatsApp().run()