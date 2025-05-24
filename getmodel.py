import google.generativeai as genai
from google.api_core import exceptions

# --- IMPORTANT ---
# Replace "PASTE_YOUR_API_KEY_HERE" with your actual Gemini API key.
# This is the most crucial step for this test.
API_KEY = "PASTE_YOUR_API_KEY_HERE"

try:
    print("Attempting to configure API key...")
    genai.configure(api_key=API_KEY)
    print("API key configured.")

    print("\nFetching list of available models...")
    model_list = list(genai.list_models()) # Use list() to force evaluation

    if model_list:
        print("Successfully fetched models:")
        for m in model_list:
            if 'generateContent' in m.supported_generation_methods:
                print(f"- {m.name}")
    else:
        # This is the case you are experiencing.
        print("\n--- The API call succeeded but returned an empty list of models. ---")
        print("This usually means the API key is valid but the project lacks permissions or has API restrictions.")
        print("Please check Step 2 and 3 below.")

except exceptions.PermissionDenied as e:
    print("\n--- ERROR: PERMISSION DENIED ---")
    print("The API key is likely correct, but the Google Cloud project it's linked to has not enabled the 'Generative Language API' or 'Vertex AI API'.")
    print("Go to your Google Cloud Console and enable it. See Step 2.")
    print(f"Full error: {e}")

except exceptions.Unauthenticated as e:
    print("\n--- ERROR: AUTHENTICATION FAILED ---")
    print("The API key you provided is invalid, expired, or incorrect.")
    print("Please double-check the key you pasted into the script. See Step 2.")
    print(f"Full error: {e}")

except Exception as e:
    print(f"\n--- AN UNEXPECTED ERROR OCCURRED ---")
    print("This could be a network issue or something else.")
    print(f"Error details: {e}")