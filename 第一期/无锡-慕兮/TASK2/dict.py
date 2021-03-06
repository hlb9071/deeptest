dict_1 = {'list': [
    {'comm_msg_info':
         {'fakeid': '2393295571',
          'content': '',
          'type': 49,
          'id': 1000001201,
          'status': 2,
          'datetime': 1516849776},
     'app_msg_ext_info':
         {'fileid': 503986284,
          'del_flag': 1,
          'cover': 'http://mmbiz.qpic.cn/mmbiz_jpg/yl6JkZAE3S9aseHLxIZLTibKKHMEHFLtaTM1DbyYj4hpQHT4WibStohHK3ZCfhqHzdmiaXBu2Bicb8ZpHL9oITGLDQ/0?wx_fmt=jpeg',
          'content_url': '/s?timestamp=1516853823&amp;src=3&amp;ver=1&amp;signature=1L5YWossLcmGdDTfpolhOqk*pe9PtsUjVlJVBcfd51oJY1Yv9cRd*GO8Usoz1cTo963J63mog-BLcXOS9toZj4ysAweqOE-smrxFpWA*N-r7I01ApehCLi*aq1qzjN6BwKGNbLwrF1K3RcVgF90tMZxm2NGyYa5aZRVXPf20BUU=',
          'author': '邱海鸿',
          'source_url': 'http://www.thepaper.cn/newsDetail_forward_1966516',
          'is_multi': 1,
          'subtype': 9,
          'content': '',
          'title': '中铁建工摊上大事了！伪造材料中标南京7亿元项目？',
          'copyright_stat': 11,
          'digest': '被业主方约谈',
        'multi_app_msg_item_list': [
              {'fileid': 503986297,
               'del_flag': 1,
               'cover': 'http://mmbiz.qpic.cn/mmbiz_jpg/yl6JkZAE3S9aseHLxIZLTibKKHMEHFLtaCRdOtXT3GHDo3NXEY9wHyjl0hSuyAPQXxYYibFiayBF45wbwfxeWedUw/0?wx_fmt=jpeg',
               'title': '厉害了我的科学家！世界首只体细胞克隆猴“中中”在上海诞生',
               'content': '',
               'content_url': '/s?timestamp=1516853823&amp;src=3&amp;ver=1&amp;signature=1L5YWossLcmGdDTfpolhOqk*pe9PtsUjVlJVBcfd51oJY1Yv9cRd*GO8Usoz1cTo963J63mog-BLcXOS9toZj4ysAweqOE-smrxFpWA*N-pyhYV0veSDGMiVez7W6paN*ga2YDGFe1eHZMX-91hUXkAMlTuqM7vQeza*CfVSzvo=',
               'copyright_stat': 100,
               'digest': '克隆猴是否存在伦理的风险？',
               'author': '',
               'source_url': 'http://www.thepaper.cn/newsDetail_forward_1966809'},
              {'fileid': 503986296,
               'del_flag': 1,
               'cover': 'http://mmbiz.qpic.cn/mmbiz_jpg/yl6JkZAE3S9aseHLxIZLTibKKHMEHFLtaZYUBnnDjzgBT5AUTVQNPm8CC5nL39Kf7P71ENQD54B16zZMSv0Vosw/0?wx_fmt=jpeg',
               'title': '长沙城管的这波执法戳中笑点，摊贩被萌到“来不及生气”',
               'content': '',
               'content_url': '/s?timestamp=1516853823&amp;src=3&amp;ver=1&amp;signature=1L5YWossLcmGdDTfpolhOqk*pe9PtsUjVlJVBcfd51oJY1Yv9cRd*GO8Usoz1cTo963J63mog-BLcXOS9toZj4ysAweqOE-smrxFpWA*N-rG30LI6LkoENEUjwDu2sK1Vnfftn6QZmOtnTWHvM1dlaM0caSbsIUcWNjg0l2US1c=',
               'copyright_stat': 100,
               'digest': '“既文明也很可爱”',
               'author': '',
               'source_url': 'http://www.thepaper.cn/newsDetail_forward_1966926'},

              {'fileid': 503986294,
               'del_flag': 1,
               'cover': 'http://mmbiz.qpic.cn/mmbiz_jpg/yl6JkZAE3S9aseHLxIZLTibKKHMEHFLtaw3ODQpeyiacfaK4S6qpVzf3FwdsUK7TOc1It4ouVHHqyYpvfEFrB3RA/0?wx_fmt=jpeg',
               'title': '贵州从江民房火灾致4死，1副县长、8名局领导等15人被免',
               'content': '',
               'content_url': '/s?timestamp=1516853823&amp;src=3&amp;ver=1&amp;signature=1L5YWossLcmGdDTfpolhOqk*pe9PtsUjVlJVBcfd51oJY1Yv9cRd*GO8Usoz1cTo963J63mog-BLcXOS9toZj4ysAweqOE-smrxFpWA*N-pWVOrPXxvJB8ASiTeqod7fXNYqmcTGScijRi4qaGhmwgV6sfP*KB74v0WzFQm3jVw=',
               'copyright_stat': 11,
               'digest': '起火原因仍在进一步调查中。',
               'author': '王哿 钟煜豪',
               'source_url': 'http://www.thepaper.cn/newsDetail_forward_1966546'},
                ]
          }
    }
]}


def read_data(value):
    if type(value) == dict:
        for k, v in value.items():
            # print(k, ": ", v)
            read_data(v)
            if k == "title" or k == "content_url":
                print(k, ":", v)
    elif type(value) == list:
        for i in value:
            read_data(i)

if __name__ == "__main__":
    read_data(dict_1)