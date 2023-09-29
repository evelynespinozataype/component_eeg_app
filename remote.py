import socketio
#import main

sio = socketio.Client()

@sio.on('connect')
def on_connect():
    print ('connected to server')

@sio.on('disconnected from server')
def on_disconnect():
    print('diconnected from server')

sio.connect('http://localhost:4000') #aquarela 3000

# Solo para test
brain_data = {'Name': ['John', 'Anna', 'Peter'],'Age': [28, 24, 35]}
sio.emit('join_comp_brainwave_app',brain_data)

def send_brainwaves(data):
    brain_data = data
    sio.emit('join_comp_brainwave_app', brain_data)
    data = ''
    brain_data = ''

# Solo para test
sio.sleep(2)

# Solo para test
sio.disconnect()

#values = main.values
#print('VALORES',values)
#def sendValue(values):
#    brain_data = values
#    sio.emit('brain_data',brain_data)
