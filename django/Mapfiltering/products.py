products=[
    {"p_name":"complan","mrp":230,"avl_qty":50},
    {"p_name": "horlicks", "mrp": 250, "avl_qty": 10},
    {"p_name": "bournvita", "mrp": 220, "avl_qty": 0},
    {"p_name": "nutricharge", "mrp": 200, "avl_qty": 100},
    {"p_name": "mylo", "mrp": 100, "avl_qty": 0},
]
pro_name=list(map(lambda item:item["p_name"],products))
print(pro_name)

pro_ava=list(filter(lambda item:item["avl_qty"]>0,products))
print(pro_ava)

pro_out=list(filter(lambda item:item["avl_qty"]==0,products))
print(pro_out)

prices=list(map(lambda item:item["mrp"],products))
print(max(prices))