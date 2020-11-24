# // 권한에 따라 실행이 달라지는 결과

if message.content.startswith('=권한'):
    if message.author.guild_permissions.administrator: # administrator , manage_messages . . 등등 여러가지 권한.
        try:
            pass


        except ValueError:
            pass

    else:
        await message.channel.send('실행 결과')


# // =권한을 입력 받음 > 메시지를 보낸 사람의 권한에 administraotr(관리자) 가 있는지 확인 > 있으면 pass 를 사용하여 아무 일도 안일어나게 만듬 > 권한이 없다면 else 문을 실행.
