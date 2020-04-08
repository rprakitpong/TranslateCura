from googletrans import Translator
import json

#t = Translator()
#s = t.translate(['haha','banana','apple',"carrots", "onions", "brocoli","oranges", "mango",'yes','no'],dest='th')
#if s:
#    for ss in s:
#        print(ss.text)

#data = {"Cura Profile": "รายละเอียดการดูแล", "JPG Image": "ภาพ JPG", "JPEG Image": "ภาพ JPEG"}
data = {"Cura Profile": "รายละเอียดการดูแล", "JPG Image": "ภาพ JPG", "JPEG Image": "ภาพ JPEG", "PNG Image": "PNG ภาพ", "BMP Image": "BMP ภาพ", "GIF Image":"ภาพ GIF", "Machine Settings": "การตั้งค่าเครื่อง", "Save to Removable Drive": "บันทึกไปยังไดรฟ์แบบถอดได้", "Save to Removable Drive {0}": "บันทึกเพื่อถอดออกไดรฟ์ {0}", "There are no file formats available to write with!": "ไม่มีรูปแบบไฟล์ที่มีอยู่ในการเขียนที่มีอยู่!", "Saving to Removable Drive<filename>{0}</filename>": "บันทึกไปยังไดรฟ์แบบถอดได้ <ชื่อไฟล์> {0} </ filename>", "Saving": "ประหยัด", "Could not save to <filename>{0}</filename>: <message>{1}</message>": "ไม่สามารถบันทึกไปยัง <ชื่อไฟล์> {0} </ filename> <ข้อความ> {1} </ ข้อความ>", "Could not find a file name when trying to write to {device}.": "ไม่พบชื่อแฟ้มเมื่อพยายามที่จะเขียนไปยังอุปกรณ์ {}", "Could not save to removable drive {0}: {1}": "ไม่สามารถบันทึกไดรฟ์แบบถอดได้{0}: {1}", "Error": "ความผิดพลาด", "Saved to Removable Drive {0} as {1}": "บันทึกไว้ในที่ถอดออกไดรฟ์ {0} เป็น {1}", "File Saved": "ไฟล์ที่บันทึกไว้", "Eject": "Eject", "Eject removable device {0}": "อุปกรณ์ที่ถอดออกได้ Eject {0}", "Warning": "คำเตือน", "Ejected {0}. You can now safely remove the drive.": "พุ่งออกมา {0} ขณะนี้คุณสามารถลบออกอย่างปลอดภัยไดรฟ์", "Safely Remove Hardware": "Safely Remove Hardware", "Failed to eject {0}. Another program may be using the drive.": "ล้มเหลวที่จะดีดออก {0} โปรแกรมอื่นอาจจะใช้ไดรฟ์", "Removable Drive": "ไดรฟ์แบบถอดได้", "\nDo you want to sync material and software packages with your account?": "คุณต้องการที่จะซิงค์แพคเกจวัสดุและซอฟต์แวร์ด้วยบัญชีของคุณหรือไม่", "Changes detected from your Ultimaker account": "พบการเปลี่ยนแปลงจากบัญชี Ultimaker ของคุณ", "Sync": "ซิงค์", "Decline": "ลดลง", "Agree": "ตกลง", "Plugin License Agreement": "ข้อตกลงการอนุญาตปลั๊กอิน", "Decline and remove from account": "ลดลงและลบออกจากบัญชี", "{} plugins failed to download": "{} ปลั๊กอินล้มเหลวในการดาวน์โหลด", "\nSyncing...": "ซิงค์ ...", "You need to quit and restart {} before changes have effect.": "คุณจำเป็นต้องปิดและเริ่มต้น {} ก่อนการเปลี่ยนแปลงมีผล", "AMF File": "AMF ไฟล์", "Solid view": "มุมมองที่เป็นของแข็ง", "Level build plate": "สร้างแผ่นระดับ", "Select upgrades": "เลือกการอัพเกรด", "USB printing": "พิมพ์ USB", "Print via USB": "พิมพ์ผ่านทาง USB", "Connected via USB": "เชื่อมต่อผ่าน USB", "A USB print is in progress, closing Cura will stop this print. Are you sure?": "พิมพ์ USB มีความคืบหน้าในการปิด Cura จะหยุดการพิมพ์นี้ คุณแน่ใจไหม?", "A print is still in progress. Cura cannot start another print via USB until the previous print has completed.": "พิมพ์ยังคงอยู่ในความคืบหน้า Cura ไม่สามารถเริ่มต้นการพิมพ์อื่นผ่านทาง USB จนกว่าพิมพ์ก่อนหน้านี้ได้เสร็จสิ้น", "Print in Progress": "พิมพ์ในความคืบหน้า", "tomorrow": "วันพรุ่งนี้", "today": "ในวันนี้", "Print over network": "พิมพ์ผ่านเครือข่าย", "Connected over the network": "เชื่อมต่อผ่านเครือข่าย", "Cura has detected material profiles that were not yet installed on the host printer of group {0}.": "Cura ได้ตรวจพบโปรไฟล์วัสดุที่ยังไม่ได้ติดตั้งบนเครื่องพิมพ์โฮสต์ของกลุ่ม {0}", "Sending materials to printer": "วัสดุเพื่อการส่งเครืองพิมพ์", "Sending Print Job": "ส่งงานพิมพ์", "Uploading print job to printer.": "งานพิมพ์อัปโหลดไปยังเครื่องพิมพ์", "Could not upload the data tothe printer.": "ไม่สามารถอัปโหลดข้อมูลไปยังเครื่องพิมพ์", "Network error": "ข้อผิดพลาดของเครือข่าย", "Print job was successfully sent to the printer.": "งานพิมพ์ถูกส่งเรียบร้อยแล้วไปยังเครื่องพิมพ์", "Data Sent": "ส่งข้อมูล", "Send and monitor print jobs from anywhere using your Ultimaker account.": "และส่งงานพิมพ์จอภาพจากที่ใดก็ได้โดยใช้บัญชีของคุณ Ultimaker", "Connect to Ultimaker Cloud": "เชื่อมต่อกับ Ultimaker เมฆ", "Get started": "เริ่ม", "Please wait until the current job has been sent.": "โปรดรอจนกว่างานปัจจุบันได้รับการส่ง", "Print error": "ข้อผิดพลาดในการพิมพ์", "You are attempting to connect to a printer that is not running Ultimaker Connect. Please update the printer to the latest firmware.": "คุณพยายามที่จะเชื่อมต่อกับเครื่องพิมพ์ที่ไม่ได้ทำงาน Ultimaker เชื่อมต่อ โปรดอัปเดตเครื่องพิมพ์กับเฟิร์มแวล่าสุด", "Update your printer": "อัพเดทเครื่องพิมพ์ของคุณ", "You are attempting to connect to {0} but it is not the host of a group. You can visit the web page to configure it as a group host.": "คุณกำลังพยายามที่จะเชื่อมต่อไปที่ {0} แต่มันไม่ได้เป็นเจ้าภาพของกลุ่ม คุณสามารถเยี่ยมชมหน้าเว็บเพื่อกำหนดค่าเป็นเจ้าภาพกลุ่ม", "Not a group host": "ไม่ได้เป็นเจ้าภาพกลุ่ม", "Configure group": "กลุ่มการกำหนดค่า", "Connect via Network": "เชื่อมต่อผ่านเครือข่าย", "Print via Cloud": "พิมพ์ผ่านระบบคลาวด์", "Connected via Cloud": "เชื่อมต่อผ่านระบบคลาวด์", "3MF File": "3MF ไฟล์", "Nozzle": "จมูกวัว", "Project file <filename>{0}</filename> contains an unknown machine type <message>{1}</message>. Cannot import the machine. Models will be imported instead.": "แฟ้มโครงการ <ชื่อไฟล์> {0} </ filename> มีประเภทเครื่องที่ไม่รู้จัก <ข้อความ> {1} </ ข้อความ> ไม่สามารถนำเข้าเครื่อง รุ่นจะถูกนำเข้าแทน", "Open Project File": "ไฟล์เปิดโครงการ", "Recommended": "แนะนำ", "Custom": "กำหนดเอง", "Support Blocker": "สนับสนุน Blocker", "Create a volume in which supports are not printed.": "สร้างไดรฟ์ที่สนับสนุนไม่ได้พิมพ์", "Per ModelSettings": "การตั้งค่าต่อรุ่น", "Configure Per Model Settings": "การกำหนดค่าการตั้งค่ารูปแบบการต่อ", "Preview": "ดูตัวอย่าง", "X-Ray view": "มุมมอง X-Ray", "G-code File": "G-รหัสไฟล์", "G File": "D เนื้อ", "Parsing G-code": "แยก G-รหัส", "G-code Details": "รายละเอียด G-รหัส", "Make sure the g-code is suitable for your printer and printer configuration before sending the file to it. The g-code representation may not be accurate.": "ตรวจสอบให้แน่ใจกรัมรหัสที่เหมาะสมสำหรับการตั้งค่าเครื่องพิมพ์และเครื่องพิมพ์ของคุณก่อนที่จะส่งไฟล์ไป การเป็นตัวแทนกรัมรหัสอาจไม่ถูกต้อง", "Post Processing": "โพสต์การประมวลผล", "Modify G-Code": "ปรับเปลี่ยน G-Code", "Unable to slice with the current material as it is incompatible with the selected machine orconfiguration.": "ไม่สามารถที่จะเชือดด้วยวัสดุในปัจจุบันในขณะที่มันไม่เข้ากันกับเครื่องที่เลือกหรือการกำหนดค่า", "Unable to slice": "ไม่สามารถชิ้น","Unable to slice with the current settings. The following settings have errors: {0}": "ไม่สามารถหั่นกับการตั้งค่าปัจจุบัน การตั้งค่าดังต่อไปนี้มีข้อผิดพลาด: {0}", "Unable to slice due to some per-model settings. The following settings have errors on one or more models: {error_labels}": "ไม่สามารถฝานเนื่องจากบางต่อการตั้งค่ารูปแบบ การตั้งค่าต่อไปนี้มีข้อผิดพลาดในหนึ่งหรือมากกว่ารุ่น: {} error_labels", "Unable to slice because the prime tower or prime position(s) are invalid.": "ไม่สามารถชิ้นเพราะหอคอยที่สำคัญหรือตำแหน่งนายกรัฐมนตรี (s) ไม่ถูกต้อง", "Unable to slice because there are objects associated with disabled Extruder %s.": "ไม่สามารถชิ้นเพราะมีวัตถุที่เกี่ยวข้องกับคนพิการ Extruder% s", "Nothing to slice because none of the models fit the build volume or are assigned to a disabled extruder. Please scale or rotate models to fit, or enable an extruder.": "ไม่มีอะไรที่จะชิ้นเพราะไม่มีรูปแบบให้พอดีกับปริมาณการสร้างหรือกำหนดให้กับเครื่องอัดรีดพิการ โปรดขนาดหรือรูปแบบหมุนเพื่อให้พอดีหรือเปิดใช้งานเครื่องอัดรีด", "Processing Layers": "เลเยอร์การประมวลผล", "Information": "ข้อมูล", "Cura 15.04 profiles": "Cura 15.04 โปรไฟล์", "Ultimaker Format Package": "Ultimaker รูปแบบแพคเกจ", "Update Firmware": "อัปเดตเฟิร์มแว", "Prepare": "เตรียมการ", "Open Compressed Triangle Mesh": "เปิดการบีบอัดสามเหลี่ยมตาข่าย", "COLLADA Digital Asset Exchange": "COLLADA แลกเปลี่ยนสินทรัพย์ดิจิตอล", "glTF Binary": "glTF ไบนารี", "glTF Embedded JSON": "glTF แบบฝัง JSON", "Stanford Triangle Format": "รูปแบบสแตนฟอสามเหลี่ยม", "Compressed COLLADA Digital Asset Exchange": "การบีบอัด COLLADA แลกเปลี่ยนสินทรัพย์ดิจิตอล", "3MF file": "ไฟล์ 3MF", "Cura Project 3MF file": "ไฟล์ Cura โครงการ 3MF", "Error writing 3mf file.": "ข้อผิดพลาดในการเขียนไฟล์ 3mf", "GCodeWriter does not support non-text mode.": "GCodeWriter ไม่สนับสนุนโหมดที่ไม่ใช่ข้อความ", "Please prepare G-code before exporting.": "โปรดเตรียม G-รหัสก่อนที่จะส่งออก", "Monitor": "หน้าจอ", "Manage backups": "จัดการการสำรองข้อมูล", "Backup": "การสำรองข้อมูล", "There was an error listing your backups.": "เกิดข้อผิดพลาดในรายการสำรองข้อมูลของคุณเป็น", "There was an error trying to restore your backup.": "มีข้อผิดพลาดพยายามที่จะเรียกคืนการสำรองข้อมูลของคุณ", "Backups": "การสำรองข้อมูล", "Uploading your backup...": "อัปโหลดสำรองข้อมูลของคุณ ...", "There was an error while uploading your backup.": "เกิดข้อผิดพลาดขณะอัปโหลดสำรองของคุณ", "Your backup has finished uploading.": "การสำรองข้อมูลของคุณมีการอัปโหลดเสร็จแล้ว", "X3D File": "X3D ไฟล์", "Cura does not accurately display layers when Wire Printing is enabled.": "Cura ไม่ถูกต้องแสดงชั้นเมื่อพิมพ์สายไฟถูกเปิดใช้งาน", "Simulation View": "จำลองดู"}
print(type(data))

with open('cura.json', 'w') as fp:
    json.dump(data, fp)

with open('cura.json', 'r') as fp:
    data2 = json.load(fp)
    print(type(data2))