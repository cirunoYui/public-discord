# 역할에 따라 실행 결과 바꾸기 

role_name = "" # 역할 아이디가 아닌 역할 이름(문자열)로 적어주세요.

role_check = discord.utils.get(message.guild.roles, name=role_name)
if message.content.startswith("=test"):
    if role_check in message.author.roles:
        try:
            pass # 역할이 있을때의 실행결과
        except ValueError: # 예외 처리
            pass
    else: # 역할이 없을경우의 실행결과 / else문은 없어도 됩니다. 
        pass