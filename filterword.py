your_list = ['나쁜말1','나쁜말2']

if message.content.startswith(message.content):
    if message.content in your_list:
        await message.delete()

# 필터링 할 말을 리스트에 지정해준 뒤, 4번째 라인  if message.content in your_list: 을 통해 메시지에 나쁜말 리스트중 하나가 포함되면 메시지를 지우는 원리