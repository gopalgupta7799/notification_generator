import datetime
from time import time, sleep
from winsound import PlaySound, SND_FILENAME, SND_LOOP, SND_ASYNC
import plyer


def doEyeExercise():
    PlaySound("Sounds/Alarm08.wav", SND_FILENAME | SND_LOOP | SND_ASYNC)
    plyer.notification.notify(
        title="Eye Exercise Break",
        message="Eye exercise must be done every 30 minutes by a software engineer",
        app_icon="Icons/eye_exercise_icon.ico"
    )
    sleep(20)
    PlaySound(None, SND_FILENAME)
    global eyeExerciseTime
    eyeExerciseTime = time()
    with open("Timings/eyeExerciseTimings.txt", 'a+') as f:
        f.write(f'Eye Exercise Done at: {str(datetime.datetime.now())}\n')


def drinkWater():
    PlaySound("Sounds/Alarm06.wav", SND_FILENAME | SND_LOOP | SND_ASYNC)
    plyer.notification.notify(
        title="Drink Water",
        message="A person should drink 3.5 L water everyday",
        app_icon="Icons/drink_water_icon.ico"
    )
    sleep(20)
    PlaySound(None, SND_FILENAME)
    global waterTime
    waterTime = time()
    with open("Timings/waterTimings.txt", 'a+') as f:
        f.write(f'Water drank at: {str(datetime.datetime.now())}\n')


def doPhysicalExercise():
    PlaySound("Sounds/Alarm07.wav", SND_FILENAME | SND_LOOP | SND_ASYNC)
    plyer.notification.notify(
        title="Physical Exercise Break",
        message="Physical exercise keeps your body fit and healthy",
        app_icon="Icons/physical_exercise_icon.ico"
    )
    sleep(20)
    PlaySound(None, SND_FILENAME)
    global physicalExerciseTime
    physicalExerciseTime = time()
    with open("TImings/physicalExerciseTimings.txt", 'a+') as f:
        f.write(f'Physical exercise Done at: {str(datetime.datetime.now())}\n')


startTime = datetime.time(0, 0, 0)
endTime = datetime.time(23, 59, 59)
eyeExerciseInterval = 3600  # 1 Hour
drinkWaterInterval = 7200  # 2 Hours
physicalExerciseInterval = 2.5*3600  # 2.5 Hours

waterTime = eyeExerciseTime = physicalExerciseTime = time()

while True:
    curr = time()
    if startTime <= datetime.datetime.now().time() <= endTime:
        if curr - eyeExerciseTime > eyeExerciseInterval:
            doEyeExercise()
        if curr - waterTime > drinkWaterInterval:
            drinkWater()
        if curr - physicalExerciseTime > physicalExerciseInterval:
            doPhysicalExercise()
    # elif datetime.datetime.now().time() >= endTime:
    #     break
