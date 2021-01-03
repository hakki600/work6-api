  
import requests
import urllib
import pandas as pd

def get_api(url):
    result = requests.get(url)
    return result.json()

# 楽天商品検索API
def search():
    # 任意のキーワードでAPIを検索した時の 商品名と価格の一覧を取得
    keyword = "星のカービィ"
    # url = f"https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?format=json&keyword={keyword}&elements=Items,count&formatVersion=2&applicationId=1019079537947262807"
    url = f"https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?format=json&keyword={keyword}&elements=Items,count&formatVersion=2&hits=30&page=1&sort=-itemPrice&applicationId=1019079537947262807"
    

    rakuten = get_api(url)
    print(rakuten.keys())
    # >> dict_keys(['Items', 'pageCount', 'TagInformation', 'hits', 'last'
    # , 'count', 'page', 'carrier', 'GenreInformation', 'first'])
    
    count = rakuten["count"]
    print(f"ヒット件数 {count}")
    
    items = rakuten["Items"]
    print(items[0].keys())
    # >> dict_keys(['mediumImageUrls', 'pointRate', 'shopOfTheYearFlag', 
    # 'affiliateRate', 'shipOverseasFlag', 'asurakuFlag', 'endTime', 'taxFlag', 
    # 'startTime', 'itemCaption', 'catchcopy', 'tagIds', 'smallImageUrls', 
    # 'asurakuClosingTime', 'imageFlag', 'availability', 'shopAffiliateUrl', 
    # 'itemCode', 'postageFlag', 'itemName', 'itemPrice', 'pointRateEndTime', 
    # 'shopCode', 'affiliateUrl', 'giftFlag', 'shopName', 'reviewCount', 
    # 'asurakuArea', 'shopUrl', 'creditCardFlag', 'reviewAverage', 'shipOverseasArea', 
    # 'genreId', 'pointRateStartTime', 'itemUrl']
    
    for item in items:
         print(item["itemName"], item["itemPrice"])
    print(len(items))
    
    
# 楽天商品価格ナビAPI
def navi():
    # 任意の商品の最安値と最高値を取得
    keyword = "Nintendo Switch  Lite ターコイズ 本体"
    url = f"https://app.rakuten.co.jp/services/api/Product/Search/20170426?format=json&keyword={keyword}&formatVersion=2&applicationId=1019079537947262807"
    rakuten_navi = get_api(url)
    # print(rakuten_navi.keys())
    # >>dict_keys(['pageCount', 'hits', 'Products', 'last', 'count',
    # 'page', 'GenreInformation', 'first'])
    products = rakuten_navi["Products"]
    for product in products:
        print(product["productName"], product["salesMaxPrice"], product["salesMinPrice"])
         
         
# 楽天商品ランキングAPI
def ranking():
    # 任意のジャンルのランキング一覧を取得し、CSV出力
    genreId = "565950"
    # 「ジャンルID」は、「年代別」「性別」と同時に指定できません。
    # url = f"https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628?format=json&age=20&sex=1&formatVersion=2&applicationId=1019079537947262807"
    url = f"https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628?format=json&genreId={genreId}&formatVersion=2&applicationId=1019079537947262807"
    rakuten_ranking = get_api(url)
    # print(rakuten_ranking.keys())
    # >>dict_keys(['Items', 'title', 'lastBuildDate'])
    Items = rakuten_ranking["Items"]
    # print(Items[0].keys())
    # >> dict_keys(['mediumImageUrls', 'pointRate', 'shopOfTheYearFlag', 'affiliateRate',
    # 'shipOverseasFlag', 'asurakuFlag', 'endTime', 'taxFlag', 'startTime', 'rank',
    # 'itemCaption', 'catchcopy', 'smallImageUrls', 'asurakuClosingTime', 'carrier',
    # 'imageFlag', 'shopAffiliateUrl', 'availability', 'itemCode', 'postageFlag',
    # 'itemName', 'itemPrice', 'pointRateEndTime', 'shopCode', 'affiliateUrl',
    # 'shopName', 'asurakuArea', 'reviewCount', 'shopUrl', 'creditCardFlag',
    # 'reviewAverage', 'shipOverseasArea', 'genreId', 'pointRateStartTime', 'itemUrl'])
    title = rakuten_ranking["title"]
    print(title)
    
    rank = []
    itemName = []
    for item in Items:
        rank.append(item["rank"])
        itemName.append(item["itemName"])
    
    df = pd.DataFrame(
        {
        'rank': rank,
        'itemName': itemName,
        }
    )
    filename = f"./out_{title}.csv"
    df.to_csv(filename, encoding="utf_8-sig")

def main():
    # search()
    # navi()
    ranking()

main()