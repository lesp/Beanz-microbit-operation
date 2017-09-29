from microbit import *
import speech
lives = 3
while True:
    display.scroll("You have "+str(lives)+" lives")
    speech.say("You have "+str(lives)+" lives to operate on the patient. Good luck")
    while lives > 0:
        if pin2.read_digital() == 1:
            display.show(Image.ANGRY)
            pin1.write_digital(1)
            speech.say("Ouch!")
            sleep(200)
            lives = lives -1
            speech.say("You have "+str(lives)+" lives left.")
            pin1.write_digital(0)
            pin2.write_digital(0)
        else:
            display.show(Image.HAPPY)
    speech.say("GAME OVER")
    lives = 3