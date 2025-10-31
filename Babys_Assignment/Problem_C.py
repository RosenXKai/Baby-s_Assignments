def find_urls (url):
    # list of urls
    urls = []
    # first occurence
    nxt = url.find('href="')

    while nxt != -1:
        start = nxt + len('href="')
        end = url.find("'", start)

        hyperlink = url[start:end]

        urls.append(hyperlink)
        nxt = url.find('href="', end)
    return urls


if __name__ == '__main__':
    print(find_urls('title="Association for Computing Machinery">ACM DL</a>: <span class="uid"><a rel="nofollow" class="external text" href="https://dl.acm.org/profile/81100248871">81100248871</a></span></span><a class="more" href="http://awards.acm.org" target="_blank">MORE ACM AWARDS</a>'))
    #['https://dl.acm.org/profile/81100248871',   'http://awards.acm.org']

    print(find_urls('<div class="clearfix text-formatted field field--name-body field--type-text-with-summary field--label-hidden field__item"><p><iframe frameborder="0" height="380" src="https://www.arcgis.com/apps/Embed/index.html?webmap=3c8015df0c3c484a96df7739a97ae967&amp;marker=-93.2324397896;44.9745203485;;;https://egis.umn.edu/bldg_detail_pages_map_marker.GIF;;&amp;level=4&#10;" width="100%"></iframe><script = src="https://use.fontawesome.com/releases/v5.8.2/js/v4-shims.js" defer crossorigin="anonymous"></script>'))
    #[]

    print(find_urls('<ul role="presentation"><li><a href="http://onestop.umn.edu/">One Stop</a></li><li><a href="https://www.myu.umn.edu/">MyU <span></span></a></li></ul></nav><small> <span id="cdate">2024</span> Regents of the <a href="https://system.umn.edu">University of Minnesota</a>. All rights reserved. The University of Minnesota is an equal opportunity educator and employer. <a href="https://privacy.umn.edu">Privacy Statement</a></small><small><a href="https://oit-drupal-prd-web.oit.umn.edu/indexAccess.php?ref_url=https://campusmaps.umn.edu/kenneth-h-keller-hall">Report Web Disability-Related Issue</a></small>'))
    #['http://onestop.umn.edu/', 'https://www.myu.umn.edu/', 'https://system.umn.edu', 'https://privacy.umn.edu', 'https://oit-drupal-prd-web.oit.umn.edu/indexAccess.php?ref_url=https://campusmaps.umn.edu/kenneth-h-keller-hall']
