from math import comb

def p_alpha(n, alpha):
    q,r=divmod(n,alpha)
    return (alpha-r)*comb(q,2)+r*comb(q+1,2)

U=29; blocks=49; block_size=4; colors=11; selected=7; delta_max=16
S=blocks*comb(block_size,2)
need=p_alpha(U,12)
upper=S+delta_max
lower=S+need
assert S==294 and need==22 and upper==310 and lower==316 and lower>upper
assert colors-selected==4
print({"selected_distinct_edges":S,"turan_p12_29":need,"complement_edge_upper":upper,"one_unselected_color_lower":lower,"contradiction_gap":lower-upper,"unselected_non_target_colors":colors-selected})
