from pluginDefault import PluginDefault
from plugins.alarm.plugin import PluginAlarm
from plugins.remote.plugin import PluginRemote
from plugins.youtube.plugin import PluginYoutube

class PluginFactory:

    def getPlugin(subject, typeS):
        themeName= subject.split(".")[0]    
        if themeName== "alarm":
            return PluginAlarm(subject, typeS)
        elif themeName== "remote":
            return PluginRemote(subject, typeS)
        elif themeName== "youtube":
            return PluginYoutube(subject, typeS)
        return PluginDefault(subject, typeS)
        