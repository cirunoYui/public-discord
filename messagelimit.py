if message.content.startswith(message.content): # 모든 메시지를 감지
    msglimit = 100 # 최대 메시지 수
    send_msg = len(message.content) # 보낸 메시지의 글자수를 읽음
    send_msg = int(send_msg) # 보낸 메시지의 글자수를 정수형으로 변환   
    if send_msg > msglimit:
        if message.author.guild_permissions.administrator:
            try:
                pass

            except ValueError:
                pass
        else:
            await message.delete()
            print(f"{author} 님! {send_msg} 개의 메시지를 한번에 보내는 것은 불가능합니다!")