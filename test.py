import platform,socket,re,uuid,json,psutil,logging
import streamlit as st
import time
import requests
#import torch
def getSystemInfo():
    try:
        info={}
        info['platform']=platform.system()
        info['platform-release']=platform.release()
        info['platform-version']=platform.version()
        info['architecture']=platform.machine()
        info['hostname']=socket.gethostname()
        info['ip-address']=socket.gethostbyname(socket.gethostname())
        info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['processor']=platform.processor()
        info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        #info['gpu']=str(torch.cuda.get_device_properties(0))
        return json.dumps(info)
    except Exception as e:
        logging.exception(e)

a = json.loads(getSystemInfo())
st.title('DEMO')
st.write(str(a))
import speedtest
speed_test = speedtest.Speedtest()
download_speed = speed_test.download()
upload_speed = speed_test.upload()
t = time.time()
requests.get("https://speedtest-ams.turnkeyinternet.net/100mb.bin")
st.write(str(time.time() - t))
