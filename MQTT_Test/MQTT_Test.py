#!/usr/bin/python3
import paho.mqtt.client as mqtt
import pymysql as MYSQL
import time

db=MYSQL.connect(host="192.168.0.104",user="MQTT_Master",passwd="mqtt",db="message_board",port=3306,unix_socket="/var/run/mysqld/mysqld.sock")
cursor=db.cursor()
cursor.execute("SELECT VERSION()")
data=cursor.fetchone()
print("Current database version : %s" %data)


broker="192.168.0.110"

# MariaDB definitions start

def MySQL_List_Sources():
    sql ="SHOW DATABASES;"
    cursor.execute(sql)
    dbs=cursor.fetchall()
    for row in dbs:
        print("Listed Databases are : %s" %row[0])

# MariaDB definitions end

# MQTT Callbacks start
def on_log(client, userdata, level, buf):
    print("Log: "+buf)

def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("Connection successful:",rc)
    elif rc==1:
        print("Connection refused - incorrect protocol version:", rc)
    elif rc==2:
        print("Connection refused - invalid client identifier:",rc)
    elif rc==3:
        print("Connection refused - server unavailable:",rc)
    elif rc==4:
        print("Connection refused - bad username or password:",rc)
    elif rc==5:
        print("Connection refused - not authorised:",rc)
    else:
        print("Unknown error occured while connecting to broker:", rc)

def on_disconnect(client, userdata, flags, rc=0):
    if rc==0:
        print("Disconnectd from broker "+str(rc))
    else:
        print("Unexpected disconnection error has occured"+str(rc))

#def on_message(client, userdata, message):
#    print("Message received: '"+str(message.payload)+ "' on topic '" +str(message.topic)+ "' with QoS " +str(message.qos))

def on_publish(client, userdata, mid):
    print("Message has been sent", mid)

def on_subscribe(client, userdata, mid, granted_qos):
    print("Client has been subscribed to topic with QoS" +str(granted_qos),mid)

def on_unsubscribe(client, userdata, mid):
    print("Client has unsubscribed from topic", mid)

def on_message(client, userdata, msg):
    topic=msg.topic
    m_decode=str(msg.payload.decode("utf-8"))
    print("Message received: ",m_decode)

# MQTT Callbacks end


client = mqtt.Client("PyCharm")
client.on_connect=on_connect
client.on_disconnect=on_disconnect
#client.on_log=on_log
print("Connecting to broker ", broker)

client.connect(broker)
client.loop_start()

client.subscribe("Testing/MQTT/messages")
client.on_subscribe=on_subscribe
client.publish("Testing/MQTT/messages","[Let us send a tuple]")
client.on_publish=on_publish
client.on_message=on_message
client.unsubscribe("Test/MQTT/messages")
client.on_unsubscribe=on_unsubscribe

time.sleep(4)
MySQL_List_Sources()

client.loop_stop()
client.disconnect()
db.close()