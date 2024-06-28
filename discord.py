from pypresence import Presence
from time import time

def turnDiscord():
    """Function for creating status in discord"""
    rpc = Presence(1254735877897322496)
    rpc.connect()
    rpc.update(
        state="sc.project",
        details="гетэвейгетэвей",
        large_image="uu1212",
        start=int(time())
    )
