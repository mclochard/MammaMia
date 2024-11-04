from curl_cffi.requests import AsyncSession

IMPERSONATE = "chrome120"

class CustomSession(AsyncSession):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    async def get(self, url, **kwargs):      
        if "allow_redirects" in kwargs:
            raise ValueError("allow_redirects cannot be set. It is always True")
        if "impersonate" in kwargs:
            raise ValueError(f"impersonate cannot be set. It is always '{IMPERSONATE}'")
          
        return await super().get(url, **kwargs,allow_redirects=True, impersonate=IMPERSONATE)
    
    async def post(self, url, **kwargs): 
        if "allow_redirects" in kwargs:
            raise ValueError("allow_redirects cannot be set. It is always True")
        if "impersonate" in kwargs:
            raise ValueError(f"impersonate cannot be set. It is always '{IMPERSONATE}'")
        
        return await super().post(url, **kwargs,allow_redirects=True, impersonate=IMPERSONATE)