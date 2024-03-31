# we'll use this to search
import re

def extract_solana_transaction_hash(url):
    try:
        """
        Extracts hash string from a given URL or text.

        Args:
        url (str): The URL string/text.

        Returns:
        str: The extracted hash string.
        """

        # Remove all spaces from the URL
        url = url.replace(" ", "")
        
        # Find match
        match = re.search(r'/tx/([A-Za-z0-9]+)', url)
        if match:
            return match.group(1)
        else:
            # if match is not found, check if the user input the hash itself, check for the length of the string which conventionally is >= 87
            # If it meets the requirement , well it could be it hehe! 
            strlen = len(url)
            if strlen >= 87:
                # return the result
                return url
            else:
                return None
    except Exception as d:
        print("extract error:", d) 

# Example link
url = 'https://solscan.io/tx/QPV4XtT2ZsH66mBg1GGCEwLTwC3SytiAeBxUapemztZvucGLt8NUVH1rR17QXocFMQpa2x48PbaZNSsVarCYSK5'

# Result
result_of_signature = extract_solana_transaction_hash(url)

print("result_of_signature:", result_of_signature)
