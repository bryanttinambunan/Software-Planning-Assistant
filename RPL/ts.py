from db import supabase

data = supabase.table("tasks").select("*").execute()

print(data.data)