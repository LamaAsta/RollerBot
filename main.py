from discord.ext import commands
import discord

token = "MTEzMzM1NDEyMzI2MjE3NzQwMA.GTTUnr.IQNZt_0VEmBTwwZxS6hHwKNpHP1SHzJMXirkCQ"
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='&',intents=intents)
#has_any_role will come in handy
#has_role
roles = ['HonoredGuests']
def run():
    @bot.group()
    async def roleRequest(ctx):
        if not ctx.invoked_subcommand:
            await ctx.send("Please give a command")
    @roleRequest.command()

    async def assign(ctx,mention:discord.Member,role:discord.Role):
        print(role+' niga')
        r = discord.utils.get(ctx.guild.roles, name=role)
        if r:
            if role in roles:
                await mention.add_roles(role.id)
                await ctx.send("{} has been given role {} by {} :)".format(mention,role,ctx.author))
            else:
                await ctx.send("The assignment of that role if beyond my capabilities :(")
        else:
            await ctx.send("Pls give a valid role ")
    
    bot.run(token)

run()       

# @bot.command()
# async def assign_role(ctx, member: discord.Member, role_name: str):
#     role = discord.utils.get(ctx.guild.roles, name=role_name)
#     if role:
#         await member.add_roles(role)
#         await ctx.send(f"Assigned {role.name} role to {member.display_name}")
#     else:
#         await ctx.send("Role not found.")