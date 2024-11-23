from flask import Flask, render_template, request
import RPi.GPIO as GPIO
import time                         

#上部分为程序的第一部分，引入了Flask库用于创建网页程序、引入GPIO库用于实现对GPIO引脚的控制

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)        #设定具体输出命令的GPIO引脚（本例中为GPIO-18引脚）

pwm = GPIO.PWM(18, 50)
pwm.start(0)

#本部分为对GPIO引脚的设置与初始化（设定特定频率控制舵机旋转90度）
#我应用的舵机是MG995型号，具体使用方法请到CSDN自行查找

@app.route('/')
def index():
    return render_template('index.html')        #绑定指定的HTML文件，获取用户的输入值


@app.route('/control_servo', methods=['POST'])
def control_servo():
    try:
        pwm.ChangeDutyCycle(7.5)
        time.sleep(1)
        pwm.ChangeDutyCycle(2.5)
        time.sleep(1)
        pwm.ChangeDutyCycle(0)
        return "舵机控制成功"
    except Exception as e:
        return f"舵机控制失败: {str(e)}"
    
#本部分通过获取从HTML输入值，控制舵机的偏转（按下按钮后先顺时针偏转90度，再逆时针偏转90度复位）


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

#设置广播的IP地址为0.0.0.0:8080的元音：我不知道该广播到哪个IP，于是就把所有网络接口分配给树莓派的IP的8080端口全给监听上了


def cleanup():
    pwm.stop()
    GPIO.cleanup()

atexit.register(cleanup)

#完成一次完整的控制流程后，终止对GPIO的调用，使接下来的用户仍然能通过控制该GPIO接口实现对舵机的控制