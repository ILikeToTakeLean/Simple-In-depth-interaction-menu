import discord # py -3 -m pip install -U discord.py
import discord_components import * # pip install --upgrade discord-components

bot = ComponentsBot("!", case_insensitive=True) # Define your prefix, here the prefix is "!" 
# "case_insensitive=True" is not needed, but basically it makes you use every command no matter where you use capitalized/small letters.

bot.remove_command("help") # Remove the already existing help command, and define your own one.

token = "bot-token-here" # Define your token in a variable, you will call this at the end of the code to run the bot.

@bot.event 
async def on_ready(): 
    print("Bot is ready.")
    DiscordComponents(bot) # Define an event which get's called when the bot is booted.

@bot.command(invoke_without_command=True) # Define a bot command.
async def help(ctx):
    await selectboxtesting(ctx) # Call the hyperfunction, which will be defining now.

async def selectboxtesting(ctx): # Creating the hyperfunction.
    embed = discord.Embed(
        title="Help panel!",
        description="Input some of your stuff in here.",
        color=0x71368a) # Creating an embed
        await ctx.reply(embed=embed,         components=[
            Select(
                placeholder="Select something",
                options=[
                    SelectOption(
                        label="Test",
                        value="1",
                        description="Testing the description!")
                ],
                custom_id="selectboxtesting") # Custom id which gets called later
        ])
    while True:
      try:
        interaction1 = await bot.wait_for("select_option",check=lambda inter: inter.custom_id == "selectboxtesting" and inter.user == ctx.author) # Bot is waiting for the author to use the select option drop menu, and also it checks the user so only the message author can use this.
        res = interaction1.values[0]
        if res == "1": # Check the value (which interaction got selected)
          await interaction1.send("You used your first interaction menu! Congrats!")# Replying to the user who called this function, and sending the interaction menu with it

bot.run(token) # Run the bots token.


# For any questions contact down bad#8487 on discord.