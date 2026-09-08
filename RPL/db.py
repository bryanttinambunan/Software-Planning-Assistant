from supabase import create_client

SUPABASE_URL = "https://efxcmtefechhaguwjquv.supabase.co"
SUPABASE_KEY = "sb_publishable_9ETKm2yGxhiC2GWPtJAulQ__a4Eitv7"

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)