import discord
import time , datetime
import asyncio

client = discord.Client() # 필요함
token = " " # 안해도 상관없음


@client.event
async def on_ready(): # 시작할시 콘솔에 나올 동작
    print('')

@client.event
async def on_message(message):
    if message.content.startswith('테스트'): # 테스트 라는 문자를 입력하면 완료! 로 반환
        await message.channel.send('완료!')




client.run(token) # 또는 봇 토큰