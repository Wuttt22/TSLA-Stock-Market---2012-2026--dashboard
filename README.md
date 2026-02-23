# 📈 TSLA Stock Market Interactive Dashboard

**จัดทำโดย:** [นายณัฐวุฒิ บิลสัน 167404910009]  
**ลิงก์สำหรับเข้าใช้งาน Dashboard:** [https://tsla-stock-market---2012-2026--dashboard-dretjb9mu57jsafuussci.streamlit.app/]  
**ชุดข้อมูลที่ใช้ (Dataset):** TSLA Stock Market 2012–2026 จาก Kaggle (ไฟล์ .CSV)
**Link https://www.kaggle.com/datasets/muhammadshayan5839/tsla-stock-market-2012-2026 Dowloadcsv**
---

## 🛠️ 1. วัตถุประสงค์และเครื่องมือที่ใช้ในการพัฒนา

โปรเจกต์นี้เป็นการสร้าง Interactive Dashboard เพื่อวิเคราะห์ข้อมูลราคาหุ้นของบริษัท Tesla (TSLA)  
โดยสามารถเปิดใช้งานผ่าน Web Browser ได้ทันที และช่วยให้ผู้ใช้งานเห็นแนวโน้มของราคาหุ้นอย่างชัดเจน

Dashboard นี้สามารถ:
- อัปโหลดไฟล์ .CSV ได้
- กรองข้อมูลตามช่วงวันที่
- แสดงสถิติสำคัญ (KPI)
- แสดงกราฟ Interactive
- แสดงรายละเอียดข้อมูลทั้งหมด

---

### 🔧 เครื่องมือที่ใช้

* **ภาษาที่ใช้:** Python  
* **Streamlit:** สำหรับสร้างหน้าเว็บแอปพลิเคชันและ Interactive UI  
* **Pandas:** สำหรับอ่านและจัดการข้อมูลตาราง (DataFrame)  
* **Plotly:** สำหรับสร้างกราฟ Interactive เช่น Line Chart, Volume Chart และ Candlestick  

---

## 📖 2. คู่มือการใช้งาน Dashboard (User Guide)

### ขั้นตอนที่ 1: การอัปโหลดข้อมูล

เมื่อเปิดลิงก์ Dashboard ขึ้นมา ให้มองที่แถบเมนูด้านซ้ายมือ (Sidebar)  
กดปุ่ม **"Upload TSLA CSV File"** แล้วเลือกไฟล์ `.CSV` ที่ดาวน์โหลดจาก Kaggle เข้าสู่ระบบ

*(<img width="1383" height="358" alt="image" src="https://github.com/user-attachments/assets/7876c4a4-8482-411f-b3c1-e8ff224256d2" />
<img width="1383" height="358" alt="image" src="https://github.com/user-attachments/assets/7876c4a4-8482-411f-b3c1-e8ff224256d2" />
)*

---

### ขั้นตอนที่ 2: การกรองข้อมูล (Filter)

หลังจากอัปโหลดไฟล์สำเร็จ จะมีเมนู **Filters** ปรากฏที่แถบด้านซ้ายมือ  

ผู้ใช้สามารถกรองข้อมูลได้โดย:

1. เลือกช่วงวันที่ (Date Range)
2. ระบบจะแสดงข้อมูลใหม่ทันทีตามช่วงวันที่ที่เลือก

ข้อมูลในกราฟและตารางจะเปลี่ยนตามเงื่อนไขที่กำหนดแบบ Real-time

*(<img width="374" height="344" alt="image" src="https://github.com/user-attachments/assets/fcedecf6-643c-4ff8-97c6-4f20c4afe2b3" />
<img width="374" height="344" alt="image" src="https://github.com/user-attachments/assets/fcedecf6-643c-4ff8-97c6-4f20c4afe2b3" />
)*

---

### ขั้นตอนที่ 3: การดูสถิติและกราฟแสดงผล

พื้นที่หลักของ Dashboard จะแสดงข้อมูลดังนี้:

### 📌 KPI (Key Performance Indicators)
- ราคาสูงสุด (Highest Price)
- ราคาต่ำสุด (Lowest Price)
- ค่าเฉลี่ยราคาปิด (Average Close)
- ปริมาณการซื้อขายรวม (Total Volume)

### 📈 กราฟแนวโน้มราคา (Price Trend)
แสดงราคาปิด (Close Price) พร้อมเส้นค่าเฉลี่ยเคลื่อนที่  
- MA7 (ค่าเฉลี่ย 7 วัน)  
- MA30 (ค่าเฉลี่ย 30 วัน)

### 📊 กราฟ Volume
แสดงปริมาณการซื้อขายรายวัน

### 🕯 กราฟ Candlestick
แสดงข้อมูล Open, High, Low, Close  
ช่วยวิเคราะห์แนวโน้มตลาดในแต่ละวัน

*(<img width="1421" height="628" alt="image" src="https://github.com/user-attachments/assets/b6ee5568-8022-45c2-98e1-2529dfea169e" />
<img width="1421" height="628" alt="image" src="https://github.com/user-attachments/assets/b6ee5568-8022-45c2-98e1-2529dfea169e" />
)*
*(<img width="1413" height="608" alt="image" src="https://github.com/user-attachments/assets/7a440e67-dad9-4a13-a0ff-d9f7a3cf23f2" />
<img width="1413" height="608" alt="image" src="https://github.com/user-attachments/assets/7a440e67-dad9-4a13-a0ff-d9f7a3cf23f2" />
)*
*(<img width="1438" height="717" alt="image" src="https://github.com/user-attachments/assets/e8b2da26-c624-46c0-b6f3-f6b3d2d02bd5" />
<img width="1438" height="717" alt="image" src="https://github.com/user-attachments/assets/e8b2da26-c624-46c0-b6f3-f6b3d2d02bd5" />
)*

---

### ขั้นตอนที่ 4: การดูรายละเอียดข้อมูลทั้งหมด

เมื่อเลื่อนลงมาด้านล่างสุดของ Dashboard  
จะพบกับตารางแสดงข้อมูลดิบ (Raw Data)  
ซึ่งเป็นข้อมูลที่ผ่านการกรองตามช่วงวันที่แล้ว

ผู้ใช้สามารถ:
- เลื่อนดูข้อมูลย้อนหลัง
- ตรวจสอบราคาหุ้นรายวัน
- ดาวน์โหลดข้อมูลที่กรองแล้วเป็นไฟล์ .CSV

*(เ<img width="1404" height="625" alt="image" src="https://github.com/user-attachments/assets/4b40ac35-e0fa-408d-81fd-3c9b7fa3e9ab" />
<img width="1404" height="625" alt="image" src="https://github.com/user-attachments/assets/4b40ac35-e0fa-408d-81fd-3c9b7fa3e9ab" />
)*

---

## 📊 สรุปผลการพัฒนา

Dashboard นี้ช่วยให้ผู้ใช้สามารถวิเคราะห์แนวโน้มราคาหุ้น TSLA  
ได้อย่างสะดวกและเข้าใจง่าย ผ่านกราฟ Interactive และตัวชี้วัดสำคัญ

เหมาะสำหรับงานด้าน Data Analysis และ Data Visualization  
รวมถึงการศึกษาแนวโน้มตลาดหุ้น
