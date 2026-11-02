"""Creates data.csv: a SMALL SYNTHETIC seed dataset (English, Bangla, Banglish)
used only to test the training pipeline. Replace/extend data.csv with real,
consented, anonymised messages for real evaluation."""
import csv, random
random.seed(7)

def pick(l): return random.choice(l)

# ---------- SCAM ----------
brands_en = ["bKash","Nagad","Rocket","DBBL","BRAC Bank","Sonali Bank","Grameenphone","Robi","Banglalink","Daraz","Pathao","Facebook","PayPal","Amazon","DHL","Apple"]
links = ["http://{b}-verify.xyz/login","bit.ly/{r}","http://{b}-secure.top/pay","tinyurl.com/{r}","http://192.168.4.{n}/{b}","https://{b}-update.click/kyc","cutt.ly/{r}","http://{b}care.online/home"]
def link(b):
    return pick(links).format(b=b.lower().replace(" ",""), r=pick(["win24","bd-pay","claim1","offer77","kyc99"]), n=random.randint(2,250))

scam_en = [
 "Dear customer, your {b} account will be blocked within 24 hours. Click {l} and enter your PIN to verify.",
 "URGENT: unusual activity detected on your {b} account. Verify your OTP immediately at {l}",
 "Congratulations! You have won a prize of $5000. To claim your prize pay a processing fee: {l}",
 "Your {b} account is suspended. Update your KYC now or it will be closed: {l}",
 "Your parcel could not be delivered. Pay a small delivery fee at {l} or it will be returned.",
 "Work from home part-time job! Earn $300 daily, no experience needed. Pay a registration fee to start. WhatsApp us.",
 "Send your verification code now to keep your {b} account active. Do not share with anyone else.",
 "You are the lucky winner of our lottery. Send gift cards worth $100 to receive your money. {l}",
 "Security alert: suspicious login on your {b} account. Confirm your password here {l}",
 "Final notice: unpaid fine. Legal action and arrest warrant will follow unless you pay today. {l}",
 "Refund pending! You were overpaid, click here to receive your cashback: {l}",
 "Earn money fast online, make $500 per day. Send an advance fee via bitcoin to join. Call now.",
 "Dear user, your {b} wallet is locked. Re-activate within 2 hours: {l} enter PIN and OTP.",
 "I sent you money by mistake. Please send it back to this number urgently, I will pay a bonus.",
 "Your tax refund is ready. Confirm your bank details and pay a small release fee: {l}",
 "Limited offer! Free gift for {b} customers. Tap the link and enter your card CVV to claim: {l}",
 "Your {b} KYC has expired. Verify now to avoid permanent block. Send the code you receive.",
 "Hi, I am from {b} support. Tell me the OTP we just sent you so I can cancel the wrong transaction.",
]
scam_bn = [
 "প্রিয় গ্রাহক, আপনার {b} অ্যাকাউন্ট ২৪ ঘণ্টার মধ্যে বন্ধ হয়ে যাবে। এখনই {l} লিংকে ক্লিক করে আপনার পিন দিন।",
 "জরুরি: আপনার {b} অ্যাকাউন্টে সন্দেহজনক লেনদেন। এখনই ওটিপি দিয়ে ভেরিফাই করুন {l}",
 "অভিনন্দন! আপনি ৫ লাখ টাকার লটারি জিতেছেন। পুরস্কার পেতে ১৫০০ টাকা রেজিস্ট্রেশন ফি পাঠান {l}",
 "আপনার {b} অ্যাকাউন্ট স্থগিত করা হয়েছে। কেওয়াইসি আপডেট করুন এখনই {l}",
 "ঘরে বসে আয় করুন দৈনিক ৫০০০ টাকা। পার্ট টাইম জব, কোনো অভিজ্ঞতা লাগবে না। রেজিস্ট্রেশন ফি জমা দিন। হোয়াটসঅ্যাপ করুন।",
 "আপনার পার্সেল ডেলিভারি হয়নি। ডেলিভারি ফি দিন {l} নাহলে ফেরত যাবে।",
 "আপনার ফোনে একটি ভেরিফিকেশন কোড গেছে। কোডটি আমাদের জানান, নাহলে {b} একাউন্ট ব্লক হবে।",
 "ভুলে আপনার নম্বরে টাকা চলে এসেছে। দয়া করে টাকা ফেরত পাঠান, জরুরি।",
 "আপনি {b} থেকে বোনাস পেয়েছেন! এখনই ক্লিক করুন {l} এবং আপনার পাসওয়ার্ড দিন।",
 "আপনার একাউন্ট লক হয়ে গেছে। আজই {l} লিংকে গিয়ে তথ্য যাচাই করুন, দেরি করলে বাতিল হয়ে যাবে।",
 "প্রিয় গ্রাহক, রিফান্ড পেতে নিচের লিংকে ক্লিক করুন এবং কার্ডের তথ্য দিন {l}",
 "আমি {b} অফিস থেকে বলছি। আপনার পিন নম্বরটা বলুন, ভুল লেনদেনটা বাতিল করে দিচ্ছি।",
]
scam_bl = [
 "Apni 5 lakh taka lottery jitechen. Ekhoni 1500 taka registration fee pathan: {l}",
 "Dear customer, apnar {b} account block hoye jabe. Ekhoni PIN diye verify korun {l}",
 "Jaruri! Apnar {b} account e shondehojonok lenden. OTP diye ekhoni verify korun {l}",
 "Ghore boshe daily 5000 taka income korun. Part time job, registration fee pathan. WhatsApp korun.",
 "Apnar {b} KYC update korun ekhoni, nahole account bondho hoye jabe. Link e click korun {l}",
 "Congratulations! Apni {b} theke bonus peyechen. Taka pete PIN den: {l}",
 "Vul kore apnar number e taka chole eshechhe. Taka ferot pathan ekhoni please.",
 "Apnar parcel ashe nai. Delivery fee pathan {l} nahole ferot jabe.",
 "Ami {b} theke bolchi. Apnar OTP code ta bolen, transaction ta cancel kore dibo.",
 "Apnar account lock hoye gese. Aj-i {l} e giye verify korun, deri korle bondho hoye jabe.",
 "Prize jitechen! Gift card pathan tahole taka pabe. Ekhoni call korun {l}",
 "Refund pabar jonno niche link e click korun ar card er information din {l}",
]

