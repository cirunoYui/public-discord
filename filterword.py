if message.content.startswith(message.content): # 모든 메시지를 감지 합니다
    if message.content in your_list: # 메시지에 your_list 에 포함된 메시지가 있으면 
        await message.delete # 지웁니다

