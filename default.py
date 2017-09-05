# -*- coding: utf-8 -*-
#------------------------------------------------------------
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.vanlife'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID1 = "UCHV7BvFPyD5Lixoo8yMRiLA"
YOUTUBE_CHANNEL_ID2 = "UCSCRVmBT1YyuAlCA8c9FJRA"
YOUTUBE_CHANNEL_ID3 = "UCYCkPUDqQjru1vx_hSaZUaw"

# Entry point
def run():
# Get params
	params = plugintools.get_params()

	if params.get("action") is None:
		main_list(params)
	else:
		action = params.get("action")
		exec action+"(params)"

	plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("vanlife.main_list "+repr(params))

plugintools.add_item( 
    #action="", 
    title="Kombi Life",
    url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID1+"/",
    thumbnail=icon,
    folder=True )

plugintools.add_item( 
    #action="", 
    title="Nomadic Life",
    url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID2+"/",
    thumbnail=icon,
    folder=True )
	
plugintools.add_item( 
    #action="", 
    title="Living In A Van",
    url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID3+"/",
    thumbnail=icon,
    folder=True )

run()