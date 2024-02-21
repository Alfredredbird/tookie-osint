from nicegui import ui
from nicegui.events import ValueChangeEventArguments

#----------------------------------------------------------------
#
# This is my webUI implementation that im working on
# You can try it out by running this file but it will not work with Alfred yet
#
#----------------------------------------------------------------


def show(event: ValueChangeEventArguments):
    name = type(event.sender).__name__
    ui.notify(f'{name}: {event.value}')

ui.button('Button', on_click=lambda: ui.notify('Click'), color="#f4a4ad")
with ui.row():
    ui.checkbox('Checkbox', on_change=show)
    ui.switch('Switch', on_change=show)
ui.radio(['A', 'B', 'C'], value='A', on_change=show).props('inline')
with ui.row():
    ui.input('Text input', on_change=show)
    ui.select(['One', 'Two'], value='One', on_change=show)
ui.link('And many more...', '/documentation').classes('mt-8')

ui.run()