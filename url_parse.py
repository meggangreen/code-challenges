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


def which_page_re(url):
    """ Uses regex to return the current page of Google search results based on
        the URL.

        >>> url = 'https://www.google.com/search?q=postgres+generate+uuid+on+insert&page=12&ei=E3SCWpQ&start=30&sa=N&biw=1245&bih=703'
        >>> which_page_re(url)
        12

    """

    import re

    m_obj = re.search(r'&page=\d*', url)
    page = int(m_obj.group(0)[6:])

    return page


def url_attrs(url):

    domain = url[:url.find('?')]

    attrs_list = url[url.find('?')+1:].split('&')

    attrs_dict = {}

    for attr in attrs_list:
        i = attr.find('=')
        attrs_dict[attr[:i]] = attr[i+1:]

    return attrs_dict


def url_attrs_re(url):

    import re

    attr_string = url[url.find('?')+1:]  # after the '?' signaling the attrs

    m_obj = re.findall(r'[+A-Za-z0-9]+=[+A-Za-z0-9]+', attr_string)

    # this loop works, but i want it in a comprehension
    attrs = {}
    for attr in m_obj:
        attr_list = attr.split('=')
        for i in range(0, len(attr_list), 2):
            attrs[attr_list[i]] = attr_list[i+1]

    # comprehension works, but it is ugly -- map?
    attrs = { attr.split('=')[i]: attr.split('=')[i+1] for i in range(
                                0, len(attr.split('=')), 2) for attr in m_obj }

    return attrs


url = 'https://www.google.com/search?q=postgres+generate+uuid+on+insert&page=12&ei=E3SCWpQ&start=30&sa=N&biw=1245&bih=703'
print which_page(url)
print url_attrs(url)


#############################

if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print("\n----- ALL TESTS PASSED -----\n")

