# CN331 Software Engineering
## Project: UniversityRegistration

```
6210612864 นาย รเณศ ชูเผือก 
6210612823 นาย วีรภัทร ลีลาวิทยานนท์ 
```

ไฟล์ประกอบไปด้วย 5 โฟลเดอร์ ได้แก่ course, static, templates, UniversityRegistration_cn331, users

**Folder: courses**
ใช้สำหรับเก็บข้อมูลหน้าต่าง index, หน้าต่างการลงทะเบียนคอร์สต่่างๆ, หน้าต่างดู status ของคอร์สต่างๆ
ซึ่งเป็นหน้าต่างที่ให้ user ใช้ประโยชน์ในการลงทะเบียนและดูข้อมูลของคอร์สที่ว่างอยู่
ซึ่งหาก user เป็น staff หน้า login ที่แสดงผลก็จะแตกต่างออกไปเล็กน้อย

**Folder: static**
ใช้สำหรับเก็บ script ต่างๆ ของเว็บไซต์ ทั้ง css จาก template และ javascript
เพื่อใช้ประโยชน์ในการเขียนและวางหน้าเว็บต่างๆ ของเว็บไซต์

**Folder: templates**
ใช้สำหรับเก็บ template html ของหน้าเว็บ ได้แก่ main.html ซึ่งเป็นส่วนของหน้าเว็บหลัก
และ navbar.html ซึ่งเป็นส่วนของ navigation bar ด้านบนของหน้าเว็บ

**Folder: UniversityRegistration_cn331**
ใช้สำหรับเก็บข้อมูล setting บางส่วนของหน้าเว็บ Login

**Folder: users**
ใช้สำหรับเก็บข้อมูลหน้าต่าง Login เพื่อใช้เข้าหน้าเว็บ และหน้าลืมรหัสผ่าน (forgot password) 
ที่เชื่่อมต่อกับ Database ของ User ที่ใช้ในการ Login เข้าหน้าเว็บ

**Interface ของ Website เมื่อ Login ผ่านฝั่งของ User**
![](https://github.com/Kaichou-brave/UniversityRegistration_cn331/blob/main/webscreenshot/pic01.png)
**Interface ของ Website เมื่อ Login ผ่านฝั่งของ Staff**
![](https://github.com/Kaichou-brave/UniversityRegistration_cn331/blob/main/webscreenshot/pic02.png)
**Interface เมื่อกดเข้าไปดูข้อมูลของแต่ละ Coure (Staff จะเห็นรายชื่อนักเรียนที่ลงทะเบียนในคอร์สนี้ด้วย)**
![](https://github.com/Kaichou-brave/UniversityRegistration_cn331/blob/main/webscreenshot/pic03.png)
**การลงทะเบียนของฝั่ง User**
![](https://github.com/Kaichou-brave/UniversityRegistration_cn331/blob/main/webscreenshot/pic04.png)
