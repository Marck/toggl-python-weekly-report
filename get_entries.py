# Using https://github.com/aarose/togglwrapper
from togglwrapper import Toggl
import json

def config(filename: str = "config"):
    """ Fetch config file """
    try:
        with open(f"{filename}.json", encoding='utf8') as data:
            return json.load(data)
    except FileNotFoundError:
        raise FileNotFoundError("JSON file wasn't found")

config = config("config")

toggl = Toggl(config['tokens']['api'])

# toggl.TimeEntries.get()

workspaces = toggl.Workspaces.get()
[{
    u'admin': True,
    u'api_token': config['tokens']['api'],
    u'id': 1234,
    u'name': u"Your workspace"
}]

# toggl.User.get()
# {u'data': {
#     u'achievements_enabled': True,
#     u'api_token': config['tokens']['api'],
#     u'email': u'your_email@domain.com',
#     u'fullname': u'Your Name'
#     }
# }

# toggl.Clients.get()
# [{
#     u'at': u'2015-07-02T14:27:59+00:00',
#     u'id': 12031893,
#     u'name': u'Client Name',
#     u'wid': 3928
# }]

# toggl.Clients.create({"client":{"name":"Very Big Company", "wid": 1234}})
# {u'data': {u'id': 294021, u'name': u'Very Big Company', u'wid': 1234}}