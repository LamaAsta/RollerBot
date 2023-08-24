from discord.ext import commands
import discord

token = "MTEzMzM1NDEyMzI2MjE3NzQwMA.GwXhEa._nCBFbMyqm9SAp6ahPO7wyfFBRSTTOIC8fuhrs"
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
    async def assign(ctx,mention:discord.Member,role:str):

        r = discord.utils.get(ctx.guild.roles, name=role)
        if r:
            if role in roles:
                if r in mention.roles:
                    await mention.add_roles(r)
                    await ctx.send("{} has been given role {} by {} :)".format(mention,r,ctx.author))
                else:
                    await ctx.send("{} Alread has the role >:(".format(mention))
            else:
                await ctx.send("The assignment of that role if beyond my capabilities :(")
        else:
            await ctx.send("Pls give a valid role ")
    
    @roleRequest.command()
    async def remove(ctx,mention:discord.Member, role:str):
        r = discord.utils.get(ctx.guild.roles, name=role)
        if r:
            if role in roles:
                if r in mention.roles:
                    await mention.remove_roles(r)
                    await ctx.send("{} has removed role {} by {} :)".format(mention,r,ctx.author))
                else:
                    await ctx.send("{} doesnt have that role to begin with ".format(mention))
            else:
                await ctx.send("The assignment of that role if beyond my capabilities :(")
        else:
            await ctx.send("Pls give a valid role ")
    bot.run(token)

run()       

