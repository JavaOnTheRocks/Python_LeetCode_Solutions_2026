class Solution(object):
    def dfs(self,row,col,image,original,color,m,n):
        #base case
        if row <0 or row>=m or col < 0 or col >= n:
            return
        if image[row][col] != original:
            return
        else:
            image[row][col]=color

        # dfs is used to perform task like graph traversal,like start from an node and visit
        
        self.dfs(row-1,col,image,original,color,m,n)#top
        self.dfs(row,col-1,image,original,color,m,n)#left
        self.dfs(row+1,col,image,original,color,m,n)#down
        self.dfs(row,col+1,image,original,color,m,n)#right

    def floodFill(self, image, sr, sc, color):
        original=image[sr][sc]
        m = len(image) #number of rows
        n=len(image[0]) #number of cols
        if original==color: # we ahve nothing to do
            return image

        self.dfs(sr,sc,image,original,color,m,n)
        return image


        


        