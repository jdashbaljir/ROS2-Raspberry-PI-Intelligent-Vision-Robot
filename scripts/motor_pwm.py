import RPi.GPIO as GPIO
import time


right_motor_a = 20
right_motor_b = 16
right_motor_en = 21
#right_motor_a = 24
#right_motor_b = 23
#right_motor_en = 25
left_motor_a = 22
left_motor_b = 27
left_motor_en = 17
#left_motor_a = 15
#left_motor_b = 14
#left_motor_en = 4
GPIO.setmode(GPIO.BCM)

GPIO.setup(right_motor_a , GPIO.OUT)
GPIO.setup(right_motor_b , GPIO.OUT)
GPIO.setup(right_motor_en , GPIO.OUT)

GPIO.setup(left_motor_a , GPIO.OUT)
GPIO.setup(left_motor_b , GPIO.OUT)
GPIO.setup(left_motor_en , GPIO.OUT)

pwm_r = GPIO.PWM(right_motor_en , 1000 )
pwm_l = GPIO.PWM(left_motor_en , 1000 )

pwm_r.start(40)
pwm_l.start(40)

def forward(second):
    print("forward Moving ")
    GPIO.output(right_motor_a,GPIO.HIGH)
    GPIO.output(right_motor_b,GPIO.LOW)
    GPIO.output(left_motor_a,GPIO.HIGH)
    GPIO.output(left_motor_b,GPIO.LOW)
    time.sleep(second)

def reverse(second):
    print("Reverse Moving ")
    GPIO.output(right_motor_a,GPIO.LOW)
    GPIO.output(right_motor_b,GPIO.HIGH)
    GPIO.output(left_motor_a,GPIO.LOW)
    GPIO.output(left_motor_b,GPIO.HIGH)
    time.sleep(second)


def right(second):
    print("Right Moving ")
    GPIO.output(right_motor_a,GPIO.LOW)
    GPIO.output(right_motor_b,GPIO.HIGH)
    GPIO.output(left_motor_a,GPIO.HIGH)
    GPIO.output(left_motor_b,GPIO.LOW)
    time.sleep(second)

def left(second):
    print("left Moving ")
    GPIO.output(right_motor_a,GPIO.HIGH)
    GPIO.output(right_motor_b,GPIO.LOW)
    GPIO.output(left_motor_a,GPIO.LOW)
    GPIO.output(left_motor_b,GPIO.HIGH)
    time.sleep(second)

def stop():
    print("Stopping Motors")
    pwm_r.ChangeDutyCycle(0)
    pwm_l.ChangeDutyCycle(0)

def exit_():
    GPIO.cleanup()


def on(second):
    print("Right Moving ")
    GPIO.output(right_motor_a,GPIO.HIGH)
    GPIO.output(right_motor_b,GPIO.HIGH)
    GPIO.output(left_motor_a,GPIO.HIGH)
    GPIO.output(left_motor_b,GPIO.HIGH)
    time.sleep(second)

def test(second):
    GPIO.output(right_motor_a,GPIO.HIGH)
    GPIO.output(right_motor_b,GPIO.LOW)
    GPIO.output(left_motor_a,GPIO.LOW)
    GPIO.output(left_motor_b,GPIO.LOW)
    time.sleep(second)
    GPIO.output(right_motor_a,GPIO.LOW)
    GPIO.output(right_motor_b,GPIO.HIGH)
    time.sleep(second)


def main():
    
    #on(2)
    #test(4)
    forward(5)
    reverse(5)
    left(4)
    right(4)
    #right_motor_a = 16
    #right_motor_b = 20
    #right_motor_en = 21
    stop()
    exit_()


if __name__ == '__main__':
    main()

