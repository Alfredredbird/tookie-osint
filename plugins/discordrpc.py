from pypresence import Presence
import time

try:
 client_id = '1280593779203637329'
 RPC = Presence(client_id)  
 RPC.connect()  


 RPC.update(
    state="Investigating",
    details="Looking For Someone",
    start=time.time()  
 )

 try:
    while True:
        time.sleep(15)  
 except KeyboardInterrupt:
    RPC.close()
except Exception:
    continue
