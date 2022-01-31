import os
from dotenv import load_dotenv

load_dotenv()

GOC_API_KEY = os.environ.get('GOC_API_KEY')

def CanadianTax(query):      #query,api_key


	API_KEY = GOC_API_KEY
	url = r"https://gstrate-cra-arc.api.canada.ca:443/ebci/ghnf/api/ext/v1/rates"
	res = requests.get(url, headers={'Accept':'*/*','user-key':API_KEY} )
	res=json.loads(res.text)

	result={}
	for item in res['GstRateProvinceList']:  
	    province = item['ProvinceCode'].lower()
	    for subset in item['GstRateDatePairList']:
	        if 'ExpiryDate' not in list(subset.keys()):
	            result[province] = subset['GstRate']
	print(result)
	try:
		print(result[query.lower()])
	    return result[query.lower()]
	except:
	    print('no match')
	    return None

if __name__ == "__main__":
	query = input()
    CanadianTax(query)