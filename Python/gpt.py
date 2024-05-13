import asyncio

from freeGPT import Client
from fuzzywuzzy import fuzz

from vtubecontrol import StartVtube
from vtubecontrol import MouthSmile

smileper = 0

async def StartMainEmul():
    await StartVtube()

    while True:
        prompt = input("👦: ")
        resp1 = Client.create_completion("gpt3", "Write what emotion you need to portray from: Nothing, smile, sadness, squinting my eyes, surprise, you need to write as strictly as possible, example: smile, with a small letter and without unnecessary letters and words. Write just one thing" + prompt)
        # print(f"🤖: {resp}")
        resp = "Smile!"
        
        nothing = fuzz.WRatio("Nothing", resp)
        smile = fuzz.WRatio("smile", resp)
        squintingeyes = fuzz.WRatio("squinting my eyes", resp)
        surprise = fuzz.WRatio("surprise", resp)

        if nothing == 100:
            result = "nothing"
        elif smile == 100:
            result = "smile"
        elif squintingeyes == 100:
            result = "squintingeyes"
        elif surprise == 100:
            result = "surprise"
        else:
            result = "nothing"

        if result == "smile":
            smileresp = Client.create_completion("gpt3", "Enter a number from -1 to 1, this will indicate the expression of your smile, -1 is sadness, 0.5 is an average facial expression, 1 is a strong smile, you only need to enter a number without further words, etc., words that your interlocutor said to you: " + prompt)
            try:
                await MouthSmile(float(smileresp))
                smileper = smileresp
                await per()
            except Exception as a:
                print(a)
            print("🤖: " + smileresp)
        # if result == "smile":
        #     smileresp = Client.create_completion("gpt3", "Enter a number from -30 to 30, this will indicate the expression of your smile, -30 is sadness, 0 is an average facial expression, 30 is a strong smile, you only need to enter a number without further words, etc., words that your interlocutor said to you: " + prompt)
        #     print("🤖: " + smileresp)

async def per():
    while True:
        await MouthSmile(float(smileper))
        await asyncio.sleep(0.6)


async def main():
    task1 = asyncio.create_task(StartMainEmul())
    task2 = asyncio.create_task(per())

    await task1
    await task2
asyncio.run(main())