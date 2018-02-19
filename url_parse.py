def which_page(url):
    """ Returns the current page of Google search results based on the URL.

        >>> url = 'https://www.google.com/search?q=postgres+generate+uuid+on+insert&page=12&ei=E3SCWpQ&start=30&sa=N&biw=1245&bih=703'
        >>> which_page(url)
        12

    """

    start = url.find('&page=')
    short_url = url[start+6:]

    end = short_url.find('&')

    page_string = short_url[:end]

    page = int(page_string)

    return page


def url_attrs(url):
    domain = url[:url.find('?')]

    attrs_list = url[url.find('?')+1:].split('&')

    attrs_dict = {}

    for attr in attrs_list:
        i = attr.find('=')
        attrs_dict[attr[:i]] = attr[i+1:]

    return attrs_dict


url = 'https://www.google.com/search?q=postgres+generate+uuid+on+insert&page=12&ei=E3SCWpQ&start=30&sa=N&biw=1245&bih=703'
print which_page(url)
print url_attrs(url)


#############################

if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print("\n----- ALL TESTS PASSED -----\n")

