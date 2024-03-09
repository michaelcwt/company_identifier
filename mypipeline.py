import json
import pprint
import google.generativeai as palm


def load_generate_prompt(file_path:str):
    with open(file_path, 'r') as file:
        content = file.read()

    return content


def palm2_identifier(_api_key:str, file_path:str)->json:
    palm.configure(api_key = _api_key)
    models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]

    text = load_generate_prompt(file_path)

    prompt_01 = """
            You are an expert at reading articles and companies identifying.

            Solve the following problem:

            I have an article below under the dash line. Please go through the article and identify the items bellow.
            - topic of the article (usually appear in the first few lines)
            - all companies name appears inside the article (exlcude those not relevant to the content of the article)
            - form corresponding url with this format "company_name" + ".com" for each company

            Show the result of companies name, their url and doccument topic in format (JSON) we expect to extract are as follows:
                {
                "related_companies": [{ "company_name":"X", "company_domain":"x.com" }, { "company_name":"Bloomberg", "company_domain":"bloomberg.com" }], 
                "topic":"X is launching two new subscription tiers, including a ‘Premium+’ ad-free plan"
                }
            --------
            """
    

    completion = palm.generate_text(
        model = models[0].name,
        prompt = prompt_01 + '\n' + text,
        temperature = 0,
        max_output_tokens = 800,
    )

    res = json.loads(completion.result)

    return res