class Solution:
    def floodFillHelper(self, image, sr, sc, color, og_color):
        ROW = len(image)
        COL = len(image[0])
        if sr < 0 or sc < 0 or sr >= ROW or sc >= COL:
            return image
        if image[sr][sc] == color:
            return image
        if image[sr][sc] == og_color:
            image[sr][sc] = color
            image = self.floodFillHelper(image, sr + 1, sc, color, og_color)
            image = self.floodFillHelper(image, sr-1, sc, color, og_color)
            image = self.floodFillHelper(image, sr, sc + 1, color, og_color)
            image = self.floodFillHelper(image, sr, sc - 1, color, og_color)
        
        return image
        
        
        
        

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        og_color = image[sr][sc]
        return self.floodFillHelper(image, sr, sc, color, og_color)

        