# logic: need to check for the surroundings
# the unchanged ones are the ones which has the non equal colors as its boundaries

# better to follow encode and decode method as we are not sure what might show up

# perfect algorithm is DFS, to go for all the neighbours and verify things to encode

# there is a chance of loop in here as one might see other too again and again, so need to use see set

def floodfill(image, sr,sc,newcolor):
    r,c = len(image), len(image[0])
    check = image[sr][sc]
    seen=set()
    seen.add((sr,sc))
    def ff(str,stc):
        possible=[[i,j] for i,j in ([str,stc+1], [str,stc-1], [str+1,stc], [str-1,stc]) if 0<=i<r and 0<=j<c and image[i][j]==check and (i,j) not in seen]
        for i,j in possible:
            seen.add((i,j))
        for i in possible:
            ff(i[0], i[1])

        image[str][stc] = newcolor
    ff(sr,sc)
    return image

print(floodfill([[1,1,1],[1,1,1],[1,0,1]], 1,1,2))

