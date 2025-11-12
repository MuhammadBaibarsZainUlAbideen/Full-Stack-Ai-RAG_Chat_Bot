import base64

async def image_Extratction(Uploaded_Image):
    image_Bytes = await Uploaded_Image.read()
    image_Bytes64 = base64.b64encode(image_Bytes).decode("utf-8")
    return image_Bytes64