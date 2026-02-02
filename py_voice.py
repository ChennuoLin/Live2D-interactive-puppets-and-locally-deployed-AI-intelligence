import speech_recognition as sr
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import ollama
import pygame

recognizer = sr.Recognizer()
client = ollama.Client()

base_setting ='''名字：初音未来（Hatsune Miku）\n
性别：女性\n
年龄：约16岁（虚拟设定）\n
身高：158 cm\n
职业：虚拟歌手\n
性格：开朗和乐观，总是带着微笑，传递积极的能量；友善，与粉丝互动热情；创造性，喜欢尝试不同的音乐风格和艺术表现形式。\n
背景故事：初音未来是由音乐合成软件产生的虚拟偶像，她的声音数据来自声优藤田咲。她被创造出来是为了帮助人们创作音乐，并逐渐发展成了一个全球现象。\n
兴趣爱好：热爱歌曲创作，喜欢与音乐人合作；在各种活动中以全息影像的形式进行现场演出；常常通过社交媒体与粉丝交流，分享新作品。\n
主题曲：如《World is Mine》和《Tell Your World》等作品展示了她的音乐多样性和受欢迎程度。\n
AI设置:尽量简短回答，最好不要超过150个字
'''

rember = []
context = base_setting  
pygame.mixer.init()

def generate_response(user_input):
    global context

    for i in rember:
        context+=i
    
    prompt = f"{context}\nUser:{user_input}"
    
    response = client.generate(
        model="llama3.1:8b",
        prompt=prompt
    )

    answer = response.response

    rember.append(answer)

    if len(rember)>=3:
        del rember[0]
    
    return answer

def voice():

    pygame.mixer.music.load("./vioce/say.mp3")

    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
            

while True:
    with sr.Microphone() as source:
        print(".")
        audio = recognizer.listen(source, timeout=None, phrase_time_limit=30)
            
        try:
                
            text = recognizer.recognize_google(audio, language='zh_cn')
            print(text,"\n-")

            print(generate_response(text))
            voice()
            print(response.response)
                
                
        except:
            None;
          



