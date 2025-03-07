from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# السماح بالاتصال من أي مصدر (Telegram WebApp)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/calculate")
async def calculate_grade(request: Request):
    data = await request.json()
    print("📥 Received data:", data)  # طباعة البيانات التي تصل إلى السيرفر
    
    if not data:
        return {"message": "❌ لم يتم إرسال بيانات صحيحة!"}

    year1 = data.get("year1", 0)
    year2 = data.get("year2", 0)
    year3 = data.get("year3", 0)
    semester1 = data.get("semester1", 0)
    target = data.get("target")

    required_semester2 = (target - (year1 * 0.2) - (year2 * 0.2) - (year3 * 0.2) - (semester1 * 0.2)) / 0.2
    required_semester2 = round(required_semester2, 2)

    if required_semester2 < 0:
        return {"message": "✅ أنت بالفعل حققت المعدل المطلوب!"}
    elif required_semester2 > 100:
        return {"message": "❌ من المستحيل تحقيق هذا التقدير!"}
    else:
        return {"message": f"🔢 تحتاج إلى {required_semester2}% في الترم الثاني من السنة الرابعة"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
