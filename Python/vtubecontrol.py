import pyvts
import asyncio
import discord

plugin_info = {
    "plugin_name": "VtubeEmulateEMO",
    "developer": "Kazilsky",
    "authentication_token_path": "./token.txt"
}

vts = pyvts.vts(plugin_info=plugin_info)

async def anm_play(anim):
    response_data = await vts.request(vts.vts_request.requestHotKeyList())
    hotkey_list = []
    for hotkey in response_data['data']['availableHotkeys']:
        hotkey_list.append(hotkey['name'])
    print(hotkey_list) 
    send_hotkey_request = vts.vts_request.requestTriggerHotKey(hotkey_list[anim])

    await vts.request(send_hotkey_request) # send request to play 'My Animation 1'
    await vts.close()

async def MouthSmile(param):
    await vts.request(vts.vts_request.requestSetParameterValue("MouthSmile", param, weight=1, mode='set'))
    print(param)

async def StartVtube():
    await vts.connect()
    await vts.request_authenticate_token()  # get token
    await vts.request_authenticate()  # use token
    new_parameter_name = "start_parameter"
    # await vts.request(
    #     vts.vts_request.requestCustomParameter(new_parameter_name)
    # )  # add new parameter
    # await MouthSmile(0)
    