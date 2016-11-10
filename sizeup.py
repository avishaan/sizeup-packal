import alfred
import os
import re

# ##
PRESS_SHORTCUT_KEY_CODE = '''tell application "System Events"
                            key code %s using %s
                        end tell'''

CTRL_OPTION_COMMAND_DOWN = "{control down, option down, command down}"
CTRL_OPTION_SHIFT_DOWN = "{control down, option down, shift down}"
KEY_CODE = "key code %s"


KEY_CODE_LEFT = "123"
KEY_CODE_RIGHT = "124"
KEY_CODE_DOWN = "125"
KEY_CODE_UP = "126"

KEY_CODE_M = "46"
KEY_CODE_C = "8"
KEY_CODE_FORWARD_SLASH = "44"
ITEMS = [
            {"name":"SnapBack", "script": PRESS_SHORTCUT_KEY_CODE % (KEY_CODE_FORWARD_SLASH, CTRL_OPTION_COMMAND_DOWN), "key": ""}
            , {"name":"Center", "script": PRESS_SHORTCUT_KEY_CODE % (KEY_CODE_C, CTRL_OPTION_COMMAND_DOWN), "key": ""}
            , {"name":"Left", "script": PRESS_SHORTCUT_KEY_CODE % (KEY_CODE_LEFT, CTRL_OPTION_COMMAND_DOWN), "key": ""}
            , {"name":"Right", "script": PRESS_SHORTCUT_KEY_CODE % (KEY_CODE_RIGHT, CTRL_OPTION_COMMAND_DOWN), "key": ""}
            , {"name":"Down", "script": PRESS_SHORTCUT_KEY_CODE % (KEY_CODE_DOWN, CTRL_OPTION_COMMAND_DOWN), "key": ""}
            , {"name":"Up", "script": PRESS_SHORTCUT_KEY_CODE % (KEY_CODE_UP, CTRL_OPTION_COMMAND_DOWN), "key": ""}
            , {"name":"Upper Left", "script": PRESS_SHORTCUT_KEY_CODE % (KEY_CODE_LEFT, CTRL_OPTION_SHIFT_DOWN), "key": "ul"}
            , {"name":"Upper Right", "script": PRESS_SHORTCUT_KEY_CODE % (KEY_CODE_UP, CTRL_OPTION_SHIFT_DOWN), "key": "ur"}
            , {"name":"Lower Left", "script": PRESS_SHORTCUT_KEY_CODE % (KEY_CODE_DOWN, CTRL_OPTION_SHIFT_DOWN), "key": "ll"}
            , {"name":"Lower Right", "script": PRESS_SHORTCUT_KEY_CODE % (KEY_CODE_RIGHT, CTRL_OPTION_SHIFT_DOWN), "key": "lr"}
            , {"name":"Full Screen", "script": PRESS_SHORTCUT_KEY_CODE % (KEY_CODE_M, CTRL_OPTION_COMMAND_DOWN), "key": ""}
        ]

def doaction(query):
    if not query:
        return
    selected = alfred.Action.from_json_str(query)["name"]
    for item in ITEMS:
        name = item["name"]
        if name == selected:
            alfred.Action.run_applescript(item["script"])


def get_items(query, part):
    feedbacks = alfred.Feedback()
    for item in ITEMS:
        name = item["name"]
        if not query or query.lower() in name.lower() or query.lower() in item["key"]:
            arg = alfred.Action.to_json_str({"part": 1, "name": name})
            feedbacks.addItem(title=name, arg=arg, icon="icons/%s.png" % name, autocomplete=name)
    return feedbacks

if __name__ == "__main__":
    ACTION_MAPS = {1: alfred.Action(1, get_items, doaction)}
    alfred.Action.run(ACTION_MAPS)
