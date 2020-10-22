
# https://medium.com/@adrianmrit/creating-simple-image-datasets-with-flickr-api-2f19c164d82f
from flickrapi import FlickrAPI

KEY = '3849cca5635f0c6ecca718b0da957ee5'
SECRET = '8569c590b522576e'

SIZES = ["url_o", "url_k", "url_h", "url_l", "url_c"]  # order of preference

def get_photos(image_tag):
    extras = ','.join(SIZES)
    flickr = FlickrAPI(KEY, SECRET)
    photos = flickr.walk(text=image_tag,
                            extras=extras,  # get the url for the original size image
                            privacy_filter=1,  # search only for public photos
                            per_page=50,
                            sort='relevance')
    return photos

def get_url(photo):
    for i in range(len(SIZES)):
        url = photo.get(SIZES[i])
        if url:  # if url is None try with the next size
            return url

def get_urls(image_tag, max):
    photos = get_photos(image_tag)
    counter=0
    urls=[]

    for photo in photos:
        if counter < max:
            url = get_url(photo)  # get preffered size url
            if url:
                urls.append(url)
                counter += 1
            # if no url for the desired sizes then try with the next photo
        else:
            break

    return urls