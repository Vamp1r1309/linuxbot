from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import message
from aiogram.utils import executor
from selenium import webdriver

import os
import glob



from os import path
from selenium import webdriver

import time



def searchVideo(text):
    download_dir = r'C:\Users\shlik\Desktop\gitTeleBot\telebot\video'
    options = webdriver.ChromeOptions()
    
    preferences = {"download.default_directory": download_dir ,
                   "directory_upgrade": True,
                   "safebrowsing.enabled": True }
    options.add_experimental_option("prefs", preferences)

    browser = webdriver.Chrome(r"C:\Users\shlik\Desktop\gitTeleBot\telebot\chromedriver.exe",options=options)
    browser.get("https://musicaldown.com/en/?ref=more")
    time.sleep(3)

    inputURL = browser.find_element_by_xpath("/html/body/div[2]/div/div/div/form/div/div[1]/input[1]")
    inputURL.clear()
    inputURL.send_keys(text)
    time.sleep(3)

    browser.find_element_by_xpath("/html/body/div[2]/div/div/div/form/div/div[2]/button").click()
    time.sleep(5)
    browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/a[1]").click()
    time.sleep(15)

    browser.close()
    browser.quit()



bot = Bot(token="2028536039:AAFwQiREAbwR61hZaOvQ91ENdImEYSPLENk")
dp = Dispatcher(bot)
send_text_bot = "Отвечу в течение 1 минуты"
@dp.message_handler()
async def videos(message : types.Message):
    text = message.text
    if "https://www.tiktok.com/" in text or "https://vm.tiktok.com/" in text:
        await bot.send_message(message.chat.id, send_text_bot)
        searchVideo(text)

        fil = glob.glob(r"video\*")
        text_video = ''
        for f in range(len(fil)):
            if ".mp4" in fil[f]:
                text_video = fil[f]
        text = text_video.split("\\")
        res = ''
        for i in text:
            if ".mp4" in i:
                res = i
                break
        video = open(f'video\\{res}', "br")
        if res in video.name.split("\\"):
            await bot.send_video(message.chat.id, video)
        else:
            await bot.send_message(message.chat.id, "Такого видео не нашлось")
        video.close()
        files = glob.glob(r"video\*")
        for f in files:
            try:
                os.remove(f)
            except OSError as e:
                print("Ошибка: %s : %s" % (f, e.strerror))
    else:
        await bot.send_message(message.chat.id, "Я ещё не знаю таких команд")


videos(message)

executor.start_polling(dp, skip_updates=True)



