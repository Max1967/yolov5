import platform,socket,re,uuid,json,psutil,logging
import streamlit as st
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
#download_speed = speed_test.download()
#upload_speed = speed_test.upload()
for i in range(10):
    download_speed = speed_test.download()
    upload_speed = speed_test.upload()
    st.write(str(download_speed/1024/1024))
    st.write(str(upload_speed/1024/1024))
