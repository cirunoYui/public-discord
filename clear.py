if message.content.startswith('=청소'):
    msgclear = message.content[3:] # =청소의 "소" 다음 글자를 읽음
    msgclear = int(msgclear) # 위에 읽은 것을 int(정수형) 으로변환
    msgclear = msgclear + 1 # 정수형으로 변환된 것에 1을 더함
    if message.author.guild_permissions.administrator:  # 역할 권한이 어드민 권한이 있으면 반응
        try:
            await message.channel.purge(limit=msgclear) # msgpurge 만큼 메시지를 청소
            await message.channel.send(f"{msgclear - 1} 개의 메시지를 삭제했습니다.") # 위에서 1을 더해줫지만 표시할때에는 1은 뺀 값을 표시
        except ValueError:
            await message.channel.send('숫자가 아닙니다.') # msgclear 변수에 정수형이 아닌 문자열이 들어왔을때 에러 표시
    else:
        await message.channel.send('권한이 없습니다.') #권한이 없음