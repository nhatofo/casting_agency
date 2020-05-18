import os
SECRET_KEY = os.urandom(32)

basedir = os.path.abspath(os.path.dirname(__file__))

auth0_config = {
    "AUTH0_DOMAIN" : "nhatofo.auth0.com",
    "ALGORITHMS" : ["RS256"],
    "API_AUDIENCE" : "https://casting_agency.auth.com"
}

pagination = {
    "example" : 10 
}

bearer_tokens = {
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJqRTFSa1U1TkRVNVJEWTFPRE5HTXpreU5UYzNSa0l3UlRsQk1qZ3dPVU14UXpsQ01FRkJPUSJ9.eyJpc3MiOiJodHRwczovL25oYXRvZm8uYXV0aDAuY29tLyIsInN1YiI6IjZJYTIwT3ZoNTJJNjlQZTROV28xcGpwejRJQ0JQY2ZlQGNsaWVudHMiLCJhdWQiOiJodHRwczovL2Nhc3RpbmdfYWdlbmN5LmF1dGguY29tIiwiaWF0IjoxNTg5Nzg2Mzk0LCJleHAiOjE1ODk4NzI3OTQsImF6cCI6IjZJYTIwT3ZoNTJJNjlQZTROV28xcGpwejRJQ0JQY2ZlIiwiZ3R5IjoiY2xpZW50LWNyZWRlbnRpYWxzIiwicGVybWlzc2lvbnMiOltdfQ.I7CvLLrQqiElee_2ZeW8u28mzhCMmN59zKnHMy3FgXYoj4ELdICdFVtpDs21qBAuzgvD35ih75NkgkmJZyNs9KN4tGpLVPkrz7Os5-v1yyhmBir5MIREaq7RCF3udFyk_kLIRKV7cB3TtRhSblfPc75zpkSNwu92WeEKlPrv22ghv5-8JgU2PMCCgkZU_J3Pfil1Tz1vrhQXknGUCW_Pn9k92ui7FqGUelldeUx6B_DaDWOVBSvE5HcGZDpDoiaW5msDF6QAXt30xpbcFxqAZguEG6kRBX-SXBpazUo9zJU7G57AlNZyJG-PrKPt7aRYojWl94HsvRiG56euN0geHA",
  "token_type": "Bearer"
}