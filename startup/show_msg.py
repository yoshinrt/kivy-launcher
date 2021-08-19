#!/usr/bin/env python3

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.scrollview import ScrollView

Builder.load_string('''
<MsgWidget>
	size_hint: 1, 1
	
	TextInput:
		text: root.msg
		text_size: self.width, self.height
		height: self.minimum_height
		size_hint_y: None
		halign: 'left'
		valign: 'top'
		readonly: True
		foreground_color: 1, 0, 0, 1
		background_color: 0, 0, 0, 1
''')

class MsgWidget(ScrollView):
	msg = StringProperty()
	
	def __init__(self, **kwargs) -> None:
		super(MsgWidget, self).__init__(**kwargs)
	
class ShowMsgApp(App):
	msg = StringProperty()
	
	def __init__(self, **kwargs):
		super(ShowMsgApp, self).__init__(**kwargs)
	
	def build(self):
		return MsgWidget(msg = self.msg)

if __name__ == '__main__':
	ShowMsgApp(msg = 'Show message').run()
