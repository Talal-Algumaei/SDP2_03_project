from channels.generic.websocket import AsyncWebsocketConsumer
import json

class DashConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.groupname='dashboard'
        await self.channel_layer.group_add(
            self.groupname,
            self.channel_name,
        )

        await self.accept()

    async def disconnect(self,close_code):

        await self.channel_layer.group_discard(
            self.groupname,
            self.channel_name
        )
    

    async def receive(self, text_data):
        datapoint = json.loads(text_data)
        N_temp = datapoint['temp_N']
        B_temp = datapoint['temp_B']
        datatosend = datapoint['data']
        print(datatosend)
        await self.channel_layer.group_send(
            self.groupname,
            {
                'type':'deprocessing',
                'temp_N':N_temp,
                'temp_B':B_temp,
                'control_com':datatosend,

            }
        )

        print ('>>>>',text_data)

        # pass


    async def deprocessing(self,event):
        New_temp_N = event['temp_N']
        New_temp_B = event['temp_B']
        Control_command = event['control_com']
        await self.send(
            text_data = json.dumps(
                {'temp_N':New_temp_N, 'temp_B':New_temp_B,
                'control_com':Control_command,})
                )
