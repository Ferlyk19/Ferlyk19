from userbot.events import register
from time import sleep


@register(outgoing=True, pattern='^.ferly(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Hai Perkenalkan Namaku Ferly Kurniawan`")
    sleep(2)
    await typew.edit("`19 Tahun`")
    sleep(2)
    await typew.edit("`Lahir di kota padang dan besar di kota garut`")
    sleep(2)
    await typew.edit("`Tinggal Di Jakarta Timur`")
    sleep(2)
    await typew.edit("`Tepatnya di kampung dukuh, Salam Kenal:)`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.sayang(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Cuma Mau Bilang`")
    sleep(3)
    await typew.edit("`Aku Sayang Kamu`")
    sleep(1)
    await typew.edit("`I LOVE YOU 💞`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Apapun Yang Terjadi`")
    sleep(3)
    await typew.edit("`Tetaplah Bernapas`")
    sleep(1)
    await typew.edit("`Dan Selalu Bersyukur`")
# Create by myself @localheart
