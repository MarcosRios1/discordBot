import discord
import asyncio
import datetime

messages = joined = 0
token = 'NzMyMDYzOTUxODY0NDYzNDcx.XwvLaA.noum0f8BbH9nTqi-qORrokZ_CZI' # Not worried about sharing this key, this bot will only be
                                                                      # used for testing purposes

def start():
    inp = input('Welcome! Press any key to start hosting your bot, or q to quit.')
    if inp == 'q':
        exit()
    else:
        run_bot()

def run_bot():
    try:
        client = discord.Client()
        print('Running bot... Press Ctrl-C to stop hosting.')

        #### Logging function, still needs work to be as efficient as possible ####
        # async def update_stats():
        #     await client.wait_until_ready()
        #     global messages, joined
        #
        #     while not client.is_closed():
        #         try:
        #             with open('stats.txt', 'a') as f:
        #                 f.write(f'Time: {str(datetime.datetime.now())}, Messages: {messages}, Members Joined: {joined} \n')
        #             messages = 0
        #             joined = 0
        #
        #             await asyncio.sleep(10)
        #         except Exception as e:
        #             print(e)
        #             await asyncio.sleep(10)

        @client.event
        async def on_member_join(member):
            global joined
            joined += 1

            for channel in member.server.channels:
                if str(channel) == 'general':
                    await client.send_message(f'''```Welcome to the server! {member.mention}```''')

        @client.event
        async def on_message(message):
            global messages
            messages += 1

            id = client.get_guild(732063599966814288)
            valid_channels = ['bot-commands']
            admins = ['blackhollow#3947']

            if str(message.channel) in valid_channels:
                if message.content.find('!commands') != -1:
                    await message.channel.send('''```Here\'s a list of my commands:
!hello
!lige
!users```''')
                elif message.content == '!hello':
                    await message.channel.send('Hi!')
                elif message.content == '!users':
                    await message.channel.send(f'''```# of Members: {id.member_count}```''')
                elif message.content == '!lige':
                    await message.channel.send('Don\'t speak that bums name in my channel.')
                elif message.content == '!admin':
                    if str(message.author) in admins:
                        await message.channel.send('```Admin Panel```')
                    else:
                        print(f'User: {message.author} tried using the admin command \'{message.content}\'')

        client.run(token)
    except:
        print('Something went wrong with your bot! Try checking the token.')

start()
