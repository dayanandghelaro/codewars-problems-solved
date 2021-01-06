def get_product_id(url): 
    # your code here
    dis_list = url.split('-')
    return dis_list[-2]
