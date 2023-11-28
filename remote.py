import socketio

sio = socketio.Client()

@sio.on('connect')
def on_connect():
    print ('connected to server 4000')

@sio.on('disconnect')
def on_disconnect():
    print('diconnected from server 4000')

#sio.connect('http://192.168.15.6:4000',namespaces=['/remote_eegapp'])
sio.connect('http://localhost:4000',namespaces=['/remote_eegapp'])

def send_brainwaves(data):
    #brain_data = data
    #print('Sending:', data)
    sio.emit('join_comp_brainwave_app',data, namespace='/remote_eegapp')

# Solo para test
#sio.sleep(2)

# Solo para test
#sio.disconnect()

# Solo para test
#brain_data = {'Name': ['John', 'Anna', 'Peter'],'Age': [28, 24, 35]}
#sio.emit('join_comp_brainwave_app',brain_data)