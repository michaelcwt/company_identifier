### Identifying Companies Name - Michael Chan
- You can assume the content (HTML) is already scrapped, so you can use a txt file to store the content and start analyzing
- You can write a function that is handled by OpenAI / LLM / Langchain, and extract relevant companies using prompt + example
- The result should be in JSON format, produced by an LLM / OpenAI or Langchain parser
- Instead of keyword matching, you should use AI / ML methods to remove irrelevant companies. For example, Reuters, Fortune could be related companies, but techcrunch should not related to this article 

### Files
- I`data.txt`: text from the given website (url)
- `mypipeline.py`: function for identifying
- `run.ipynb`: notebook to run the pipeline and demo

### Things to note & Methods I used
- I have used a palm2 model provided by google and you will need to use your own API key to access. Unfortunetly under regional restriction, I will not able to provide any demo here.
- Personally, I think GPT 3.5 or latest version will perform even better, same API key will be needed and higher cost.
- Lastly, if we have multiple website as example, we could provide one-shot or few-shot learning to LLM, which will helps to ace better result.
# company_identifier
