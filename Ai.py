from fastapi import FastAPI,UploadFile,File,Form,Response, Cookie, Request
from pydantic import BaseModel
from openai import OpenAI
from DataBase import get_conversation,save_message,init_db_chat,init_db_iamge,save_iamge,user_id,save_user_id,deleting,init_db_pay,get_pay,mpay
from file import extracting_pdf_file
from Image import image_Extratction
import traceback
from fastapi.middleware.cors import CORSMiddleware
import uuid
from dotenv import load_dotenv
import os
from retrival_from_DB import retrieve
import time

init_db_chat()
init_db_pay()
init_db_iamge()
user_id()
load_dotenv()



app = FastAPI()

openai = os.getenv("OPENAI_API_KEY")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:7080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/paywall")
async def chat(id:str = Form(...)):
    try:
        print(id)
        print("y")
        reply = {"paywall": 0}
        print("yy")
        calling = get_pay(id)
        print("yyy")
        if len(calling) >=100 and calling[len(calling)-1]["paid"] == 0 :
            print("yyyy")
            reply = {"paywall":1}
        
        mpay(id)
        print('yyyyy')
    except:
        reply = {"paywall": 0}
        print("Whattttttttt")
    print(reply)


    return reply






@app.post("/chat")
async def chat(request: Request,response: Response,message : str = Form(...),session_id:str|None=Cookie(default=None)):
    print(request.cookies)

    if not session_id:
        session_id = str(uuid.uuid4())
        response.set_cookie(key="session_id",value=session_id,httponly=True)
    deleting(session_id)


    history = get_conversation(session_id)
    getting_data = retrieve(message)
    turing_to_str = ''.join(str(getting_data))
    print(turing_to_str)
    history.append({"role": "user", "content": message+turing_to_str})
    response1 = openai.chat.completions.create(

        model="gpt-4o-mini",
        messages=history,
        max_tokens=150,
        temperature=0.7
    )
    reply = response1.choices[0].message.content
    save_user_id(session_id)
    save_message(session_id,"user",message)
    save_message(session_id, "assistant", reply)
    return {"reply":reply}

# @app.post("/uploadfile")
# async def upload_file(response: Response,uploaded_file: UploadFile = File(...),session_id:str|None=Cookie(default=None)):
#     if not session_id:
#         session_id = str(uuid.uuid4())
#         response.set_cookie(key="session_id",value=session_id,httponly=True)
#     name_of_file = uploaded_file.filename
#     if name_of_file.endswith(".txt"):
#        content = await uploaded_file.read()
#        file_text = content.decode("utf-8", errors="ignore")

#        history = get_conversation(session_id)
#        history.append({"role": "user", "content": file_text})

#        response = openai.chat.completions.create(
#            model="gpt-4o-mini",
#            messages=history,
#            max_tokens=500,
#            temperature=0.7
#        )
#        reply = response.choices[0].message.content
#        save_user_id(session_id)

#        save_message(session_id, "user", f"[Uploaded file: {uploaded_file.filename}]\n{file_text[:500]}...")
#        save_message(session_id, "assistant", reply)

#        return {"reply": reply}
#     if name_of_file.endswith(".pdf"):
#         content = await extracting_pdf_file(uploaded_file)
#         history = get_conversation(session_id)
#         history.append({"role": "user", "content": content})

#         response = openai.chat.completions.create(
#            model="gpt-4o-mini",
#            messages=history,
#            max_tokens=500,
#            temperature=0.7
#         )
#         reply = response.choices[0].message.content
#         save_user_id(session_id)

#         save_message(session_id, "user", f"[Uploaded file: {uploaded_file.filename}]\n{content[:500]}...")
#         save_message(session_id, "assistant", reply)

#         return {"reply": reply}
# @app.post("/uploadimage")
# async def image(request: Request,response: Response, uploaded_image: UploadFile = File(...),session_id:str|None=Cookie(default=None)):
#     if not session_id:
#         session_id = str(uuid.uuid4())
#         response.set_cookie(key="session_id",value=session_id,httponly=True)
#     try:
#         name_of_file = uploaded_image.filename 
#         if name_of_file.endswith(".jpg")  or name_of_file.endswith(".png") or name_of_file.endswith(".gif") or name_of_file.endswith(".jpeg") or name_of_file.endswith(".webp"):
#             base_64 = await image_Extratction(uploaded_image)
#         history = get_conversation(session_id)
#         history.append({"role":"user","content":[{
#             "type":"text",
#             "text":"Describe this Picture"
#         },
#         {
#             "type":"image_url",
#             "image_url":{
#                 "url":f"data:image/jpeg;base64,{base_64}"
#             }
#         }]
#                         })
#     except Exception as e:
#         return {"error": str(e)}
#     response = openai.chat.completions.create(
#            model="gpt-4o-mini",
#            messages=history,
#            max_tokens=300,
#            temperature=0.7
#     )
#     reply = response.choices[0].message.content
#     save_user_id(session_id)
#     save_iamge(session_id, "user", base_64)
#     save_iamge(session_id, "assistant", reply)
        


#     return {"reply": reply}

    


