from Music.utils.youtube import ytube
video_id = "rCC70UbMuFY"


async def dwn(id):
    file_path = await ytube.download(id, True, False)
    return file_path

dwn(video_id)