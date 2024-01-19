#soon to be fully implemented
#plugins need to have the module be nammed "run()" in order to be used.
   #the below function will be fully available after some changes
def run(lol):
   """-lol"""
   
   return


def phoneosint():
 uname = ""
 try:
    import phonenumbers
    from phonenumbers import carrier, geocoder, timezone
 except:
    print("Couldent Import Modules") 
 """Gathers info about a given phone number"""
 try:
  phone_number = phonenumbers.parse(str(uname))
 except:
     print("Input must be a valid phone number") 
 phone_number_national = phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.NATIONAL)
 phone_number_international = phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
 isp = carrier.name_for_number(phone_number, 'en')
 time_zone = timezone.time_zones_for_number(phone_number)
 location = geocoder.description_for_number(phone_number, 'en')

 print(f"[!] Fetching Phone Number : {str(uname)}")
 print(f"[+] {phone_number}")
 print(f"[+] International Format : {phone_number_international}")        
 print(f"[+] National Format : {phone_number_national}")           
 print(f"[+] Time Zone : {time_zone}")
 print(f"[+] ISP : {isp}")
 print(f"[+] Location : {location}")