# ---------- NORMAL ----------
ham_en = [
 "Hey, are we still on for lunch at 1pm tomorrow? I will bring the notes.",
 "Your account was debited BDT 500 at a retail store on 22/10. For any query call the number on your card.",
 "Meeting moved to 3pm on Thursday. Please bring the project report.",
 "Happy birthday! Hope you have a great day, let's catch up this weekend.",
 "Can you send me the assignment file when you are free? Thanks.",
 "Your order #4821 has been shipped and will arrive on Tuesday. Track it in the official app.",
 "Reminder: your dentist appointment is tomorrow at 10:30am.",
 "I reached home safely. See you in class on Sunday.",
 "Thanks for your payment. Your receipt is attached to your email.",
 "Please review the draft and share your feedback by Friday.",
 "Mom said dinner is ready. Come home early today.",
 "The class is cancelled today because the teacher is sick. Check the group for updates.",
 "You received BDT 1000 from Rahim. Your new balance is shown in the app.",
 "Don't forget the group study at the library at 4pm.",
 "Your electricity bill for October is available in the official app. Due date is the 30th.",
 "Great job on the presentation today! The team really liked it.",
 "Can you call me when you are free? Nothing urgent.",
 "Salary has been credited to your account. Have a nice weekend.",
]
ham_bn = [
 "কালকে দুপুর ১টায় লাঞ্চে দেখা হচ্ছে তো? আমি নোটগুলো নিয়ে আসব।",
 "ভাই, ক্লাসের অ্যাসাইনমেন্টটা পাঠাতে পারবে? ধন্যবাদ।",
 "আজ রাতে বাসায় ফিরতে একটু দেরি হবে। খাবার রেখে দিও।",
 "শুভ জন্মদিন! আল্লাহ তোমাকে ভালো রাখুক। এই সপ্তাহে দেখা করব।",
 "আপনার অ্যাকাউন্ট থেকে ৫০০ টাকা কাটা হয়েছে। কোনো প্রশ্ন থাকলে কার্ডের পেছনের নম্বরে কল করুন।",
 "মিটিং বৃহস্পতিবার বিকেল ৩টায় হবে। রিপোর্টটা সাথে এনো।",
 "আমি নিরাপদে পৌঁছে গেছি। রবিবার ক্লাসে দেখা হবে।",
 "আপনার অর্ডারটি পাঠানো হয়েছে, মঙ্গলবার পৌঁছাবে। অফিসিয়াল অ্যাপে ট্র্যাক করুন।",
 "আম্মু বলেছে রাতের খাবার তৈরি। আজ তাড়াতাড়ি বাসায় এসো।",
 "আজ শিক্ষক অসুস্থ থাকায় ক্লাস বন্ধ। গ্রুপে আপডেট দেখে নিও।",
 "আপনি রহিমের কাছ থেকে ১০০০ টাকা পেয়েছেন। নতুন ব্যালেন্স অ্যাপে দেখুন।",
 "ফ্রি থাকলে একবার ফোন দিও, তেমন জরুরি কিছু না।",
 "বিকেল ৪টায় লাইব্রেরিতে গ্রুপ স্টাডি, ভুলো না।",
 "প্রেজেন্টেশন দারুণ হয়েছে আজ! সবাই খুব পছন্দ করেছে।",
]
ham_bl = [
 "Kalke dupur 1tay lunch e dekha hocche to? Ami note gula niye ashbo.",
 "Bhai, assignment ta pathate parbi? Thanks.",
 "Aj raate bashay ferte ektu deri hobe. Khabar rekhe dis.",
 "Shuvo jonmodin! Ei weekend e dekha korbo.",
 "Ami nirapode pouchhe gechi. Sunday class e dekha hobe.",
 "Meeting Thursday bikel 3tay hobe. Report ta sathe niye asho.",
 "Amma bolse raater khabar ready. Aj taratari bashay esho.",
 "Free thakle ekbar call dio, temon joruri kichu na.",
 "Group study library te bikel 4tay, bhule jaish na.",
 "Presentation ta darun hoyeche aj! Shobai khub pochondo korse.",
 "Tomar order ta pathano hoyeche, Tuesday pouchabe. Official app e track koro.",
 "Rahim er kach theke 1000 taka peyecho. Balance app e dekho.",
]

rows=[]
def gen(templates, label, n):
    for _ in range(n):
        t=pick(templates); b=pick(brands_en)
        s=t.format(b=b,l=link(b)) if "{" in t else t
        # light spelling noise to mimic variation
        if random.random()<0.25: s=s.replace("account","acount").replace("verify","verfy").replace("ekhoni","ekhon")
        if random.random()<0.15: s=s.upper() if s.isascii() else s
        if random.random()<0.2: s=s.replace("bKash","bkash").replace("Nagad","nagad")
        rows.append((label,s))
gen(scam_en,1,150); gen(scam_bn,1,130); gen(scam_bl,1,130)
# normal messages: include every template several times (+ small noise)
for tpl in (ham_en,ham_bn,ham_bl):
    for t in tpl:
        for _ in range(6):
            s=t
            if random.random()<0.2 and s.isascii(): s=s.lower()
            rows.append((0,s))
random.shuffle(rows)
with open("data.csv","w",newline="",encoding="utf-8") as f:
    w=csv.writer(f); w.writerow(["label","text"]); w.writerows(rows)
print(len(rows),"rows; scam =",sum(r[0] for r in rows))
