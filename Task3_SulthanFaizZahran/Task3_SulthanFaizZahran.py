import urllib.request
from urllib import request, parse

import requests
import json
from statistics import mean


def get_product(name_product) :
    url = 'https://gql.tokopedia.com/graphql/SearchProductQueryV4'
    payload = [
        {"operationName": "SearchProductQueryV4",
         "variables":
             {
                 "params": "device=desktop&navsource=&ob=23&page=1&q="+name_product+"&related=true&rows=60&safe_search=false&scheme=https&shipping=&source=search&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&st=product&start=0&topads_bucket=true&unique_id=57fcb00c7a6454faee84cb57292543da&user_addressId=&user_cityId=&user_districtId=&user_id=19713913&user_lat=&user_long=&user_postCode=&user_warehouseId=0&variants="},
         "query": "query SearchProductQueryV4($params: String!) {\n  ace_search_product_v4(params: $params) {\n    header {\n      totalData\n      totalDataText\n      processTime\n      responseCode\n      errorMessage\n      additionalParams\n      keywordProcess\n      componentId\n      __typename\n    }\n    data {\n      banner {\n        position\n        text\n        imageUrl\n        url\n        componentId\n        trackingOption\n        __typename\n      }\n      backendFilters\n      isQuerySafe\n      ticker {\n        text\n        query\n        typeId\n        componentId\n        trackingOption\n        __typename\n      }\n      redirection {\n        redirectUrl\n        departmentId\n        __typename\n      }\n      related {\n        position\n        trackingOption\n        relatedKeyword\n        otherRelated {\n          keyword\n          url\n          product {\n            id\n            name\n            price\n            imageUrl\n            rating\n            countReview\n            url\n            priceStr\n            wishlist\n            shop {\n              city\n              isOfficial\n              isPowerBadge\n              __typename\n            }\n            ads {\n              adsId: id\n              productClickUrl\n              productWishlistUrl\n              shopClickUrl\n              productViewUrl\n              __typename\n            }\n            badges {\n              title\n              imageUrl\n              show\n              __typename\n            }\n            ratingAverage\n            labelGroups {\n              position\n              type\n              title\n              url\n              __typename\n            }\n            componentId\n            __typename\n          }\n          componentId\n          __typename\n        }\n        __typename\n      }\n      suggestion {\n        currentKeyword\n        suggestion\n        suggestionCount\n        instead\n        insteadCount\n        query\n        text\n        componentId\n        trackingOption\n        __typename\n      }\n      products {\n        id\n        name\n        ads {\n          adsId: id\n          productClickUrl\n          productWishlistUrl\n          productViewUrl\n          __typename\n        }\n        badges {\n          title\n          imageUrl\n          show\n          __typename\n        }\n        category: departmentId\n        categoryBreadcrumb\n        categoryId\n        categoryName\n        countReview\n        customVideoURL\n        discountPercentage\n        gaKey\n        imageUrl\n        labelGroups {\n          position\n          title\n          type\n          url\n          __typename\n        }\n        originalPrice\n        price\n        priceRange\n        rating\n        ratingAverage\n        shop {\n          shopId: id\n          name\n          url\n          city\n          isOfficial\n          isPowerBadge\n          __typename\n        }\n        url\n        wishlist\n        sourceEngine: source_engine\n        __typename\n      }\n      violation {\n        headerText\n        descriptionText\n        imageURL\n        ctaURL\n        ctaApplink\n        buttonText\n        buttonType\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"}
    ]

    req = requests.post(url=url, json=payload).json()
    list_products = req[0]['data']['ace_search_product_v4']['data']['products']

    worth_buying_category = []
    considered_category = []
    not_recomended_category = []
    others_category = []
    # print(list_products)
    result_product = []
    price_list = []

    for i in range(0, len(list_products)):
        product_price = int(list_products[i]['price'].replace("Rp", "").replace(".", ""))
        price_list.append(product_price)

    average = round(mean(price_list), 3)

    for product in list_products:
        product_price = int(product['price'].replace("Rp", "").replace(".", ""))
        product_id = product['id']
        rate = float(product['ratingAverage'])
        amount_sale = 0
        for label in product['labelGroups']:
            if label['position'] == 'integrity':
                amount_sale = int(
                    label['title'].replace("rb", "000").replace("+", "").replace("Terjual ", "").replace(" ", ""))
                # print(label)

        product_key = product['gaKey'].split('/')[-1]
        product_referer = 'https://www.tokopedia.com/'+ product['gaKey'].split('/')[-2] + '/' + product_key
        # print(product_referer)
        cookies = {
            'bm_sz': 'DAEE0C87EF04A2BB5A502D59A750970C~YAAQdMMmF/mTD3iGAQAAcjg1sxM6yl54NM9h59vqeBdZhFHA+ohQcKEcOstWm2nBeAf8ob/ILDUkSaFA44ptMAPftmbSDbJESwa6jhKFqoc8fgvkak8plW9p8nFDPleSrCG79xX188AtT6GjpMVq/WYvqpEEWQ8t/NYnMMcJk18eofQLNfbBviJ2sFy9TDJYqA54J2v1QHlJ0PYuKJY2bxYA9Pu9hJtgf3RqF26/LtYkQx2EUY6vWl/f9HWmUjk6ng3DzdWHYVc2nGTDfxe/H0cJPGT2k/fwLkHYl0wv5VIP9OA3c7s=~3617590~3617862',
            '_SID_Tokopedia_': '7HPBQp_Xm1YzfF2OMnipDWxNLQPS-y1DwI4QkgPshwg9ZdTYW4_HZKwreoB7-11EzMu-Gl-GB2VcJJ6GZqmyz2zHBPcyVw1Eb2iJXkFH66JFpGJO0NkNPz9Ae7GgAaMP',
            'DID': 'a391acb67f19d0170eebfadb65261134a1e208d28b28bcaeb1c1bf35261cf85e523db59b50a4993472f49efd97454893',
            'DID_JS': 'YTM5MWFjYjY3ZjE5ZDAxNzBlZWJmYWRiNjUyNjExMzRhMWUyMDhkMjhiMjhiY2FlYjFjMWJmMzUyNjFjZjg1ZTUyM2RiNTliNTBhNDk5MzQ3MmY0OWVmZDk3NDU0ODkz47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=',
            '_gcl_au': '1.1.2739026.1678043856',
            '_UUID_NONLOGIN_': 'c6256dc66b46279e82d833526b5cb71c',
            'hfv_banner': 'true',
            'ak_bmsc': '07F1FF035185298AA8235D038949701A~000000000000000000000000000000~YAAQdMMmF1mUD3iGAQAARj01sxMyKrWFnw7YlQV+xwZwySdRphgg/M3k4bbOvkCadvnbhsq+fVg5WVvYzLzl2g+galUOyBK9oSkdi8eiTrfu1btL33ZRDq8CXXgKyTYR+3Z2dlf3SwLILiWFCjZDP+TsH79n22GHFfiil/I/wJMs0Kd8VvSvXiL83EA82cpJfoYRx20MdG3U275ihpIjJP7HORZJHB0E1HKxlDqvWhq04YoHJs64h0v5oIQ/BTkY36OuEtavDAyjnzej2iIPpvFmb5TkqXG+vpjBdxKP0MrdGdWhja/OgDcFfpGc3GyQ8vWSEac+iEvFqkQAj05cgj26EphnGs8WD7nWqTmDbN+NVWtZP1rxZSLvY4wsTUmpgBJ68LrwUiap74SpTAw0CqXyfRulaa/Scg03JfguWuGNdoVXdPNt09rDWbArAQHo425xdhR4xj+Yvf+NK5K05WsGCH/XM7Wb68QlvDVYa5+1y0IPCaJDM6JNWm/Fcg==',
            '_gid': 'GA1.2.1430000158.1678043856',
            '_dc_gtm_UA-126956641-6': '1',
            '_dc_gtm_UA-9801603-1': '1',
            '_UUID_CAS_': 'af38880c-c236-492b-863b-d35cb8e104a8',
            '_CASE_': '20793f123f796169696c6f77793a123f79616b7779373937796179113a303a292f3a7b0b2e283a2f79777938123f79616a6c6d77793734353c796179797779373a2f7961797977792b18347961797977792c123f79616a69696a6b686c6e777928123f79616a6a6e686b6e6c687779280f222b3e79617969337977792c3328796179002007792c3a293e33342e283e04323f0779616a69696a6b686c6e770779283e292d32383e042f222b3e07796107796933077977077904042f222b3e353a363e07796107790c3a293e33342e283e28077926772007792c3a293e33342e283e04323f0779616b770779283e292d32383e042f222b3e07796107796a6e36077977077904042f222b3e353a363e07796107790c3a293e33342e283e2807792606797779370e2b3f796179696b6968766b68766b6d0f6b69616a6c61686d706b6c616b6b7926',
            '_gat_UA-9801603-1': '1',
            '__asc': 'eb544306186b3354f002981f9a9',
            '__auc': 'eb544306186b3354f002981f9a9',
            '_fbp': 'fb.1.1678043861257.1277017143',
            '_abck': '631D1BF2ABF931783C2AE231F326E446~0~YAAQdMMmF0+VD3iGAQAAWVo1swmdktK933iW4eB5//Yf9+IjHCCu70G6z5e0Rz11Eadxfm6yyBHkk6v8jf1bTt3gbdZKt/5zss4mhkIyIAGc6rcIghO2yZMlWfr4UzfaCbMtfkZuBT/+VG6nSrvh1goFD0oPgvNO+TraJmeeDOWsy1dR7NKSSmH2J2qz2q0EDkeVtUwqPE5kBb3XCgcKG19Z42i/As9EgmSMqrqaL2eCqFO9vc9yQaABUMqxNKfAegvdWuHKqHfX2Bqg9O076/mJFeQkp+xUdb7MuNlxlwig0yzQ33xgFPW11mGKJeIVj0/KaMPCFnbeBx5ChonpbE1cMUZG1cUvKLPyxIczmxPM6ALp2yTqyNi9V+rACTohJW26LoqIa6OzGAgdnk+wrdBZw4tunjLVWlk=~-1~-1~-1',
            'bm_sv': '3FEB864096F31846222C50FB391155B8~YAAQdMMmF1CVD3iGAQAAWVo1sxMZle9rl1iiRPN/IVgtwGTDs47IgImOsqPrVp8l+DGdgeIUAxWQ1gqD+JZwWo0mjeN32J7UzirhwPDskFbdCEOEp6QDIbXsB6Ux0p5AOw0W96COGUv1EQ2faOno+D8MhHzNoP6RT0gOFnvO7uj+jgTkTwTtNLKbQH5JhiWlGETb4Nh3S8d+ERqkHM5Myx0Bb6cc6rkvittLXHHyxBzt8WoqLVJ51TEv9QPc4GvHTVpE~1',
            '_ga_70947XW48P': 'GS1.1.1678043856.1.1.1678043864.52.0.0',
            'AMP_TOKEN': '%24NOT_FOUND',
            '_ga': 'GA1.2.267300492.1678043856',
        }

        headers = {
            'authority': 'gql.tokopedia.com',
            'accept': '*/*',
            'accept-language': 'en-GB,en;q=0.9',
            'content-type': 'application/json',
            # 'cookie': 'bm_sz=DAEE0C87EF04A2BB5A502D59A750970C~YAAQdMMmF/mTD3iGAQAAcjg1sxM6yl54NM9h59vqeBdZhFHA+ohQcKEcOstWm2nBeAf8ob/ILDUkSaFA44ptMAPftmbSDbJESwa6jhKFqoc8fgvkak8plW9p8nFDPleSrCG79xX188AtT6GjpMVq/WYvqpEEWQ8t/NYnMMcJk18eofQLNfbBviJ2sFy9TDJYqA54J2v1QHlJ0PYuKJY2bxYA9Pu9hJtgf3RqF26/LtYkQx2EUY6vWl/f9HWmUjk6ng3DzdWHYVc2nGTDfxe/H0cJPGT2k/fwLkHYl0wv5VIP9OA3c7s=~3617590~3617862; _SID_Tokopedia_=7HPBQp_Xm1YzfF2OMnipDWxNLQPS-y1DwI4QkgPshwg9ZdTYW4_HZKwreoB7-11EzMu-Gl-GB2VcJJ6GZqmyz2zHBPcyVw1Eb2iJXkFH66JFpGJO0NkNPz9Ae7GgAaMP; DID=a391acb67f19d0170eebfadb65261134a1e208d28b28bcaeb1c1bf35261cf85e523db59b50a4993472f49efd97454893; DID_JS=YTM5MWFjYjY3ZjE5ZDAxNzBlZWJmYWRiNjUyNjExMzRhMWUyMDhkMjhiMjhiY2FlYjFjMWJmMzUyNjFjZjg1ZTUyM2RiNTliNTBhNDk5MzQ3MmY0OWVmZDk3NDU0ODkz47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=; _gcl_au=1.1.2739026.1678043856; _UUID_NONLOGIN_=c6256dc66b46279e82d833526b5cb71c; hfv_banner=true; ak_bmsc=07F1FF035185298AA8235D038949701A~000000000000000000000000000000~YAAQdMMmF1mUD3iGAQAARj01sxMyKrWFnw7YlQV+xwZwySdRphgg/M3k4bbOvkCadvnbhsq+fVg5WVvYzLzl2g+galUOyBK9oSkdi8eiTrfu1btL33ZRDq8CXXgKyTYR+3Z2dlf3SwLILiWFCjZDP+TsH79n22GHFfiil/I/wJMs0Kd8VvSvXiL83EA82cpJfoYRx20MdG3U275ihpIjJP7HORZJHB0E1HKxlDqvWhq04YoHJs64h0v5oIQ/BTkY36OuEtavDAyjnzej2iIPpvFmb5TkqXG+vpjBdxKP0MrdGdWhja/OgDcFfpGc3GyQ8vWSEac+iEvFqkQAj05cgj26EphnGs8WD7nWqTmDbN+NVWtZP1rxZSLvY4wsTUmpgBJ68LrwUiap74SpTAw0CqXyfRulaa/Scg03JfguWuGNdoVXdPNt09rDWbArAQHo425xdhR4xj+Yvf+NK5K05WsGCH/XM7Wb68QlvDVYa5+1y0IPCaJDM6JNWm/Fcg==; _gid=GA1.2.1430000158.1678043856; _dc_gtm_UA-126956641-6=1; _dc_gtm_UA-9801603-1=1; _UUID_CAS_=af38880c-c236-492b-863b-d35cb8e104a8; _CASE_=20793f123f796169696c6f77793a123f79616b7779373937796179113a303a292f3a7b0b2e283a2f79777938123f79616a6c6d77793734353c796179797779373a2f7961797977792b18347961797977792c123f79616a69696a6b686c6e777928123f79616a6a6e686b6e6c687779280f222b3e79617969337977792c3328796179002007792c3a293e33342e283e04323f0779616a69696a6b686c6e770779283e292d32383e042f222b3e07796107796933077977077904042f222b3e353a363e07796107790c3a293e33342e283e28077926772007792c3a293e33342e283e04323f0779616b770779283e292d32383e042f222b3e07796107796a6e36077977077904042f222b3e353a363e07796107790c3a293e33342e283e2807792606797779370e2b3f796179696b6968766b68766b6d0f6b69616a6c61686d706b6c616b6b7926; _gat_UA-9801603-1=1; __asc=eb544306186b3354f002981f9a9; __auc=eb544306186b3354f002981f9a9; _fbp=fb.1.1678043861257.1277017143; _abck=631D1BF2ABF931783C2AE231F326E446~0~YAAQdMMmF0+VD3iGAQAAWVo1swmdktK933iW4eB5//Yf9+IjHCCu70G6z5e0Rz11Eadxfm6yyBHkk6v8jf1bTt3gbdZKt/5zss4mhkIyIAGc6rcIghO2yZMlWfr4UzfaCbMtfkZuBT/+VG6nSrvh1goFD0oPgvNO+TraJmeeDOWsy1dR7NKSSmH2J2qz2q0EDkeVtUwqPE5kBb3XCgcKG19Z42i/As9EgmSMqrqaL2eCqFO9vc9yQaABUMqxNKfAegvdWuHKqHfX2Bqg9O076/mJFeQkp+xUdb7MuNlxlwig0yzQ33xgFPW11mGKJeIVj0/KaMPCFnbeBx5ChonpbE1cMUZG1cUvKLPyxIczmxPM6ALp2yTqyNi9V+rACTohJW26LoqIa6OzGAgdnk+wrdBZw4tunjLVWlk=~-1~-1~-1; bm_sv=3FEB864096F31846222C50FB391155B8~YAAQdMMmF1CVD3iGAQAAWVo1sxMZle9rl1iiRPN/IVgtwGTDs47IgImOsqPrVp8l+DGdgeIUAxWQ1gqD+JZwWo0mjeN32J7UzirhwPDskFbdCEOEp6QDIbXsB6Ux0p5AOw0W96COGUv1EQ2faOno+D8MhHzNoP6RT0gOFnvO7uj+jgTkTwTtNLKbQH5JhiWlGETb4Nh3S8d+ERqkHM5Myx0Bb6cc6rkvittLXHHyxBzt8WoqLVJ51TEv9QPc4GvHTVpE~1; _ga_70947XW48P=GS1.1.1678043856.1.1.1678043864.52.0.0; AMP_TOKEN=%24NOT_FOUND; _ga=GA1.2.267300492.1678043856',
            'origin': 'https://www.tokopedia.com',
            'referer': product_referer,
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
            'x-device': 'desktop',
            'x-source': 'tokopedia-lite',
            'x-tkpd-akamai': 'pdpGetLayout',
            'x-tkpd-lite-service': 'zeus',
            'x-version': '1066a7c',
        }

        json_data = [
            {
                'operationName': 'PDPGetLayoutQuery',
                'variables': {
                    'shopDomain': product['gaKey'].split('/')[-2],
                    'productKey': product_key,
                    'layoutID': '',
                    'apiVersion': 1,
                    'userLocation': {
                        'cityID': '176',
                        'addressID': '0',
                        'districtID': '2274',
                        'postalCode': '',
                        'latlon': '',
                    },
                    'extParam': '',
                },
                'query': 'fragment ProductVariant on pdpDataProductVariant {\n  errorCode\n  parentID\n  defaultChild\n  sizeChart\n  totalStockFmt\n  variants {\n    productVariantID\n    variantID\n    name\n    identifier\n    option {\n      picture {\n        urlOriginal: url\n        urlThumbnail: url100\n        __typename\n      }\n      productVariantOptionID\n      variantUnitValueID\n      value\n      hex\n      stock\n      __typename\n    }\n    __typename\n  }\n  children {\n    productID\n    price\n    priceFmt\n    optionID\n    optionName\n    productName\n    productURL\n    picture {\n      urlOriginal: url\n      urlThumbnail: url100\n      __typename\n    }\n    stock {\n      stock\n      isBuyable\n      stockWordingHTML\n      minimumOrder\n      maximumOrder\n      __typename\n    }\n    isCOD\n    isWishlist\n    campaignInfo {\n      campaignID\n      campaignType\n      campaignTypeName\n      campaignIdentifier\n      background\n      discountPercentage\n      originalPrice\n      discountPrice\n      stock\n      stockSoldPercentage\n      startDate\n      endDate\n      endDateUnix\n      appLinks\n      isAppsOnly\n      isActive\n      hideGimmick\n      isCheckImei\n      minOrder\n      __typename\n    }\n    thematicCampaign {\n      additionalInfo\n      background\n      campaignName\n      icon\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment ProductMedia on pdpDataProductMedia {\n  media {\n    type\n    urlOriginal: URLOriginal\n    urlThumbnail: URLThumbnail\n    urlMaxRes: URLMaxRes\n    videoUrl: videoURLAndroid\n    prefix\n    suffix\n    description\n    variantOptionID\n    __typename\n  }\n  videos {\n    source\n    url\n    __typename\n  }\n  __typename\n}\n\nfragment ProductHighlight on pdpDataProductContent {\n  name\n  price {\n    value\n    currency\n    __typename\n  }\n  campaign {\n    campaignID\n    campaignType\n    campaignTypeName\n    campaignIdentifier\n    background\n    percentageAmount\n    originalPrice\n    discountedPrice\n    originalStock\n    stock\n    stockSoldPercentage\n    threshold\n    startDate\n    endDate\n    endDateUnix\n    appLinks\n    isAppsOnly\n    isActive\n    hideGimmick\n    __typename\n  }\n  thematicCampaign {\n    additionalInfo\n    background\n    campaignName\n    icon\n    __typename\n  }\n  stock {\n    useStock\n    value\n    stockWording\n    __typename\n  }\n  variant {\n    isVariant\n    parentID\n    __typename\n  }\n  wholesale {\n    minQty\n    price {\n      value\n      currency\n      __typename\n    }\n    __typename\n  }\n  isCashback {\n    percentage\n    __typename\n  }\n  isTradeIn\n  isOS\n  isPowerMerchant\n  isWishlist\n  isCOD\n  isFreeOngkir {\n    isActive\n    __typename\n  }\n  preorder {\n    duration\n    timeUnit\n    isActive\n    preorderInDays\n    __typename\n  }\n  __typename\n}\n\nfragment ProductCustomInfo on pdpDataCustomInfo {\n  icon\n  title\n  isApplink\n  applink\n  separator\n  description\n  __typename\n}\n\nfragment ProductInfo on pdpDataProductInfo {\n  row\n  content {\n    title\n    subtitle\n    applink\n    __typename\n  }\n  __typename\n}\n\nfragment ProductDetail on pdpDataProductDetail {\n  content {\n    title\n    subtitle\n    applink\n    showAtFront\n    isAnnotation\n    __typename\n  }\n  __typename\n}\n\nfragment ProductDataInfo on pdpDataInfo {\n  icon\n  title\n  isApplink\n  applink\n  content {\n    icon\n    text\n    __typename\n  }\n  __typename\n}\n\nfragment ProductSocial on pdpDataSocialProof {\n  row\n  content {\n    icon\n    title\n    subtitle\n    applink\n    type\n    rating\n    __typename\n  }\n  __typename\n}\n\nquery PDPGetLayoutQuery($shopDomain: String, $productKey: String, $layoutID: String, $apiVersion: Float, $userLocation: pdpUserLocation, $extParam: String) {\n  pdpGetLayout(shopDomain: $shopDomain, productKey: $productKey, layoutID: $layoutID, apiVersion: $apiVersion, userLocation: $userLocation, extParam: $extParam) {\n    requestID\n    name\n    pdpSession\n    basicInfo {\n      alias\n      createdAt\n      isQA\n      id: productID\n      shopID\n      shopName\n      minOrder\n      maxOrder\n      weight\n      weightUnit\n      condition\n      status\n      url\n      needPrescription\n      catalogID\n      isLeasing\n      isBlacklisted\n      menu {\n        id\n        name\n        url\n        __typename\n      }\n      category {\n        id\n        name\n        title\n        breadcrumbURL\n        isAdult\n        isKyc\n        minAge\n        detail {\n          id\n          name\n          breadcrumbURL\n          isAdult\n          __typename\n        }\n        __typename\n      }\n      txStats {\n        transactionSuccess\n        transactionReject\n        countSold\n        paymentVerified\n        itemSoldFmt\n        __typename\n      }\n      stats {\n        countView\n        countReview\n        countTalk\n        rating\n        __typename\n      }\n      __typename\n    }\n    components {\n      name\n      type\n      position\n      data {\n        ...ProductMedia\n        ...ProductHighlight\n        ...ProductInfo\n        ...ProductDetail\n        ...ProductSocial\n        ...ProductDataInfo\n        ...ProductCustomInfo\n        ...ProductVariant\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n',
            },
        ]

        response = requests.post('https://gql.tokopedia.com/graphql/PDPGetLayoutQuery', cookies=cookies, headers=headers, json=json_data).json()
        # print(response[0]['data']['pdpGetLayout']['components'][0])
        for product_detail in response[0]['data']['pdpGetLayout']['components']:
            if product_detail['name'] == 'product_detail':
                for content in product_detail['data'][0]['content']:
                    # print(content['title'])
                    if content['title'] == 'Deskripsi':
                        product_description = content['subtitle']
        data = {
            "id_produk" : product_id,
            "nama_produk" : product['name'],
            "deskripsi_produk" : product_description,
            "nama_penjual" : product['gaKey'].split('/')[-2],
            "rating_produk" : rate,
            "jumlah_product_terjual" : amount_sale
        }
        print(data)
        if product_price > average and rate > 4 and amount_sale > 10:
            worth_buying_category.append(data)
        elif product_price > average and rate < 4 and amount_sale > 10:
            considered_category.append(data)
        elif product_price > average and rate < 2 and amount_sale > 10:
            not_recomended_category.append(data)
        else:
            others_category.append(data)

    result = {
        "layak_dibeli": worth_buying_category,
        "perlu_dipertimbangkan": considered_category,
        "tidak_layak_dibeli" : not_recomended_category,
        "lainnya" : others_category
    }
    print(json.dumps(result))

if __name__ == '__main__':
    name_product = input("silahkan masukkan product yang ingin anda cari : ")
    get_product(name_product)
