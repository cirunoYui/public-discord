token = ""
client = discord.Client()
m_aTime = 1
m_s_Time = 2
m_thTIme = 3
m_aTime = int(m_aTime)
m_s_Time = int(m_s_Time)
m_thTIme = int(m_thTIme)

@client.event
async def on_ready():
    print(f"start at: {datetime.datetime.today}")

@client.event
async def on_message(message):
    if message.content.startswith(값):
            초기 표시 결과
            await message.channel.send('',embed=embed)

        def checkReq(m):
            return m.author == message.author and m.channel == message.channel
        try:
            m = await client.wait_for("message", timeout=10, check=checkReq)
        except:
            await message.channel.send() #10초 동안 아무반응이 없다면 실행됨
        if m.content == "":
            실행코드
        else:
            그 의외 처리 코드

client.run(token)