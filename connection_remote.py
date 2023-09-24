import socketio
#import main

sio = socketio.Client()

@sio.on('connect')
def on_connect():
    print ('connected to server')

@sio.on('disconnected from server')
def on_disconnect():
    print('diconnected from server')

sio.connect('http://localhost:3000')

#values = main.values
#print('VALORES',values)
def sendValue(values):
    brain_data = values
    sio.emit('brain_data',brain_data)
