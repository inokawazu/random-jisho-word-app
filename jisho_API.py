import requests

api_URL = u"http://jisho.org/api/v1/search/words?keyword="

def search_JISHO(search_string):
    '''search_JISHO uses the requests python library to take search entries from Jisho.org. search_JISHO returns a json from the json() method.'''
    response = requests.get(url = api_URL+search_string)
    if response:
        return response.json()
    else:
        print("Failed to get data. Check your internet connection.")
        return response.json()

def display_definitions(number_of_entries,jisho_response):
    '''disply_definitions(n , response) takes a response json from search_JISHO returns a list of entries of n entries'''
    data = jisho_response['data']

    if len(data) == 0:
        return ['Didn\'t find it on JISHO']

    number_of_entries_to_take = min(number_of_entries,len(data))

    data = data[:number_of_entries_to_take]

    output = []

    for data_entry in data:
        slug_string = data_entry["slug"]

        jp_wds_rds = []
        for jp_word in data_entry["japanese"]:
            if "word" in jp_word and "reading" in jp_word:
                jp_wds_rds.append(jp_word["word"]+"("+jp_word["reading"]+")")
            elif "reading" in jp_word:
                jp_wds_rds.append(jp_word["reading"])
            elif "word" in jp_word:
                jp_wds_rds.append(jp_word["word"])
        jp_wds_rds = '\n'.join(jp_wds_rds)

        eng_defs = []
        for sense in data_entry["senses"]:
            eng_defs.append(', '.join(sense["english_definitions"]))
        eng_defs = '\n'.join(eng_defs)

        tmp_entry = "Word: " + slug_string + "\n" + "Japanese: " + jp_wds_rds + "\n" + "English: " + eng_defs
        output.append(tmp_entry)
        # print(tmp_entry.encode(encoding='utf-8'))

    return output



# test_search_result = search_JISHO("girls")
# print(len(display_definitions(3, test_search_result)))

# test_search_result_list = test_search_result['data']
#
# print(len(test_search_result_list))
# import json
# for i in range(min(3,len(test_search_result['data']))):
#     print(test_search_result['data'][i]['slug'].encode(encoding='UTF-8'))
#     for jp_entry in test_search_result['data'][i]['japanese']:
#         print(jp_entry.kyp)
# dict_keys(['slug', 'is_common', 'tags', 'jlpt', 'japanese', 'senses', 'attribution'])
# for data_entry in test_search_result['data']:
#     try:
#         print(data_entry)
#     except:
#         pass
# print(type(test_search_result['data']))
# def main():
#     api_URL = u"http://jisho.org/api/v1/search/words?keyword="
#     #Add stuff here that will be used always with the jisho_API
# if __name__ == "__main__":
#     main()
# Define a search function here.
# search_keyword = input()
# prompt="Please enter a word: "
# test_
#
# test_response = requests.get(test_URL)
#
# if test_response:
#     print(test_response)
#     print(test_response.text.encode('utf-8'))
# else:
#     print("Failed to get data. Check your internet connection.")
