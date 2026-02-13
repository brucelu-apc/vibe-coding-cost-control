import argparse
import os
import sys
from dotenv import load_dotenv
from supabase import create_client, Client, ClientOptions

def main():
    parser = argparse.ArgumentParser(description="Log AI API costs to Supabase.")
    parser.add_argument("--project", required=True, help="Project name")
    parser.add_argument("--model", required=True, help="Model name")
    parser.add_argument("--tin", type=int, required=True, help="Input tokens")
    parser.add_argument("--tout", type=int, required=True, help="Output tokens")
    
    args = parser.parse_args()

    # Load from the provided .env path or current directory
    load_dotenv(override=True)
    
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")
    
    if not url or not key:
        print("Error: SUPABASE_URL or SUPABASE_SERVICE_ROLE_KEY not found in environment.")
        sys.exit(1)

    try:
        # Connect to 'billing' schema as requested
        supabase = create_client(url, key, options=ClientOptions(schema="billing"))
        
        data = {
            "project_name": args.project,
            "model": args.model,
            "tokens_in": args.tin,
            "tokens_out": args.tout,
            # cost_usd can be calculated here or in DB trigger
        }
        
        res = supabase.table("cost_logs").insert(data).execute()
        print(f"Successfully logged cost for project '{args.project}'.")
        print(f"Result: {res.data}")
        
    except Exception as e:
        print(f"Error logging cost: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
