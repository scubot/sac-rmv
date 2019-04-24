import discord
from discord.ext import commands


class SACRMV(commands.Cog):
    def __init__(self, bot):
        self.version = "2.0.0"
        self.bot = bot

    @commands.command()
    async def air(self, ctx, start_pressure: int, end_pressure: int, bottom_time: int, average_depth: int, tank_sp: int,
                  tank_capacity: int):
        pressure = (average_depth * 0.099376) + 1
        bars_consumed = end_pressure - start_pressure

        sac = bars_consumed / bottom_time / pressure
        rmv = (tank_capacity / tank_sp) * sac

        embed = discord.Embed(title="SAC/RMV Calculation")
        embed.add_field(name="Surface Air Consumption", value="{:0.2f}".format(sac))
        embed.add_field(name="Respiratory Mean Volume", value="{:0.2f}".format(rmv))
        await ctx.send(embed=embed)