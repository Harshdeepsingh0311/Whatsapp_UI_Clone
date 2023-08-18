# Packages to be used
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from kivy.uix.camera import Camera
from kivy.core.window import Window

# To give the window a size of mobile
Window.size = (375, 650)

KV = '''
#Main Screen
Screen: 
    BoxLayout:
        orientation: 'vertical'

        #Navbar
        MDTopAppBar:
            title: 'WhatsApp'
            right_action_items: [['camera-outline', lambda x: app.camera()],['magnify', lambda x: print('Magnify Clicked')],['dots-vertical', lambda x: print('Dots Clicked')]]
        
        #Tabs section
        MDTabs:
            id: tabs #To retrieve it by python code

<Tab>
    MDLabel:
        text: 'Tabs'
        halign: 'center'

            
<ChatTab>
    # To make a scrollable window
    ScrollView:
        MDList:

            #Chats
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
    #To Add own status
    TwoLineIconListItem:
        pos_hint: {'center_x': 0.5,'center_y': 0.95}
        text: 'My status'
        secondary_text: 'Tap to add status update'
        IconLeftWidget:
            icon: 'account-plus'
    MDLabel:
        pos_hint: {'center_x': 0.5,'center_y': 0.85}
        text: '   Recent Updates'
        theme_text_color: 'Secondary'
    
    # Status of others
    MDList:
        pos_hint: {'center_x': 0.5,'center_y': 0.64}
        TwoLineIconListItem:
            text: 'Person 1'
            secondary_text: 'Today, 12:17 pm'
            IconLeftWidget:
                icon: 'account-circle-outline'
        TwoLineIconListItem:
            text: 'Person 2'
            secondary_text: 'Today, 9:12 am'
            IconLeftWidget:
                icon: 'account-circle-outline'
        TwoLineIconListItem:
            text: 'Person 3'
            secondary_text: 'Today, 7:03 am'
            IconLeftWidget:
                icon: 'account-circle-outline'
            
    # General security Message
    MDLabel:
        pos_hint: {'center_x': 0.5,'center_y': 0.3}
        text: 'Your status updates are end to end encrypted'
        halign: 'center'
        theme_text_color: 'Secondary'

            
    

<CallsTab>
    # To create a call link
    TwoLineIconListItem:
        pos_hint: {'center_x': 0.5,'center_y': 0.95}
        text: 'Create a call link'
        secondary_text: 'Share a link for your WhatsApp call'
        MDFloatingActionButton:
            pos_hint: {'center_x': 0.08,'center_y': 0.4}
            icon: 'link-variant'
            md_bg_color: app.theme_cls.primary_color
    
    MDLabel:
        pos_hint: {'center_x': 0.5,'center_y': 0.85}
        text: '   Recent'
        theme_text_color: 'Secondary'

    # Recent Calls
    MDList:
        pos_hint: {'center_x': 0.5,'center_y': 0.64}
        TwoLineIconListItem:
            text: 'Person 1'
            secondary_text: 'Today, 12:17 pm'
            IconLeftWidget:
                icon: 'account-circle-outline'
            
        TwoLineIconListItem:
            text: 'Person 2'
            secondary_text: 'Today, 9:12 am'
            IconLeftWidget:
                icon: 'account-circle-outline'
        TwoLineIconListItem:
            text: 'Person 3'
            secondary_text: 'Today, 7:03 am'
            IconLeftWidget:
                icon: 'account-circle-outline'
            
    MDFloatingActionButton:
        id: button
        icon: 'phone-plus'
        md_bg_color: app.theme_cls.primary_color
        x: root.width - self.width - dp(10)
        y: dp(10)
    

<CommunityTab>
    # Just image community section
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

# Classes for each tab in navbar
class ChatTab(MDFloatLayout, MDTabsBase):
    pass

class StatusTab(MDFloatLayout, MDTabsBase):
    pass

class CallsTab(MDFloatLayout, MDTabsBase):
    pass

class CommunityTab(MDFloatLayout, MDTabsBase):
    pass


# Main app
class WhatsApp(MDApp):
    def build(self):
        # To change the theme and title of the window
        self.theme_cls.primary_palette = 'Teal'
        self.theme_cls.primary_hue = '700'
        self.title = 'WhatsApp'
        screen = Builder.load_string(KV)

        return screen
    
    def on_start(self):
        # To add widgets from outside of KV File
        self.root.ids.tabs.add_widget(CommunityTab(icon='account-group'))
        self.root.ids.tabs.add_widget(ChatTab(title='Chats'))
        self.root.ids.tabs.add_widget(StatusTab(title='Status'))
        self.root.ids.tabs.add_widget(CallsTab(title='Calls'))

    def camera(self):
        # Future upgradation
        print('camera clicked')

WhatsApp().run()