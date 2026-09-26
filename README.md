# Object-Color-Detection-with-Python

Object Color Detection (การตรวจจับวัตถุตามสีที่กำหนด) ด้วย Python และ OpenCV ซึ่งเป็นพื้นฐานสำคัญสำหรับนำไปประยุกต์ใช้ในงานคัดแยกชิ้นงานตามสีครับ

คำอธิบายการทำงาน

cv2.cvtColor(..., cv2.COLOR_BGR2HSV): แปลงภาพเป็น HSV เพราะการแยกสีในโมเดลนี้ทำได้ง่ายและเสถียรต่อแสงเงามากกว่า RGB

cv2.inRange(...): ใช้กรองสีให้ออกมาเป็นภาพขาวดำ (Mask) โดยสีที่เราสนใจจะเป็นสีขาว ส่วนฉากหลังจะเป็นสีดำ

cv2.findContours(...): ค้นหาขอบเขตของวัตถุสีขาวใน Mask เพื่อนำพิกัดไปวาดกรอบสี่เหลี่ยม (cv2.rectangle) ครอบตัววัตถุ

*****************************************************************************

🚀 รวมโปรแกรม AI และระบบอัตโนมัติ พร้อมใช้งานสำหรับบริษัท โรงงาน ร้านค้า และสถานศึกษา

✅ โปรแกรม AI นับจำนวนคนเข้า–ออกแบบเรียลไทม์ รองรับ Webcam / IP Camera พร้อม Dashboard และรายงาน 🛒 https://shopee.co.th/product/119639499/45117863699/

✅ โปรแกรมตรวจข้อสอบปรนัยสำหรับโรงเรียน ตรวจจากกระดาษคำตอบด้วย Webcam หรือ Scanner สรุปคะแนนและ Export Excel 🛒 https://shopee.co.th/product/119639499/57217847213/

✅ ระบบลงเวลาด้วยใบหน้า Face Recognition บันทึกเวลาเข้า–ออก พร้อมสรุปรายงาน Excel เหมาะสำหรับบริษัทและโรงเรียน 🛒 https://shopee.co.th/product/119639499/51367848067/

✅ โปรแกรม AI ตรวจจับไฟและควัน แจ้งเตือนพร้อมภาพผ่าน LINE รองรับ Webcam / IP Camera และบันทึกเหตุการณ์ 🛒 https://shopee.co.th/product/119639499/26045820693/

✅ ชุดกริ่ง SOS Wi-Fi พร้อมไฟและเสียงเตือน ช่วยแจ้งเหตุฉุกเฉินได้อย่างรวดเร็ว เหมาะสำหรับสำนักงาน โรงงาน โรงเรียน และจุดบริการ 🛒 https://shopee.co.th/product/119639499/57567842533

✅ เครื่องอ่านบาร์โค้ดอัตโนมัติ สำหรับตรวจสอบสินค้า บันทึกข้อมูล และประยุกต์ใช้กับสายการผลิตหรือคลังสินค้า 🛒 https://shopee.co.th/product/119639499/42528635974/

✅ เครื่องอ่านสีวัสดุอุตสาหกรรมอัตโนมัติ ตรวจสอบและจำแนกสีวัสดุด้วยระบบประมวลผลภาพ เหมาะสำหรับงานควบคุมคุณภาพ 🛒 https://shopee.co.th/product/119639499/45605941899/

✅ ระบบแจ้งเตือนฉุกเฉินผ่านมือถือ พร้อมอุปกรณ์สัญญาณ กดปุ่มเพียงครั้งเดียวบนมือถือ ระบบสั่งงานไฟและเสียงแจ้งเตือนได้ทันที 🛒 https://shopee.co.th/product/119639499/51805846456/

💡 สามารถปรับแต่งโปรแกรมและพัฒนาฟังก์ชันเพิ่มเติมให้เหมาะกับหน้างานจริงได้ รองรับงาน AI, IoT, Image Processing, Python, Dashboard และระบบ Automation

*****************************************************************************

ช่องทางติดต่อ:

ชื่อ : ภาธสุ ดวงมาลา

ตำแหน่ง : R&D Manager

Tel : 0641900551

E-mail : nextsoftware.pp@gmail.com

Line : https://lin.ee/THH8PAt

Medium : https://dr-pathasu-doung.medium.com

Website : https://nextsoftwarethailand.com, https://autoworks24.com

บริษัท เน็กซ์ ซอฟต์แวร์ จำกัด 

ที่อยู่ หมู่บ้าน inizio เลขที่ 888/257 ถนนมะลิวัลย์ ตำบลบ้านทุ่ม อำเภอเมืองขอนแก่น จังหวัดขอนแก่น 40000 เลขที่ผู้เสียภาษี : 0405558003118

ผลงานและประวัติการทำงาน

สามารถดูผลงานและประวัติการทำงานได้ที่

AI, Image Processing : https://www.dropbox.com/scl/fi/tskimhifw0hlcdea5e8t8/Next-Software-2026.pdf?rlkey=f26k2b7t69doklzwxyx54qsmh&dl=0

IoT : https://www.dropbox.com/scl/fi/a5mj4ucjotjv4xrh6sh9q/NS_IOT2025.pdf?rlkey=t0cwl0l4b81w73do2drhqqjp0&dl=0

SEO, Website : https://www.dropbox.com/scl/fi/4q811q0s88xtd8usf5e25/WEB-DEVELOPER-SEARCH-ENGINE-OPTIMIZATION.pdf?rlkey=nvqvndrxv7v9yrfmlcgtplmtx&dl=0
