import socketio

sio = socketio.Client()

@sio.on('connect')
def on_connect():
    print ('connected to server 4000')

@sio.on('disconnect')
def on_disconnect():
    print('diconnected from server 4000')

sio.connect('http://localhost:4000',namespaces=['/remote'])

def send_brainwaves(data):
    #brain_data = data
    #print('Sending:', data)
    sio.emit('join_comp_brainwave_app',data, namespace='/remote')

# Solo para test
#sio.sleep(2)

# Solo para test
#sio.disconnect()

# Solo para test
#brain_data = {'Name': ['John', 'Anna', 'Peter'],'Age': [28, 24, 35]}
#sio.emit('join_comp_brainwave_app',brain_data)

#values = main.values
#print('VALORES',values)
#def sendValue(values):
#    brain_data = values
#    sio.emit('brain_data',brain_data)
