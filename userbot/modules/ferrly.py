from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.goblok(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Pertama-tama kamu norak`")
    sleep(2)
    await typew.edit("`Kedua kamu dongo`")
    sleep(1)
    await typew.edit("`Dan yang terakhir kamu goblok anjing`")

@register(outgoing=True, pattern='^.hallo(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`iya hallo juga kamu`")
    sleep(2)
    await typew.edit("`iya kamu`")
    sleep(1)
    await typew.edit("`kamu bukan jodohku 😢`")

@register(outgoing=True, pattern='^.ngelek(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`ini otakmu`")
    sleep(2)
    await typew.edit("`🧠`")
    sleep(1)
    await typew.edit("`Lola anjing kudu di service`")

@register(outgoing=True, pattern='^.nyanyi(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(4)
    await typew.edit("`gas nyanyi kuy...`")
    sleep(3)
    await typew.edit("`lihat kebunku`")
    sleep(2)
    await typew.edit("`penuh dengan bunga`")
    sleep(2)
    await typew.edit("`ada yang merah dan ada yang putih`")
    sleep(2)
    await typew.edit("`setiap hari ku siram semua`")
    sleep(2)
    await typew.edit("`mawar melati semua nya....`")
    sleep(2)
    await typew.edit("`indaahhhhhhhhh`")
    sleep(1)
    await typew.edit("`horeee kamu pintar 👏👏`")
